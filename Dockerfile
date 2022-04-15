FROM hitokizzy/begoluh:slim-buster
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
RUN git clone -b dev1 https://github.com/hitokizzy/TOD-UBOT /home/tod/
WORKDIR /home/tod
CMD ["bash", "todubot"]