import asyncio
import datetime
import random
import re

from telethon.tl.types import Message

from .. import loader


@loader.tds
class ZhabaMod(loader.Module):
    """Модуль для @toadbot"""

    strings = {"name": "Zhaba"}

    async def client_ready(self, client, db):
        """ready"""
        self.client = client
        self.db = db
        self.su = db.get("Su", "su", {})
        self.me = await client.get_me()
        if "name" not in self.su:
            self.su.setdefault("name", self.me.first_name)
            self.su.setdefault("users", [self.me.id, 1124824021])
            self.db.set("Su", "su", self.su)
        self.ded = {
            "жабу с работы": "@toadbot Завершить работу",
            "Можно откормить": "@toadbot Откормить жабу",
            "можно покормить": "@toadbot Покормить жабу",
            "Можно отправиться": "отправиться в золотое подземелье",
            "жаба в данже": "рейд старт",
            "Можно на арену!": "@toadbot На арену",
            "Используйте атаку": "@toadbot На арену",
            "можно отправить": "работа крупье",
            "золото": "отправиться в золотое подземелье",
            "кв": "начать клановую войну",
            "напади": "напасть на клан",
            "арена": "на арену",
            "реанимируй": "реанимировать жабу",
            "карту": "отправить карту",
            "снаряга": "мое снаряжение",
            "инвентарь": "мой инвентарь",
            "туса": "жабу на тусу",
            "туси": "начать тусу",
            "рейд": "рейд старт",
            "работа": "завершить работу",
            "минималист": "выбрать усилитель минималист",
            "предел": "выбрать усилитель на пределе",
            "леденец": "отдать леденец",
            "кулон": "скрафтить кулон братвы",
            "лидерку": "передать клан",
            "буках": "букашки",
            "аптек": "аптечки",
            "ледик": "леденцы",
            "Ближний бой: Пусто": "скрафтить клюв цапли",
            "Дальний бой: Пусто": "скрафтить букашкомет",
            "Наголовник: Пусто": "скрафтить наголовник из клюва цапли",
            "Нагрудник: Пусто": "скрафтить нагрудник из клюва цапли",
            "Налапники: Пусто": "скрафтить налапники из клюва цапли",
            "Банда: Пусто": "взять жабу",
            "Покормить жабенка": "@toadbot Покормить жабенка",
            "Брак вознаграждение": "@toadbot Брак вознаграждение",
            "Забрать жабенка": "@toadbot Забрать жабенка",
            "В детский сад!": "@toadbot Отправить жабенка в детсад",
            "Отправить жабенка на махач": "@toadbot Отправить жабенка на махач",
        }

    async def err(self, chat, cmn):
        """работа с ответом жабабота"""
        try:
            async with self.client.conversation(chat, exclusive=False) as conv:
                await conv.send_message(cmn)
                global RSP
                RSP = await conv.get_response()
                await conv.cancel_all()
        except Exception:
            pass

    async def npn(self, chat, msg):
        cmn = self.ded[msg]
        await self.err(chat, cmn)
        if not RSP:
            return
        if "Вы не участвуете" in RSP.text or "Ваша жаба на тусе" in RSP.text:
            return
        await asyncio.sleep(random.randint(3, 33))
        if "Ваша жаба в предсмертном" in RSP.text or "Для участия" in RSP.text:
            await RSP.respond("реанимировать жабу")
        elif "Ваша жаба на" in RSP.text:
            await RSP.respond("завершить работу")
        await asyncio.sleep(random.randint(3, 33))
        await self.client.send_message(chat, cmn)

    async def scmd(self, m):
        """статус юзербота"""
        if len(m.text) < 3:
            txt = "<b>Status:"
            if "auto" in self.su:
                txt += " <b>🐸</b>"
            elif "chats" in self.su:
                txt += f" <b>🐸 in {self.su['chats']}</b>"
            else:
                txt += " <b>⛔️</b>"
            txt += f"\n\n  🤰🏿Откормить:"
            if "gs" in self.su:
                txt += " <b>🐸</b>"
            elif "gss" in self.su:
                txt += f" <b>🐸 in {self.su['gss']}</b>"
            else:
                txt += " <b>⛔️</b>"
            txt += "\n  💂🏿‍♂️Снаряжение:"
            if "as" in self.su:
                txt += " <b>🐸</b>"
            elif "ass" in self.su:
                txt += f" <b>🐸 in {self.su['ass']}</b>"
            else:
                txt += " <b>⛔️</b>"
            txt += f"\n  🎎 Семья:"
            if "hs" in self.su:
                txt += " <b>🐸</b>"
            elif "hss" in self.su:
                txt += f" <b>in {self.su['hss']}</b>"
            else:
                txt += " <b>⛔️</b>"
            txt += f"\n  🔦Подземелье:"
            if "fs" in self.su:
                txt += " <b>🐸</b>"
            elif "fss" in self.su:
                txt += f" <b>🐸 in {self.su['fss']}</b>"
            else:
                txt += " <b>⛔️</b>"
            txt += "\n  🥊Арена:"
            if "buto" in self.su:
                txt += " <b>🐸</b>"
            elif "butos" in self.su:
                txt += f" <b>🐸 in {self.su['butos']}</b>"
            else:
                txt += " <b>⛔️</b>"
            txt += f"\n\nРабота\n\n  🃏Крупье:"
            if "cs" in self.su:
                txt += " <b>🐸</b>"
            elif "css" in self.su:
                txt += f" <b>in {self.su['css']}</b>"
            else:
                txt += " <b>⛔️</b>"
            txt += "\n  👩🏾‍🍳Столовая:"
            if "ss" in self.su:
                txt += " <b>🐸</b>"
            elif "sss" in self.su:
                txt += f" <b>in {self.su['sss']}</b>"
            else:
                txt += " <b>⛔️</b>"
            txt += "\n  💣Грабитель: "
            if "es" in self.su:
                txt += " <b>🐸</b>"
            elif "ess" in self.su:
                txt += f" <b>in {self.su['ess']}</b>"
            else:
                txt += " <b>⛔️</b>"
            txt += "\n\nХод в походе: 🐸"
            txt += "\nДоступ: 🐸 (<code>.s su</code>) — список юзеров"
            txt += f"\nНик для команд: <b>{self.su['name']}</b>"
            txt += "\n\n🛂Гайд: <b>@jabuser</b>"
            return await m.edit(txt)
        if m.text.split(" ", 2)[1] == "su":
            reply = await m.get_reply_message()
            if len(m.text) < 13 and not reply:
                txt = "Могут управлять ботом:"
                for i in self.su["users"]:
                    txt += f"\n<a href='tg://user?id={i}'>{i}</a>"
                txt += "\n\n(<code>.s su</code> ID или реплай)"
                return await m.edit(txt)
            msg = reply.sender_id if reply else int(m.text.split(" ", 2)[2])
            if msg in self.su["users"]:
                self.su["users"].remove(msg)
                txt = f"🖕🏾 {msg} <b>успешно удален</b>"
            else:
                self.su["users"].append(msg)
                txt = f"🤙🏾 {msg} <b>успешно добавлен</b>"
            self.db.set("Su", "su", self.su)
            return await m.edit(txt)
        if m.text.split(" ", 2)[1] == "nn":
            if len(m.text) < 4:
                await m.edit(
                    "🐖пиши <code>.s nn Ник</code>\n (ник должен содержать больше 2 букв)"
                )
            msg = m.text.split(" ", 2)[2]
            self.su["name"] = msg.casefold()
            txt = f"👻 <code>{self.su['name']}</code> успешно изменён"
            self.db.set("Su", "su", self.su)
            return await m.edit(txt)
        if m.text.split(" ", 2)[1] == "ub":
            txt = "<b>👑Userbot:</b>"
            i = "auto"
            n = "chats"
        elif m.text.split(" ", 2)[1] == "ar":
            txt = "<b>🥊Арена:</b>"
            i = "buto"
            n = "butos"
        elif m.text.split(" ", 2)[1] == "jk":
            txt = "<b>🃏Крупье:</b>"
            i = "cs"
            n = "css"
        elif m.text.split(" ", 2)[1] == "js":
            txt = "<b>👩🏾‍🍳Столовая:</b>"
            i = "ss"
            n = "sss"
        elif m.text.split(" ", 2)[1] == "jg":
            txt = "<b>💣Грабитель:</b>"
            i = "es"
            n = "ess"
        elif m.text.split(" ", 2)[1] == "pz":
            txt = "<b>🔦Подземелье:</b>"
            i = "fs"
            n = "fss"
        elif m.text.split(" ", 2)[1] == "ok":
            txt = "<b>🤰🏿Откормить:</b>"
            i = "gs"
            n = "gss"
        elif m.text.split(" ", 2)[1] == "fm":
            txt = "<b>🎎 Семья:</b>"
            i = "hs"
            n = "hss"
        elif m.text.split(" ", 2)[1] == "sn":
            txt = "<b>💂🏿‍♂️Снаряжение:</b>"
            i = "as"
            n = "ass"
        else:
            return
        if "+" in m.text:
            self.su.setdefault(i, {})
            if n in self.su:
                self.su.pop(n)
            txt += "<b> для всех жаб</b>"
            return await m.edit(txt)
        msg = m.chat_id if len(m.text) < 9 else int(m.text.split(" ", 2)[2])
        if "-" not in str(msg):
            return await m.edit(
                "ид чата начинается с '-', напиши <code>узнать ид</code>"
            )
        if i in self.su:
            self.su.pop(i)
            txt += "<b> деактивирован</b>"
        elif n in self.su and msg in self.su[n]:
            self.su[n].remove(msg)
            txt += f"<b> удален чат</b> {msg}"
            if self.su[n] == []:
                self.su.pop(n)
                txt += "\n\n<b>деактивирован</b>"
            return await m.edit(txt)
        elif n in self.su and msg not in self.su[n]:
            txt += f"<b> добавлен чат</b> {msg}"
            self.su[n].append(msg)
        else:
            self.su.setdefault(n, [msg])
            txt += f"<b> в чате</b> {msg}"
        self.db.set("Su", "su", self.su)
        await m.edit(txt)

    async def watcher(self, m):
        """алко"""
        ct = datetime.datetime.now()
        n = (
            (self.me.id % 100) + 7
            if (self.me.id % 100) < 33
            else int(self.me.id % 100 / 3)
        )
        try:
            if (
                isinstance(m, Message)
                and m.sender_id in self.su["users"]
                and " " in m.text
                and (
                    m.text.casefold().startswith(self.su["name"])
                    or m.text.startswith(f"@{self.me.username}")
                    or str(self.me.id) in m.text
                )
            ):
                chat = m.peer_id
                reply = await m.get_reply_message()
                if "нуждается в реанимации" in m.text and m.buttons:
                    await asyncio.sleep(random.randint(3, n))
                    await m.respond("реанимировать жабу")
                    await asyncio.sleep(random.randint(3, n))
                    await m.click()
                elif "ход: " in m.text and m.buttons:
                    await asyncio.sleep(random.randint(3, n))
                    await m.click()
                elif "сломалось" in m.text and (
                    "as" in self.su or ("ass" in self.su and chat in self.su["ass"])
                ):
                    await asyncio.sleep(random.randint(3, n))
                    cmn = "мое снаряжение"
                    await self.err(chat, cmn)
                    if not RSP and "🗡" not in RSP.text:
                        return
                    for i in (i for i in self.ded if i in RSP.text):
                        await asyncio.sleep(random.randint(3, n))
                        await m.respond(self.ded[p])
                elif "Банда получила" in m.text:
                    await asyncio.sleep(random.randint(3, n))
                    await m.respond("отдать леденец")
                    await asyncio.sleep(random.randint(3, n))
                    cmn = "моя банда"
                    await self.err(chat, cmn)
                    if not RSP and "📿" not in RSP.text:
                        return
                    if "Кулон: Пусто" in RSP.text:
                        await asyncio.sleep(random.randint(3, n))
                        await m.respond("скрафтить кулон братвы")
                elif "тыкпых" in m.text:
                    if reply:
                        return await reply.click()
                    if "тыкпых " not in m.text:
                        return
                    reg = re.search(r"/(\d+)/(\d+)", m.text)
                    if not reg:
                        return
                    msg = await self.client.get_messages(
                        int(reg.group(1)), ids=int(reg.group(2))
                    )
                    await msg.click()
                elif "буках" in m.text and self.su["name"] in ("кушки", "альберт"):
                    await asyncio.sleep(
                        random.randint(n + ct.minute, 111 + (ct.microsecond % 100))
                    )
                    cmn = "мой баланс"
                    await self.err(chat, cmn)
                    if not RSP:
                        return
                    if "У тебя" in RSP.text:
                        await m.respond("взять жабу")
                    elif "Баланс" not in RSP.text:
                        return
                    jab = int(re.search(r"жабы: (\d+)", RSP.text).group(1))
                    if jab < 50:
                        return
                    await m.reply(f"отправить букашки {jab}")
                elif "del" in m.text:
                    chat = 1124824021
                    cmn = "мои жабы"
                    await self.err(chat, cmn)
                    if not RSP:
                        return
                    await self.client.delete_dialog(chat, revoke=True)
                    for i in re.findall(r"(-\d+)", RSP.text):
                        chat = int(i)
                        async for msg in self.client.iter_messages(
                            chat, from_user="me"
                        ):
                            await msg.delete()
                elif "напиши в " in m.text:
                    chat = m.text.split(" ", 4)[3]
                    if chat.isnumeric():
                        chat = int(chat)
                    if reply:
                        msg = reply
                    else:
                        msg = m.text.split(" ", 4)[4]
                    await self.client.send_message(chat, msg)
                elif "напиши " in m.text:
                    txt = m.text.split(" ", 2)[2]
                    if reply:
                        return await reply.reply(txt)
                    await m.respond(txt)
                else:
                    cmn = m.text.split(" ", 2)[1]
                    if reply and cmn in ("ледик", "аптек", "буках"):
                        return await reply.reply(
                            f"отправить {self.ded[cmn]} {m.text.split(' ', 2)[2]}"
                        )
                    msg = m.text.split(" ", 2)[1]
                    if msg not in self.ded:
                        return
                    if msg in ("напади", "арена"):
                        return await self.npn(chat, msg)
                    if msg in ("карту", "лидерку"):
                        return await m.reply(self.ded[msg])
                    await asyncio.sleep(random.randint(3, n))
                    await m.respond(self.ded[msg])
            if (
                "auto" not in self.su
                and "chats" not in self.su
                or (ct.minute not in (n + 3, n + 21))
            ):
                return
            await asyncio.sleep(
                random.randint(ct.hour * 3, 99 + (ct.microsecond % 100))
            )
            if "minute" in self.su and (-1 < (ct.minute - self.su["minute"]) < 1):
                return
            if "minute" in self.su:
                self.su["minute"] = ct.minute
            else:
                self.su.setdefault("minute", ct.minute)
            self.db.set("Su", "su", self.su)
            chat = 1124824021
            cmn = "мои жабы"
            await self.err(chat, cmn)
            if not RSP:
                return
            await self.client.delete_dialog(chat, revoke=True)
            for i in re.findall(r"(\d+) \| (-\d+)", RSP.text):
                chat = int(i[1])
                if "chats" in self.su and chat not in self.su["chats"]:
                    continue
                if "cs" in self.su or ("css" in self.su and chat in self.su["css"]):
                    job = "работа крупье"
                elif "ss" in self.su or ("sss" in self.su and chat in self.su["css"]):
                    job = "поход в столовую"
                elif "es" in self.su or ("ess" in self.su and chat in self.su["css"]):
                    job = "работа грабитель"
                else:
                    job = None
                try:
                    cmn = "Моя жаба"
                    await self.err(chat, cmn)
                except Exception:
                    continue
                if not RSP and "Имя жабы" not in RSP.text:
                    continue
                s = "alive"
                if "Нужна реанимация" in RSP.text:
                    s = "dead"
                if "Хорошее" in RSP.text:
                    await asyncio.sleep(
                        random.randint(n + ct.minute, 111 + (ct.microsecond % 100))
                    )
                    await RSP.respond(f"использовать леденцы {random.randint(1, 3)}")
                jab = re.search(r"Б.+: (\d+)", RSP.text)
                if not jab:
                    continue
                await asyncio.sleep(random.randint(3, n))
                cmn = "@toadbot Жаба инфо"
                await self.err(chat, cmn)
                if not RSP and "🏃‍♂️" not in RSP.text:
                    continue
                for p in (p for p in self.ded if p in RSP.text):
                    if (
                        (
                            p == "Можно откормить"
                            and "gs" not in self.su
                            or ("gss" in self.su and chat not in self.su["gss"])
                        )
                        or (
                            p == "можно отправить"
                            and (
                                job == None
                                or (
                                    "подземелье можно через 2" not in RSP.text
                                    and (int(i[0]) > 77 and int(jab.group(1)) > 1500)
                                )
                            )
                        )
                        or (
                            p == "Можно на арену!"
                            and (
                                "buto" not in self.su
                                or ("butos" in self.su and chat not in self.su["butos"])
                            )
                        )
                        or (
                            p == "Можно отправиться"
                            and (
                                "fs" not in self.su
                                or ("fss" in self.su and chat not in self.su["fss"])
                            )
                        )
                        or (
                            p in ("Можно откормить", "Можно отправиться")
                            and (int(jab.group(1)) < 1500)
                        )
                    ):
                        continue
                    if (
                        s == "dead"
                        and job != "поход в столовую"
                        and job == None
                        and p not in ("Можно откормить", "можно покормить")
                    ):
                        await asyncio.sleep(random.randint(3, n))
                        await RSP.respond("реанимировать жабу")
                    if p == "можно отправить":
                        return await RSP.respond(job)
                    await asyncio.sleep(random.randint(3, n))
                    await RSP.respond(self.ded[p])
                if "не в браке" in RSP.text or (
                    "hs" not in self.su
                    and ("hss" in self.su and chat not in self.su["hss"])
                ):
                    continue
                await asyncio.sleep(random.randint(3, n))
                cmn = "Моя семья"
                await self.err(chat, cmn)
                if not RSP:
                    continue
                if "У вас нет" in RSP.text:
                    continue
                if not RSP.buttons:
                    continue
                s = len(RSP.buttons)
                await asyncio.sleep(random.randint(3, n))
                await RSP.respond(self.ded[RSP.buttons[0][0].text])
                if s == 1:
                    continue
                await asyncio.sleep(random.randint(3, n))
                await RSP.respond(self.ded[RSP.buttons[1][0].text])
                if s == 2:
                    continue
                await asyncio.sleep(random.randint(3, n))
                await RSP.respond(self.ded[RSP.buttons[2][0].text])
        except Exception:
            return
