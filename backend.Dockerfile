FROM python:buster
COPY . /code/
WORKDIR /code
RUN pip install pipenv && \
    pipenv install --deploy --system