from helper.progress import progress_for_pyrogram
from pyrogram import Client, filters
from pyrogram.types import (  InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from helper.database import find
import os
from PIL import Image
import time

@Client.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "help":
        await msg.message.edit(
            text=f"""
𝙵𝚘𝚕𝚕𝚘𝚠 𝚝𝚑𝚎𝚜𝚎 𝚂𝚝𝚎𝚙𝚜 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙼𝚎𝚑..
 
➠ 𝙲𝚘𝚗𝚏𝚒𝚐𝚞𝚛𝚎 𝚝𝚑𝚎 𝚂𝚎𝚝𝚝𝚒𝚗𝚐𝚜 𝚋𝚎𝚏𝚘𝚛𝚎 𝚞𝚜𝚒𝚗𝚐 𝚖𝚎.....
➠ 𝚂𝚎𝚗𝚍 𝚊 𝚙𝚑𝚘𝚝𝚘 𝚝𝚘 𝚜𝚎𝚝 𝚒𝚝 𝚊𝚜 𝚢𝚘𝚞𝚛 𝚌𝚞𝚜𝚝𝚘𝚖 𝚝𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕..... 
➠ 𝚂𝚎𝚗𝚍 𝚊𝚗𝚢 𝙵𝚒𝚕𝚎 𝚘𝚛 𝚖𝚎𝚍𝚒𝚊 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝 𝚝𝚘 𝚛𝚎𝚗𝚊𝚖𝚎..... 
➠ 𝚃𝚑𝚊𝚝'𝚜 𝚒𝚝, 𝚊𝚗𝚍 𝚛𝚎𝚜𝚝 𝚒𝚜 𝚖𝚒𝚗𝚎 𝚠𝚘𝚛𝚔.....

📝 𝙰𝚟𝚊𝚒𝚕𝚊𝚋𝚕𝚎 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 📝

- /start - 𝚂𝚝𝚊𝚛𝚝 𝚝𝚑𝚎 𝙱𝚘𝚝
- /help - 𝙷𝚘𝚠 𝚝𝚘 𝚄𝚜𝚎
- /about - 𝙰𝚋𝚘𝚞𝚝 𝙼𝚎
- /settings - 𝙲𝚘𝚗𝚏𝚒𝚐𝚞𝚛𝚎 𝚂𝚎𝚝𝚝𝚒𝚗𝚐𝚜 
- /show_thumb & /del_thumb - 𝙵𝚘𝚛 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕

© 𝙼𝚊𝚍𝚎 𝚠𝚒𝚝𝚑 ❣️ @KR_BOTZ & @BGM_LinkzZ """, 
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("🐼 𝐁𝐀𝐂𝐊 🐼",callback_data = "start"), 
	  InlineKeyboardButton("↪️ 𝐂𝐥𝐨𝐬𝐞 ↩️",callback_data = "cancel")
          ]]
        ) 
    ) 

@Client.on_callback_query(filters.regex('cancel'))
async def cancel(bot,update):
	try:
		await update.message.delete()
	except:
		return
@Client.on_callback_query(filters.regex('rename'))
async def rename(bot,update):
	user_id = update.message.chat.id
	date = update.message.date
	await update.message.delete()
	await update.message.reply_text("__Please enter the new filename...__",	
	reply_to_message_id=update.message.reply_to_message.message_id,  
	reply_markup=ForceReply(True))
	
