FROM python:alpine3.19

# Set the working directory in the container
WORKDIR /app

# Alternatively, to be more explicit and potentially avoid other issues:
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the run.py file into the container at /app
COPY run.py /app/

# Run app.py using Gunicorn
CMD ["gunicorn", "-w", "9", "--bind", "unix:/app/gunicorn.sock", "run:app"]
