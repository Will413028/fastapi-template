# fastapi-template

## How to Run

### Run the Server

```bash
make run
```

### Code lint

```bash
make lint
```

### Run Tests

```bash
make test
```

### Export Requirements
```bash
make lock
```

### Deploy to remote server by ansible
```bash
make deploy
```

### Docker

#### Build Image

```bash
sudo docker build -t <image_name>:<tag> .
```

#### Run Docker Container

```bash
docker run --name test -p 8000:8000
```

### Database Operations

#### Auto-generate Migration

```bash
alembic revision --autogenerate -m "migration message"
```

#### Database Migration

```bash
alembic upgrade head
```

### Docker Compose

```bash
sudo docker-compose up -d --build
```

### Virtual Environment

#### Create Virtual Environment

```bash
poetry shell
```

### Pre-commit

Install Pre-commit Hooks

```bash
pre-commit install
```

### Dependency Management

Install Dependencies

```bash
poetry install
```

### Add Dependency
```bash
poetry add <library_name>
```

### Add Dependency to dev
```bash
poetry add <library_name> --dev
```
