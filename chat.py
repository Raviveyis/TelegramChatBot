from sozler.message import(
salam, necesen, getdim, geldim, RaviBey,
ban, emoji1, emoji2, fed, niye, ne, hay,
mal, can, balam, xos, hara, gel, gordum,
team, pp, info)

from telethon import TelegramClient, events
from telethon import Button
from Config import Config 
import logging
import random

logging.basicConfig(level=logging.INFO,format='%(name)s - [%(levelname)s] - %(message)s')
LOGGER = logging.getLogger(__name__)

isleyen = []

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
ravibey = TelegramClient('ravibey', api_id, api_hash).start(bot_token=bot_token)

@ravibey.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in ravibey.iter_participants(event.chat_id):
     ravi = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"""                      
╔═════════════════
║▻ 🙋‍♀️ Salam {ravi}
║
║▻ 🙎‍♀️ Mənim Adım [{Config.BOT_NAME}](t.me/{Config.BOT_USERNAME}) Mən 
║▻ 🇦🇿 Azərbaycan Dilində Chat Botuyam
║▻ 💌 Bacarıqlarımı Görmək Üçün
║▻ 📚 Kömək Info Butonuna Toxun
╚═════════════════
""",buttons=(
    [Button.inline(f"📚 Əmrlər", data="info"),
	Button.inline(f"📑 Təkliflər", data="reklam")],
    [Button.url('✜ Qrupa əlavə et ✜',f"http://t.me/{Config.BOT_USERNAME}?startgroup=new")],
	[Button.url('💬 Qrup', f"https://t.me/{Config.SUPPORT_CHANNEL}"),
    Button.url('📺 Kanal', f'https://t.me/{Config.SUPPORT_CHANNEL}')],),
            link_preview=False)

@ravibey.on(events.callbackquery.CallbackQuery(data="start"))
async def start(event):
  if event.is_private:
    async for usr in ravibey.iter_participants(event.chat_id):
        ravi = f"[{usr.first_name}](tg://user?id={usr.id})"
    await event.edit(f"""                      
╔═════════════════
║▻ 🙋‍♀️ Salam {ravi}
║
║▻ 🙎‍♀️ Mənim Adım [{Config.BOT_NAME}](t.me/{Config.BOT_USERNAME}) Mən 
║▻ 🇦🇿 Azərbaycan Dilində Chat Botuyam
║▻ 💌 Bacarıqlarımı Görmək Üçün
║▻ 📚 Kömək Info Butonuna Toxun
╚═════════════════
""",buttons=(
    [Button.inline(f"📚 Əmrlər", data="info"),
	Button.inline(f"📑 Təkliflər", data="reklam")],
    [Button.url('✜ Qrupa əlavə et ✜',f"http://t.me/{Config.BOT_USERNAME}?startgroup=new")],
	[Button.url('💬 Qrup', f"https://t.me/{Config.SUPPORT_CHANNEL}"),
    Button.url('📺 Kanal', f'https://t.me/{Config.SUPPORT_CHANNEL}')],),
            link_preview=False)

@ravibey.on(events.callbackquery.CallbackQuery(data="reklam"))
async def handler(event):	
    await event.edit(f"**[{Config.BOT_NAME}](t.me/{Config.BOT_USERNAME}) Təkliflər üçün sahib'lə əlaqə saxlaya bilərsiniz.**",
                buttons=(
	[Button.url('🎉 Sahib', f'https://t.me/{Config.OWNER_USERNAME}')],
	[Button.url('💬 Qrup', f'https://t.me/{Config.SUPPORT_GROUP}'),
    Button.url('📺 Kanal', f"https://t.me/{Config.SUPPORT_CHANNEL}")],
	[Button.inline(f"◅ Geri", data="start")]),
            link_preview=False)                      

@ravibey.on(events.callbackquery.CallbackQuery(data="info"))
async def yeni_mesaj(event):
    await event.edit(f"""
                      
╔═════════════════
║▻ 
║
║▻ [{Config.BOT_NAME}](t.me/{Config.BOT_USERNAME}) Mən 
║▻ 
║▻ 
║▻ 
╚═════════════════                    
""",buttons=(
	[Button.url('✜ Qrupa əlavə et ✜',f"http://t.me/{Config.BOT_USERNAME}?startgroup=new")],
	[Button.url('🎉 Sahib', f'https://t.me/{Config.OWNER_USERNAME}')],
	[Button.inline("◅ Geri", data="start")],),
            link_preview=False)



