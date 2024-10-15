from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=200, default="",)
    text = models.TextField()
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        default="",
    )

    def __str__(self) -> str:
        return self.text[:50]
