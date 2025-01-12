import typing as tp
from uuid import UUID

from fastapi import APIRouter, Body, Depends, Path, Query, Response, status

from domain.entities.app import App
from domain.enums import StateEnum
from logic.interactors.app import AppInteractor
from presentation.api.dependencies import get_interactor
from presentation.api.schemas.specific_format import Root, Settings, Specification

kind = "specific_format"
router = APIRouter(prefix=f"/{kind}", tags=[kind])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(
    schema: tp.Annotated[Root, Body()],
    interactor: tp.Annotated[AppInteractor, Depends(get_interactor)],
) -> UUID:
    result = await interactor.create(app=App.from_root(kind=kind, root=schema))  # type: ignore
    return result.id


@router.get("/{uuid}/", status_code=status.HTTP_200_OK)
async def fetch(
    uuid: tp.Annotated[UUID, Path()],
    interactor: tp.Annotated[AppInteractor, Depends(get_interactor)],
) -> App:
    return await interactor.fetch(kind=kind, id_=uuid)


@router.get("/{uuid}/state/", status_code=status.HTTP_200_OK)
async def fetch_state(
    uuid: tp.Annotated[UUID, Path()],
    interactor: tp.Annotated[AppInteractor, Depends(get_interactor)],
) -> StateEnum:
    return await interactor.fetch_state(kind=kind, id_=uuid)


@router.delete("/{uuid}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    uuid: tp.Annotated[UUID, Path()],
    interactor: tp.Annotated[AppInteractor, Depends(get_interactor)],
) -> Response:
    await interactor.delete(kind=kind, id_=uuid)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{uuid}/state/", status_code=status.HTTP_200_OK)
async def update_status(
    uuid: tp.Annotated[UUID, Path()],
    state_: tp.Annotated[StateEnum, Query(alias="state")],
    interactor: tp.Annotated[AppInteractor, Depends(get_interactor)],
) -> Response:
    await interactor.update_state(kind=kind, id_=uuid, state=state_)
    return Response(status_code=status.HTTP_200_OK)


@router.patch("/{uuid}/settings/", status_code=status.HTTP_200_OK)
async def update_settings(
    uuid: tp.Annotated[UUID, Path()],
    settings: tp.Annotated[Settings, Body()],
    interactor: tp.Annotated[AppInteractor, Depends(get_interactor)],
) -> Response:
    await interactor.update_settings(kind=kind, id_=uuid, settings=settings.model_dump(mode="json"))
    return Response(status_code=status.HTTP_200_OK)


@router.patch("/{uuid}/specification/")
async def update_specification(
    uuid: tp.Annotated[UUID, Path()],
    specification: tp.Annotated[Specification, Body()],
    interactor: tp.Annotated[AppInteractor, Depends(get_interactor)],
) -> Response:
    await interactor.update_specification(kind=kind, id_=uuid, specification=specification.model_dump(mode="json"))
    return Response(status_code=status.HTTP_200_OK)
