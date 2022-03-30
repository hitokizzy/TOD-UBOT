FROM hitokizzy/ygnyolongbego:slim-buster

#clonning repo 
RUN git clone -b RAM-UBOT https://github.com/hitokizzy/Ibel-Ubot /home/ibels/
WORKDIR /home/ibels/


CMD ["python3", "-m", "ibels"]
