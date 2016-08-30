from django.db.models.query import QuerySet
from django.db.models import Q

from course.models import Course

class StudentQueryset(QuerySet):

    def _order_by_first_name(self):
        return self.order_by('first_name')

    def active(self):
        return self._order_by_first_name().filter(active=True)

    def inactive(self):
        return self._order_by_first_name().filter(active=False)

    def fulltime(self):
        return self._order_by_first_name().filter(course__full_time=True)

    def parttime(self):
        return self._order_by_first_name().filter(course__full_time=False)

    def ios(self):
        ios_course = Course.objects.get(name__iexact='iOS Fulltime')
        return self._order_by_first_name().filter(course=ios_course)

    def android(self):
        android_course = Course.objects.get(name__iexact='Android Fulltime')
        return self._order_by_first_name().filter(course=android_course)

    def swift(self):
        swift_course = Course.objects.get(name__iexact='Swift')
        return self._order_by_first_name().filter(course=swift_course).order_by('first_name')

    def algos(self):
        return self._order_by_first_name().filter(active=True, current_project__weight__lte=109)

    def hackathon(self):
        return self._order_by_first_name().filter(
            Q(current_project__weight__gt=140, current_project__weight__lte=199) |
            Q(current_project__weight__gt=230)
        )
