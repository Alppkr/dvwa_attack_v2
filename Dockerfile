FROM python:3.11-slim
RUN addgroup -S nonroot \
    && adduser -S nonroot -G nonroot
USER nonroot
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
CMD python3 -u /app/main.py
