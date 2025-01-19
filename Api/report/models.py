from django.db import models
from user.models import User
from missingPerson.models import MissingPerson

# Create your models here.
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    missingPerson = models.ForeignKey(MissingPerson, on_delete=models.CASCADE, related_name="reports")
    message = models.CharField(max_length=1000)

    def __str__(self):
        return f"report by {self.user.firstname} {self.missingPerson.firstName}"
