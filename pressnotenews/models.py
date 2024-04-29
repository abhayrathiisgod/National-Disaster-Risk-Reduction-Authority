from django.db import models

# Create your models here.


class Author(models.Model):
    Author_id = models.AutoField(primary_key=True)
    name = models.CharField()
    name_ne = models.CharField()

    def __str__(self) -> str:
        return self.name


class Type(models.Model):
    Type_id = models.AutoField(primary_key=True)
    name = models.CharField()
    name_ne = models.CharField()

    def __str__(self) -> str:
        return self.name

# make 2 urls all with sumary and individual specific


class NewsInfo(models.Model):
    id = models.AutoField(primary_key=True)
    # author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, null=True)
    # type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, null=True)
    title = models.TextField()
    title_ne = models.TextField()
    description = models.TextField()
    description_ne = models.TextField()
    summary = models.TextField()
    summary_ne = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/news_info')

    def __str__(self) -> str:
        return self.title


class PressNote(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, null=True)
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, null=True)
    title = models.TextField()
    title_ne = models.TextField()
    description = models.TextField()
    description_ne = models.TextField()
    summary = models.TextField()
    summary_ne = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/press-note')
    file = models.FileField(upload_to='uploads/files/press-note')
    image = models.ImageField(upload_to='uploads/images/press-note')
    is_published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
