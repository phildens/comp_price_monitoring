FROM python:3.7
WORKDIR /usr/src/app
COPY *.py /usr/src/app/
COPY all_models.txt /usr/src/app/
COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./database_connect.py" ]
