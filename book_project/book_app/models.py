from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES =(
        ('Available','Available'),
        ('Checked Out', 'Checked Out'),
        ('Reserved','Reserved'),
        ('On hold','On hold')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_by = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.book_name