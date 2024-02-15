# contributions/models.py

from django.db import models
from django.contrib.auth.models import User

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Contribution(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    deadline = models.DateField()
    target = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Contributions(models.Model):
    contribution = models.ForeignKey(Contribution, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    amount_contributed = models.DecimalField(max_digits=10, decimal_places=2)
    contributed_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    contribution = models.ForeignKey(Contribution, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.contribution.name}"
