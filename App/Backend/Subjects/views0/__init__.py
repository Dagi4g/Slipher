
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

from .entry import (SubtopicEntryListView,
                        SubtopicEntryCreateView,
                        SubtopicEntryUpdateView,
                        SubtopicEntryDeleteView,
                        )

from .review import (ShouldReviewView,
                     RememberedView,
                     ForgotView,
                     )

from .Planned.planned_subject import (PlannedSubjectsListView,
                                      
                      )

from .Planned.planned_topic import (PlannedTopicsListView,)

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
        "SubTopicDeleteView",

        #entry related views.
        "SubtopicEntryListView",
        "SubtopicEntryCreateView",
        "SubtopicEntryUpdateView",
        "SubtopicEntryDeleteView",

        #reviwew related views.
        "ShouldReviewView",
        "RememberedView",
        "ForgotView",
        
        #plan related view.
        "PlannedSubjectsListView",
        "PlannedTopicsListView",

        ]
