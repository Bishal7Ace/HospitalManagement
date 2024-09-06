from django.apps import AppConfig


class AccountingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Accounting'
    
    def ready(self) -> None:
        from . import signals