from django.apps import AppConfig


class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_core.customer'

    def ready(self):
        import crm_core.customer.signals  # noqa
