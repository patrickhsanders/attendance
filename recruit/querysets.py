from django.db.models.query import QuerySet
from django.db.models import Q

from course.models import Course

class JobQueryset(QuerySet):

    def for_company(self, company_id):
        return self.filter(company_id=company_id)

    def currently_employed(self):
        return self.filter(end_date__isnull=True)

    def not_currently_employed(self):
        return self.filter(end_date__isnull=False)