import socket 
import struct 
import logging

logging.basicConfig(level=logging.DEBUG)

def run_server(host,port):
    #create socket server
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            #option
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((host,port))
            server.listen()
            logging.info(f"Server started !!!- listening on {host}:{port}")
            while True:
                conn, addr = server.accept()
                with conn:
                    logging.info(f"Connected by {addr}")
                    #read fixed-length header (2bytes, big-endian)
                    fixed_length_header = conn.recv(2)
                    logging.debug(f"Fixed length header: {fixed_length_header}")
                    if not fixed_length_header: #if b'' close connection
                        break
                    #! : !Network byte order, 
                    #H : 2bytes-16bits, unsigned short, in range 0x0000 to 0xFFFF or 0 to 65535.
                    #!H : Universal Network byte order, 
                    json_header_length = struct.unpack('!H', fixed_length_header)
                    logging.info(f"JSON header length: {json_header_length}")
    

if __name__ == "__main__":
    HOST='127.0.0.1'
    PORT=6799
    run_server(HOST,PORT)