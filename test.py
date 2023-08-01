import time
import rdata

host = "127.0.0.1"
port = 60162
socket = rdata.load_socket(host,port)
# method insert
request = rdata.insert(socket,"teste","teste","2",'{"nome":"luis"}')
response = rdata.response(socket)
print(response)
time.sleep(10)
# method update
request = rdata.update(socket,"teste","teste","2",'{"telegram":"lpereira12"}')
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



