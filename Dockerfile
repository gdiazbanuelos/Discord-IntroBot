FROM ubuntu:20.04

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get install -y python3.10 python3-distutils python3-pip python3-apt ffmpeg

RUN pip3 install discord.py asyncio PyNaCl

COPY . .

CMD ["python3", "bot.py"]