FROM hitokizzy/ygnyolongbego:slim-buster

#clonning repo 
RUN git clone -b master https://github.com/hitokizzy/ibel-ubot.git /root/userbot
WORKDIR /root/userbot

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","ibels"]
