from django.db import models


class StaffModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Staff')
    info = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'


class GalleryModel(models.Model):
    image = models.ImageField(upload_to='gallery')
    text = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'


class NewsModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news')
    description = models.TextField(null=True)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class BannerModel(models.Model):
    image = models.ImageField(upload_to='banners')
    text = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
