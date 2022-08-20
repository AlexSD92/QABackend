from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Answer
from django.utils.text import slugify
from random import randrange


@receiver(pre_save, sender=Answer)
def generate_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(f"{instance.answer_summary}-{randrange(10)}-{instance.answer_author}")
        instance.slug = slug