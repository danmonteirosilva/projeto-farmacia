FROM python:3.9.5
ENV PYTHONUNBUFFERRED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/