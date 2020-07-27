FROM python:3.6
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE 9091

CMD [ "python", "src/app.py" ]


