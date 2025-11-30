import socket
from typing import Union, List, Tuple

_Address = Tuple[str, int]

class Comm:
    def __init__(self, af:socket.AddressFamily=socket.AF_INET, st:socket.SocketKind=socket.SOCK_STREAM):
        # only support AF_INET and SOCK_STREAM now
        self.__addressfamily = af
        self.__sockettype = st
        self.__address:_Address = None
        self.__socket:socket.socket = None
    
    def close(self):
        if(not self.isclose()):
            self.__socket.close()

    def isclose(self):
        if(self.__socket is None):
            return True
        return False
    
    def connect(self, address:_Address):
        self.__address = address

    def open(self):
        self.close()
        self.__socket = socket.socket(self.__addressfamily, self.__sockettype)
        self.__socket.connect(self.__address)

    def read(self, len:int, timeout:float=None)->bytes:
        if(self.isclose()):
            raise 'socket is close!'
        self.__socket.settimeout(timeout)
        return self.__socket.recv(len)


    def write(self, data:bytes, timeout:float=None):
        if(self.isclose()):
            raise 'socket is close!'
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
        print(f'{e}')
    finally:
        comm.close()

if __name__ == '__main__':
    main()