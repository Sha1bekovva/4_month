from django.db import models

class Film(models.Model):
    GENRE = (
        ('Фантастика', 'Фантастика'),
        ('История', 'История'),
        ('Ужасы', 'Ужасы')
    )
    image = models.ImageField(upload_to='films/', verbose_name='Загрузите фото')
    title = models.CharField(max_length=100, verbose_name='Название фильма')
    create_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name='Укажите жанр',
                            default='История')
    author = models.CharField(max_length=100, default='Иванов Иван')
    description = models.TextField(verbose_name='Описание')
    video_film = models.URLField(verbose_name='Вставьте ссылку')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural  = 'Фильмы'
