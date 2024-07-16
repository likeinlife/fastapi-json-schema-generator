from fastapi import APIRouter, Response, status

router = APIRouter()


@router.get(
    "/health/",
    summary="Check service health",
    status_code=status.HTTP_200_OK,
)
def healthcheck() -> Response:
    return Response(status_code=status.HTTP_200_OK)
