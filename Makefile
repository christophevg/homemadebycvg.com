all: run

run: .venv
	uv run gunicorn __init__:app

.venv:
	uv add -r requirements.base.txt

clean:
	rm -rf .venv
