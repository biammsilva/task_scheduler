FROM python:3.8.2-alpine

WORKDIR /app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv

RUN pipenv install --system --deploy

COPY . /app/

CMD ["python", "manage.py", "runserver"]
