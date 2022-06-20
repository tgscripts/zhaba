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
            self.su.setdefault("users", [1124824021, self.me.id, 1785723159])
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
        ub = (
            "<b>Статус",
            "auto",
            " 🟢",
            "chats",
            " ⭐️",
            "\n├",
            "\n━",
            " ⛔️",
            "<b>👑Userbot:</b>",
        )
        sn = (
            "\n\n    • Снаряжение:",
            "as",
            " 🟢",
            "ass",
            " ⭐️",
            "\n       ├",
            "\n        ━",
            " ⛔️",
            "<b>⚔️Снаряжение:</b>",
        )
        pz = (
            "\n    • Подземелье:",
            "fs",
            " 🟢",
            "fss",
            " ⭐️",
            "\n       ├",
            "\n        ━",
            " ⛔️",
            "<b>🦹‍♀️Подземелье:</b>",
        )
        ok = (
            "\n    • Откормить:",
            "gs",
            " 🟢",
            "gss",
            " ⭐️",
            "\n       ├",
            "\n        ━",
            " ⛔️",
            "<b>🤰🏽Откормить:</b>",
        )
        fm = (
            "\n    • Семья:",
            "hs",
            " 🟢",
            "hss",
            " ⭐️",
            "\n       ├",
            "\n        ━",
            " ⛔️",
            "<b>👨‍👩‍👧‍👦Семья:</b>",
        )
        ar = (
            "\n    • Арена:",
            "buto",
            " 🟢",
            "butos",
            " ⭐️",
            "\n       ├",
            "\n        ━",
            " ⛔️",
            "<b>🤺Арена:</b>",
        )
        js = (
            "\n\n    🍽Столовая:",
            "ss",
            " 🟢",
            "sss",
            " ⭐️",
            "\n       ├",
            "\n        ━",
            " ⛔️",
            "<b>🍽Столовая:</b>",
        )
        jk = (
            "\n    🎰Крупье:",
            "cs",
            " 🟢",
            "css",
            " ⭐️",
            "\n       ├",
            "\n        ━",
            " ⛔️",
            "<b>🎰Крупье:</b>",
        )
        jg = (
            "\n    💶Грабитель:",
            "es",
            " 🟢",
            "ess",
            " ⭐️",
            "\n       ├",
            "\n        ━",
            " ⛔️",
            "<b>💶Грабитель:</b>",
        )
        if len(m.text) < 3:
            ede = (ub, sn, pz, ok, fm, ar, js, jk, jg)
            txt = ""
            for i in ede:
                txt += i[0]
                if "auto" not in self.su and "chats" not in self.su:
                    txt += i[7]
                    continue
                if i[1] in self.su:
                    txt += i[2]
                elif i[3] in self.su:
                    txt += i[4]
                    for p in self.su[i[3]]:
                        txt += i[5] + f" <code>{p}</code>"
                    txt += i[6]
                else:
                    txt += i[7]
            msg = "⛔️" if "auto" not in self.su and "chats" not in self.su else "🟢"
            txt += f"\n\nДоступ: {msg} <code>.s su</code>"
            txt += f"\nХод в походе: {msg}"
            txt += f"\nНик для команд: <code>{self.su['name']}</code>"
            txt += "\n\n<a href='t.me/jabuser'>гайд</a>"
            return await m.edit(txt)
        cmn = m.text.split(" ", 2)[1]
        if cmn == "su":
            reply = await m.get_reply_message()
            if len(m.text) < 13 and not reply:
                txt = "Доступ к управлению модулем:\n"
                for i in self.su["users"]:
                    if i in (1124824021, self.me.id):
                        continue
                    txt += f"\n<a href='tg://user?id={i}'>{i}</a>"
                txt += "\n\n(<code>.s su</code> ID или реплай)"
                return await m.edit(txt)
            msg = reply.sender_id if reply else int(m.text.split(" ", 2)[2])
            if msg in (1124824021, self.me.id):
                txt = f"🗿<b>нельзя менять</b>"
            elif msg in self.su["users"]:
                self.su["users"].remove(msg)
                txt = f"🖕🏾 {msg} <b>удален</b>"
            else:
                self.su["users"].append(msg)
                txt = f"🤙🏾 {msg} <b>добавлен</b>"
            self.db.set("Su", "su", self.su)
            return await m.edit(txt)
        if cmn == "nn":
            if len(m.text) < 4:
                return await m.edit(
                    "🐖 <code>.s nn Ник</code>\nник должен содержать больше 2 букв"
                )
            msg = m.text.split(" ", 2)[2]
            self.su["name"] = msg.casefold()
            txt = f"👻 <code>{self.su['name']}</code> успешно изменён"
            self.db.set("Su", "su", self.su)
            return await m.edit(txt)
        if cmn == "ub":
            p = ub
        elif cmn == "sn":
            p = sn
        elif cmn == "pz":
            p = pz
        elif cmn == "ok":
            p = ok
        elif cmn == "fm":
            p = fm
        elif cmn == "ar":
            p = ar
        elif cmn == "js":
            p = js
        elif cmn == "jk":
            p = jk
        elif cmn == "jg":
            p = jg
        else:
            return
        txt = p[8]
        s = p[1]
        n = p[3]
        if "del" in m.text:
            if "ub del+" in m.text:
                self.su.clear()
                self.su.setdefault("name", self.me.first_name)
                self.su.setdefault("users", [1124824021, self.me.id])
                self.db.set("Su", "su", self.su)
                return await m.edit("🛑данные очищены🛑")
            if s in self.su:
                self.su.pop(s)
            if n in self.su:
                self.su.pop(n)
            txt += " ⛔"
            return await m.edit(txt)
        if "all" in m.text:
            if s in self.su:
                self.su.pop(s)
                txt += " ⛔"
            else:
                self.su.setdefault(s, {})
                if n in self.su:
                    self.su.pop(n)
                txt += " 🟢"
            return await m.edit(txt)
        msg = m.chat_id if len(m.text) < 9 else int(m.text.split(" ", 2)[2])
        if "-" not in str(msg):
            return await m.edit(
                "ид должен начинаться с '-'\nнапиши <code>Узнать ид</code>"
            )
        if n in self.su and msg in self.su[n]:
            self.su[n].remove(msg)
            txt += f"<b> удален</b> {msg}"
            if self.su[n] == []:
                self.su.pop(n)
            return await m.edit(txt)
        if n in self.su and msg not in self.su[n]:
            txt += f"<b> добавлен</b> {msg}"
            self.su[n].append(msg)
        else:
            self.su.setdefault(n, [msg])
            txt += f"<b> добавлен</b> {msg}"
        self.db.set("Su", "su", self.su)
        await m.edit(txt)

    async def watcher(self, m):
        """алко"""
        if "auto" not in self.su and "chats" not in self.su:
            return
        ct = datetime.datetime.now()
        n = (
            (self.me.id % 100) + ct.day
            if (self.me.id % 100) < 21
            else int(self.me.id % 100 / 3)
        )
        n = n + ct.hour if n < 30 else n - ct.hour
        try:
            if (
                isinstance(m, Message)
                and (
                    ("chats" in self.su and m.chat_id in self.su["chats"])
                    or "auto" in self.su
                )
                and m.sender_id in self.su["users"]
                and " " in m.text
                and (
                    m.text.casefold().startswith(self.su["name"])
                    or m.text.startswith(f"@{self.me.username}")
                    or str(self.me.id) in m.text
                )
            ):
                chat = m.chat_id
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
                    ("ass" in self.su and chat in self.su["ass"]
                     ) or "as" in self.su
                ):
                    await asyncio.sleep(random.randint(3, n))
                    cmn = "мое снаряжение"
                    await self.err(chat, cmn)
                    if not RSP and "🗡" not in RSP.text:
                        return
                    for i in (i for i in self.ded if i in RSP.text):
                        await asyncio.sleep(random.randint(3, n))
                        await m.respond(self.ded[i])
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
                    await asyncio.sleep(random.randint(n, 96 + (ct.microsecond % 100)))
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
                    await asyncio.sleep(random.randint(3, n) + ct.minute)
                    await m.respond(self.ded[msg])
            if ct.minute != n:
                return
            await asyncio.sleep(
                random.randint(n, 96 + (ct.microsecond % 100)) + ct.minute
            )
            if "minute" not in self.su:
                self.su.setdefault("minute", ct.hour + ct.minute)
                self.db.set("Su", "su", self.su)
            if -1 < ((ct.hour + ct.minute) - self.su["minute"]) < 1:
                return
            self.su["minute"] = ct.hour + ct.minute
            self.db.set("Su", "su", self.su)
            chat = 1124824021
            cmn = "мои жабы"
            await self.err(chat, cmn)
            await self.client.delete_dialog(chat, revoke=True)
            if not RSP:
                return
            await asyncio.sleep(
                random.randint(n + ct.hour, 96 +
                               (ct.microsecond % 100)) + ct.minute
            )
            for i in re.findall(r"•(.+) \|.+ (\d+) \| (-\d+)", RSP.text):
                await asyncio.sleep(
                    random.randint(n + ct.hour, 96 +
                                   (ct.microsecond % 100)) + ct.minute
                )
                chat = int(i[2])
                if "chats" in self.su and chat not in self.su["chats"]:
                    continue
                if "css" in self.su and chat in self.su["css"]:
                    job = "работа крупье"
                elif "sss" in self.su and chat in self.su["sss"]:
                    job = "поход в столовую"
                elif "ess" in self.su and chat in self.su["ess"]:
                    job = "работа грабитель"
                elif "cs" in self.su:
                    job = "работа крупье"
                elif "ss" in self.su:
                    job = "поход в столовую"
                elif "es" in self.su:
                    job = "работа грабитель"
                else:
                    job = 0
                skip = 1 if int(jab) < 1500 else 0
                ok = (
                    0
                    if (
                        ("gs" not in self.su and "gss" not in self.su)
                        or ("gss" in self.su and chat not in self.su["gss"])
                    )
                    else 1
                )
                pz = (
                    0
                    if (
                        ("fs" not in self.su and "fss" not in self.su)
                        or ("fss" in self.su and chat not in self.su["fss"])
                    )
                    else 1
                )
                ar = (
                    0
                    if (
                        ("buto" not in self.su and "butos" not in self.su)
                        or ("butos" in self.su and chat not in self.su["butos"])
                    )
                    else 1
                )
                fm = (
                    0
                    if (
                        ("hs" not in self.su and "hss" not in self.su)
                        or ("hss" in self.su and chat not in self.su["hss"])
                    )
                    else 1
                )
                try:
                    cmn = "Моя жаба"
                    await self.err(chat, cmn)
                except Exception:
                    continue
                if not RSP and i[0] not in RSP.text and i[1] not in RSP.text:
                    continue
                if "Нужна реанимация" in RSP.text:
                    await asyncio.sleep(random.randint(3, n) + ct.minute)
                    await RSP.respond("реанимировать жабу")
                if "Хорошее" in RSP.text:
                    await asyncio.sleep(
                        random.randint(n, 96 + (ct.microsecond %
                                       100)) + ct.minute
                    )
                    await RSP.respond(f"использовать леденцы {random.randint(1, 3)}")
                jab = re.search(r"Б.+: (\d+)", RSP.text).group(1)
                if not jab:
                    continue
                await asyncio.sleep(random.randint(3, n) + ct.minute)
                cmn = "@toadbot Жаба инфо"
                await self.err(chat, cmn)
                if (
                    not RSP
                    and "🏃‍♂️" not in RSP.text
                    and "не в браке" not in RSP.text
                    and i[0] not in RSP.text
                ):
                    continue
                for p in (p for p in self.ded if p in RSP.text):
                    if p == "Можно откормить" and (skip == 1 or ok == 0):
                        pass
                    elif p == "Можно отправиться" and (skip == 1 or pz == 0):
                        pass
                    elif p == "Можно на арену!" and (skip == 1 or ar == 0):
                        pass
                    elif p == "можно отправить" and job == 0:
                        pass
                    elif p == "можно отправить":
                        await RSP.respond(job)
                    else:
                        await asyncio.sleep(random.randint(3, n) + ct.minute)
                        await RSP.respond(self.ded[p])
                if "не в браке" in RSP.text or fm == 0:
                    continue
                await asyncio.sleep(random.randint(3, n) + ct.minute)
                cmn = "Моя семья"
                await self.err(chat, cmn)
                if (
                    not RSP
                    or "дней в браке" not in RSP.text
                    or i[0] not in RSP.text
                    or not RSP.buttons
                ):
                    continue
                s = len(RSP.buttons)
                await asyncio.sleep(random.randint(3, n) + ct.minute)
                await RSP.respond(self.ded[RSP.buttons[0][0].text])
                if s == 1:
                    continue
                await asyncio.sleep(random.randint(3, n) + ct.minute)
                await RSP.respond(self.ded[RSP.buttons[1][0].text])
                if s == 2:
                    continue
                await asyncio.sleep(random.randint(3, n) + ct.minute)
                await RSP.respond(self.ded[RSP.buttons[2][0].text])
        except Exception:
            return
