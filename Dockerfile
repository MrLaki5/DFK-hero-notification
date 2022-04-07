FROM ubuntu:focal-20220316

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt -y --no-install-recommends install   gcc \
                                                                            g++ \
                                                                            python3 \
                                                                            python3-dev \
                                                                            python3-pip && \
    apt clean

RUN pip3 install --upgrade pip && \
    pip3 install web3

COPY dfk_hero.py dfk_hero.py
COPY email_client.py email_client.py
COPY worker.py worker.py
COPY config.json config.json

CMD ["python3", "./worker.py", "--config", "./config.json"]
