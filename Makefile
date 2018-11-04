build: clean
	docker-compose build

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs sudo rm -rf

test:
	docker-compose run web pytest

generate-sample-envs:
	mkdir .envs
	touch .envs/.web
	touch .envs/.db
	echo "POSTGRES_USER=sample" >> .envs/.db
	echo "POSTGRES_PASSWORD=sample" >> .envs/.db
	echo "SECRET_KEY=secret" >> .envs/.web
	echo "DJANGO_SETTINGS_MODULE=config.settings.local" >> .envs/.web

change-permissions:
	find . -exec sudo chown $(USER):$(USER) {} \;
	find . -type d -exec sudo chmod 755 {} \;
	find . -type f -exec sudo chmod 644 {} \;
