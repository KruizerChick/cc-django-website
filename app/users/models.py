from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(
        _("Name of User"), blank=True, max_length=255,
        help_text='This is what shows as the blog post author. Standard: First Name and Last Initial',
        )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
