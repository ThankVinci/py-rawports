from py_rawports.transport import RawPort, Interface
from py_rawports.interfaces import FileDescriptor
import threading

link = ('/tmp/rawports/rfile', '/tmp/rawports/wfile')

def demo1():
    port = RawPort()
    try:
        port.open(Interface.FileDescriptor, link)
        port.write(b'Little pigs, let me come in.')
        print(port.read(32))
    except Exception as e:
        print(f'{e}')
    finally:
        port.close()

def demo2():
    port = RawPort()
    try:
        port.open(FileDescriptor.Comm().open(link))
        port.write(b'Here\'s Johnny!')
        print(port.read(32))
    except Exception as e:
        print(f'{e}')
    finally:
        port.close()

def demo3():
    def AtoB():
        print('A write to B start')
        link = ('/tmp/rawports/pipe-b-a', '/tmp/rawports/pipe-a-b')
        port = RawPort()
        try:
            port.open(Interface.FileDescriptor, link)
            port.write(b'Little pigs, let me come in.')
            print(port.read(32))
        except Exception as e:
            print(f'{e}')
        finally:
            port.close()

    def BtoA():
        print('B write to A start')
        port = RawPort()
        try:
            link = ('/tmp/rawports/pipe-a-b', '/tmp/rawports/pipe-b-a')
            port.open(Interface.FileDescriptor, link)
            print(port.read(32))
            port.write(b'Little pigs, let me come out.')
        except Exception as e:
            print(f'{e}')
        finally:
            port.close()
    
    threading.Thread(target=AtoB).start()
    threading.Thread(target=BtoA).start()

def main():
    demo1()
    demo2()
    demo3()

if __name__ == '__main__':
    main()
