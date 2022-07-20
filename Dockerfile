FROM python:3
RUN mkdir /app
ADD . /app
WORKDIR /app
CMD [ "python", "./scrambled_data_challange.py" ]