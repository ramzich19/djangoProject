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

    image = models.ImageField('Изображение', upload_to='images/', blank=None, null=True)

    in_archive = models.BooleanField(default=False)
    objects = BlogPostManager()

    def __str__(self):
        return f"{self.name} из категории \"{self.blog_category.name}\""


    class Meta:
        verbose_name='Мероприятие'
        verbose_name_plural='Мероприятия'


class TopBack(models.Model):
    name = models.CharField('ФИО', max_length=120)
    description = models.CharField('Почтовый индекс', max_length=120, blank=True, null=True)
    email = models.EmailField('Email', max_length=120, blank=True, null=True )
    phone = models.CharField('Номер телефона', max_length=11)
    iin = models.CharField('ИИН', max_length=120, blank=True, null=True)
    adres = models.CharField('Юридический адрес', max_length=120, blank=True, null=True)
    child = models.CharField('Должность', max_length=120, blank=True, null=True)
    place = models.CharField('Место работы', max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Физ лицо'
        verbose_name_plural = 'Физ лица'


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
