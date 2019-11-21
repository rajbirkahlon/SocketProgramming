import socket

print ('UDP client intializing.\n')
with open('README.md') as f:
    content = f.read().splitlines() #writing content of test file to object
contentLen = len(content) #measuring how many lines there are

for x in range(0,contentLen): #for loop to iterate through each test file line captured
    clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print ("Client socket made.")

    message = content[x] #current test file line put into its own object
    print (message, 'is being sent to server.')
    clientSock.sendto(message.encode(), (socket.gethostname(), 1547)) #sendto requires the message being sent (encoded), but also the host name and port number)
    modmessage, serverAddress = clientSock.recvfrom(2049) #message retreived from server when available
    print ('Length of each word returned from server:', modmessage.decode())
    clientSock.close()
    print ('clientSock closed.\n')


