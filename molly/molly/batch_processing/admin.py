import threading

from models import Batch
from django.contrib import admin

def run_batch(modeladmin, request, queryset):
    def run(batches):
        try:
            for batch in batches:
                batch.run()
        except Exception, e:
            print repr(e)
            
    for batch in queryset:
        if not batch.currently_running:
            batch.pending = True
            batch.save()
    thread = threading.Thread(target=run, args=[queryset])
    thread.daemon = True
    thread.start()
run_batch.short__description = "Run selected batch jobs"

class BatchAdmin(admin.ModelAdmin):
    list_display = ['title', 'cron_stmt', 'enabled', 'last_run', 'pending',
                    'currently_running']
    ordering = ['title']
    actions = [run_batch]

admin.site.register(Batch, BatchAdmin)
