from os import getenv

SECRET_KEY = getenv("SECRET_KEY")
DB_NAME = getenv("DB_NAME")
DB_USERNAME = getenv("DB_USERNAME")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
API_KEY = getenv("API_KEY")
API_SECRET = getenv("API_SECRET")
CLOUD_NAME = getenv("CLOUD_NAME")
BOOTSTRAP_SERVE_LOCAL = getenv("BOOTSTRAP_SERVE_LOCAL")