from django.db import models
    
# Create your models here.
class Message(models.Model):
    to = models.CharField(max_length=50)
    start = models.CharField(max_length=50)
    writer = models.ForeignKey('user.SomUser', on_delete=models.CASCADE, null=False)
    #writer = models.CharField(max_length=50)
    pub_date=models.DateTimeField()
    body=models.TextField()
    lastMsg = models.DateTimeField()
    
    def __str__(self):
        return self.body
    def summaryBody(self):
        return self.body[:25]

class Reply(models.Model):
    messageId = models.ForeignKey("Message",on_delete=models.CASCADE,db_column="MessageId")
    replyId = models.ForeignKey("self",on_delete=models.CASCADE,blank=True,null=True)
    writer = models.ForeignKey('user.SomUser', on_delete=models.CASCADE, null=False)
    #writer = models.CharField(max_length=50)
    body = models.TextField()
    pub_date=models.DateTimeField()
   
    def __str__(self):
        return self.body
    def summary(self):
        return self.body[:25] 