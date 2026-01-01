from __future__ import annotations
import io
from typing import Tuple

_PathPair = Tuple[str, str] # read_path write_path

class Comm:
    def __init__(self, block:bool=True):
        self.__block:bool = block
        self.__reader:io.BufferedReader = None
        self.__writer:io.BufferedWriter = None
    
    def isclosed(self)->bool:
        if(self.__reader is None or self.__writer is None):
            return True
        return False
    
    def isopen(self)->bool:
        return not self.isclosed()
    
    # open reader writter
    def open(self, pthpair:_PathPair)->Comm:
        self.close()
        self.__reader = open(pthpair[0], 'rb')
        self.__writer = open(pthpair[1], 'wb')
        if(self.isclosed()):
            raise IOError('Can not open file io! check file path')
        return self

    def close(self)->bool:
        if(not self.isclosed()):
            if(self.__reader is not None):
                try:
                    self.__reader.close()
                finally:
                    self.__reader = None
            if(self.__writer is not None):
                try:
                    self.__writer.close()
                finally:
                    self.__writer = None
        return True

    def read(self, len:int, timeout:float=None)->bytes:
        if(self.isclosed()):
            raise IOError('reader is close!')
        return self.__reader.read(len)

    def write(self, data:bytes, timeout:float=None)->int:
        if(self.isclosed()):
            raise IOError('writter is close!')
        len = self.__writer.write(data)
        self.__writer.flush()
        return len

def main():
    comm = Comm()
    try:
        comm.open(('/tmp/rawports/rfile', '/tmp/rawports/wfile'))
        comm.write(b'fileio message!')
        print(comm.read(32))
    except Exception as e:
        print(f'Exception:{e} ')
    finally:
        comm.close()

if __name__ == '__main__':
    main()