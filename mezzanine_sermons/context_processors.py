from django.conf import settings

from mezzanine_sermons.models import Slideshow


def get_slideshows(request):
    slideshows = Slideshow.objects.all()
    # except:
    #     random_block = Slideshow.objects.none()
    return {'slideshows': slideshows}
