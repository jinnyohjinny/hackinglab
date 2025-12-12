FROM alpine:3.18

RUN apk add --no-cache \
    apache2 \
    apache2-utils \
    perl \
    perl-cgi \
    perl-json

RUN mkdir -p /var/www/localhost/cgi-bin \
    && mkdir -p /var/www/localhost/static \
    && mkdir -p /run/apache2 \
    && chown -R apache:apache /var/www/localhost

COPY cgi-bin/ /var/www/localhost/cgi-bin/
COPY static/ /var/www/localhost/static/
COPY httpd.conf /etc/apache2/httpd.conf

RUN chmod +x /var/www/localhost/cgi-bin/*.cgi \
    && chown -R apache:apache /var/www/localhost

EXPOSE 80

CMD ["httpd", "-D", "FOREGROUND"]
