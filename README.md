# Simple Application Protocol

## Overview

- Extend from Echo Server and Client which only handle raw bytes. This implements a TCP server-client application with a custom application protocol header. In simple words, using protocol means both client and server must have argeement on the protocol. Client know how to construct the message and server know how to parse the message.

## Protocol
Understand the Message Structure. The message will have 3 parts: 
- Fixed-length header : 2 bytes, big-endian, unsigned short, store value 0x0000 to 0xFFFF, or 0 - 65535. this length is used to determine the length of the json-header.
- JSON Header: A variable-length UTF-8 encoded dictionary with:
    - byteorder: System byte order (e.g., "big" or "little", optional).
    - content-length: Length of the content in bytes.
    - content-type: Type of the content (e.g., "text/json", "binary/my-binary-type").
    - content-encoding: Encoding of the content (e.g., "utf-8", "binary").
- message_content : actual message content. 

## How to run
### Run server
In current working directory, open new terminal and run:
```bash
python3 server.py
```

### Run client
In current working directory, open new terminal and run:
```bash
python3 client.py
```



    


