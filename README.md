# fastapi-template

Run
```
uvicorn main:app --reload
```

Docker build
```
sudo docker build -t <image name>:<tag> .
```

Docker Run
```
sudo docker run -p <port>:8080 <container>
```

Test
```
python -m pytest
```

Database migration
```
alembic upgrade head
```