FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn pydantic

COPY . .

EXPOSE 8000

CMD ["uvicorn", "consql:app", "--host", "0.0.0.0", "--port", "8000"]
