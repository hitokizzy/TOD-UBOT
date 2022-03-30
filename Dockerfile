FROM hitokizzy/ygnyolongbego:slim-buster

#clonning repo 
RUN git clone -b master https://github.com/hitokizzy/ibel-ubot.git /root/ibels \
    && chmod 777 /root/ibels \
    && mkdir /root/ibels/bin/

CMD [ "bash", "start" ]
