from fastapi import FastAPI

from . import api_error, base_error, domain_error, validations


def register(app: FastAPI) -> None:
    domain_error.register(app)
    api_error.register(app)
    base_error.register(app)
    validations.register(app)
