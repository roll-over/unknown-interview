from enum import Enum


class MatchRelation(Enum):
    not_shown = "not_shown"
    shown = "shown"
    skipped = "skipped"
    liked = "liked"
    disliked = "disliked"
