from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Question
from django.utils.text import slugify
from random import randrange


@receiver(pre_save, sender=Question)
def generate_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(f"{instance.question_summary}-{randrange(10)}-{instance.question_author}")
        instance.slug = slug