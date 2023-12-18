FROM python:3.11
WORKDIR /usr/src/app
RUN apt-get update
RUN git clone https://github.com/gustavozantut/frame_renamer ./
COPY ./frame_renamer/app /usr/src/app
RUN rm -rf ./frame_renamer
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN rm requirements.txt
ENTRYPOINT ["python", "frame_renamer.py"]