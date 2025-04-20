FROM ubuntu:latest
LABEL authors="korot"

ENTRYPOINT ["top", "-b"]