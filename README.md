# fastapi-template

## How to Run

### Run the Server

```bash
uvicorn src.main:app --reload
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

### Ansible deploy 
```bash
ansible-playbook -i inventory.ini playbook.yml
```

### Testing

Run Tests

```bash
python -m pytest
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
poetry add <library_name> --dev-dependency
```

### Export Requirements

Export Requirements to Text Files

```bash
poetry export -f requirements.txt -o ./requirements/prod.txt
```

```bash
poetry export -f requirements.txt -o ./requirements/dev.txt --with dev
```

### Code Formatting

```bash
ruff check --fix

ruff format
```

### Additional Libraries

#### Structlog

Reference: [Structlog](https://myapollo.com.tw/blog/python-structlog/)

#### IceCream

Reference: [IceCream Module](https://myapollo.com.tw/blog/python-module-icecream/)

#### Better-Exceptions

Reference: [Better-Exceptions](https://myapollo.com.tw/blog/python-better-exceptions/)

#### Rich

Reference: [Rich Library](https://github.com/Textualize/rich)

### VS Code Debugger Configuration

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: FastAPI",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "src.main:app",
                "--reload"
            ],
            "jinja": true
        }
    ]
}
```