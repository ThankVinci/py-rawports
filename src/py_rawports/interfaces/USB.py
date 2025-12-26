
import usb.core, usb.util, libusb_package
from usb.backend import libusb1
from usb.core import Device

from enum import IntEnum
from typing import Union, List, Tuple, Any, Callable, Type

be = libusb1.get_backend(find_library=libusb_package.find_library)

class HWID:
    def __init__(self, VID:int=0x0000, PID:int=0x0000):
        self.VID = VID
        self.PID = PID
    
    def __call__(self, dev:Device)->bool:
        return dev.idVendor == self.VID and dev.idProduct == self.PID

class _DEVInfo:
    # usbdevice info, match one device via HWID and ADDR
    def __init__(self, hwID:HWID, Addr:int, DEVNAME:str):
        self.__hwID = hwID
        self.__Addr = Addr
        self.devname = DEVNAME
    
    def __call__(self,dev)->bool:
        return self.__hwID(dev) and dev.address == self.__Addr 

class _SCANInfo:
    # usbscan info, match hwID and ADDR(if have)
    # if Addr is None and host is connected to multiple devices with the same HWID, the scanner can scan all devices.
    # if Addr is not None, then only one device will be matched.
    def __init__(self, hwID:HWID, Addr:int=None):
        self.__hwID = hwID
        self.__Addr = Addr
    
    def __call__(self,dev)->bool:
        __MATCH_ADDR = self.__Addr is None or dev.address == self.__Addr
        return self.__hwID(dev) and __MATCH_ADDR

class _USBFinder:
    # _USBFinder.scan will try to scan all deivce that match _SCANInfo
    @classmethod
    def scan(cls, match_func:_SCANInfo)->Tuple[Device]:
        __devs_info = []
        if(callable(match_func)):
            for dev in usb.core.find(find_all=True, backend=be, custom_match=match_func):
                __devs_info.append(_DEVInfo(dev.idVendor, dev.idProduct, dev.address, dev.product))
        return tuple(__devs_info)

    # _USBFinder.find will find only one device that matches _DEVInfo or _SCANInfo
    @classmethod
    def find(cls, match_func:Union[_DEVInfo, _SCANInfo])->Union[Device, None]:
        __dev = None
        if(callable(match_func)):
            __dev = usb.core.find(find_all=False, backend=be, custom_match=match_func)
        return __dev

class Comm:
    def __init__(self, inEndpoint:int=0x81, outEndpoint:int=0x01):
        self.__INEP:int = inEndpoint
        self.__OUTEP:int = outEndpoint
        self.__dev:Device = None
    
    # open usb device by matching function object
    def open(self, match_func:_SCANInfo)->bool:
        self.close()
        self.__dev = _USBFinder.find(match_func)
        return self.isopen()
    
    def isopen(self)->bool:
        return self.__dev is not None

    def close(self)->bool:
        if(not self.isclosed()):
            usb.util.dispose_resources(self.__dev)
        self.__dev = None
        return True

    def isclosed(self)->bool:
        if(self.__dev is None):
            return True
        return False

    def read(self, len:int, timeout:float=None)->bytes:
        if(self.isclosed()):
            raise IOError('usb is close!')
        if(timeout is not None):
            timeout = int(timeout * 1000) # s -> ms
        data = self.__dev.read(self.__INEP, len, timeout)
        return data.tobytes()

    def write(self, data:bytes, timeout:float=None)->int:
        if(self.isclosed()):
            raise IOError('usb is close!')
        if(timeout is not None):
            timeout = int(timeout * 1000) # s -> ms
        return self.__dev.write(self.__OUTEP, data, timeout)

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