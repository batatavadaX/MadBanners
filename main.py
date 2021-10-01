from pyrogram import Client, filters

import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
 
from crop import crop_logo
from sticker import stick_logo
from text import write_text


BOT_TOKEN = os.environ.get('BOT_TOKEN')
API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')

m = Client("m", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


# @m.on_message(filters.command("savelogo", prefixes="/"))

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

@m.on_callback_query()
async def download_file(Client, query: CallbackQuery):
  if query.data == "download_file":
    k=await Client.download_media(message=query.message.reply_to_message, file_name="banner/logo.png")
    await query.message.edit_text(text="download thai gyu")
    await query.message.reply_text(
    "Winner Set Karo",
    quote=True,
    reply_markup=InlineKeyboardMarkup([
      [InlineKeyboardButton(text="haa", callback_data="winners")],
    ])
  )
  elif query.data == "cl_ose":
    await query.message.edit_text(text="Je logo set karavo hoy a mokalane ne")
  elif query.data == "winners":
   keyboard = ([[KeyboardButton("winner nu naam enter karo")]])
   await message.reply_text("test", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=TruE))    
   
   
   
   
   
   
      # with open("banner/winners.txt", "w") as f:
        # for item in k:
        # f.write(item + "\n")
   # await query.message.reply("Winners Set Kari didha ")


    
m.run()
