FROM python:3.6
EXPOSE 5000
ENV FLASK_ENV=development
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# WORKDIR creates non existing directory and sets it as workdir
WORKDIR /code
COPY requirements.txt /code
RUN pip3 install -r requirements.txt
COPY . /code/