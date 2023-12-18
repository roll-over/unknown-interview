from uuid import UUID

from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse

from app.api.schemas.base import UserRole
from app.api.schemas.cv import CVRequestSchema, CVResponseSchema
from app.api.schemas.user import UserResponseSchema
from app.services import Records as CVRecords
from app.utils import current_user

cv_router = APIRouter(prefix="/cvs", tags=["CVs"])


@cv_router.post(
    "/",
    response_model=CVResponseSchema,
    summary="Create new CV for user",
)
async def create_cv(
    request: Request,
    data: CVRequestSchema,
    CV: CVRecords,
    cv_owner: UserResponseSchema = Depends(current_user),
):
    return await CV.prepare_record(data, owner_data=cv_owner, role=UserRole.applicant)


@cv_router.get(
    "/random_cv",
    response_model=CVResponseSchema,
    summary="Return random user CV",
)
async def get_random_cv(
        CV: CVRecords,
        cv_owner: UserResponseSchema = Depends(current_user),
):
    return await CV.get_matched_record(owner_data=cv_owner, role=UserRole.employer)


@cv_router.get(
    "/{cv_id}",
    response_model=CVResponseSchema,
    summary="Return user CV by ID",
)
async def get_user_cv(
        cv_id: UUID,
        CV: CVRecords,
        record_owner: UserResponseSchema = Depends(current_user),
):
    return await CV.get_record(
        record_id=cv_id,
        owner_data=record_owner,
        role=UserRole.applicant,
    )


@cv_router.patch(
    "/{cv_id}",
    response_model=CVResponseSchema,
    summary="Update user CV by ID",
)
async def update_user_cv(
    request: Request,
    data: CVRequestSchema,
    cv_id: UUID,
    CV: CVRecords,
    cv_owner: UserResponseSchema = Depends(current_user),
):
    return await CV.update_record(
        data,
        record_id=cv_id,
        owner_data=cv_owner,
        role=UserRole.applicant,
    )


@cv_router.delete(
    "/{cv_id}",
    summary="Delete user CV by ID",
)
async def delete_user_cv(
        cv_id: UUID,
        CV: CVRecords,
        cv_owner: UserResponseSchema = Depends(current_user),

):
    deleted_cv = await CV.delete_record(
        record_id=cv_id,
        owner_data=cv_owner,
        role=UserRole.applicant,
    )

    if deleted_cv:
        return JSONResponse(
            content={"message": "User CV deleted successfully"},
            status_code=status.HTTP_200_OK,
        )
