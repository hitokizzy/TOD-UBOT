FROM hitokizzy/ibel:slim-buster

#clonning repo 
RUN git clone -b master https://github.com/hitokizzy/TOD-UBOT /home/tod/
WORKDIR /home/tod/


CMD ["python3", "-m", "tod"] & ["python3", "-m", "main.py"]
