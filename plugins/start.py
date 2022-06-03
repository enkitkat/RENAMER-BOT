from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_photo(
        photo="https://telegra.ph/file/e954574ef60c1790caa79.jpg", 
        caption =f"""
	𝐈𝐭'𝐬 𝐏𝐨𝐰𝐞𝐫 𝐅𝐮𝐥𝐥 {message.from_user.mention} 😎 𝐅𝐢𝐥𝐞 𝐑𝐞𝐧𝐚𝐦𝐞𝐫 𝐛𝐨𝐭 + 𝐅𝐢𝐥𝐞 𝟐 𝐕𝐢𝐝𝐞𝐨 𝐂𝐨𝐧𝐞𝐫𝐭𝐞𝐫 𝐁𝐎𝐓 𝐰𝐢𝐭𝐡 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 💖 𝐒𝐡𝐚𝐫𝐞 𝐀𝐧𝐝 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐔𝐬.....!!!🦋
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ" ,url="https://t.me/+MB8a61q_98A3MThl"), 
	  InlineKeyboardButton("Uᴘᴅᴀᴛᴇ", url="https://t.me/+hR6DpC_xpPBiM2Zl")
          ],[
          InlineKeyboardButton("🧩 Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ 🧩", url="https://t.me/kr_admin_bot")
          ],[
          InlineKeyboardButton("🧞‍♀️ Hᴇʟᴘ 🧞‍♂️",callback_data = "help"), 
          InlineKeyboardButton("↪️ Cʟᴏsᴇ ↩️",callback_data = "cancel")
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
       ,InlineKeyboardButton("↪️ 𝐂ʟᴏsᴇ ↩️",callback_data = "cancel")  ]]))
