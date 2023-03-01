# LISA-KOREA | @LISA_FAN_LK

import os
from functions.display_progress import progress_for_pyrogram, humanbytes
from plugins.config import Config
from plugins.dl_button import ddl_call_back
from plugins.youtube_dl_button import youtube_dl_call_back
from plugins.settings.settings import OpenSettings
from plugins.translation import Translation
from pyrogram import Client, types
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.database.database import db
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

START_IMG_URL = "https://telegra.ph/file/9b11307f07f5d92295f4d.jpg"

@Client.on_callback_query()
async def button(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=Translation.START_TEXT.format(update.from_user.mention),
            reply_markup=Translation.START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=Translation.HELP_TEXT,
            reply_markup=Translation.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=Translation.ABOUT_TEXT,
            reply_markup=Translation.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "premium":
        await bot.send_photo(update.message.chat.id, START_IMG_URL, """
        ➥ UPI ID : praveenonnew@okaxis
        ➥ Paytm : /QR_CODE

        Send Payment Screenshot & Your Telegram Id @alpha_romeo_06""",
          reply_markup=types.InlineKeyboardMarkup([[
                                   types.InlineKeyboardButton("premium upgrade",
                                                              callback_data="close")
                               ]])
        )
    elif update.data == "paid":
        await bot.send_photo(update.message.chat.id, START_IMG_URL, """
        PAID PLANS AVAILABLE

🛡️ PLAN 🛡️

🌸 Per Month ₹80/$1.3
🌸 Allowed Links
🌸 No limit
🌸 Mediafire link support
🌸 Fembed link support
🌸 No Timeout
🌸 Support other link
 Send Payment Screenshot & Your Telegram Id @alpha_romeo_06
 Please upgrade your subscription""",
          reply_markup=types.InlineKeyboardMarkup([[
                                   types.InlineKeyboardButton("paid plans",
                                                              callback_data="close")
                               ]])
        )
    elif update.data == "PLANS":
        await bot.send_photo(update.message.chat.id, START_IMG_URL, """
        How To Use This Bot 🤔
   
𖣔 First go to the /settings and change the bot behavior as your choice.

𖣔 Send me the custom thumbnail to save it permanently.

𖣔 Send url | New Name.mkv

𖣔 Youtube link support ✓

𖣔 Google drive link support ✓

𖣔 Zee5 shows support ✓

𖣔 Mediafire link support ✓

𖣔 Voot shows Support ✓

𖣔 Tiktok link support ✓

𖣔 Mdisk link support ✓

𖣔 Fembed link support ✓

𖣔 Magnet link 

𖣔 ONLY PAID USER SUPPORT THIS LINKS

𖣔 Select the desired option.

𖣔 Then be relaxed your file will be uploaded soon..
Send Payment Screenshot & Your Telegram Id @alpha_romeo_06
𖣔  to Set caption as Reply to Media""",
          reply_markup=types.InlineKeyboardMarkup([[
                                   types.InlineKeyboardButton("plans",
                                                              callback_data="close")
                               ]])
        )
    elif update.data == "OpenSettings":
        await update.answer()
        await OpenSettings(update.message)
    elif update.data == "showThumbnail":
        thumbnail = await db.get_thumbnail(update.from_user.id)
        if not thumbnail:
            await update.answer("You didn't set any custom thumbnail!", show_alert=True)
        else:
            await update.answer()
            await bot.send_photo(update.message.chat.id, thumbnail, "Custom Thumbnail",
                               reply_markup=types.InlineKeyboardMarkup([[
                                   types.InlineKeyboardButton("Delete Thumbnail",
                                                              callback_data="deleteThumbnail")
                               ]]))
    elif update.data == "deleteThumbnail":
        await db.set_thumbnail(update.from_user.id, None)
        await update.answer("Okay, I deleted your custom thumbnail. Now I will apply default thumbnail.", show_alert=True)
        await update.message.delete(True)
    elif update.data == "setThumbnail":
        await update.message.edit_text(
            text=Translation.TEXT,
            reply_markup=Translation.BUTTONS,
            disable_web_page_preview=True
        )

    elif update.data == "triggerUploadMode":
        await update.answer()
        upload_as_doc = await db.get_upload_as_doc(update.from_user.id)
        if upload_as_doc:
            await db.set_upload_as_doc(update.from_user.id, False)
        else:
            await db.set_upload_as_doc(update.from_user.id, True)
        await OpenSettings(update.message)
    elif "close" in update.data:
        await update.message.delete(True)

    elif "|" in update.data:
        await youtube_dl_call_back(bot, update)
    elif "=" in update.data:
        await ddl_call_back(bot, update)

    else:
        await update.message.delete()
