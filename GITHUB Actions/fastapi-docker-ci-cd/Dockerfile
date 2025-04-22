# Use Ubuntu latest as the base image
FROM ubuntu:latest

# Install dependencies
RUN apt update && apt install -y python3 python3-pip python3-venv

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Create and activate virtual environment, then install dependencies
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port the FastAPI app runs on (change if needed)
EXPOSE 8000

# Command to run the application
CMD ["/app/venv/bin/python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
