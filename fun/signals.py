from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from fun.models import Upload
from django.dispatch import receiver
from django.utils.text import slugify

def unique_slug_generator(instance):
    slug = ''

    if instance.slug == '':
        slug = instance.your_name + ' ' + instance.opponent_name
        slug = slugify(slug)

        if Upload.objects.filter(slug=slug).exists():
            last = Upload.objects.last()
            slug = slug + ' ' + str(last.id)

    slug = slugify(slug)
    return slug

@receiver(pre_save, sender=Upload)
def create_slug(sender, instance, **kwargs):
    instance.slug = unique_slug_generator(instance)
    print(instance.slug)
    return
