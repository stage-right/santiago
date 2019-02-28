FROM alpine:3.5

ARG DO_TKN

ENV DO_TOKEN=$DO_TKN

RUN apk update && apk upgrade && apk add git python py-pip

RUN pip install git+git://github.com/stage-right/santiago.git#egg=santiago

ENTRYPOINT ["santiago"]
