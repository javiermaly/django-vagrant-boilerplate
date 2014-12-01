FROM progrium/buildstep
MAINTAINER Alvaro Lizama Molina <nekrox@gmail.com>

ADD src/  /app
RUN apt-get update
RUN apt-get -y install nodejs-legacy npm
RUN npm install -g yuglify
RUN /build/builder
EXPOSE 80
CMD ["/start", "web"]
