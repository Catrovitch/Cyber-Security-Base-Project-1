from django.apps import AppConfig

def start():
    from .models import Account, Creditcard

    p1, created = Account.objects.get_or_create(
        username='donna',
        password='donna123',
        admin=True)

    p2, created = Account.objects.get_or_create(
        username='bob',
        password='bob123',
        admin=False)

    creditcard1 = Creditcard.objects.get_or_create(number=123456, credit=0, owner=p1)
    creditcard2 = Creditcard.objects.get_or_create(number=234567, credit=0, owner=p2)


class BankConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bank'

    def ready(self):
        import os
        if os.environ.get('RUN_MAIN'):
            start()