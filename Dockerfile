FROM python:3-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3","-u","./main.py" ]