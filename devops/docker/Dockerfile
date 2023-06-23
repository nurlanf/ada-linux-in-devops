FROM python:3

COPY application /application

RUN pip install -r /application/requirements.txt

WORKDIR /application

EXPOSE 8080

CMD [ "python","script.py" ]