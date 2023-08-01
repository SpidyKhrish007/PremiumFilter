import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("I AM ALIVE DONT WORRY :) PRESS 👉 /start \n\nPʀᴇss 👉 /help Fᴏʀ Hᴇʟᴩ ;)\n\n\nPʀᴇss 👉 /ping Tᴏ CHECK MY PING 😁")

@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("PRESS 👉 /movies FOR HOW TO REQUEST CONTENT IN PROPER WAY 📃\n\nPRESS 👉 /series TO LEARN HOW TK REQUEST SERIES IN CORRECT WAY 📃\n\n\nPʀᴇss 👉 /tutorial FOR TUTORIAL ABOUT HOW TO GET DIRECT FILES FROM ME 🤗")

@Client.on_message(filters.command("credits", CMD))
async def help(_, message):
    await message.reply_text("THIS IS CODED BY DEVS @YEDEKHO\n\n  THANKS FOR EVA MARIA ﹝ ʙᴀsᴇ ᴄᴏᴅᴇ ﹞")

@Client.on_message(filters.command("movies", CMD))
async def movie(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\nᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ᴀᴠᴀᴛᴀʀ: ᴛʜᴇ ᴡᴀʏ ᴏғ ᴡᴀᴛᴇʀ\n\n🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)\n\nᴄᴏᴅᴇᴅ ʙʏ @yedekho")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\nꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ᴍᴏɴᴇʏ ʜᴇɪsᴛ S01E01\n\n🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)\n\nᴄᴏᴅᴇᴅ ʙʏ @yedekho")

@Client.on_message(filters.command("download", CMD))
async def tutorial(_, message):
    await message.reply_text("👉 Sᴇɴᴅ Aɴʏ Mᴏᴠɪᴇs / Sᴇʀɪᴇs Nᴀᴍᴇ Wɪᴛʜ Cᴏᴛᴛᴇᴄᴛ Sᴩᴇʟʟɪɴɢ Aɴᴅ I Wɪʟʟ Sᴇɴᴅ Tʜᴇ Fɪʟᴇ Lɪɴᴋ/n/nCᴏʀʀᴇᴄᴛ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛɪɴɢ Mᴇᴛʜᴏᴅ 👉 /movies /n/nCᴏʀʀᴇᴄᴛ Sᴇʀɪᴇs Rᴇǫᴜᴇsᴛɪɴɢ Mᴇᴛʜᴏᴅ 👉 /series")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pɪɴɢ🔥!\n{time_taken_s:.3f} ms")