@ravibey.on(events.NewMessage(pattern='(?i)bot+'))
@ravibey.on(events.NewMessage(pattern='(?i)chatbot+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"Botun işləməsi üçün /chatbot yazin")

@ravibey.on(events.NewMessage(pattern="^/chatbot ?(.*)"))
async def chatbot(event):
    global isleyen
    emr = event.pattern_match.group(1)
    qrup = event.chat_id
    if emr == "ON" or emr == "on" or emr == "On":
        if qrup not in isleyen:
            isleyen.append(qrup)
            aktiv_olundu = "✅ **ChatBot Qrupda Aktiv Olundu !**"
            await event.reply(aktiv_olundu)
            return
        await event.reply("⚠️ **ChatBot Hal-hazırda Qrupda Aktivdir !**")
        return
    elif emr == "OFF" or emr == "off" or emr == "Off":
        if qrup in isleyen:
            isleyen.remove(qrup)
            await event.reply("⛔️ **ChatBot Qrupda Deaktiv Olundu !**")
            return # aykhan026 | aykhan_s
        await event.reply("⚠️ **ChatBot Hal-Hazırda Deaktivdir !**")
        return
    
    else:
        await event.reply("🤖 Chatbot u Aktiv Edmək Üçün On və  Off yazın")

@ravibey.on(events.NewMessage)
async def chatbot(event):
    global isleyen
    mesaj = str(event.raw_text)
    qrup = event.chat_id
    if qrup not in isleyen:
        return
    if "Salam" in mesaj or "salam" in mesaj:
        await event.reply(f"{random.choice(salam)}")
    if "necesen" in mesaj or "necəsən" in mesaj or "netersen" in mesaj or "nətərsən" in mesaj or "Netersen" in mesaj:
        await event.reply(f"{random.choice(necesen)}")
    if "Getdim" in mesaj or "getdim" in mesaj or "getdım" in mesaj:
        await event.reply(f"{random.choice(getdim)}")
    if "Geldim" in mesaj or "geldim" in mesaj or "geldım" in mesaj or "Geldım" in mesaj:
        await event.reply(f"{random.choice(geldim)}")
    if "@RaviBey" in mesaj or "RaviBey" in mesaj or "Ravi" in mesaj:
        await event.reply(f"{random.choice(RaviBey)}")
    if "Xaos" in mesaj or "xaos" in mesaj:
        await event.reply(f"{random.choice(fed)}")
    if "Ban" in mesaj or "ban" in mesaj or "/gban" in mesaj or "gban" in mesaj in mesaj or "/ban" in mesaj:
        await event.reply(f"{random.choice(ban)}")
    if "😁" in mesaj or "😬" in mesaj or "😄" in mesaj or "🥶" in mesaj or "😌" in mesaj:
        await event.reply(f"{random.choice(emoji1)}")
    if "🤣" in mesaj or "😅" in mesaj in mesaj or "😂" in mesaj or "😄" in mesaj:
        await event.reply(f"{random.choice(emoji2)}")
    if "Niye" in mesaj or "niye" in mesaj or "Niyə" in mesaj or "niyə" in mesaj:
        await event.reply(f"{random.choice(niye)}")
    if "Nə" in mesaj or "nə" in mesaj or "Ne" in mesaj or "ne" in mesaj or "what" in mesaj in mesaj or "What" in mesaj:
        await event.reply(f"{random.choice(ne)}")
    if "Hay" in mesaj or "hay" in mesaj in mesaj or "haay" in mesaj:
        await event.reply(f"{random.choice(hay)}")
    if "Mal" in mesaj or "mal" in mesaj in mesaj or "Qoyun" in mesaj or "qoyun" in mesaj:
        await event.reply(f"{random.choice(mal)}")
    if "Can" in mesaj or "can" in mesaj or "Haycan" in mesaj or "haycan" in mesaj or "uss" in mesaj:
        await event.reply(f"{random.choice(can)}")
    if "Balam" in mesaj or "balam" in mesaj:
        await event.reply(f"{random.choice(balam)}")
    if "xos" in mesaj or "Xos" in mesaj in mesaj or "Xoş" in mesaj or "xoş" in mesaj:
        await event.reply(f"{random.choice(xos)}")
    if "Hara" in mesaj or "hara" in mesaj or "haraya" in mesaj or "Haraya" in mesaj or "haraki" in mesaj:
        await event.reply(f"{random.choice(hara)}")
    if "Gəl" in mesaj or "gəl" in mesaj or "Gel" in mesaj or "gel" in mesaj:
        await event.reply(f"{random.choice(gel)}")
    if "Gördüm" in mesaj or "gördüm" in mesaj or "Gordum" in mesaj or "gordum" in mesaj:
        await event.reply(f"{random.choice(gordum)}")
    if "info" in mesaj or "Info" in mesaj:
        await event.reply(f"{random.choice(info)}")
    if "tema" in mesaj or "Tema" in mesaj:
        await event.reply(f"{random.choice(team)}")   
    if "pp" in mesaj or "PP" in mesaj:
        await event.reply(f"{random.choice(pp)}")
	       

print(">> Bot işləyir narahat olmayın.\n\nImza: RaviBey<<")
ravibey.run_until_disconnected()
