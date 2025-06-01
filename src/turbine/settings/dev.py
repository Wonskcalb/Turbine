from .base import *  # noqa F403
from .base import env, BASE_DIR

DEBUG = True

SECRET_KEY = "ThisIsNotThePasswordYoureLookingFor"

DATABASES = {
    "default": env.db_url(
        "DATABASE_URL",
        default=f"sqlite:///{BASE_DIR}/local.sqlite3"
    )
}
