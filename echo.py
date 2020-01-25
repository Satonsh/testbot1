from telethon.sync import TelegramClient, events

with TelegramClient('name', 1151409, 06ed8b1b54e3f6e001cf9e9078392a1b) as client:
   client.send_message('me', 'Hello, myself!')
   print(client.download_profile_photo('me'))

   @client.on(events.NewMessage(pattern='(?i).*Hello'))
   async def handler(event):
      await event.reply('Hey!')

   client.run_until_disconnected()