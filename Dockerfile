FROM hitokizzy/begoluh:slim-buster

RUN git clone -b master https://github.com/hitokizzy/TOD-UBOT /home/tod/
WORKDIR /home/tod
CMD ["python3","-m","tod"]
