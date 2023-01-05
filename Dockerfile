FROM python:3.11.1

COPY . /usr/src/stori-test

WORKDIR /usr/src/stori-test

RUN python3 -m pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]