FROM docker.elastic.co/elasticsearch/elasticsearch:7.10.0

WORKDIR /usr/share/elasticsearch
RUN mkdir /etc/elasticsearch
RUN mkdir /etc/elasticsearch/sudachi

COPY analysis-sudachi-7.10.0-2.1.0.zip /usr/share/elasticsearch/

RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install file:////usr/share/elasticsearch/analysis-sudachi-7.10.0-2.1.0.zip
COPY sudachi-dictionary-20201223/system_full.dic /usr/share/elasticsearch/config/sudachi/system_core.dic
COPY sudachi.json /usr/share/elasticsearch/config/sudachi

USER 1000:1000
