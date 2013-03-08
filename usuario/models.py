from django.db import models
from django.contrib.auth.models import User
from cupon.models import Cupon
import os
# Create your models here.


def get_image_path(perfil, filename):
    return os.path.join('avatar', str(perfil.user.username), filename)

class Perfil(models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField(upload_to=get_image_path, verbose_name='avatar')

	def __str__(self):
		return "%s's profile" % self.user


class HistorialCupones(models.Model):
	user = models.ForeignKey(User)
	cupon = models.ForeignKey(Cupon)


# Capturar el avatar de nuevos usuarios
from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.twitter import TwitterBackend
from social_auth.signals import pre_update


# Actualizar avatar
def social_extra_values(sender, user, response, details, **kwargs):
    result = False

    if "id" in response:
            from urllib2 import urlopen, HTTPError
            from django.template.defaultfilters import slugify
            from django.core.files.base import ContentFile

            try:
                url = None
                if sender == FacebookBackend:
                    url = "http://graph.facebook.com/%s/picture?type=large" \
                    % response["id"]
                elif sender == TwitterBackend:
                 	url = response["profile_image_url"]
                 	
                if url:
                    avatar = urlopen(url)
                    user.perfil.avatar = slugify(user.username +" social") + '.jpg',
                    ContentFile(avatar.read())

                    user.save()

            except HTTPError:
                pass
            result = True
    return result

pre_update.connect(social_extra_values, sender=None)
