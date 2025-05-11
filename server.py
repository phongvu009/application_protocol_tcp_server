import socket 
import struct 
import json
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
                    json_header_length  = struct.unpack('!H', fixed_length_header)[0]
                    logging.info(f"JSON header length: {json_header_length}")
                    #read JSON header
                    json_header = conn.recv(json_header_length) # sever need to know exactly how many bytes to read
                    json_header = json.loads(json_header.decode('utf-8')) # convert raw byte sequence into json string, then convert into python dictionary
                    logging.debug(f"JSON header: {json_header}")
                    #parse JSON header
                    content_length = json_header['content_length']
                    content_type = json_header['content_type']
                    content_encoding = json_header['content-encoding']

                    #read message content
                    message_content = conn.recv(content_length) # read next chunk
                    if content_encoding == 'utf-8':
                        message_content = message_content.decode('utf-8')
                    logging.info(f"Message content: {message_content}")
                    logging.info(f"Content type: {content_type}, Encoding: {content_encoding}")
    

if __name__ == "__main__":
    HOST='127.0.0.1'
    PORT=6799
    run_server(HOST,PORT)