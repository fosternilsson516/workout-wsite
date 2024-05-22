# Workout Plan Website

## Summary
This is a website I built for my friend. This website is only for display and can be viewed at: [Workout-site](https://ployease.com) its still currently a work in progress and is not reusable.

## Stack and Tools
This website showcases my full stack and networking skills. Here are the details of the stack and tools I used to build it:

### Server Side
- **Flask** and **Python**: The server side is built using Flask and Python.
- **Database**: I used `psycopg2` directly with a PostgreSQL server, without SQLAlchemy. While the website does not involve any complex SQL operations, I prefer having fine-grained control over the database server. This setup also allows me to practice using `psql` and general DB Admin tasks.
- **Email Server**: I set up a `Flask-Mail` server that is initialized with the application.

### Client Side
- **JavaScript, HTML, and CSS**: The client side is built with simple JS, HTML, and CSS, without any frameworks.

## Network Stack
The network stack for this website is quite intricate, designed to display my networking skills and understanding of various technologies. Here's how it's set up:

### Cloud Server
- **Operating System**: Ubuntu 22.04
- **Docker**: Pre-built image to run an Nginx container.

### Nginx Container
- **Reverse Proxy**: Nginx container with a reverse proxy that points to the container's IP (not the host) and a specific port using Docker bridge mode.
- **SSL**: SSL is installed directly on the host cloud server. The Nginx container has ports 443 and 80 open with volume mounts for dynamic updates of the SSL certificates.

### Reverse SSH Tunnel
- **Setup**: Traffic is forwarded through a reverse SSH tunnel established from a Linux (Ubuntu) based container running on my physical Proxmox host (Type 1 Hypervisor).
- **Application Hosting**: This container holds my Flask application and uses Gunicorn for serving the website.
- **Database Hosting**: Another LXC container runs the PostgreSQL database.

### Security
- **Firewall**: UFW is used to lock down all ports except for the necessary ones, ensuring secure communication between containers.

### Benefits of the Setup
- **Network Isolation**: Nginx, and the application + database containers run on separate hosts, providing network isolation.
- **SSH Encryption**: Using SSH encryption for security.
- **Firewall Bypass**: The reverse SSH tunnel allows bypassing any local network firewalls if needed.
- **Efficiency**: Nginx is efficient and lightweight, allowing multiple Nginx containers to run on a small cloud server, each serving different websites.

## Future Enhancements
My next tasks include adding easier health management tools like Prometheus, along with Terraform for automated deployment of new sites, and Jenkins for Continuous Deployment/Continuous Integration (CD/CI).

