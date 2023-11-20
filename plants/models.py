from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):
    taxonomy = [
        'Araceae',
        'Asteraceae',
        'Lamiaceae',
        'Rosaceae',
        'Fabaceae',
        'Poaceae',
        'Asparagaceae',
        'Solanaceae',
        'Cactaceae',
        'Rubiaceae',
        'Ericaceae',
        'Crassulaceae',
        'Cyperaceae',
        'Gesneriaceae',
        'Piperaceae',
        'Apocynaceae',
        'Myrtaceae',
        'Moraceae',
        'Liliaceae',
        'Orchidaceae',
        'Rutaceae',
        'Arecaceae',
        'Pothos Family',
        'Bromeliaceae',
        'Marantaceae',
        'Zamiaceae',
        'Araliaceae',
        'Oleaceae',
        'Scrophulariaceae',
        'Polypodiaceae',
        'Begoniaceae',
        'Urticaceae',
        'Geraniaceae',
        'Amaranthaceae',
        'Primulaceae',
        'Campanulaceae',
        'Melastomataceae',
        'Loranthaceae',
        'Oxalidaceae',
        'Verbenaceae',
        'Hydrophyllaceae',
        'Portulacaceae',
        'Cannaceae',
        'Caryophyllaceae',
        'Aizoaceae',
        'Araliaceae',
        'Euphorbiaceae',
        'Saxifragaceae',
        'Thymelaeaceae',
        'Hyacinthaceae',
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    plant_request = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    requested_children = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(1)])
    image = models.ImageField(
        upload_to='images/', default='../default_post_ecbbyj.jpg', blank=True
    )
    taxonomy_choices = models.CharField(
        max_length=32, choices=taxonomy, default=None
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
