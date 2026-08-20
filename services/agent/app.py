import socket
import time

def test_connection(host,port):
    try:
        with socket.create_connection((host,port),timeout=3):
            print(f"SUCCESS: {host}:{port} is reachable")
    except Exception as e:
        print(f"ERROR: {host}:{port} is not reachable. Exception: {e}")

    print()

while True:
    test_connection("db-tool",8000)
    test_connection("pdf-tool",8000)
    time.sleep(10)