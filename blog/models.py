from django.db import models

class Blog(models.Model):
      title = models.CharField(max_length=100)
      pub_date = models.DateTimeField()
      body = models.TextField(max_length=1000)
      image = models.ImageField(upload_to='images/')

# Create a migration

#Migrate

#add to the admin
