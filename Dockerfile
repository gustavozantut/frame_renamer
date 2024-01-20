FROM python:3.11
RUN apt-get update
RUN git clone https://github.com/gustavozantut/frame_renamer/ /usr/src/app/frame_renamer/
WORKDIR /usr/src/app/frame_renamer/
RUN pip install -r ./requirements.txt
RUN rm ./requirements.txt
RUN rm ./Dockerfile
WORKDIR /usr/src/app/frame_renamer/app/
ENTRYPOINT ["python", "frame_renamer.py"]