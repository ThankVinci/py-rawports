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
        self.__address:_Address = None
        self.__socket:socket.socket = None
    
    def close(self):
        if(not self.isclosed()):
            self.__socket.close()
        self.__socket = None

    def isclosed(self):
        if(self.__socket is None):
            return True
        return False
    
    def open(self, address:_Address):
        self.close()
        if(checkAddress(address)):
            self.__address = address
            self.__socket = socket.socket(self.__addressfamily, self.__sockettype)
            self.__socket.connect(self.__address)

    def read(self, len:int, timeout:float=None)->bytes:
        if(self.isclosed()):
            raise IOError('socket is close!')
        self.__socket.settimeout(timeout)
        return self.__socket.recv(len)


    def write(self, data:bytes, timeout:float=None):
        if(self.isclosed()):
            raise IOError('socket is close!')
        self.__socket.settimeout(timeout)
        return self.__socket.send(data)

def main():
    comm = Comm()
    try:
        comm.open(('127.0.0.1', 11451))
        comm.write(b'114514')
        print(comm.read(20))
    except Exception as e:
        print(f'Exception:{e} ')
    finally:
        comm.close()

if __name__ == '__main__':
    main()