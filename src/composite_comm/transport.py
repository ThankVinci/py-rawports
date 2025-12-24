from enum import IntEnum, Enum
from typing import Union
from interfaces import Socket, USB, Serial

class Interface(Enum):
    Socket  = 0
    USB     = 1
    Serial  = 2

class Comm:
    __INTF = (Socket.Comm, USB.Comm, Serial.Comm)
    def __init__(self, ):
        self.__comm:Union[Socket.Comm, ] = None
    
    def open(self, type:Interface, connection:tuple):
        self.close()
        self.__comm = Comm.__INTF[type]()
        self.__comm.open(connection)

    def close(self):
        if(not self.isclosed()):
            self.__comm.close()
    
    def isclosed(self):
        return self.__comm is None or self.__comm.isclosed()
    
    def read(self, len:int):
        return self.__comm.read(len)

    def write(self, data:bytes):
        return self.__comm.write(data) 
    
def main():
    comm = Comm()
    try:
        comm.open(Interface.Socket, ('127.0.0.1', 11451))
        comm.write(b'114514')
        print(comm.read(20))
    except Exception as e:
        print(f'{e}')
    finally:
        comm.close()

if __name__ == '__main__':
    main()
