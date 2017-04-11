from django.contrib import admin

from ask.models import User, Ask, Answer, Tag, UserVote
# Register your models here.

admin.site.register(User)
admin.site.register(Ask)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(UserVote)
