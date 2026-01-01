import io
from io import BufferedReader, BufferedWriter
from typing import Tuple

_PathPair = Tuple[str, str] # read_path write_path

class Comm:
    def __init__(self, block:bool=True):
        self.__block:bool = block
        self.__reader:BufferedReader = None
        self.__writter:BufferedWriter = None
    
    def isclosed(self)->bool:
        if(self.__reader is None or self.__writter is None):
            return True
        return False
    
    def isopen(self)->bool:
        return not self.isclosed()
    
    # open reader writter
    def open(self, pthpair:_PathPair)->bool:
        self.close()
        self.__reader = io.open(pthpair[0], 'rb')
        self.__writter = io.open(pthpair[1], 'wb')
        if(self.isclosed()):
            raise IOError('Can not open file io! check file path')
        return self.isopen()

    def close(self)->bool:
        if(not self.isclosed()):
            try:
                self.__reader.close()
            except:
                pass
            try:
                self.__writter.close()
            except:
                pass
        self.__reader:BufferedReader = None
        self.__writter:BufferedWriter = None
        return True

    def read(self, len:int, timeout:float=None)->bytes:
        if(self.isclosed()):
            raise IOError('reader is close!')
        return self.__reader.read(len)

    def write(self, data:bytes, timeout:float=None)->int:
        if(self.isclosed()):
            raise IOError('writter is close!')
        len = self.__writter.write(data)
        self.__writter.flush()
        return len

def main():
    comm = Comm()
    try:
        comm.open(('/home/johnsmith/rfile', '/home/johnsmith/wfile'))
        comm.write(b'fileio message!')
        print(comm.read(32))
    except Exception as e:
        print(f'Exception:{e} ')
    finally:
        comm.close()

if __name__ == '__main__':
    main()