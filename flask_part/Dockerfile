FROM python:3.7
WORKDIR /usr/src/app
COPY main.py /usr/src/app/
COPY requirements.txt /usr/src/app/
COPY templates/ /usr/src/app/templates/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

CMD [ "python", "./main.py" ]