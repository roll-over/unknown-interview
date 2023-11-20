from app.db.models import Note
from app.services.repository.interfaces import MongoBeanieRepository
from app.services.repository.services import NoteService


class NoteRepositoryModel(MongoBeanieRepository):
    model = Note


def get_note_repository():
    return NoteService(NoteRepositoryModel)
