from django.apps import AppConfig
import os

class SoporteConfig(AppConfig):
    name = 'soporte'

    def ready(self):
	    from . import tares
	    if (os.environ.get('RUN_MAIN', None)) == 'true':
	    	tares.start_scheduler()
