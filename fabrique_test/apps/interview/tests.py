from datetime import timedelta
from pprint import pprint

from django.urls import reverse
from django.utils.timezone import now

from fabrique_test.apps.core.tests import BaseApiTestCase

from .models import (
    Interview
)



class InterViewAPITestCase(BaseApiTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        for i in range(10):
            Interview.objects.create(title=f'title-{i}', description=f'description-{i}',
                                     start_at=now() + timedelta(days=i), end_at=now() + timedelta(weeks=i))

    def test_get_all_interviews(self):
        url = reverse('api:interview-list')
        response = self.client.get(url)
        pprint(response.data)
