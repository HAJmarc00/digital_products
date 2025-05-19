from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    description  = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'),blank=True, upload_to='categories/')
    is_enable = models.BooleanField(_('Is Enable'), default=True)
    created_time = models.DateTimeField(_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated Time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description  = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'),blank=True, upload_to='products/')
    is_enable = models.BooleanField(_('Is Enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated Time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')



class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPES = (
        (FILE_AUDIO, _('audio')),
        (FILE_VIDEO, _('video')),
        (FILE_PDF, _('pdf'))
    )
    product = models.ForeignKey('Product', verbose_name=_('product'),related_name='files' ,on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file_type = models.PositiveSmallIntegerField(_('file type'), choices=FILE_TYPES)
    file = models.FileField(_('file'), upload_to='files/%y/%m/%d/')
    is_enable = models.BooleanField(_('Is Enable'), default=True)
    created_time = models.DateTimeField(_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated Time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('File')
        verbose_name_plural = _('Files')

