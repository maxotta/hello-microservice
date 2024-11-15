FROM ubuntu:20.04
LABEL maintainer="maxmilio@kiv.zcu.cz" \
      org.opencontainers.image.source="https://github.com/maxotta/hello-microservice"

ENV DEBIAN_FRONTEND noninteractive

RUN apt -y update
RUN apt -y install python3
RUN apt -y install python3-pip
RUN pip3 install Flask

RUN mkdir /service
COPY hello-service.py /service/hello-service.py

EXPOSE 5000

CMD ["python3", "/service/hello-service.py"]
