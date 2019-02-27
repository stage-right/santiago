FROM alpine:latest

ARG DO_TKN

ENV DO_TOKEN=$DO_TKN

RUN apk update && apk upgrade && apk add git

RUN pip install git+git://github.com/stage-right/santiago.git#egg=santiago

ENTRYPOINT ["santiago"]
