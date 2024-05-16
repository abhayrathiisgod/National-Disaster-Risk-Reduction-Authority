from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Donater, Project
from django.utils import timezone
from django.core.exceptions import ValidationError


@receiver(pre_save, sender=Donater)
def update_donater(sender, instance, **kwargs):
    if not instance.donater_created_at:
        instance.donater_created_at = timezone.now()
    instance.donater_updated_at = timezone.now()


@receiver(pre_save, sender=Project)
def update_donater(sender, instance, **kwargs):
    if instance.start_date >= instance.end_date:
        raise ValidationError("End date must be after the start date.")
    if not instance.created_at:
        instance.created_at = timezone.now()
    instance.updated_at = timezone.now()


@receiver(post_save, sender=Donater)
def delete_old_icon(sender, instance, **kwargs):
    if instance.id:
        try:
            old_instance = Donater.objects.get(pk=instance.pk)
            if instance.icon != old_instance.icon:
                old_instance.icon.delete(save=False)
        except Donater.DoesNotExist:
            pass


@receiver(post_delete, sender=Donater)
def delete_icon(sender, instance, **kwargs):
    if instance.icon:
        instance.icon.delete(save=False)
