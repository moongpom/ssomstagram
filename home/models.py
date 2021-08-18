from django.db import models
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50) #CharField: 제한있는 문자열
    writer=models.CharField(max_length=50)    
    pub_date=models.DateTimeField()
    body=models.TextField()
    image = models.ImageField(upload_to="mediaForm/",blank=False,null=False)

    #아래 함수는 밑에서 설명
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:80]