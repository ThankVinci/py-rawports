from enum import IntEnum
from typing import Union
from interfaces import Socket, USB, Serial

class Interface(IntEnum):
    Socket  = 0
    USB     = 1
    Serial  = 2

class Comm:
    __INTF = (Socket.Comm, USB.Comm, Serial.Comm)
    def __init__(self, ):
        self.__comm:Union[Socket.Comm, USB.Comm, Serial.Comm] = None
    
    def open(self, *args)->bool:
        if(isinstance(args[0], Comm.__INTF)):
            self.__open_instance(*args)
        else:
            self.__new_interface(*args)
        return self.isopen()
    
    # open a communication instance
    def __open_instance(self, instance:Union[Socket.Comm, USB.Comm, Serial.Comm]):
        self.close()
        self.__comm = instance

    # create an interface using default parameters
    def __new_interface(self, type:Interface, connection:tuple):
        self.close()
        self.__comm = Comm.__INTF[type]()
        self.__comm.open(connection)
    
    def isopen(self)->bool:
        return self.__comm.isopen()

    def close(self)->bool:
        if(not self.isclosed()):
            self.__comm.close()
        return True
    
    def isclosed(self)->bool:
        return self.__comm is None or self.__comm.isclosed()
    
    def read(self, len:int, timeout:float = None)->bytes:
        return self.__comm.read(len, timeout)

    def write(self, data:bytes, timeout:float = None)->int:
        return self.__comm.write(data, timeout) 
    
def main():
    comm = Comm()
    try:
        __socket = Socket.Comm()
        __socket.open(('127.0.0.1', 11451))
        comm.open(__socket)
        comm.write(b'114514')
        print(comm.read(20))
    except Exception as e:
        print(f'{e}')
    finally:
        comm.close()

if __name__ == '__main__':
    main()
