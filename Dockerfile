FROM python:3.9.5
ENV PYTHONUNBUFFERRED=1
WORKDIR /pycharm
COPY requirements.txt /pycharm/
RUN pip install -r requirements.txt
COPY . /pycharm/