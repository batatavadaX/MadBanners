from pyrogram import Client, filters
from pyrogram.types import Message

import os

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from crop import crop_logo
from sticker import stick_logo
from text import write_text


BOT_TOKEN = os.environ.get('BOT_TOKEN')
API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')

m = Client("m", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@m.on_message(filters.command("savelogo", prefixes="/"))
async def download_file(Client, message: Message):
  if message.reply_to_message.photo or message.reply_to_message.document:
    k=await Client.download_media(message=message.reply_to_message, file_name="banner/logo.png")
    b=f"logo download thi gayo {k}"
    await message.reply(b)
    
@m.on_message(filters.private & (filters.document | filters.photo))
async def auto_logo(Client, message):
  await message.reply_text(
    "Save karaso ke nai ?",
    quote=True,
    reply_markup=InlineKeyboardMarkup([
      [InlineKeyboardButton(text="haa", callback_data="download_file")],
      [InlineKeyboardButton(text="nathi karavu", callback_data="cl_ose")]
    ])
  )
  
@m.on_message(filters.command("setwinners", prefixes="/"))
async def set_winners(Client, message: Message):
  if message.reply_to_message.text:
    k = message.reply_to_message.text.split("\n")
    with open("banner/winners.txt", "w") as f:
      for item in k:
        f.write(item + "\n")
  await message.reply("Winners Set Kari didha ")
@m.on_message(filters.command("makebanner", prefixes="/"))
async def make_banner(clayy: Client, message: Message):
  crop_logo()
  stick_logo()
  write_text()
  await clayy.send_photo(message.chat.id, "banner/banner.png")
  
m.run()
