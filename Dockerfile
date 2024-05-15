FROM python:3.12.1-slim

WORKDIR /usr/src/app

# Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY ./requirements/prod.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
