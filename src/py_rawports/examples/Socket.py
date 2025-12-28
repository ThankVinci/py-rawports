from py_rawports.transport import Comm, Interface
from py_rawports.interfaces import Socket

link = ('127.0.0.1', 11451)

def demo1():
    comm = Comm()
    try:
        comm.open(Interface.Socket, link)
        comm.write(b'Little pigs, let me come in.')
        print(comm.read(32))
    except Exception as e:
        print(f'{e}')
    finally:
        comm.close()

def demo2():
    comm = Comm()
    try:
        __socket = Socket.Comm()
        __socket.open(link)
        comm.open(__socket)
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
