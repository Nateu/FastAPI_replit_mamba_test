run: api test

test:
	poetry run mamba --format=documentation --enable-coverage specs/*_spec.py && coverage html

api:
	cd /home/runner/FastAPI/api && uvicorn main:app --reload --host 0.0.0.0 --port 8080 &

cov:
	nohup python -m http.server 8000 -d htmlcov &
