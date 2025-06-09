
from .homepage import slipher
from .subject import SubjectListView,SubjectCreateView,SubjectUpdateView,SubjectDeleteView

from .topic import TopicListView

__all__ = [
        'slipher',
        "SubjectListView",
        "SubjectCreateView",
        "SubjectUpdateView",
        "SubjectDeleteView",
        "TopicListView",
        ]
