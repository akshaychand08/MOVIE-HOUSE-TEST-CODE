from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from plugins.malik.mbin import malikk
from os import environ




NOTFOUN = InlineKeyboardMarkup([[InlineKeyboardButton("Request", url="https://t.me/m_admins")]]) 

GSLB = InlineKeyboardMarkup([[InlineKeyboardButton("♻️ 𝐉𝐨𝐢𝐧 𝙂𝙧𝙤𝙪𝙥 ", url="https://t.me/+gXuMKXOWm1UyOTdl")],[ InlineKeyboardButton("♻️ 𝐉𝐨𝐢𝐧 𝙂𝙧𝙤𝙪𝙥 ", url="https://t.me/+gXuMKXOWm1UyOTdl")]]) 

HSTN = InlineKeyboardMarkup([[InlineKeyboardButton("❇️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ❇️", url=f"http://t.me/{malikk.u_name}?startgroup=true") ],[ InlineKeyboardButton('♻️ ʜᴇʟᴘ ♻️', callback_data='help'), InlineKeyboardButton('⚡️ᴜᴘᴅᴀᴛᴇs⚡️', url='https://t.me/m_house786')],[InlineKeyboardButton('sᴇᴀʀᴄʜ ɪɴʟɪɴᴇ', switch_inline_query_current_chat=''), InlineKeyboardButton('♻️ ᴀʙᴏᴜᴛ ♻️', callback_data='about')],[ InlineKeyboardButton('✅ sᴜʙsᴄʀɪʙᴇ ᴍʏ ʏᴛ ᴄʜᴀɴɴᴇʟ ✅', url='https://youtube.com/channel/UCPaHDqWf3D3w2nxb8p3sr4A')]])  

HSTNN = InlineKeyboardMarkup([[InlineKeyboardButton('❇️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ❇️', url=f'http://t.me/{malikk.u_name}?startgroup=true') ],[ InlineKeyboardButton('♻️ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ♻️', url='https://t.me/m_house786')],[ InlineKeyboardButton('🔹 ʜᴇʟᴘ 🔹', url=f"http://t.me/{malikk.u_name}?start=help")]])

GROUP_RULES = InlineKeyboardMarkup([[InlineKeyboardButton('♻️ GROUP RULES ♻️', callback_data='group_rules')]])

TFRADE = InlineKeyboardMarkup([[InlineKeyboardButton('♻️ Help ♻️', url=f"https://t.me/{malikk.u_name}?start=help"),InlineKeyboardButton('💎 Updates 💎', url='https://t.me/m_house786')],[InlineKeyboardButton('🌴 Bots Channel 🌴', url='https://t.me/malik_bots')]])
