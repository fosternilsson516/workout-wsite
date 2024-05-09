FROM python:alpine3.19

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py using Gunicorn
CMD ["gunicorn", "-w", "9", "--bind", "unix:/app/gunicorn.sock", "run:app"]
