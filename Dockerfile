FROM python:3.8-alpine
WORKDIR /app1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python","app1.py"]


