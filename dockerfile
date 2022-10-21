FROM python:3.10.4-alpine3.15

COPY . /app

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD ["python","manage.py","runserver","0.0.0.0:80000"]