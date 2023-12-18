FROM python:3.11
WORKDIR /usr/src/app
RUN apt-get update
RUN git clone https://github.com/gustavozantut/yolov5_alpr ./
COPY ./yolov5_alpr/app /usr/src/app
RUN rm -rf ./yolov5_alpr
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN rm requirements.txt
ENTRYPOINT ["python", "frame_renamer.py"]