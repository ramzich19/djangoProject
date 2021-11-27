from django.db import models

class BlogCategory(models.Model):
    name = models.CharField(max_length = 255, verbose_name= 'Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

class BlogPostQueryset(models.QuerySet):
    def find_by_title_in_qs(self, post_title):
        return self.filter(title__icontains = post_title)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQueryset(self.model, using=self._db)
    def all(self):
        return self.get_queryset().filter(in_archive=False)
    def find_by_title_in_qs(self, post_title):
        return self.get_queryset().find_by_title_in_qs(post_title)


class Articles(models.Model):
    blog_category = models.ForeignKey(BlogCategory, verbose_name='Имя категории', on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length=200, verbose_name = 'Название')
    text = models.TextField(verbose_name ='Текст')
    image = models.ImageField('Изображение',blank=True, null=True)
    price = models.CharField(max_length=10, verbose_name = 'Цена',blank=True, null=True)
    date = models.DateField(verbose_name = 'Дата',blank=True, null=True)
    in_archive = models.BooleanField(default=False)
    objects = BlogPostManager()

    def __str__(self):
        return f"{self.name} из категории \"{self.blog_category.name}\""


    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'


class TopBack(models.Model):
    # articles = models.ForeignKey(Articles, verbose_name = "Имя товара",on_delete = models.CASCADE, blank=True, null=True)
    message = models.CharField('Message', max_length=120,blank=True, null=False)
    # description = models.CharField('Описание', max_length=250, blank=True, null=True)
    # email = models.EmailField('Email', max_length=120, blank=True, null=True )
    # phone = models.CharField('Номер телефона', max_length=11)
    # iin = models.CharField('ИИН', max_length=120, blank=True, null=True)
    # adres = models.CharField('Юридический адрес', max_length=120, blank=True, null=True)
    # child = models.CharField('Должность', max_length=120, blank=True, null=True)
    # place = models.CharField('Место работы', max_length=120, blank=True, null=True)

    def __str__(self):
        return self.message
        # return f"{self.message} из товаров \"{self.articles.name}\""

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Formback(models.Model):
    name = models.CharField('Полное наименование организации', max_length=120)
    description = models.CharField('Направление деятельности', max_length=120, blank=True, null=True)
    email = models.EmailField('Email', max_length=120, blank=True, null=True )
    phone = models.CharField('Номер телефона', max_length=11)
    iin = models.CharField('БИН/ИИН', max_length=120, blank=True, null=True)
    adres = models.CharField('Юридический адрес', max_length=120, blank=True, null=True)
    child = models.CharField('Почтовый индекс', max_length=120, blank=True, null=True)
    bank = models.CharField('Банковские реквизиты', max_length=120, blank=True, null=True)
    fio = models.CharField('ФИО Первого руководителя', max_length=120, blank=True, null=True)
    first = models.CharField('Должность первого руководителя', max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Юр лицо'
        verbose_name_plural = 'Юр лица'



class FeedBack(models.Model):
    name = models.CharField('Name', max_length=120)
    email = models.EmailField('email', max_length=120, blank=True, null=True )
    description = models.CharField('описание', max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'
