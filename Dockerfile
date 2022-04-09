FROM ubuntu:focal-20220316

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt -y --no-install-recommends install gcc \
                                                                          g++ \
                                                                          python3 \
                                                                          python3-dev \
                                                                          python3-pip && \
    apt clean

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

COPY dfk_notifier dfk_notifier
COPY config.json config.json

CMD ["python3", "dfk_notifier", "--config", "./config.json"]
