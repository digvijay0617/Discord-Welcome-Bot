from __future__ import unicode_literals

import os

# Discord Settings
DISCORD_CLIENT_ID = os.environ.get('DISCORD_CLIENT_ID', '794118381287505941')
DISCORD_SECRET = os.environ.get('DISCORD_SECRET', 'tq9CnFl_L9MC-OzP7ZXXkjHXE0m05Mie')
DISCORD_PUBLIC_KEY = os.environ.get('DISCORD_PUBLIC_KEY', '8145699bb5a23703d8090fc115064196104bdf11e23dbcea8a3f79c663b994c5')

# Bot Settings
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'Nzk0MTE4MzgxMjg3NTA1OTQx.X-2KYA.5dbp7wxTBglgbgBnERhpdVVWKTo')

# Google Settings
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', 'AIzaSyDOyGreOLIrHJCqBbHtt6QYewsiVh7zlM4')
GOOGLE_ENGINE_ID = os.environ.get('GOOGLE_ENGINE_ID', 'e31b260be6bfe6d76')

REQUEST_TIMEOUT = 30  # In second

#  Database setting
DATABASES = {
    'DATABASE_URL': os.environ.get('DATABASE_URL')
}
