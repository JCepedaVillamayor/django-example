build: clean
	docker-compose build

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs sudo rm -rf

test:
	docker-compose run web pytest


change-permissions:
	find . -exec sudo chown $(USER):$(USER) {} \;
	find . -type d -exec sudo chmod 755 {} \;
	find . -type f -exec sudo chmod 644 {} \;
