from django.apps import AppConfig


class SheetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sheets'
    def ready(self) -> None:
        import sheets.signals
        return super().ready()