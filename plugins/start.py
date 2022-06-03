from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 
from Script import script
from pyrogram.types import CallbackQuery

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_photo(
        photo="https://telegra.ph/file/be833e64240bfd11a306d.jpg", 
        caption =f"""
	<b> Iᴛ's PᴏᴡᴇʀFᴜʟ {message.from_user.mention} 🧛‍♂️ Fɪʟᴇs Rᴇɴᴀᴍᴇʀ Bᴏᴛ ➕ Fɪʟᴇ 2 Vɪᴅᴇᴏ Cᴏɴᴇʀᴛᴇʀ BOT Wɪᴛʜ Pᴇʀᴍᴀɴᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ 💞....!! 
Sʜᴀʀᴇ Aɴᴅ Sᴜᴘᴘᴏʀᴛ Us......!!! 🦋 </b>
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ" ,url="https://t.me/BATMAN_0"), 
	  InlineKeyboardButton("Uᴘᴅᴀᴛᴇ", url="https://t.me/BATMAN_0")
          ],[
          InlineKeyboardButton("😎 Owner 😎", url="https://t.me/BATMAN_0")
          ],[
          InlineKeyboardButton("🧞‍♀️ Hᴇʟᴘ 🧞‍♂️",callback_data = "help"), 
          InlineKeyboardButton("🚫 Cʟᴏsᴇ 🚫",callback_data = "cancel")
          ]]
          )
        )

@Client.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "help":
        await msg.message.edit(
            text=Script.HELP_TXT , 
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("⚡️ 𝐁𝐀𝐂𝐊 ⚡️",callback_data = "start"), 
	  InlineKeyboardButton("🚫 𝐂𝐥𝐨𝐬𝐞 🚫",callback_data = "cancel")
          ]]
        ) 
    ) 

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__What do you want me to do with this file?__\n**File Name** :- <code>{filename}</code> \n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 𝐑ᴇɴᴀᴍᴇ ",callback_data = "rename")
       ,InlineKeyboardButton("🚫 𝐂ʟᴏsᴇ 🚫",callback_data = "cancel")  ]]))
