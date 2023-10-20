from typing import Union
from uuid import UUID

from app.api.schemas.relation import RelationSchema
from app.db.models import User

from .repository.repositories import chat_repo
from .unitorwork import MatchVacancyCVUoW


class ChatHandler:
    """A class that handles chat activities.

    Attributes:
        matches: An instance of MatchVacancyCVUoW for managing matches.
        chats: An instance of ChatUoW (now user repo directly) for managing chat.
    """

    def __init__(self):
        self.matches = MatchVacancyCVUoW()
        self.chats = chat_repo()

    async def update_match_relation(
            self,
            *,
            relation_data: RelationSchema,
            owner_data: User,
    ) -> Union[UUID | None]:
        """Update relation in match, if relations equal create chat.

        Args:
            owner_data: The owner data object associated with the record.
            relation_data: The dictionary of CV, Vacancy ID and new relation.

        Returns:
            ID of created chat, if relations equal, otherwise None.
        """
        match_record = await self.matches.update_relation(
            owner_data=owner_data,
            new_relation=relation_data.relation,
            cv_id=relation_data.cv_id,
            vacancy_id=relation_data.vacancy_id,
        )

        relation = await self.matches.check_relation(match_record)
        if not relation:
            return

        chat = await self.chats.create_one(  # !!! Replace after ChatUoV implementation
            {
                "employer_id": owner_data.custom_id,
                "applicant_id": owner_data.custom_id,
                "match_id": match_record.custom_id,
            }
        )
        await self.matches.update_match_chat_id(
            chat_id=chat.custom_id,
            match_record=match_record,
        )

        return chat.custom_id
