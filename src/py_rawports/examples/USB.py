from py_rawports.transport import Comm, Interface
from py_rawports.interfaces import USB

link = (0x1F3A, 0x3B04)

def demo1():
    comm = Comm()
    try:
        comm.open(Interface.USB, link)
        comm.write(b'Little pigs, let me come in.')
        print(comm.read(32))
    except Exception as e:
        print(f'{e}')
    finally:
        comm.close()

def demo2():
    comm = Comm()
    try:
        __usbdev = USB.Comm()
        __usbdev.open(link)
        comm.open(__usbdev)
        comm.write(b'Here\'s Johnny!')
        print(comm.read(32))
    except Exception as e:
        print(f'{e}')
    finally:
        comm.close()

def main():
    demo1()
    demo2()

if __name__ == '__main__':
    main()
