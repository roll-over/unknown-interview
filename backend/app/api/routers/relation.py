from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse

from app.api.schemas.relation import RelationSchema
from app.api.schemas.user import UserResponseSchema
from app.services import Relations as MatchRelation
from app.utils import current_user

relation_router = APIRouter(prefix="/relation", tags=["Relations"])


@relation_router.post(
    "",
    summary="Update employer or applicant relation for offer record",
)
async def update_relation(
    request: Request,
    data: RelationSchema,
    Match: MatchRelation,
    cv_owner: UserResponseSchema = Depends(current_user),
):
    relation_match = await Match.update_match_relation(
        relation_data=data,
        owner_data=cv_owner,
    )

    if relation_match:
        return JSONResponse(
            content={"chat_id": f"{relation_match}"},
            status_code=status.HTTP_200_OK,
        )

    return JSONResponse(
        content={"message": "Employer relation updated"},
        status_code=status.HTTP_202_ACCEPTED,
    )
