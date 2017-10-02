from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='wkj6_l=@ae+th5$l*d_)xzw8=z%l$s0_^s7z=^ztp&2iomk)q(')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
