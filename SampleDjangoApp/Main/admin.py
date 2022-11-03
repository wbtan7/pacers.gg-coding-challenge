from django.contrib import admin

from Main.models import ScoreLog

class ScoreLogAdmin(admin.ModelAdmin):
    list_display = ('score','user')
    list_editable = list_display
    list_display_links = None

    search_fields = ('score' ,'user__username')
    list_filter = ('score', 'user__username')

admin.site.register(ScoreLog, ScoreLogAdmin)