import socket as sk
# import logging as lg



# lg.basicConfig(filename='server.log',level=lg.DEBUG)
s=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
s.bind(('localhost',2345))
s.listen(2)
c,add=s.accept()
# lg.info('got connection from',add)
print('got connection from',add)
while True:
    rc_data=c.recv(1024).decode('utf-8')
    # lg.info('from client:' , rc_data)
    print('from client:' , rc_data)
    rc_data=input('->')
    c.send(rc_data.encode('utf-8'))

