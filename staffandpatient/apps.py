from django.apps import AppConfig


class StaffandpatientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staffandpatient'

def ready(self) -> None:
    from staffandpatient import signals