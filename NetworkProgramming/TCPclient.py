import socket

print ('TCP client intializing.\n')
with open('README.md') as f:
    content = f.read().splitlines() #writing content of test file to object
contentLen = len(content) #measuring how many lines there are

for x in range(0,contentLen): #for loop to iterate through each test file line captured
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Client socket made.")
    print('Connecting to host.')
    clientSock.connect((socket.gethostname(), 1546))
    print('Client connected to host.')
    sentence = content[x] #current test file line put into its own object
    print (sentence, " is being sent to server.")
    clientSock.send(sentence.encode())
    print ('Sentence encoded and sent.')
    modSentence = clientSock.recv(1025) #message retreived from server when available
    print ('Length of each word returned from server:', modSentence.decode())
    clientSock.close()
    print ('clientSock closed.\n')