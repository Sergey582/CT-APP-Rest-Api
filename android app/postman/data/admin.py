
from django.contrib import admin
from .models import (Task,
                     Answer,
                     Test,
                     )

admin.site.register(Task)
admin.site.register(Answer)
admin.site.register(Test)
