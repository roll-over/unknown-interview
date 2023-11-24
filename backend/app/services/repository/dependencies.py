from typing import Annotated

from fastapi import Depends

from .repositories import (
    chat_message_repo,
    chat_repo,
    cv_repo,
    note_repo,
    profession_repo,
    skill_repo,
    user_repo,
    vacancy_repo,
)
from .services import (
    ChatMessageService,
    ChatService,
    NoteService,
    ProfessionService,
    SkillService,
    UserService,
    VacancyCVService,
)

CVsRepository = Annotated[VacancyCVService, Depends(cv_repo)]
VacanciesRepository = Annotated[VacancyCVService, Depends(vacancy_repo)]
NotesRepository = Annotated[NoteService, Depends(note_repo)]
UserRepository = Annotated[UserService, Depends(user_repo)]
ProfessionsRepository = Annotated[ProfessionService, Depends(profession_repo)]
SkillsRepository = Annotated[SkillService, Depends(skill_repo)]
ChatsRepository = Annotated[ChatService, Depends(chat_repo)]
ChatMessagesRepository = Annotated[ChatMessageService, Depends(chat_message_repo)]
