from django.db import models


select = (
    ('1','1'),
    ('2','2'),
)

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    feature_image = models.ImageField(upload_to='tutorial/images/')
    attachment = models.FileField(upload_to='tutorial/attachments/')
    select = models.CharField(max_length=10,choices=select,default='1')


