FROM python:3.6

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "--bind", ":80", "bringo-backend.wsgi:application"]
