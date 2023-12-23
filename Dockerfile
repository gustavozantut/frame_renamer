FROM python:3.11-slim
RUN apt-get update
RUN git clone https://github.com/gustavozantut/frame_renamer/ /usr/src/app/frame_renamer/
WORKDIR /usr/src/app/frame_renamer/
RUN pip install -r ./requirements.txt
RUN rm ./requirements.txt
ENTRYPOINT ["python", "frame_renamer.py"]