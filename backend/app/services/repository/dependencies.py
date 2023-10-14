from typing import Annotated

from fastapi import Depends

from .interfaces import AbstractBaseRepository
from .repositories import (
    chat_message_repo,
    chat_repo,
    cv_note_repo,
    cv_repo,
    profession_repo,
    skill_repo,
    user_repo,
    vacancy_note_repo,
    vacancy_repo,
)

CVsRepository = Annotated[AbstractBaseRepository, Depends(cv_repo)]
VacanciesRepository = Annotated[AbstractBaseRepository, Depends(vacancy_repo)]
CVNotesRepository = Annotated[AbstractBaseRepository, Depends(cv_note_repo)]
VacancyNotesRepository = Annotated[AbstractBaseRepository, Depends(vacancy_note_repo)]
UserRepository = Annotated[AbstractBaseRepository, Depends(user_repo)]
ProfessionsRepository = Annotated[AbstractBaseRepository, Depends(profession_repo)]
SkillsRepository = Annotated[AbstractBaseRepository, Depends(skill_repo)]
ChatsRepository = Annotated[AbstractBaseRepository, Depends(chat_repo)]
ChatMessagesRepository = Annotated[AbstractBaseRepository, Depends(chat_message_repo)]
