from py_rawports.transport import Comm, Interface
from py_rawports.interfaces import USB

def demo1():
    comm = Comm()
    try:
        comm.open(Interface.USB, (0x1F3A, 0x3B04))
        comm.write(b'114514')
        print(comm.read(20))
    except Exception as e:
        print(f'{e}')
    finally:
        comm.close()

def demo2():
    comm = Comm()
    try:
        __usbdev = USB.Comm()
        __usbdev.open((0x1F3A, 0x3B04))
        comm.open(__usbdev)
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
