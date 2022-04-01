FROM hitokizzy/ibel:slim-buster

#clonning repo 
RUN git clone -b master https://github.com/hitokizzy/TOD-todUBOT /home/tod/
WORKDIR /home/tod/


CMD ["python3", "-m", "tod"] 
