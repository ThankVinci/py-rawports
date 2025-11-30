import socket

def start(data:bytes, host='localhost', port=11451):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        cnt = 0
        while(cnt < 10):
            client_socket.send(data)
            data = client_socket.recv(1024)
            print(f'recv data from server:{data[0:20]}')
            cnt += 1
    except Exception as e:
        print('excetion in client')
    finally:
        client_socket.close()

if __name__ == '__main__':
    start(b'114514')