from fastapi import FastAPI

from . import base_error, validations


def register(app: FastAPI) -> None:
    base_error.register(app)
    validations.register(app)
