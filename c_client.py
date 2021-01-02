import socket as sk


cli=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
cli.connect(('localhost',2345))
msg=input('->')

while msg!='bye':
    cli.send(msg.encode('utf-8'))

    data=cli.recv(1024).decode('utf-8')
    print('reply from server:',data)
    msg=input('->')
# cli.close()



