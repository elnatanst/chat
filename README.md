# chat
python 3 terminal chat  server

all the project is with python standard library so no need requirements.txt.

the server can run on docker with the commands:

#build the image::
docker build -t chat .

#run the container with the port and container name::
docker run --name chat -d -p 10000:10000 chat

#run the client
for local docker:
python3 client.py 127.0.0.1

if the docker run on remote server so change the url

#messages format please follow the the format 
register command (if first enter):

register:{your name}
for example :
register:david

send message command:

send:{member name},{member name}:message  

#the server close connection after 60s with timeout

#server logs
the server to console and to file name chat.py
the location on docker is "/chat/chat.log"

to get the log file from the container you can use the command:

docker cp chat:/chat/chat.log . (the "." is the current location you can change it)

#Good luck (to me :blush:)

