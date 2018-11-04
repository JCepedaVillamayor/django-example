from .base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ["*"]

SECRET_KEY = env.str("SECRET_KEY", "9#crrbb5*qnel6y4l!fwlmx5&+17!f_x=e2ms9@pex+qrqo!_%")
