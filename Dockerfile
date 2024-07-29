FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy application code
COPY . /app

# Set the working directory
WORKDIR /app

# Run the application
CMD ["python", "main.py"]
