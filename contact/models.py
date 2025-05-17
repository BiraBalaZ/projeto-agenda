from django.db import models
from django.utils import timezone

# ID (primary key - automatico)
# first_name (string), last_name (string), phone (string),
# email (email), created_date (date), description (text),
# category (foreign key), show (boolean), owner (foreign key),
# picture (image).


class Contact(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 20, blank = True)
    phone = models.CharField(max_length = 15)
    email = models.EmailField(max_length = 254, blank = True)
    created_date = models.DateTimeField(default = timezone.now)
    description = models.TextField(blank = True)
    # category = models.ForeignKey("app.Model", on_delete = models.CASCADE)
    # show = models.BooleanField()
    # owner = models.ForeignKey("app.Model", on_delete = models.CASCADE)
    # picture = models.ImageField(upload_to = None, height_field = None, width_field = None, max_length = None)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


