import os
from typing import Tuple

_PathPair = Tuple[str, str] # read_path write_path

class Comm:
    def __init__(self, block:bool=True):
        self.__block:bool = block
        self.__fd_read:int = -1
        self.__fd_write:int = -1
    
    def isclosed(self)->bool:
        if(self.__fd_read == -1 or self.__fd_write == -1):
            return True
        return False

    def isopen(self)->bool:
        return not self.isclosed()
    
    # open fd_r fd_w
    def open(self, pthpair:_PathPair)->bool:
        self.close()
        self.__fd_read = os.open(pthpair[0], os.O_RDONLY)
        self.__fd_write = os.open(pthpair[1], os.O_WRONLY)
        if(self.isclosed()):
            raise IOError('Can not open file descriptor! check file path')
        return self.isopen()

    def close(self)->bool:
        if(not self.isclosed()):
            try:
                os.close(self.__fd_read)
            except:
                pass
            try:
                os.close(self.__fd_write)
            except:
                pass
        self.__fd_read = -1
        self.__fd_write = -1
        return True

    def read(self, len:int, timeout:float=None)->bytes:
        if(self.isclosed()):
            raise IOError('read file descriptor is close!')
        return os.read(self.__fd_read, len)

    def write(self, data:bytes, timeout:float=None)->int:
        if(self.isclosed()):
            raise IOError('write file descriptor is close!')
        return os.write(self.__fd_write, data)

def main():
    comm = Comm()
    try:
        comm.open(('/Users/johnsmith/Desktop/workspace/rfile', '/Users/johnsmith/Desktop/workspace/rfile'))
        comm.write(b'fd message!')
        print(comm.read(32))
    except Exception as e:
        print(f'Exception:{e} ')
    finally:
        comm.close()

if __name__ == '__main__':
    main()