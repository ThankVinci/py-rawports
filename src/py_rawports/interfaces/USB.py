import usb.core, usb.util
from usb.backend import libusb1
from usb.core import Device
import libusb_package

from typing import Union, List, Tuple, Any, Callable

be = libusb1.get_backend(find_library=libusb_package.find_library)

class _DEVInfo:
    # usbdevice info, match one device via VID, PID and ADDR
    def __init__(self, VID:int, PID:int, ADDR:int, DEVNAME:str):
        self.__VID = VID
        self.__PID = PID
        self.__ADDR = ADDR
        self.devname = DEVNAME
    
    def __call__(self,dev):
        return dev.idVendor == self.__VID and dev.idProduct == self.__PID and dev.address == self.__ADDR 

class _SCANInfo:
    # usbscan info, match VID and PID, if host connect more devices which have same PID and VID, the scanner can scan all devices.
    def __init__(self, VID:int, PID:int):
        self.__VID = VID
        self.__PID = PID
    
    def __call__(self,dev):
        return dev.idVendor == self.__VID and dev.idProduct == self.__PID 

class _USBFinder:
    # _USBFinder.scan will try to scan all deivce
    @classmethod
    def scan(cls, match_func:_SCANInfo):
        __devs_info = []
        if(callable(match_func)):
            for dev in usb.core.find(find_all=True, backend=be, custom_match=match_func):
                __devs_info.append(_DEVInfo(dev.idVendor, dev.idProduct, dev.address, dev.product))
        return tuple(__devs_info)

    @classmethod
    def find(cls, match_func:_DEVInfo):
        __dev = None
        if(callable(match_func)):
            __dev = usb.core.find(find_all=False, backend=be, custom_match=match_func)
        return __dev

_Address = Tuple[_SCANInfo, int, int] # scaninfo, inep_addr, outep_addr

class Comm:
    def __init__(self, inep:int=0x81, outep:int=0x01):
        self.__dev:Device = None
        self.__inep:int = inep
        self.__outep:int = outep
    
    def close(self):
        if(not self.isclosed()):
            usb.util.dispose_resources(self.__dev)
        self.__dev = None

    def isclosed(self):
        if(self.__dev is None):
            return True
        return False
    
    def open(self, match_func:_SCANInfo):
        self.close()
        self.__dev = _USBFinder.find(match_func)

    def read(self, len:int, timeout:float=None)->bytes:
        if(self.isclosed()):
            raise IOError('usb is close!')
        timeout = int(timeout * 1000) # s -> ms
        data = self.__dev.read(self.__inep, len, timeout)
        return data.tobytes()

    def write(self, data:bytes, timeout:float=None):
        if(self.isclosed()):
            raise IOError('usb is close!')
        timeout = int(timeout * 1000) # s -> ms
        return self.__dev.write(self.__outep, data, timeout)

def main():
    comm = Comm()
    try:
        comm.open(_SCANInfo(0x0101, 0x1010))
        comm.write(b'114514')
        print(comm.read(20))
    except Exception as e:
        print(f'Exception:{e} ')
    finally:
        comm.close()

if __name__ == '__main__':
    main()