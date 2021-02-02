# streamlit_sample

streamlit sample project

# Installation

1. downlaod data

```bash
cd data
./download.sh
```

2. download elasticsearch plugin 

```bash
cd env/elasticsearch
./download.sh
```

# Usage

## prepare

```bash
docker-compose up
```

Wait for standing up of elasticsearch, and then type command below.

```bash
docker-compose run etl python main.py run 
```

## server run 

```bash
docker-compose up
```

Wait for standing up of elasticsearch, and then access at http://localhost:8501

# License

"streamlit_sample" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

