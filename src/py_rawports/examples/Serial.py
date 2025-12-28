from py_rawports.transport import Comm, Interface
from py_rawports.interfaces import Serial

link = (r'\\.\COM7', 115200, 8)

def demo1():
    comm = Comm()
    try:
        comm.open(Interface.Serial, link)
        comm.write(b'Little pigs, let me come in.')
        print(comm.read(32))
    except Exception as e:
        print(f'{e}')
    finally:
        comm.close()

def demo2():
    comm = Comm()
    try:
        __serial = Serial.Comm()
        __serial.open(link)
        comm.open(__serial)
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
