# Base image
FROM python:3.9-slim

# Working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


# Copy the rest of the project files
COPY . .

RUN python manage.py collectstatic --noinput

# Expose the server port
EXPOSE 8000

# Command to start the server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi"]