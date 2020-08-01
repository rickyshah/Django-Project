from django.db import models
from django.contrib import auth


# User class is built in attributes of auth module
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.user)
        # return f"@{self.user}"
