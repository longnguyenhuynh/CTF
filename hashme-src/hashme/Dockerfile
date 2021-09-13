FROM php:7.4.3-apache

RUN apt-get update

COPY ./src /var/www/html

WORKDIR /var/www/html

RUN chown -R root /var/www/html && chgrp -R root /var/www/html && chmod 755 -R /var/www/html

EXPOSE 80