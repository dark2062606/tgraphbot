import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Jebot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Jebot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Salom, men Telegraph Botiman

 Surat yoki videolarni telegrafga yuklashim mumkin. 

 Mendan qanday foydalanish haqida ko'proq bilish uchun yordam tugmasini bosing</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Yordam", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Kanal", url="https://t.me/Api_Kod")
                                    ],[
                                      InlineKeyboardButton(
                                            "Dasturchi", url="https://t.me/Liderboy")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Telegraph Bot-yordam!

 Fayl hajmi 5mb dan kam bo'lgan rasm yoki videoni yuboring, men uni telegraphga yuklayman.

@TgraphUploaderbot</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Orqaga", callback_data="start"),
                                        InlineKeyboardButton(
                                            "Bot haqida", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "Dasturchi", url="https://t.me/Liderboy")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Bot haqida!</b>

<b>Dasturchi:</b> <a href="https://t.me/Liderboy">Arslonbek</a>

<b>Kanal:</b> <a href="https://t.me/Api_Kod">Api Kod</a>

<b>iTarona bot:</b> <a href="https://t.me/iTarona_bot">iTarona bot</a>

<b>@LiderBoy</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Orqaga", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Dasturchi", url="https://t.me/Liderboy")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("Telegraph ga yuklanmoqda...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Rasm hajmi 5 mb dan yuqori!") 
    else:
        await msg.edit_text(f'**Telegraph ga yuklandi!\n\ https://telegra.ph{response[0]}\n\n @TgraphUploaderbot**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Jebot.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("Telegraph ga yuklanmoqda...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Video hajmi 5 mb dan yuqori!") 
    else:
        await msg.edit_text(f'**Telegraph ga yuklandi!\n\n https://telegra.ph{response[0]}\n\n @TgraphUploaderbot**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Jebot.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("Telegraph ga yuklanmoqda...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif hajmi 5 mb dan yuqori!") 
    else:
        await msg.edit_text(f'**Telegraph ga yuklandi!\n\n https://telegra.ph{response[0]}\n\n@TgraphUploaderbot**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Jebot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Bot Started!
"""
)

Jebot.run()
