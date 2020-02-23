FROM python:3.6

RUN mkdir /chat

COPY s_c.py /chat/s_c.py
WORKDIR /chat
EXPOSE 10000
CMD [ "python", "./s_c.py" ]