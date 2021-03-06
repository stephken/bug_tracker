from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class MyUser(AbstractUser):
    pass


class Ticket(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    time_date = models.DateTimeField(default=timezone.now)
    assigned_to = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="assigned_to", blank=True, null=True)
    assigned_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="assigned_by")
    completed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="completed_by", blank=True, null=True)
    NEW = "N"
    DONE = "D"
    IN_PROGRESS = "IP"
    INVALID = "IV"
    TICKET_STATUS_CHOICES = [
        (NEW, "New"), (IN_PROGRESS, "In Progress"),
        (DONE, "Done"), (INVALID, "Invalid"),
    ]
    ticket_status_choices = models.CharField(max_length=2, choices=TICKET_STATUS_CHOICES, default=NEW,)
    
    def __str__(self):
        return self.title