DjangoMVPTools is a starter kit project for the rapid development of your new startup or side project. The purpose of this project is to provide you with common templates, apps, and chunks of code to create a simple website as fast as possible.

## ToDo

[X] - add blog article template

[X] - add contact form

[X] - add profile page

[X] - add search

[X] - add comments

[ ] - add email subscription

[X] - profile dropdown menu

[X] - flat pages

[ ] - tags for posts

## Installation

Add import Path in settings.py:

```
from pathlib import Path
```

Add required apps to the INSTALLED_APPS:

```
INSTALLED_APPS = [
...
    'django.contrib.sites',
    'django.contrib.flatpages',
    'compressor',
    'demo',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'crispy_bootstrap5',
    'taggit',
    'django_browser_reload',
    'sorl.thumbnail',
    'django_comments_ink',
    'django_comments',
    'avatar',
    'core',
    'honeypot',
    # 'newsletter',
...
]
```

Add browser-reload middleware:

```
MIDDLEWARE = [
...
    # django-browser-reload
    'django_browser_reload.middleware.BrowserReloadMiddleware',

]
```

Configure templates:

```
TEMPLATES = [
    {
        ...
        'DIRS': [Path(BASE_DIR).joinpath("templates")],
        ...
    },
]
```

Add SITE_ID:

```
SITE_ID = 1
```

Add other settings to settings.py:

```
# staitc and media
STATIC_URL = '/static/'
STATIC_ROOT = Path(BASE_DIR).joinpath("static")
MEDIA_ROOT = Path(BASE_DIR).joinpath("media")
MEDIA_URL = '/media/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # django-compressor
    'compressor.finders.CompressorFinder',
)

# auth
AUTH_USER_MODEL = 'core.User'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# crispy
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# comments-ink
COMMENTS_APP = "django_comments_ink"
COMMENTS_HIDE_REMOVED = False

COMMENTS_INK_SALT = "G0h5gt073h6gH4p25GS2g5AQ2Tm256yGt134tMP5TgCX$&HKOYRV"
COMMENTS_INK_CONFIRM_EMAIL = True  # Set to False to disable confirmation
COMMENTS_INK_FROM_EMAIL = "hello@example.com"
COMMENTS_INK_CONTACT_EMAIL = "hello@example.com"

# Default to True, use False to allow other
# backend (say Celery based) send your emails.
COMMENTS_INK_THREADED_EMAILS = False

COMMENTS_INK_API_USER_REPR = lambda user: user.username

COMMENTS_INK_SEND_HTML_EMAIL = True

# This setting is to apply a maximum thread level of 1 to all apps by default.
COMMENTS_INK_MAX_THREAD_LEVEL = 3

# This setting applies a maximum thread level of 1 only to the 'quotes.quote'
# app model. Useful in case you want to allow different levels of comment
# nesting to different app models.
# COMMENTS_INK_MAX_THREAD_LEVEL_BY_APP_MODEL = {
#     'quotes.quote': 3  # Meaning 4 levels: from 0 to 3.
# }

COMMENTS_INK_APP_MODEL_OPTIONS = {
    "default": {
        "who_can_post": "all",  # Valid values: "users", "all".
        "comment_flagging_enabled": True,
        "comment_reactions_enabled": True,
        "object_reactions_enabled": True,
    },
    "demo.post": {
        "check_input_allowed": "demo.models.check_comments_input_allowed"
    },
}

# All HTML elements rendered by django-comments-ink use the 'dci' CSS selector,
# defined in 'django_comments_ink/static/django_comments_ink/css/comments.css'.
# You can alter the CSS rules applied to your comments adding your own custom
# selector to the following setting.
COMMENTS_INK_CSS_CUSTOM_SELECTOR = "dci dci-custom"

# The theme dir, corresponds with any of the directories listed
# with the template directory: comments/themes/<theme_dir>.
COMMENTS_INK_THEME_DIR = "simple_reply"


# Display up to the given number of comments in the last page to avoid
# creating another page containing only these amount of comments.
COMMENTS_INK_MAX_LAST_PAGE_ORPHANS = 4

# Number of comments per page. When <=0 pagination is disabled.
COMMENTS_INK_COMMENTS_PER_PAGE = 100

# Do not override Django Rest Framework renderer_classes and pagination_class.
COMMENTS_INK_OVERRIDE_DRF_DEFAULTS = False

COMMENTS_XTD_LIST_ORDER = ('order')

# define login and urls
LOGIN_URL = '/a/login/'
LOGIN_REDIRECT_URL = '/a/profile/'
# define email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# set django-avatar amount of avatars stored for each user
AVATAR_MAX_AVATARS_PER_USER = 1
# django-newsletter thumb resizer (sorl-thumbnail)
NEWSLETTER_THUMBNAIL = 'sorl-thumbnail'
HONEYPOT_FIELD_NAME = 'phone'
```