@Client.on_callback_query(filters.regex("doc"))
async def doc(bot,update):
     new_name = update.message.text
     name = new_name.split(":-")
     new_filename = name[1]
     file_path = f"downloads/{new_filename}"
     file = update.message.reply_to_message
     ms = await update.message.edit("``` Trying To Download...```")
     c_time = time.time()
     try:
     	path = await bot.download_media(message = file, progress=progress_for_pyrogram,progress_args=( "``` Trying To Download...```",  ms, c_time   ))
     except Exception as e:
     	await ms.edit(e)
     	return
     	
     splitpath = path.split("/downloads/")
     dow_file_name = splitpath[1]
     old_file_name =f"downloads/{dow_file_name}"
     os.rename(old_file_name,file_path)
     user_id = int(update.message.chat.id)
     thumb = find(user_id)
     if thumb:
     		ph_path = await bot.download_media(thumb)
     		Image.open(ph_path).convert("RGB").save(ph_path)
     		img = Image.open(ph_path)
     		img.resize((320, 320))
     		img.save(ph_path, "JPEG")
     		c_time = time.time()
     		await ms.edit("```Trying To Uploading```")
     		c_time = time.time()
     		try:
     			await bot.send_document(update.message.chat.id,document = file_path,thumb=ph_path,caption = f"**{new_filename}**",progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
     			await ms.delete()
     			os.remove(file_path)
     			os.remove(ph_path)
     		except Exception as e:
     			await ms.edit(e)
     			os.remove(file_path)
     			os.remove(ph_path)
     			     		     		
     else:
     		await ms.edit("```Trying To Uploading```")
     		c_time = time.time()
     		try:
     			await bot.send_document(update.message.chat.id,document = file_path,caption = f"**{new_filename}**",progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
     			await ms.delete()
     			os.remove(file_path)
     		except Exception as e:
     			await ms.edit(e)
     			os.remove(file_path)
     			     		   		
     		
@Client.on_callback_query(filters.regex("vid"))
async def vid(bot,update):
     new_name = update.message.text
     name = new_name.split(":-")
     new_filename = name[1]
     file_path = f"downloads/{new_filename}"
     file = update.message.reply_to_message
     ms = await update.message.edit("``` Trying To Download...```")
     c_time = time.time()
     try:
     	path = await bot.download_media(message = file, progress=progress_for_pyrogram,progress_args=( "``` Trying To Download...```",  ms, c_time   ))
     except Exception as e:
     	await ms.edit(e)
     	return
     
     splitpath = path.split("/downloads/")
     dow_file_name = splitpath[1]
     old_file_name =f"downloads/{dow_file_name}"
     os.rename(old_file_name,file_path)
     duration = 0
     metadata = extractMetadata(createParser(file_path))
     if metadata.has("duration"):
     		duration = metadata.get('duration').seconds
     user_id = int(update.message.chat.id)
     thumb = find(user_id)
     if thumb:
     		ph_path = await bot.download_media(thumb)
     		Image.open(ph_path).convert("RGB").save(ph_path)
     		img = Image.open(ph_path)
     		img.resize((320, 320))
     		img.save(ph_path, "JPEG")
     		c_time = time.time()
     		await ms.edit("```Trying To Uploading```")
     		c_time = time.time()
     		try:
     			await bot.send_video(update.message.chat.id,video = file_path,caption = f"**{new_filename}**",thumb=ph_path,duration =duration, progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
     			await ms.delete()
     			os.remove(file_path)
     			os.remove(ph_path)   				
     		except Exception as e:
     				await ms.edit(e)
     				os.remove(file_path)
     				os.remove(ph_path)
     				
     else:
     		await ms.edit("```Trying To Uploading```")
     		c_time = time.time()
     		try:
     			await bot.send_video(update.message.chat.id,video = file_path,caption = f"**{new_filename}**",duration = duration, progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
     			await ms.delete()
     			os.remove(file_path)
     		except Exception as e:
     			await ms.edit(e)
     			os.remove(file_path)
   
     			     		     		
@Client.on_callback_query(filters.regex("aud"))
async def aud(bot,update):
     new_name = update.message.text
     name = new_name.split(":-")
     new_filename = name[1]
     file_path = f"downloads/{new_filename}"
     file = update.message.reply_to_message
     ms = await update.message.edit("``` Trying To Download...```")
     c_time = time.time()
     try:
     	path = await bot.download_media(message = file , progress=progress_for_pyrogram,progress_args=( "``` Trying To Download...```",  ms, c_time   ))
     except Exception as e:
     	await ms.edit(e)
     	return
     splitpath = path.split("/downloads/")
     dow_file_name = splitpath[1]
     old_file_name =f"downloads/{dow_file_name}"
     os.rename(old_file_name,file_path)
     duration = 0
     metadata = extractMetadata(createParser(file_path))
     if metadata.has("duration"):
     	duration = metadata.get('duration').seconds
     user_id = int(update.message.chat.id)
     thumb = find(user_id)
     if thumb:
     		ph_path = await bot.download_media(thumb)
     		Image.open(ph_path).convert("RGB").save(ph_path)
     		img = Image.open(ph_path)
     		img.resize((320, 320))
     		img.save(ph_path, "JPEG")
     		await ms.edit("```Trying To Uploading```")
     		c_time = time.time()
     		try:
     			await bot.send_audio(update.message.chat.id,audio = file_path,caption = f"**{new_filename}**",thumb=ph_path,duration =duration, progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
     			await ms.delete()
     			os.remove(file_path)
     			os.remove(ph_path)
     		except Exception as e:
     			await ms.edit(e)
     			os.remove(file_path)
     			os.remove(ph_path)
     else:
     		await ms.edit("```Trying To Uploading```")
     		c_time = time.time()
     		try:
     			await bot.send_audio(update.message.chat.id,audio = file_path,caption = f"**{new_filename}**",duration = duration, progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
     			await ms.delete()
     			os.remove(file_path)
     		except Exception as e:
     			await ms.edit(e)
     			os.remove(file_path)		
