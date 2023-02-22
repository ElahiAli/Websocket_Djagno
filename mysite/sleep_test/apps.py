from django.apps import AppConfig


class SleepTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sleep_test'

    def ready(self):
        import sleep_test.signals