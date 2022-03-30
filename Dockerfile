FROM hitokizzy/ygnyolongbego:slim-buster

#clonning repo 
RUN git clone -b master https://github.com/hitokizzy/ibel-ubot.git /root/ibels
WORKDIR /root/ibels

ENV PATH="/home/ibels/bin:$PATH"

CMD ["python3","-m","ibels"]
