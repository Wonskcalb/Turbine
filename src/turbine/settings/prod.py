from .base import *  # noqa F403
from .base import env

SECRET_KEY = env("SECRET_KEY")
