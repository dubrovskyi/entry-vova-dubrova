FROM python:3.7-slim

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "hello.py"]
