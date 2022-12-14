#(Β©)Codexbotz

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "<b>π΅πΎπππ°ππ³ ππ·π΄ π΅πΈπππ πΌπ΄πππ°πΆπ΄ π΅ππΎπΌ ππ·π΄ π³π± π²π·π°π½π½π΄π» (ππΈππ· π΅πΎπππ°ππ³ ππΎπππ΄)....\n\nπΎπ\n\nππ΄π½π³ ππ·π΄ πΏπΎππ π»πΈπ½πΊ</b>", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("<b>π« π΄πππΎπ\n\nππ·πΈπ π΅πΎπππ°ππ³π΄π³ πΏπΎππ πΈπ π½πΎπ π΅ππΎπΌ πΌπ π³π± π²π·π°π½π½π΄π» πΎπ π»πΈπ½πΊ πΈπ π½πΎπ ππ°πΊπ΄π½ π΅ππΎπΌ π³π± π²π·π°π½π½π΄π»...</b>", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "<b>π΅πΎπππ°ππ³ ππ·π΄ π»π°ππ πΌπ΄πππ°πΆπ΄ π΅ππΎπΌ ππ·π΄ π³π± π²π·π°π½π½π΄π» (ππΈππ· π΅πΎπππ°ππ³ ππΎπππ΄)....\n\nπΎπ\n\nππ΄π½π³ ππ·π΄ πΏπΎππ π»πΈπ½πΊ</b>", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("<b>π« π΄ππππ\n\nππ·πΈπ π΅πΎπππ°ππ³π΄π³ πΏπΎππ πΈπ π½πΎπ π΅ππΎπΌ πΌπ π³π± π²π·π°π½π½π΄π» πΎπ π»πΈπ½πΊ πΈπ π½πΎπ ππ°πΊπ΄π½ π΅ππΎπΌ π³π± π²π·π°π½π½π΄π»...</b>", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("β‘ πππΌππ πππ β‘", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>π·π΄ππ΄ πΈπ ππΎππ π»πΈπ½πΊ</b>\n\n{link}", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("<b>π« π΄ππππ\n\nππ·πΈπ π΅πΎπππ°ππ³π΄π³ πΏπΎππ πΈπ π½πΎπ π΅ππΎπΌ πΌπ π³π± π²π·π°π½π½π΄π» πΎπ π»πΈπ½πΊ πΈπ π½πΎπ ππ°πΊπ΄π½ π΅ππΎπΌ π³π± π²π·π°π½π½π΄π»...</b>", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("β‘ SHARE URL β‘", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>π·π΄ππ΄ πΈπ ππΎππ π»πΈπ½πΊ</b>\n\n{link}", quote=True, reply_markup=reply_markup)
