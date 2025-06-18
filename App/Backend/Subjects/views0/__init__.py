
from .homepage import slipher
from .subject import SubjectListView,SubjectCreateView,SubjectUpdateView,SubjectDeleteView

from .topic import (TopicListView,
                    TopicCreateView,
                    TopicUpdateView,
                    TopicDeleteView
                    )
from .subtopic import (SubtopicListView,
                       SubtopicCreateView,
                       SubTopicUpdateView,
                       SubTopicDeleteView
                       )


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
        "TopicDeleteView",
        #subtopic related views.
        "SubtopicListView",
        "SubtopicCreateView",
        "SubTopicUpdateView",
        "SubTopicDeleteView"
        ]
