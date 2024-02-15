from django.contrib import admin
from .models import Owner, Contribution, Contributor, Contributions, Comment

# Register your models with the admin site
admin.site.register(Owner)
admin.site.register(Contribution)
admin.site.register(Contributor)
admin.site.register(Contributions)
admin.site.register(Comment)
