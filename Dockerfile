FROM python3

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install  -r  requirements.txt 

COPY .  /app

#set a default command 

CDM  python3 main.py 
