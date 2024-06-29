.PHONY: run
run:
	uvicorn src.main:app --reload

.PHONY: lint
lint:
	ruff format
	ruff check --fix

.PHONY: test
test:
	python3 -m pytest

.PHONY: lock
lock:
	poetry export -f requirements.txt -o ./requirements/prod.txt
	poetry export -f requirements.txt -o ./requirements/dev.txt --with dev

.PHONY: deploy
deploy:
	ansible-playbook -i inventory.ini playbook.yml