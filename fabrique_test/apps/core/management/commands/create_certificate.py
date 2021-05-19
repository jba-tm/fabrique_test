import os
import json

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from fabrique_test import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        UserModel = get_user_model()
        # key_string = kwargs['key_string']
        try:
            user = UserModel.objects.get(username=username)

            if not user.check_password(password) or not user.is_superuser:
                raise Exception('Access denied')
        except UserModel.DoesNotExist:
            raise Exception('User does not exist')

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        private_key_str = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        public_key = private_key.public_key()

        public_key_str = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        path = os.path.join(settings.PROJECT_DIR, 'settings', 'secrets.json')
        try:
            with open(path, 'r') as f:
                secrets = json.loads(f.read())
        except FileNotFoundError:
            secrets = {}

        secrets['PRIVATE_KEY'] = private_key_str.decode('utf-8')
        secrets['PUBLIC_KEY'] = public_key_str.decode('utf-8')

        with open(path, 'w') as f:
            f.write(json.dumps(secrets, sort_keys=True))
