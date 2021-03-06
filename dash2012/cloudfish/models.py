from django.db import models
from cloudfish import SUPPORTED_CLOUDS
from auth.models import Account
from django.core import signing

class Cloud(models.Model):

    type = models.CharField(max_length=32, choices=SUPPORTED_CLOUDS)

    # This is a JSON content, encrypted using the users password.
    # Must be re-generated every time the user changes its password.
    auth_data = models.CharField(max_length=1024)

    account = models.ForeignKey(Account, related_name='clouds')


    def add_auth_data(self, salt, **kwargs):
        """
        Build a JSON object with all **kwargs and then
        Sign this content using the salt
        """
        _data = signing.dumps(kwargs, salt=salt)
        self.auth_data = _data
        return _data

    def decode_auth_data(self, salt):
        return signing.loads(self.auth_data, salt=salt)