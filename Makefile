
APP_NAME=app
DOCKER_TAG=latest

devG:
	gunicorn src.main:app -c ./src/infastructure/config/runtime/gunicorn.conf.py

dev:
	python src/main.py

docker: build run

build:
	docker build -t $(APP_NAME):$(DOCKER_TAG) .

run:
	docker run -i -p 2000:2000 --env-file .env $(APP_NAME):$(DOCKER_TAG)

clean:
	docker stop $(APP_NAME) || true
	docker rm $(APP_NAME) || true
	docker rmi $(APP_NAME):latest || true
	find . -type d -name "__pycache__" -exec rm -r {} +
