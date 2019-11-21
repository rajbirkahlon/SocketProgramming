import socket

print ('UDP server intializing.\n')
serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print ("Server socket made.")
serverSock.bind((socket.gethostname(), 1547)) #bind using socket library function gethostname() and custom port number
print ('Server is ready.')

while True:
    message, addr= serverSock.recvfrom(2049) #stores message and addr of client so it can send data back later
    modmessage = message.decode() #message converted from encoded byte back to original form
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    print ('message is: ', modmessage)
    wordArray = modmessage.split(' ') #seperate sentence to individual strings of words
    print('The words in the message are:', wordArray) #check if done properly
    lenmax = len(wordArray) #how many words in the line
    countArray = "" #used to capture the length of each word later
    print('lenmax is: ', lenmax)

    x = 0
    while x < lenmax: #do following for each word
        lw = len(wordArray[x]) #capture length of word into an object
        print(wordArray[x], ' has lw: ', lw) #display what is length of current word being processed
        countArray = countArray + " " + str(lw) #store length of current word into count string
        print('countArray so far is: ', countArray) #keep track of count string so far
        x = x + 1 #move onto next word
    serverSock.sendto(countArray.encode(),addr) #send count string back to client
    print ('Server is ready again.\n')


