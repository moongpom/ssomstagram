from django.db import models
    
# Create your models here.
class Message(models.Model):
    to = models.CharField(max_length=50)
    start = models.CharField(max_length=50)
    writer = models.ForeignKey('user.SomUser', on_delete=models.CASCADE, null=False)
    pub_date=models.DateTimeField()
    body=models.TextField("쪽지")
    
    def summaryStart(self):
        return self.start[:20]

class Reply(models.Model):
    messageId = models.ForeignKey("Message",on_delete=models.CASCADE,db_column="MessageId")
    replyId = models.ForeignKey("self",on_delete=models.CASCADE,blank=True,null=True)
    writer = models.ForeignKey('user.SomUser', on_delete=models.CASCADE, null=False)
    body = models.TextField('댓글')
    pub_date=models.DateTimeField()
   

    def summary(self):
        return self.body[:10] 