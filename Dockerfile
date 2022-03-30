FROM hitokizzy/ygnyolongbego:slim-buster

#clonning repo 
RUN git clone -b master https://github.com/hitokizzy/ibel-ubot.git /home/ibels \
    && chmod 777 /home/ibels \
    && mkdir /home/ibels/bin/

CMD [ "bash", "start" ]
