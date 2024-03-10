# FLASK

Flask is a web framework, it’s a Python module that lets you develop web applications easily. It’s has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager) or such features.

It does have many cool features like url routing, template engine. It is a WSGI web app framework.

## Getting Started

First, create .env file and setting up the environment.

```text
FLASK_APP=src:create_app
FLASK_RUN_PORT={YOUR PORT NUMBER}

# if you want to run the app in development mode
FLASK_ENV=development
FLASK_DEBUG=1
```

Then, create .venv and install the dependencies.

```bash
python -m venv .venv
pip install -r requirements.txt
```

Finally, run the app.

```bash
flask run
```

## Dependencies

```text
blinker==1.7.0
click==8.1.7
colorama==0.4.6
Flask==3.0.2
itsdangerous==2.1.2
Jinja2==3.1.3
MarkupSafe==2.1.5
PyMySQL==1.1.0
python-dotenv==1.0.1
Werkzeug==3.0.1
```
