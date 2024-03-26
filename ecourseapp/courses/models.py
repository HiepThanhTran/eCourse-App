from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
from django.db import models


class User(AbstractUser):
    avatar = CloudinaryField(null=True)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=20, default='tag')

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=100, unique=True)
    description = RichTextField()
    image = CloudinaryField()

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.subject


class Tag(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    subject = models.CharField(max_length=255, unique=True)
    content = RichTextField()
    image = CloudinaryField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name='lessons')

    def __str__(self):
        return self.subject


class Interaction(BaseModel):
    class Meta:
        abstract = True

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(Interaction):
    content = RichTextField()


class Like(Interaction):
    class Meta:
        unique_together = ('user', 'lesson')


class Rating(Interaction):
    rating = models.DecimalField(max_digits=2, decimal_places=1)
