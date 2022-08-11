FROM python:3.10-slim

# Curl for test and vim for edit
#RUN apt-get update -y && \
#    apt-get install -y \
#    vim \
#    curl

WORKDIR /app

COPY ./req.txt /app/req.txt

RUN pip install -r req.txt

COPY app ./

CMD ["python", "app.py"]