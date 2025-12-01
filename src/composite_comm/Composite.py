from enum import IntEnum
from typing import Union
from transports import Socket, USB, Serial

class CommType(IntEnum):
    Socket = 0
    USB = 1
    Serial = 2

class Comm:
    def __init__(self, ):
        self.__comm:Union[Socket.Comm, ] = None
    
    def connect(self, type:CommType, connection:tuple):
        if(type == CommType.Socket):
            self.__comm = Socket.Comm()
            self.__comm.connect(connection)

    def close(self):
        self.__comm.close()
    
    def isclosed(self):
        return self.__comm.isclosed()

    def open(self, idx:int=0):
        self.close()
        self.__comm.open(idx)
    
    def read(self, len:int):
        return self.__comm.read(len)

    def write(self, data:bytes):
        return self.__comm.write(data) 
    
def main():
    comm = Comm()
    try:
        comm.connect(CommType.Socket, ('127.0.0.1', 11451))
        comm.open()
        comm.write(b'114514')
        print(comm.read(20))
    except Exception as e:
        print(f'{e}')
    finally:
        comm.close()

if __name__ == '__main__':
    main()
