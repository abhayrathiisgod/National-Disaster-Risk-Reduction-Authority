from django.db import models
from django.core.validators import FileExtensionValidator
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
    image = models.ImageField(upload_to='uploads/news_info', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])

    def __str__(self) -> str:
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = NewsInfo.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(NewsInfo, self).save(*args, **kwargs)


class PressNote(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True)
    title = models.TextField()
    title_ne = models.TextField()
    description = models.TextField()
    description_ne = models.TextField()
    summary = models.TextField()
    summary_ne = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/press-note', validators=[
        FileExtensionValidator(allowed_extensions=["pdf", "doc",
                                                   "docx"])])
    file = models.FileField(upload_to='uploads/files/press-note', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    is_published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        self.file.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = PressNote.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)
            if self.file != old_instance.file:
                old_instance.file.delete(save=False)

        super(PressNote, self).save(*args, **kwargs)
