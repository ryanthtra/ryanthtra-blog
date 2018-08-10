from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length = 255)
  publish_date = models.DateTimeField()
  image = models.ImageField(upload_to='media/')
  body = models.TextField()

  # Custom title for post object in admin
  def __str__(self):
    return self.title

  def publish_date_pretty(self):
    return self.publish_date.strftime('%b %e %Y')

  def summary(self):
    # limit character count to 100
    return self.body[:100]