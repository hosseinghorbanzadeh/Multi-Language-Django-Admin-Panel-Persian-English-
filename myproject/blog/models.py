from django.db import models
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    content = models.TextField(_("Content"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

