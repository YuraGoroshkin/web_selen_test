FROM python:3.11

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install chromedriver-py
RUN mkdir /usr/src/app/logs
COPY . .
ENTRYPOINT [ "pytest"]