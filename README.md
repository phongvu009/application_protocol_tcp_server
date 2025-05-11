# Simple Application Protocol

## Overview

- Extend from Echo Server and Client which only handle raw bytes. This implements a TCP server-client application with a custom application protocol header. Using an application protocol header, especially a fixed-length one, provides structure to raw byte streams. This header acts like a label, defining message boundaries and carrying essential metadata like content length and message type. This enables receivers to efficiently parse, interpret, and process messages correctly. It also supports protocol evolution and improves error handling compared to dealing with unstructured raw bytes. Ultimately, headers ensure reliable and organized communication between applications.

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



    


