from .settings_common import *

# 開発環境の環境設定

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing': False,  # 既定のロガーを無効化
    # ロガーの設定
    'loggers': {
        # Djangoが使うロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリが使うロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev',
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(lineno)d',
                '%(message)s'
            ])
        },
    }
}
