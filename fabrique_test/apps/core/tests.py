from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model, models

UserModel = get_user_model()


class BaseApiTestCase(APITestCase):
    def setUp(self):
        self.set_groups_and_users()

    def set_groups_and_users(self):
        self.admin_group = models.Group.objects.create(name='admin')
        self.moderator = UserModel.objects.create_user(username='moderator', password='moderator', is_staff=True)
        self.moderator.groups.set([self.admin_group])

