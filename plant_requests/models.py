from django.db import models
from django.contrib.auth.models import User
from plants.models import Plant


class PlantRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-request_date']

    def __str__(self):
        return f'{self.requester} - {self.plant} - {self.request_date} - Approved: {self.is_approved}'