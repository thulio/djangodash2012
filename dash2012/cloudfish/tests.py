from django.test import TestCase
from cloudfish.models import Cloud
from cloudfish import CLOUD_RACKSPACE
from auth.models import Account
from django.contrib.auth.models import User
from django.core.signing import BadSignature
from django.test.client import Client


class KeyEncriptiontest(TestCase):
    def test_encode_decode_auth_data(self):
        """
        Tests that the auth_data is correctly signed
        """
        user = User(username='daltonmatos', password='mypassword')
        account = Account()
        account.user = user
        cloud = Cloud(type=CLOUD_RACKSPACE, account=account)

        auth_data = {'user': 'username', 'key': 'my_api_key'}

        _data = cloud.add_auth_data(salt='mypassword', **auth_data)
        self.assertEquals(_data, cloud.auth_data)
        self.assertRaises(BadSignature, cloud.decode_auth_data,
            salt='worng-salt')
        self.assertEquals(auth_data, cloud.decode_auth_data(salt='mypassword'))

    def test_validate_email(self):
        """
        Tests if an email is alredy in use
        """
        user = User(email="daltonmatos@email.com", password="mypassword")
        user.save()
        client = Client()
        response = client.post("/register",
                {"email": user.email, "password": user.password,
                 "confirm-password": user.password})

        self.assertIn("This email is already in use.", response.content)

