# # start from base image
# FROM python:3.13.11-slim

# # run this before we do anything
# RUN pip install pandas pyarrow

# # create a folder to working in
# WORKDIR /app

# # copy fileA as fileB in the folder you created
# COPY pipeline.py pipeline.py

# # this will run first thing when container runs
# ENTRYPOINT ["python", "pipeline.py"]




FROM python:3.13.10-slim

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /app

# Add virtual environment to PATH so we can use installed packages
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files first (better layer caching)
COPY "pyproject.toml" "uv.lock" ".python-version" ./

# Install dependencies from lock file (ensures reproducible builds)
RUN uv sync --locked --no-install-project

COPY pipeline.py pipeline.py

# Set entry point
ENTRYPOINT ["python", "pipeline.py"]