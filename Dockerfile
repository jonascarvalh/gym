FROM python:3.11.9
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
