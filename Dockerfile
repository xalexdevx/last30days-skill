FROM python:3.11-slim

WORKDIR /app

# copy files
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# run with uvicorn on Railway's dynamic port
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]