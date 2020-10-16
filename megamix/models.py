from django.db import models


class member(models.Model):
    image_ulr = models.ImageField(upload_to='programmers/', default=None)
    name = models.CharField(max_length=32)
    discription = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class programming_language(models.Model):
    language_name = models.CharField(max_length=32)
    icon = models.ImageField(null=True, upload_to='languages_icon/', default=None)

    def __str__(self):
        return self.language_name


class project(models.Model):
    language = models.ForeignKey(programming_language, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=32)
    describe = models.CharField(max_length=1024)
    image = models.ImageField(upload_to='projects/', default=None)
    programmers = models.ForeignKey(member, on_delete=models.deletion.SET_NULL, null=True)

    def __str__(self):
        return '{} by {}'.format(self.title, self.programmers)


class customer_message(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    message = models.CharField(max_length=2048)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'message from {} in {}'.format(self.name,self.create_at)