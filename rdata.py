import socket


def load_socket(host,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    return s

def response(socket):
    data = socket.recv(1024).decode
    return data

def insert(socket,collection,book,key,value):
    request = f"&collection={collection}&book={book}&route=collection.books.documents.insert&key={key}&value={value}\n"
    socket.send(request.encode('utf-8'))

def update(socket,collection,book,key,value):
    request = f"&collection={collection}&book={book}&route=collection.books.documents.update&key={key}&value={value}\n"
    socket.send(request.encode('utf-8'))

def get(socket,collection,book,key,meta):
    if(meta=="" or meta==0):
        request =f"&collection={collection}&book={book}&route=collection.books.documents.get&key={key}\n"
    else:
        request = f"&collection={collection}&book={book}&route=collection.books.documents.get&key={key}&meta=1\n"

    socket.send(request.encode('utf-8'))

def list(socket,collection,book,limit,meta):
    request = f"&collection={collection}&book={book}&route=collection.books.documents.list&limit={limit}&meta={meta}\n"
    socket.send(request.encode('utf-8'))

def delete(socket,collection,book,key):
    request = f"&collection={collection}&book={book}&route=collection.books.documents.delete&key={key}\n"
    socket.send(request.encode('utf-8'))
