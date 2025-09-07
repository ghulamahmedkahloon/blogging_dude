from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def edit(self,name,description,image):
        self.name = name
        self.description = description
        self.image = image
        self.save()
    
    def short_description(self):
        # Split the description into words
        words = self.description.split()
        if len(words) > 50:
            # If words are more than 50 add ... after 50 words
            # ' '.join joins by adding a space between words
            return ' '.join(words[:50])+ '...'
        else:
            # If words are already less than 50 return as it is
            return self.description