
from django.contrib import admin
from .models import Post

from django.utils.translation import gettext_lazy as _


admin.site.site_header = _("My Admin Panel")       # جایگزین "پنل مدیریت من"
admin.site.site_title = _("Blog Management")       # جایگزین "مدیریت بلاگ"
admin.site.index_title = _("Welcome to the Dashboard")  # جایگزین "به داشبورد خوش آمدید"

# رجیستر مدل با نام فارسی
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "content")
    list_filter = ("created_at",)
    #verbose_name = _("مطلب")
    #verbose_name_plural = _("مطالب")
'''

from django.contrib import admin
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from .models import Post

# چک کردن زبان فعلی و جایگزینی متن‌ها
current_lang = translation.get_language()

if current_lang == 'fa':
    admin.site.site_header = "پنل مدیریت من"
    admin.site.site_title = "مدیریت بلاگ"
    admin.site.index_title = "به داشبورد خوش آمدید"
else:
    admin.site.site_header = "My Admin Panel"
    admin.site.site_title = "Blog Management"
    admin.site.index_title = "Welcome to the Dashboard"

# رجیستر مدل با نام فارسی
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "content")
    list_filter = ("created_at",)
    verbose_name = "مطلب"
    verbose_name_plural = "مطالب"
'''