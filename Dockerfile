FROM python:3.11-slim

WORKDIR /app

# copy files
COPY . .

# install dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt || true

# default command (you can change this)
CMD ["python3", "scripts/last30days.py", "AI trends"]