from django.db import models


class Maqola(models.Model):
    title=models.CharField(max_length=100)
    matn=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"

class Rasm(models.Model):
    rasm=models.FileField(upload_to="static/media/")
    maqola=models.ForeignKey(Maqola,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.maqola.title}"

