

from django.contrib import admin
from .models import Post , comment
from django_summernote.admin import SummernoteModelAdmin
from django.urls import reverse
from django.utils.html import format_html



class CommentInline(admin.TabularInline):
    model = comment
    extra = 0
    can_delete = False
    readonly_fields = ('edit_link',)

    def edit_link(self, obj):
        if obj.pk:
            url = reverse("admin:Blog_comment_change", args=[obj.pk])
            return format_html('<a href="{}">ویرایش / حذف</a>', url)
        return "-"



class AdminPost(SummernoteModelAdmin):
    summernote_fields=('description',)
    inlines = [CommentInline]
    list_display=[
        'title',
        "description",
        'get_tags'
       
    ]

    search_fields=[
        "title"
    ]


    def get_tags(self, obj):
        result=[
        
        ]
        for tag in obj.tag.all():
            result.append(tag.name)
        return ", ".join(result)        


admin.site.register(comment)
admin.site.register(Post , AdminPost)    