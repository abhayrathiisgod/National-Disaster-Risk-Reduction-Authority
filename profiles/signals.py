from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist
import os
from .models import OfficersHead, CommiteProfile, ExecutiveCommitteHead, InformationOfficer, NationalCouncilHead, OfficersSpokesPerson, OfficerProfile

# Define signals for post_delete and pre_save


@receiver(post_delete, sender=OfficersHead)
@receiver(post_delete, sender=CommiteProfile)
@receiver(post_delete, sender=ExecutiveCommitteHead)
@receiver(post_delete, sender=InformationOfficer)
@receiver(post_delete, sender=NationalCouncilHead)
@receiver(post_delete, sender=OfficersSpokesPerson)
@receiver(post_delete, sender=OfficerProfile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(pre_save, sender=OfficersHead)
@receiver(pre_save, sender=CommiteProfile)
@receiver(pre_save, sender=ExecutiveCommitteHead)
@receiver(pre_save, sender=InformationOfficer)
@receiver(pre_save, sender=NationalCouncilHead)
@receiver(pre_save, sender=OfficersSpokesPerson)
@receiver(pre_save, sender=OfficerProfile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except ObjectDoesNotExist:
        return False

    if old_instance.image:
        if not old_instance.image == instance.image:
            if os.path.isfile(old_instance.image.path):
                os.remove(old_instance.image.path)
