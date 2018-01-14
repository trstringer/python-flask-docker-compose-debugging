FROM python:alpine3.6
WORKDIR /usr/src/app
EXPOSE 8000

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "app:app"]
