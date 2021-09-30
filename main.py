from pyrogram import Client, filters
from pyrogram.types import Message

import os


from crop import crop_logo
from sticker import stick_logo
from text import write_text


BOT_TOKEN = os.environ.get('BOT_TOKEN')
API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')

m = Client("m", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@m.on_message(filters.command("savelogo", prefixes="/"))
async def save_logo(Client, message: Message):
  if message.reply_to_message.photo or message.reply_to_message.document:
    k=await message.client.download_media(message=reply_message, file_name="banner/logo.png")
    b=f"Downloaded {k}"
    await message.reply(message.chat_id, b)
    
@m.on_message(filters.command("setwinners", prefixes="/"))
async def set_winners(Client, message: Message):
  if message.reply_to_message.text:
    k = message.reply_to_message.text.split("\n")
    with open("banner/winners.txt", "wb") as f:
      f.write(k)

@m.on_message(filters.command("makebanner", prefixes="/"))
async def make_banner(clayy: Client, message: Message):
  crop_logo()
  stick_logo()
  write_text()
  await clayy.send_photo(message.chat_id, "banner/banner.png")
  
m.run()
