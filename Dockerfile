# Python base image
FROM python:3.9-slim

# Çalışma dizinine geç
WORKDIR /app

# Gerekli paketleri yükle
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Uygulamayı kopyala
COPY . .

# Uygulamayı başlat
CMD ["python", "app.py"]

