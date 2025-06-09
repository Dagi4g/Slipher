
from .homepage import slipher
from .subject import SubjectListView,SubjectCreateView,SubjectUpdateView,SubjectDeleteView

from .topic import TopicListView,TopicCreateView

__all__ = [
        'slipher',
        "SubjectListView",
        "SubjectCreateView",
        "SubjectUpdateView",
        "SubjectDeleteView",
        "TopicListView",
        "TopicCreateView",
        ]
