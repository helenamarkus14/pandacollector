from django.db import models

# Create your models here.
GENDER_CHOICES = (
	("f", "female"),
	("m", "male")
)

class Panda(models.Model):

    name = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

