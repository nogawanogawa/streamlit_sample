#!/bin/sh

wget https://github.com/WorksApplications/elasticsearch-sudachi/releases/download/v2.1.0/analysis-sudachi-7.10.0-2.1.0.zip
wget http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict/sudachi-dictionary-20201223-full.zip
unzip sudachi-dictionary-20201223-full.zip
rm sudachi-dictionary-20201223-full.zip