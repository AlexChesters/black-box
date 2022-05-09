import os

def is_development_environment():
    return os.environ.get("ENVIRONMENT", "production") == "development"
