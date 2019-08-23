
FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
    
RUN pip install docker-py feedparser nosexcover prometheus_client pycobertura pylint pytest pytest-cov requests setuptools sphinx
RUN wget -qO /usr/local/bin/qcoverage  https://github.com/qnib/qcoverage/releases/download/v0.1/qcoverage_v0.1_Linux \
 && chmod +x /usr/local/bin/qcoverage

WORKDIR /app
COPY . /app

RUN pip install flask



EXPOSE 5000 

ENTRYPOINT ["python"]

CMD ["app.py"]
