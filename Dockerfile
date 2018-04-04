FROM debian:latest

LABEL author="@mthbernardes"
LABEL collaborator="@btamburi"

WORKDIR /opt/mailbot

COPY run.sh $WORKDIR
COPY mailbot.py $WORKDIR

RUN mkdir /data
RUN echo "postfix postfix/mailname string mail.example.com" | debconf-set-selections
RUN echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-set-selections
RUN apt update && apt -y upgrade && apt install -y postfix python3 python3-pip && pip3 install telepot
RUN chmod +x /opt/mailbot/run.sh
RUN postconf -e 'virtual_alias_maps= hash:/data/virtual'
RUN /etc/init.d/postfix start

EXPOSE 25

ENTRYPOINT ["/opt/mailbot/run.sh"]
