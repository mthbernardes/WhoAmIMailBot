FROM debian

MAINTAINER Matheus Bernardes <mthbernardes@gmail.com>
EXPOSE 25
WORKDIR /opt/mailbot
COPY . $WORKDIR
ARG domain
RUN mkdir /data
RUN echo "postfix postfix/mailname string $domain" | debconf-set-selections
RUN echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-set-selections 
RUN apt update && apt -y upgrade && apt install -y postfix python3 python3-pip
RUN pip3 install telepot
RUN postconf -e 'virtual_alias_maps= hash:/data/virtual'
RUN /etc/init.d/postfix start
ENTRYPOINT ["python3","mailbot.py"]
