FROM python:3.6

RUN mkdir /chat

COPY server.py /chat/server.py
WORKDIR /chat
EXPOSE 10000
CMD [ "python", "./server.py" ]