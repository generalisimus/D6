import datetime
from django.db import models
from django.utils import timezone



class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

def validate_decimals(value):
    try:
        return round(float(value), 2)
    except:
        raise ValidationError(
            _('%(value)s is not an integer or a float  number'),
            params={'value': value},
        )

class Edition(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=1)
    price = models.FloatField(validators=[validate_decimals])
    edition = models.ForeignKey(Edition,  on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    image = models.ImageField(null=True, blank=True, upload_to='images/')


    def __str__(self):
        return self.title
def friend_book():
    return Book.objects.all()

class Friends(models.Model):
    first_name = models.CharField(max_length=13)
    last_name = models.CharField(max_length=13)
    book = models.ForeignKey('Book', on_delete=models.DO_NOTHING,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.first_name