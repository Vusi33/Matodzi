from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()
    def _str_(self):
        return self.name
