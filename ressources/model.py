from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


class Ticket(models.Model):
    """Model representing a ticket."""
    pass


class Review(models.Model):
    """Model representing a review."""
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)  # Foreign key to the Ticket model
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])  # Positive small integer field with rating validators
    headline = models.CharField(max_length=128)  # Character field for the review headline
    body = models.CharField(max_length=8192, blank=True)  # Character field for the review body (optional)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Foreign key to the user model specified in settings
    time_created = models.DateTimeField(auto_now_add=True)  # DateTimeField set to current time on creation


class UserFollows(models.Model):
    """Model representing user follows."""

    class Meta:
        unique_together = (
        'user', 'followed_user',)  # Specifies that 'user' and 'followed_user' should be unique together
