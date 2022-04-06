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

# WORKDIR /build
# CMD ["/bin/bash", "-c", "make"]
