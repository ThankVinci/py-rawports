from py_rawports.transport import Comm, Interface
from py_rawports.interfaces import Serial

def demo1():
    comm = Comm()
    try:
        comm.open(Interface.Serial, (0x1F3A, 0x3B04))
        comm.write(b'114514')
        print(comm.read(20))
    except Exception as e:
        print(f'{e}')
    finally:
        comm.close()

def demo2():
    comm = Comm()
    try:
        __serial = Serial.Comm()
        __serial.open((r'\\.\COM7', 115200, 8))
        comm.open(__serial)
        comm.write(b'114514')
        print(comm.read(20))
    except Exception as e:
        print(f'{e}')
    finally:
        comm.close()

def main():
    # demo1()
    demo2()

if __name__ == '__main__':
    main()
