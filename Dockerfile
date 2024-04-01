FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r require.txt

EXPOSE 8000

CMD ["uvicorn", "base-api:practice_api", "--host", "0.0.0.0", "--port", "8000"]