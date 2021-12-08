FROM python:latest
WORKDIR /app

COPY . /app/plant_watering
WORKDIR /app/plant_watering

RUN pip install -r requirements.txt
RUN python setup.py install

WORKDIR /app

ENTRYPOINT ["python", "-m", "plantwatering.run"]