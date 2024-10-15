# Platform.sh settings.
from platformshconfig import Config

config = Config()
if config.is_valid_platform():
    ALLOWED_HOSTS.append('.platformsh.site')

    if config.appDir:
        STATIC_ROOT = Path(config.appDir) / 'static'
    if config.projectEntropy:
        SECRET_KEY = config.projectEntropy
    
    if not config.in_build():
        db_settings = config.credentials('database')
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': db_settings['path'],
                'USER': db_settings['username'],
                'PASSWORD': db_settings['password'],
                'HOST': db_settings['host'],
                'PORT': db_settings['port'],
            },
        }