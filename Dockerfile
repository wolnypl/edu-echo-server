

ARG WERSJAOS="8.5"
FROM rockylinux:$WERSJAOS
ARG WERSJAOS="v8.5"
#usedadd only for example purposes
RUN useradd nobleprog 
RUN ["echo", "nobleprog", "|", "passwd", "--stdin", "nobleprog"]
RUN yum -y update; yum -y install vim iproute httpd python3-mod_wsgi; yum clean all
ENTRYPOINT ["/entrypoint.sh"]


LABEL version="3.0"
LABEL org.opencontainers.image.authors="Peter_F"
EXPOSE 80/tcp
ENV WERSJA="3.0"
ENV DYSTRYBUCJA rockylinux

VOLUME /dane

USER nobleprog 
WORKDIR /home/nobleprog
RUN pwd 
ADD dane.txt .
RUN mkdir $WERSJAOS 
USER root
ADD entrypoint.sh /
COPY hello.py /var/www/wsgi/hello.py
COPY Dockerfile /
#RUN echo "WSGIScriptAlias /hello /var/www/wsgi/hello.py" >/etc/httpd/conf.d/hello.conf
RUN echo "WSGIScriptAlias / /var/www/wsgi/hello.py" >/etc/httpd/conf.d/hello.conf

