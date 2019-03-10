FROM python:3.7-alpine

COPY Solutions /Solutions
COPY requirements.txt /Solutions

WORKDIR /Solutions

RUN apk add linux-headers
RUN apk --no-cache --update-cache add bash gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev
RUN wget --quiet --output-document=/etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install pandas

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]

CMD [ "python", "./Solutions/Task_2.py" ]
