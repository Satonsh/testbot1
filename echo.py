from telethon import TelegramClient

# Use your own values from my.telegram.org
api_id = 1086018
api_hash = '3c2f1a043c1a22d5b0af74b8268993d5c'

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))
