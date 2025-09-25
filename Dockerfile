FROM astral/uv:python3.9-trixie-slim
ADD requirements.txt /app/requirements.txt
ADD main.py /app/main.py
ADD pyproject.toml /app/pyproject.toml
WORKDIR /app
RUN uv add -r requirements.txt
RUN uv sync --locked
CMD ["uv", "run", "main.py"]