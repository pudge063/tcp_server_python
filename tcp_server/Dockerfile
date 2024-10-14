FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
curl \
python3-dev \
libpq-dev \
libxml2-dev \
libxslt1-dev

# Установка зависимостей Python
RUN pip install --upgrade pip && \
pip install requests

# Копирование кода приложения
COPY . /tcp_server

# Запуск сервера
WORKDIR /tcp_server

EXPOSE 9090

CMD ["python", "server.py"]