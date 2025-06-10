
from .homepage import slipher
from .subject import SubjectListView,SubjectCreateView,SubjectUpdateView,SubjectDeleteView

from .topic import TopicListView,TopicCreateView,TopicUpdateView,TopicDeleteView

__all__ = [
        'slipher',
        "SubjectListView",
        "SubjectCreateView",
        "SubjectUpdateView",
        "SubjectDeleteView",
        #topic related views.
        "TopicListView",
        "TopicCreateView",
        "TopicUpdateView",
        "TopicDeleteView"
        ]
