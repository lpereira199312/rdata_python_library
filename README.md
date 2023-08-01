# Rdata Library / python

This is the repository of the Rdata library for the python language.

## Focus

This library must meet some requirements, see the list below:

1. Simple and easy to use.
2. Easy to maintain/upgrade.
3. Reusable

## Usage

```python
import time
import rdata

host = {host}
port = {port}
socket = rdata.load_socket(host,port)
# method insert
request = rdata.insert(socket,"teste","teste","2",'{"name":"rdata"}')
response = rdata.response(socket)
print(response)
time.sleep(10)
# method update
request = rdata.update(socket,"teste","teste","2",'{"new_name":"best rdata"}')
response = rdata.response(socket)
print(response)
time.sleep(10)
# method get with meta
request = rdata.get(socket,"teste","teste","2",1)
response = rdata.response(socket)
print(response)
time.sleep(10)
# method list
request = rdata.list(socket,"teste","teste",10,0)
response = rdata.response(socket)
print(response)
time.sleep(10)
# method delete
request = rdata.delete(socket,"teste","teste","2")
response = rdata.response(socket)
print(response)
socket.close()
```

## Considerations
This library is under development and may change over time. The integrity of existing methods will be maintained to avoid compatibility issues in the future.

## Contributions
You can contribute to the development of the ecosystem by helping to improve this library. Feel free to improve and submit your work with a pull request.


@author Luis Pereira
