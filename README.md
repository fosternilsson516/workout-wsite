# Workout Plan Website

## Summary
This is a website I built for my friend. This website is only for display and can be viewed at: [Workout-site](https://mark-kuhpal.ployease.com) its still currently a work in progress and is not reusable.

## Stack and Tools
This website showcases my full stack and networking skills. Here are the details of the stack and tools I used to build it:

### Server Side
- **Flask** and **Python**: The server side is built using Flask and Python.
- **Database**: I used `psycopg2` directly with a PostgreSQL server, without SQLAlchemy. While the website does not involve any complex SQL operations, I prefer having fine-grained control over the database server. This setup also allows me to practice using `psql` and general DB Admin tasks.
- **Email Server**: I set up a `Flask-Mail` server that is initialized with the application.

### Client Side
- **JavaScript, HTML, and CSS**: The client side is built with simple JS, HTML, and CSS, without any frameworks.

## Network Stack
I was able to simplify my network quite a bit with cloudflare. Here's how it's set up:

### Proxmox Containers
- **Reverse Proxy**: Nginx container with a reverse proxy that points to the port my gunicorn server is running on.
- **Application Hosting**: This container holds my Flask application and uses Gunicorn for serving the website.
- **Database Hosting**: Another LXC container runs the PostgreSQL database.


### Cloudflare Tunnels
- **Setup**: I used cloudflare to expose this website securely over https.
- **SSL/TLS**: Certificates created with cloudflare and downloaded on the host origin server for full end-to-end encryption.


### Security
- **Firewall**: UFW is used to lock down all ports except for the necessary ones, ensuring secure communication between containers.


## Future Enhancements
My next tasks include adding easier health management tools like netdata to start and maybe Prometheus later on, along with Terraform, Ansible, and GitHub Actions for automated infrastructure deployments and configuration management and CD/CI.

