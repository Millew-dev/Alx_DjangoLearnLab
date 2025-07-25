from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_migrate)
def create_admin_group(sender, **kwargs):
    Group.objects.get_or_create(name='Admin')
