from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Plant(models.Model):
    taxonomy = [
        ('Unknown', 'Unknown'),
        ('Araceae', 'Araceae'),
        ('Asteraceae', 'Asteraceae'),
        ('Lamiaceae', 'Lamiaceae'),
        ('Rosaceae', 'Rosaceae'),
        ('Fabaceae', 'Fabaceae'),
        ('Poaceae', 'Poaceae'),
        ('Asparagaceae', 'Asparagaceae'),
        ('Solanaceae', 'Solanaceae'),
        ('Cactaceae', 'Cactaceae'),
        ('Rubiaceae', 'Rubiaceae'),
        ('Ericaceae', 'Ericaceae'),
        ('Crassulaceae', 'Crassulaceae'),
        ('Cyperaceae', 'Cyperaceae'),
        ('Gesneriaceae', 'Gesneriaceae'),
        ('Piperaceae', 'Piperaceae'),
        ('Apocynaceae', 'Apocynaceae'),
        ('Myrtaceae', 'Myrtaceae'),
        ('Moraceae', 'Moraceae'),
        ('Liliaceae', 'Liliaceae'),
        ('Orchidaceae', 'Orchidaceae'),
        ('Rutaceae', 'Rutaceae'),
        ('Arecaceae', 'Arecaceae'),
        ('Pothos Family', 'Pothos Family'),
        ('Bromeliaceae', 'Bromeliaceae'),
        ('Marantaceae', 'Marantaceae'),
        ('Zamiaceae', 'Zamiaceae'),
        ('Araliaceae', 'Araliaceae'),
        ('Oleaceae', 'Oleaceae'),
        ('Scrophulariaceae', 'Scrophulariaceae'),
        ('Polypodiaceae', 'Polypodiaceae'),
        ('Begoniaceae', 'Begoniaceae'),
        ('Urticaceae', 'Urticaceae'),
        ('Geraniaceae', 'Geraniaceae'),
        ('Amaranthaceae', 'Amaranthaceae'),
        ('Primulaceae', 'Primulaceae'),
        ('Campanulaceae', 'Campanulaceae'),
        ('Melastomataceae', 'Melastomataceae'),
        ('Loranthaceae', 'Loranthaceae'),
        ('Oxalidaceae', 'Oxalidaceae'),
        ('Verbenaceae', 'Verbenaceae'),
        ('Hydrophyllaceae', 'Hydrophyllaceae'),
        ('Portulacaceae', 'Portulacaceae'),
        ('Cannaceae', 'Cannaceae'),
        ('Caryophyllaceae', 'Caryophyllaceae'),
        ('Aizoaceae', 'Aizoaceae'),
        ('Araliaceae', 'Araliaceae'),
        ('Euphorbiaceae', 'Euphorbiaceae'),
        ('Saxifragaceae', 'Saxifragaceae'),
        ('Thymelaeaceae', 'Thymelaeaceae'),
        ('Hyacinthaceae', 'Hyacinthaceae'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = CloudinaryField(
        'image', default='../default_post_ecbbyj.jpg', blank=True
    )
    taxonomy_choices = models.CharField(
        max_length=32, choices=taxonomy, default=None
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
