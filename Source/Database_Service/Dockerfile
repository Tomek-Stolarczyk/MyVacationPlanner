FROM python:3-onbuild
COPY . /usr/src/app

ENV FLASK_APP=Database_Service.py
RUN pip install ptvsd
CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m flask run -h 0.0.0.0 -p 80