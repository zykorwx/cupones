from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.


def get_image_path(perfil, filename):
    return os.path.join('imagenes/usuarios/usr_'+perfil.user.username, 'avatar', filename)

class Perfil(models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField(upload_to=get_image_path, verbose_name='avatar')

	def __str__(self):
		return "%s's profile" % self.user




# Capturar el avatar de nuevos usuarios
from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.twitter import TwitterBackend
from social_auth.signals import socialauth_registered
from django.db.models.signals import post_save

def new_users_handler(sender, user, response, details, **kwargs):
    user.is_new = True
    if user.is_new:
        if "id" in response:
            from urllib2 import urlopen, HTTPError
            from django.template.defaultfilters import slugify
            from django.core.files.base import ContentFile

            try:
                url = None
                if sender == FacebookBackend:
                    url = "http://graph.facebook.com/%s/picture?type=square" \
                    % response["id"]
                elif sender == TwitterBackend:
                 	url = response["profile_image_url"]
                 	
                if url:
                    avatar = urlopen(url)
                    perfil = Perfil(user=user)

                    perfil.avatar.save(slugify(user.username +" social") + '.jpg',
                            ContentFile(avatar.read()))

                    perfil.save()

            except HTTPError:
                pass
    return False

socialauth_registered.connect(new_users_handler, sender=None)
