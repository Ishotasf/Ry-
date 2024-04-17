# Ported By @disinikazu & @Riizzvbss
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# ReCode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de


import time
from datetime import datetime

from speedtest import Speedtest

from . import (
     StartTime,
     kazu_cmd,
     DEVLIST,
     eor,
     humanbytes,
     devs_cmd,
     )
from time import sleep


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@kazu_cmd(pattern=r"^pink$", incoming=True, from_users=DEVLIST)
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Cpink$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ping = await eor(ping, "**HAI 👋🏻**")
    await ping.edit("**I AM RYN**")
    await ping.edit("**IYAA GUA RYN⚡**")
    await ping.edit("**RYN USERBOT⚡**")
    await ping.edit("**⚡YOSHIEKI RYN⚡**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await ping.edit("⚡")
    sleep(3)
    await ping.edit(
        f"**Ryn UBot**\n\n"
        f"**Ping!! :** `%sms`\n"
        f"**UpTime :** `{uptime}` \n"
        f"**Owner :** {user.first_name} (tg://user?id={user.id})" % (duration)
    )


@kazu_cmd(pattern="ping$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xping = await eor(ping, "**Pinging....**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xping.edit(
        f"**𝗦𝗘𝗣𝗢𝗡𝗚!! 🍭**\n**𝗣𝗜𝗡𝗚** : %sms\n**𝗕𝗢𝗧 𝗨𝗣𝗧𝗜𝗠𝗘** : {uptime}🕛" % (duration)
    )


@kazu_cmd(pattern="lping$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Lping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    lping = await eor(ping, "**𝗛𝗔𝗜 👋**")
    await lping.edit("**𝗜'𝗠 𝗥𝗬𝗡𝗨𝗕𝗢𝗧**")
    await lping.edit("**𝗦𝗘𝗟𝗔𝗠𝗔𝗧 𝗗𝗔𝗧𝗔𝗡𝗚...**")
    await lping.edit("**𝗧𝗨𝗡𝗚𝗚𝗨 𝗦𝗘𝗕𝗘𝗡𝗧𝗔𝗥...**")
    await lping.edit("**𝗠𝗘𝗠𝗨𝗟𝗔𝗜....**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await lping.edit(
        f"**Ping !!** "
        f"`%sms` \n"
        f"**Uptime -** "
        f"`{uptime}` \n"
        f"**Master :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@kazu_cmd(pattern="Rping$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Kping$")
async def _(pong):
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kopong = await eor(pong, "**P**")
    await kopong.edit("**WOI**")
    await kopong.edit("**⚡**")
    await kopong.edit("**🫰**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await kopong.edit(
        f"**NIH**"
        f"\nRyn UBot `%sms` \n"
        f"**Yoo!!**"
        f"\nSalken! Saya {user.first_name} (tg://user?id={user.id})』 \n" % (duration)
    )


# .keping & kping Coded by Koala


@kazu_cmd(pattern=r"Ryn$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Kaz$")
async def _(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kping = await eor(pong, "Mengecek Sinyal...")
    await kping.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await kping.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await kping.edit("**40% ████▒▒▒▒▒▒**")   
    await kping.edit("**60% ██████▒▒▒▒**")
    await kping.edit("**80% ████████▒▒**")
    await kping.edit("**80% ████████▒▒**")
    await kping.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await kping.edit("RYN UBOT DIMULAI...")
    sleep(3)
    await kping.edit(
        f"**Saya Active Tuan Yoshieki Ryn ^⁠_⁠^ !!**\n**Ping!!** : %sms\n**Uptime** : {uptime}🕛" % (duration)
    )


@kazu_cmd(pattern="speedtest$")
async def _(speed):
    xxnx = await eor(speed, "**Running speed test...**")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@kazu_cmd(pattern="pong$")
async def _(pong):
    start = datetime.now()
    xx = await eor(pong, "**Assalamualaikum Tuan**")
    await xx.edit("**Waalaikumsalam.....**")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("Tunggu...")
    sleep(3)
    await xx.edit("**𝙿𝙸𝙽𝙶!**\n`%sms`" % (duration))
    )


@kazu_cmd(pattern=r"ryping$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Kaz$")
async def _(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ryping = await eor(pong, "Hai, I'm RynUbot.")
    await ryping.edit("**░░░░░░░░░░░░░░░░░░░░ 0℅**")
    await ryping.edit("**██░░░░░░░░░░░░░░░░░░ 10℅**")
    await ryping.edit("**███░░░░░░░░░░░░░░░░░ 30℅**")
    await ryping.edit("**████░░░░░░░░░░░░░░░░ 40℅**")
    await ryping.edit("**█████░░░░░░░░░░░░░░░ 45℅**")
    await ryping.edit("**██████░░░░░░░░░░░░░░ 50℅**")
    await ryping.edit("**███████░░░░░░░░░░░░░ 58℅**")
    await ryping.edit("**████████░░░░░░░░░░░░ 65℅**")
    await ryping.edit("**█████████░░░░░░░░░░░ 70℅**")
    await ryping.edit("**█████████████░░░░░░░ 75℅**")
    await ryping.edit("**████████████████░░░░ 83℅**")
    await ryping.edit("**██████████████████░░ 95℅**")
    await ryping.edit("**████████████████████ 100℅**")

    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await ryping.edit(
        f"❏ **RynUbot**\n"
        f"├• **RynPong** - `%sms`\n"
        f"├• **RynUptime -** `{uptime}` \n"
        f"└• **RynUbot :** {client.me.mention}" % (duration)
