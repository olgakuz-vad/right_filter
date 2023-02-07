from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=100, blank=True, verbose_name="Фамилия")
    email = models.EmailField(blank=True, verbose_name="email")
    is_active = models.BooleanField(default=True,)
    ratingAuthor = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.authorUser}'

    def get_absolute_url(self):
        return reverse('author', kwargs={'author_id': self.pk})

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['id']

def update_rating(self):
    postRaiting = self.post_set.aggregate(postRait=Sum('raiting'))
    pRat = 0
    pRat +=postRaiting.get('postRait')

    commentRaiting = self.authorUser.comment_set.aggregate(commentRait=Sum('raiting'))
    cRat = 0
    cRat +=commentRait.get('commentRaiting')

    self.raitingAuthor =pRat *3 + cRat
    self.save()

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=255, verbose_name="Название")
    text = models.TextField(verbose_name="Текст статьи")

    NEWS = 'News'
    ARTICLE = 'Article'
    CATEGORY_CHOICES =(
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryPost = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=ARTICLE)
    postCategory = models.ManyToManyField(Category, through='PostCategory', verbose_name="Категория")
    dateCreate = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    photo = models.ImageField(upload_to="photo/", verbose_name="Фото")
    slug = models.SlugField(max_length=100)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['dateCreate', 'title']


    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -=1
        self.save()

    def preview(self):
         return self.text[0:123]+'...'


class PostCategory(models.Model):
    postTrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    commentCreate = models.DateTimeField(auto_now_add=True)
    raiting = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.text()

def like(self):
    self.rating +=1
    self.save()

def dislike(self):
    self.rating -=1
    self.save()
