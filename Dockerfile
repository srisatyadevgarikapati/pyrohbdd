
FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
    
RUN pip install pytest-docker


WORKDIR /app
COPY . /app
RUN ls
RUN pip install flask



EXPOSE 5000 

ENTRYPOINT ["python"]

CMD ["app.py"]
