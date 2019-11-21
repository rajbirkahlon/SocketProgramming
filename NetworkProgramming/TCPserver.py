import socket

print ('TCP server intializing.\n')
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Server socket made.')
serverSock.bind((socket.gethostname(), 1546))
serverSock.listen(1)
print ('Server is ready.')

while True:
    connSock, addr = serverSock.accept() #create connection socket when cleint connects and capture address to return data to later
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
    sentence = connSock.recv(1025).decode() #message converted from encoded byte back to original form
    wordArray = sentence.split(' ') #seperate sentence to individual strings of words
    print ('The words in the message are:', wordArray) #check if done properly
    lenmax = len(wordArray) #how many words in the line
    countArray = "" #used to capture the length of each word later

    x = 0 #used in following while loop
    while x<lenmax: #do following for each word
        lw = len(wordArray[x]) #capture length of word into an object
        print (wordArray[x],' has lw: ', lw) #display what is length of current word being processed
        countArray = countArray+ " " + str(lw) #store length of current word into count string
        print ('countArray so far is: ', countArray) #keep track of count string so far
        x = x+1 #move onto next word
    connSock.send(countArray.encode()) #send count string back to client
    connSock.close() #close this connection socket because the client's request has been completed
    print('commSock closed.')



