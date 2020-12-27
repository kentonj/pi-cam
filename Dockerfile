FROM python:3.9-buster

RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install ffmpeg libsm6 libxext6 -y

RUN mkdir /pi-cam
WORKDIR /pi-cam

ENV READTHEDOCS=True
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh
COPY ./app.py ./app.py
COPY ./src ./src

ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "./entrypoint.sh" ]
CMD [ "serve" ]
