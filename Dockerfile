FROM hitokizzy/begoluh:slim-buster

RUN git clone -b master https://github.com/hitokizzy/TOD-UBOT /home/tod/
WORKDIR /home/tod
CMD ["bash", "todubot"]
