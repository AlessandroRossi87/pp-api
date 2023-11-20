from django.db import models
from django.contrib.auth.models import User
from plants.models import Plant


class Reaction(models.Model):
    reactions = [
        (1, 'Hydrate'),
        (2, 'Moist'),
        (3, 'Drought'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(
        Plant, related_name='reactions', on_delete=models.CASCADE
    )
    reaction_type = models.IntegerField(choices=reactions)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'plant', 'reaction_type']

    def __str__(self):
        return f'{self.owner} {self.plant} - {self.get_reaction_type_display()}'