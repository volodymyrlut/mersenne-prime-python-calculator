FROM python:3
MAINTAINER Volodymyr Lut "volodymyr@lut.rocks"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["main.py"]
