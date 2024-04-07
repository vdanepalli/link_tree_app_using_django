from django.db import models

# Create your models here.

class Profile(models.Model):
    # name, slug, bg_color
    BG_CHOICES = (
        ('black', 'Black'), # left is stored in the database, right is what is shown to the user for selection
        ('green', 'Green'),
        ('yellow', 'Yellow'),
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)
    
    def __str__(self):
        return self.name
    
    # By default you have something like modelName_set = link_set
    # But since we defined related_name = 'links', we now can simply say Profile.links

class Link(models.Model):
    text = models.CharField(max_length=100)
    url = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links") # deletes all links if profile is deleted
    
    def __str__(self):
        return f"{self.text} | {self.url}"
    
    # many to many
    # many to one
    # one to one