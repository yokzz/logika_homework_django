from django.db import models

class LibraryBook(models.Model):
    title = models.CharField(max_length=63)
    author = models.CharField(max_length=63)
    isbn = models.CharField(max_length=63)
    available = models.BooleanField()
    
    def __str__(self):
        return f"Book name: {self.title}, Author: {self.author}"
    
    class Meta:
        ordering = ["author"]
        unique_together = ["isbn"]
        verbose_name = "Book"
        verbose_name_plural = "Books"