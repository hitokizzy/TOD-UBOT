FROM hitokizzy/ygnyolongbego:slim-buster

#clonning repo 
RUN git clone -b master https://github.com/hitokizzy/Ibel-Ubot /home/ibels/
WORKDIR /home/ibels/


CMD ["python3", "-m", "ibels"]
