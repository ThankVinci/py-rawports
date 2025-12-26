import socket
from typing import Union, List, Tuple

_Address = Tuple[str, int]

# a simple check
def checkAddress(address:_Address)->bool:
    if(isinstance(address, (list, tuple))):
        if(len(address) == 2 
           and isinstance(address[0], str) 
           and isinstance(address[1], int)):
            return True
    return False

class Comm:
    def __init__(self, AF:socket.AddressFamily=socket.AF_INET, SK:socket.SocketKind=socket.SOCK_STREAM):
        self.__AddressFamily:socket.AddressFamily = AF
        self.__SocketKind:socket.SocketKind = SK
        self.__socket:socket.socket = None
    
    # open a socket connection
    def open(self, address:_Address)->bool:
        self.close()
        if(checkAddress(address)):
            self.__socket = socket.socket(self.__AddressFamily, self.__SocketKind)
            try:
                self.__socket.connect(address)
            except:
                self.close()
        return self.isopen()

    def isopen(self)->bool:
        return self.__socket is not None
    
    def close(self)->bool:
        if(not self.isclosed()):
            self.__socket.close()
        self.__socket = None
        return True

    def isclosed(self)->bool:
        if(self.__socket is None):
            return True
        return False
    
    def read(self, len:int, timeout:float=None)->bytes:
        if(self.isclosed()):
            raise IOError('socket is close!')
        self.__socket.settimeout(timeout)
        return self.__socket.recv(len)

    def write(self, data:bytes, timeout:float=None)->int:
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