import socket
from typing import Union, List, Tuple

_Address = Tuple[str, int]

# a simple check
def checkAddress(address:_Address):
    if(isinstance(address, (list, tuple))):
        if(len(address) == 2 
           and isinstance(address[0], str) 
           and isinstance(address[1], int)):
            return True
    return False

class Comm:
    def __init__(self, af:socket.AddressFamily=socket.AF_INET, st:socket.SocketKind=socket.SOCK_STREAM):
        # only support AF_INET and SOCK_STREAM now
        self.__addressfamily = af
        self.__sockettype = st
        self.__addresses:Tuple[_Address] = None
        self.__socket:socket.socket = None
    
    def close(self):
        if(not self.isclose()):
            self.__socket.close()
        self.__socket = None

    def isclose(self):
        if(self.__socket is None):
            return True
        return False
    
    def connect(self, addresses:Union[_Address, Tuple[_Address]]):
        __addresses = []
        if(checkAddress(addresses)):
            addresses = (addresses, )
        if(isinstance(addresses, (tuple, list))):
            for i in range(len(addresses)):
                if(checkAddress(addresses[i])):
                    __addresses.append(addresses[i])
        self.__addresses = tuple(__addresses)
    
    def open(self, idx:int=0):
        self.close()
        self.__socket = socket.socket(self.__addressfamily, self.__sockettype)
        if(idx >= len(self.__addresses)):
            raise IOError(f'can not open {idx}')
        self.__socket.connect(self.__addresses[idx])

    def read(self, len:int, timeout:float=None)->bytes:
        if(self.isclose()):
            raise IOError('socket is close!')
        self.__socket.settimeout(timeout)
        return self.__socket.recv(len)


    def write(self, data:bytes, timeout:float=None):
        if(self.isclose()):
            raise IOError('socket is close!')
        self.__socket.settimeout(timeout)
        self.__socket.send(data)

def main():
    comm = Comm()
    comm.connect(('127.0.0.1', 11451))
    try:
        comm.open()
        comm.write(b'114514')
        print(comm.read(20))
    except Exception as e:
        print(f'Exception:{e} ')
    finally:
        comm.close()

if __name__ == '__main__':
    main()