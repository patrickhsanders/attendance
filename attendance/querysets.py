from django.db.models.query import QuerySet


class RegisterQueryset(QuerySet):

    def open(self):
        return self.filter(checkout__isnull=True)

    def closed(self):
        return self.filter(checkout__isnull=False)

    def for_student(self, student_object):
        return self.filter(student=student_object)

    def for_student_with_id(self, student_id):
        return self.filter(student__pk=student_id)

    def order_by_student_first_name(self):
        return self.order_by('student__first_name')