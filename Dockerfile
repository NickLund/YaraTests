FROM buildpack-deps:buster as libbuild
RUN apt-get update; apt-get install -y autoconf automake bison flex gcc libssl1.1:amd64 libssl-dev libtool make; rm -rf /var/lib/apt/lists/*;
COPY . /src/yara
WORKDIR /src/yara
RUN export DESTDIR=/opt/yara;/src/yara/bootstrap.sh; /src/yara/configure; rm /src/yara/libyara/grammar.c; rm /src/yara/libyara/lexer.c;  make; make install

FROM python:3 as pybuild
COPY --from=libbuild /opt/yara /
WORKDIR /root
RUN git clone https://github.com/VirusTotal/yara-python
WORKDIR /root/yara-python
RUN mkdir -p /opt/yara-python; python setup.py build --dynamic-linking; python setup.py install --root /opt/yara-python;

FROM python:3 as release
RUN apt-get update; apt-get install -y vim; apt-get clean; rm -rf /var/lib/apt/lists/*;
COPY --from=libbuild /opt/yara /
COPY --from=pybuild /opt/yara-python /
RUN ldconfig;
