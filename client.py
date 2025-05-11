import socket
import logging
import sys
import json
import struct

logging.basicConfig(level=logging.DEBUG)

def run_client(host,port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host,port))
        #instead seding raw bytes , we will send protocol message

        #prepare message content
        content = "Hello, World"
        content_bytes = content.encode('utf-8') #encode binary -> decimal -> utf-8: text
        logging.debug(f"Content bytes: {content_bytes}")
        content_length = len(content_bytes) # length of message
        logging.debug(f"Content length: {content_length}")

        #create JSON header
        json_header = {
            'byteorder' : sys.byteorder, #byte order : big-endian or little-endian
            'content_length' : content_length,
            'content_type' : 'text/plain',
            'content-encoding': 'utf-8'
        }
        #convert json type into json string , then convert into byte sequence
        json_header_bytes = json.dumps(json_header).encode('utf-8')
        logging.debug(f"JSON header bytes: {json_header_bytes}")
        #H → 0x48
        #logging.debug(f"JSON header in HEX: {json_header_bytes.hex()}")
        json_header_length = len(json_header_bytes)
        logging.debug(f"JSON header length: {json_header_length}")

        #Create fixed-length header (2bytes, big-endian) - num oflength in 2 bytes
        #!H : big-endian, unsigned short , store value 0x0000 to 0xFFFF, or 0 - 65535
        fixed_length_header = struct.pack('!H', json_header_length)
        logging.debug(f"Metadata header bytes: {fixed_length_header}")

        #[2-byte length][JSON header][Message content]
        #[2-byte length] : how big JSON header is -2 bytes
        #JSON header : metadata about message content - 104 bytes
        #Message content : actual message - 12 bytes
        message = fixed_length_header + json_header_bytes + content_bytes
        logging.debug(f"Message bytes: {message}")
        logging.debug(f"Message length: {len(message)}") 
        #send message to server
        client.sendall(message)
        



if __name__ == "__main__":
    HOST='127.0.0.1'
    PORT=6799   
    run_client(HOST,PORT)