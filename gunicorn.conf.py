import os

# Binding to a Unix socket
bind = "unix:/var/run/gunicorn.sock"

# Worker Processes (Adjust based on your needs)
workers = (os.cpu_count() * 2) + 1

# Threading (If applicable)
threads = 1

# Logging
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "info"

# Timeout (Increase if needed for long-running requests)
timeout = 30

# Keepalive (Adjust based on your needs)
keepalive = 2

# Daemonize (Optional, run in the background)
daemon = True