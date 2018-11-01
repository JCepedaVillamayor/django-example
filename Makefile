build: clean
	docker-compose build

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs sudo rm -rf
