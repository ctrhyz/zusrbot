from telethon import TelegramClient, events, types
import time
import random
import asyncio
import os
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import logging
##################################################################################
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
##################################################################################
prefix = '/'
api_id = 
api_hash = ''
log_ch_id = -
capp = False
save_file_pp = True
last_name = ['운 명 ✨','G E N E R A T E D ⚡','俺 わ 誰 ✨','(≧∇≦)','(✿◡‿◡)','S T O R E ✨']
##################################################################################
client = TelegramClient('zusrbot',api_id, api_hash)
client.parse_mode = 'html'

dir_pp = os.path.join(os.getcwd(), 'pfp')
if not os.path.exists(dir_pp):
    os.makedirs(dir_pp)
##################################################################################
async def clear_terminal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        me = await client.get_me()
        print(f"Started!\nHello {me.first_name} {me.last_name}, you logged in as @{me.username}\n")
        await asyncio.sleep(86400)
##################################################################################
async def change_pp():
    if capp == True:
        while True:
            pics = os.listdir(dir_pp)
            if pics:
                pic = random.choice(pics)
                file = await client.upload_file(os.path.join(dir_pp, pic))
                await client(UploadProfilePhotoRequest(fallback=True,file=file))
            print(f"your photo profile has been updated with {pic}")
            await asyncio.sleep(1800)
    else:
        await asyncio.sleep(0.21)
        print('AutoChange pfp ability has been disabled')
##################################################################################
async def change_lastname():
    while True:
        randomln = random.choice(last_name)
        await client(UpdateProfileRequest(last_name=randomln))
        me = await client.get_me()
        print(f"your name changed to {me.first_name} {me.last_name}")
        await asyncio.sleep(180)
##################################################################################
@client.on(events.NewMessage(outgoing=True, pattern=f'{prefix}savepp'))
async def save_pp(svpp):
    msg = svpp.message.message
    smg = msg.split()
    if len(smg) > 1:
        bjir = int(smg[1]) if smg[1].isdigit() else smg[1]
        get_usr = await client.get_entity(bjir)
        dl = await client.download_profile_photo(get_usr, file=dir_pp)
        await client.send_file(log_ch_id, dl, caption=f"""save pp from {"(Not Found)" if get_usr.username is None else "@"+get_usr.username} with id <a href="tg://user?id={get_usr.id}">{get_usr.id}</a>""")
        await svpp.edit('Hi')

    elif svpp.is_reply:
        replied = await svpp.get_reply_message()
        sender = replied.sender
        dl = await client.download_profile_photo(sender, file=dir_pp)
        await client.send_file(log_ch_id, dl, caption=f"""save pp from {"(Not Found)" if sender.username is None else "@"+sender.username} with id <a href="tg://user?id={sender.id}">{sender.id}</a>""")
        await svpp.edit('Hi')

    elif svpp.is_reply == False:
        hayi = await svpp.get_input_chat()
        hiya = await client.get_entity(hayi)
        if hiya:
            dl = await client.download_profile_photo(hiya, file=dir_pp)
            await client.send_file(log_ch_id, dl, caption=f"""save pp from {"(Not Found)" if hiya.username is None else "@"+hiya.username} with id <a href="tg://user?id={hiya.id}">{hiya.id}</a>""")
            await svpp.edit('Hi')
        
    if save_file_pp == False:
        os.remove(dl)
    print("Savepp Triggered")
##################################################################################
@client.on(events.NewMessage(outgoing=True, pattern=f'{prefix}info'))
async def info(info):
    if info.is_reply:
        replied = await info.get_reply_message()
        sender = replied.sender
        if isinstance (sender, types.Channel):
            await info.edit(f"""Info Channel:
- Title: {sender.title}
- ID: {sender.id}
- Username: {"Not Found" if sender.username is None else "@"+sender.username}
- Date Created: {time.ctime(sender.date.timestamp())}""")
        
        if sender.bot:
            await info.edit(f"""Info Bot:
- Username: {"Not Found" if sender.username is None else "@"+sender.username}
- ID: <a href="tg://user?id={sender.id}">{sender.id}</a>
- First Name: {sender.first_name}
- Last Name: {sender.last_name}""")

        else:
            await info.edit(f"""Info User:
- Username: {"Not Found" if sender.username is None else "@"+sender.username}
- ID: <a href="tg://user?id={sender.id}">{sender.id}</a>
- First Name: {sender.first_name}
- Last Name: {sender.last_name}""")

    elif info.is_reply == False:
        type = await info.get_chat()
        msg = info.message.message
        word = msg.split()
        if len(word) > 1:
            lah = int(word[1]) if word[1].isdigit() else word[1]
            get_usr = await client.get_entity(lah)
            if isinstance (get_usr, types.User):
                await info.edit(f"""Info User:
- Username: {"Not Found" if get_usr.username is None else "@"+get_usr.username}
- ID: <a href="tg://user?id={get_usr.id}">{get_usr.id}</a>
- First Name: {get_usr.first_name}
- Last Name: {get_usr.last_name}""")

                if get_usr.bot:
                    await info.edit(f"""Info Bot:
- Username: {"Not Found" if get_usr.username is None else "@"+get_usr.username}
- ID: <a href="tg://user?id={get_usr.id}">{get_usr.id}</a>
- First Name: {get_usr.first_name}
- Last Name: {get_usr.last_name}""")

            elif get_usr.megagroup:
                await info.edit(f"""Info Group:
- Title: {get_usr.title}
- ID: {get_usr.id}
- Username: {"Not Found" if get_usr.username is None else "@"+get_usr.username}
- Date Created: {time.ctime(get_usr.date.timestamp())}""")

            elif isinstance (get_usr, types.Channel):
                await info.edit(f"""Info Channel:
- Title: {get_usr.title}
- ID: {get_usr.id}
- Username: {"Not Found" if get_usr.username is None else "@"+get_usr.username}
- Date Created: {time.ctime(get_usr.date.timestamp())}""")

        elif info.is_private == False:
            await info.edit(f"""Info Current Chat:
- Title: {type.title}
- ID: {type.id}
- Username: {"Not Found" if type.username is None else "@"+type.username}
- Date Created: {time.ctime(type.date.timestamp())}""")

        elif info.is_private == True:
            await info.edit(f"""Info User:
- Username: {"Not Found" if type.username is None else "@"+type.username}
- ID: <a href="tg://user?id={type.id}">{type.id}</a>
- First Name: {type.first_name}
- Last Name: {type.last_name}""")

    print("Info Triggered")
##################################################################################
client.start()
client.loop.create_task(clear_terminal())
client.loop.create_task(change_lastname())
client.loop.create_task(change_pp())
client.loop.run_forever()
