# -*- coding: utf-8 -*-
import logging
import sqlite3
import random, time, asyncio
from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime
from datetime import timedelta
from aiogram.utils.markdown import quote_html
from time import gmtime
from time import strptime
from decimal import Decimal
from aiogram.utils.callback_data import CallbackData

# from filters import IsAdminFilter

logging.basicConfig(level=logging.INFO)

# bot init
#bot = Bot(token='5123414660:AAHk8PxHEztznIuRMXNNlAN2ZzFIdcj8hhg')
bot = Bot(token='5287614807:AAEhFJW9kHAPSCnQuILjpDljK7k82ItKwQQ')
dp = Dispatcher(bot)
cb_options = CallbackData("post","button","user","ui")

# admin filters
#dp.filters_factory.bind(IsAdminFilter)

# datebase
connect = sqlite3.connect("users.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id BIGINT,
    balance INT,
    bank BIGINT,
    rating BIGINT,
    bitcoin BIGINT,
    expe BIGINT,
    last_stavka INT,
    last_bonus INT,
    car1 INT,
    car2 INT,
    car3 INT,
    car4 INT,
    car5 INT,
    car6 INT,
    car7 INT,
    car8 INT,
    car9 INT,
    car10 INT,
    car11 INT,
    user_name STRING,
    case1 INT,
    case2 INT,
    case3 INT,
    user_status STRING,
    cart INT,
    stavka INT,
    game INT,
    last_grab INT,
    pet1 INT,
    pet2 INT,
    pet3 INT,
    pet4 INT,
    pet5 INT,
    pet6 INT,
    pet7 INT,
    pet8 INT,
    pet9 INT,
    pet_name STRING,
    pet_hp INT,
    pet_eat INT,
    pet_mood INT,
    games INT,
    registr_time INT,
    last_work INT,
    checking INT,
    checking1 INT,
    checking2 INT,
    checking3 INT,
    pet10 INT,
    status STRING,
    car12 INT,
    case4 INT,
    snow INT,
    last_snow INT,
    promo1 INT,
    promo2 INT,
    promo3 INT,
    promo4 INT,
    promo5 INT,
    promo6 INT,
    promo7 INT,
    promo8 INT,
    promo9 INT,
    promo10 INT,
    promo11 INT,
    promo12 INT,
    promo13 INT,
    promo14 INT,
    promo15 INT,
    promo16 INT,
    promo17 INT,
    promo18 INT,
    promo19 INT,
    promo20 INT,
    promo21 INT,
    promo22 INT,
    promo23 INT,
    promo24 INT,
    suprise INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot(
    chat_id INT,
    last_stavka INT,
    curs INT, 
    last_curs INT,
    ivent INT,
    promo1 INT,
    promo2 INT,
    promo3 INT,
    promo4 INT,
    promo5 INT,
    promo6 INT,
    promo7 INT,
    promo8 INT,
    promo9 INT,
    promo10 INT,
    promo11 INT,
    promo12 INT,
    promo13 INT,
    promo14 INT,
    promo15 INT,
    promo16 INT,
    promo17 INT,
    promo18 INT,
    promo19 INT,
    promo20 INT,
    promo21 INT,
    promo22 INT,
    promo23 INT,
    promo24 INT
)
""")


###########################################СТАРТОВАЯ КОМАНДА###########################################
# start command


@dp.message_handler(commands=['start'])
async def start_cmd(message):
    msg = message
    user_id = msg.from_user.id
    user_name = msg.from_user.full_name
    user_status = "Player"
    pet_name = "name"
    status = "Игрок"
    chat_id = message.chat.id
    cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    if cursor.fetchone() is None:
       cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (user_id, 10000000000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, user_name, 0, 0, 0, user_status, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, pet_name, 100, 100, 100, 0, datetime.now(), 0, 0, 0, 0, 0, 0, status, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
       cursor.execute("INSERT INTO bot VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (chat_id, 0, 1000000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
       connect.commit()
    else:
       cursor.execute("INSERT INTO bot VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (chat_id, 0, 1000000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
       connect.commit()
       return
    photo = open('start.jpg', 'rb')
    name1 = message.from_user.get_mention(as_html=True)
    await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'👋 Привет, {name1} \nЯ  BOT для игры в различные игры.\nТебе выдан подарок в размере 1.000.000.000$.\nТак же ты можешь добавить меня в беседу для игры с друзьями.\n🆘 Чтобы узнать все команды введи "Помощь"', parse_mode='html')


@dp.message_handler(commands=['Помощь','help'],commands_prefix='!?./')
async def gui_main(message: types.Message):
    msg = message
    user = msg.from_user.get_mention('Игрок',as_html=True)
    user_link = msg.from_user.first_name
   
    buttons = [
    types.InlineKeyboardButton(text="Основное", callback_data=cb_options.new(button = "activity",user = user_link,ui = 'head')),
    types.InlineKeyboardButton(text="Игры", callback_data =cb_options.new(button = "games",user = user_link,ui = 'head')),
    types.InlineKeyboardButton(text="Развлекательное", callback_data=cb_options.new(button = "fun",user = user_link, ui = 'head'))
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    text = f"{user},выберите категорию:\n  1️⃣ Основное\n  2️⃣ Игры\n  3️⃣ Развлекательное \n\n 🆘 По всем вопросам - @bacarty"
    await message.answer(text, reply_markup=keyboard, parse_mode='html')


@dp.callback_query_handler(cb_options.filter(ui =['head'] ))
async def option(call:types.CallbackQuery,callback_data:dict):
   button = callback_data["button"]
   user = callback_data["user"]
   if button == 'activity':  
      await bot.send_message(call.message.chat.id, f"@{user}, комманды менеджмента ресурсов:  \n💡 Разное:\n   📒 Профиль/профиль\n   💸 Б/Баланс\n   👨 Ник - узнать ник   \n  🏦 Банк/снять/положить [сумма]\n  🤝 Дать/дать [сумма] [команда работает ответом на сообщение]\n   💎 Топ\n   💈 Ежедневный бонус\n  💻 Работать\n   🚗 Мой гараж - узнать о своих машинах\n   📦 Беседа - вступить официальную беседу BCR\n\n  Магазин"   , parse_mode='html')
   elif button == 'games':
      await bot.send_message(call.message.chat.id, f"@{user}, игровые комманды:  \n💡 🚀 Игры:\n 🎮 Спин [ставка]\n 🎰 Казино [ставка]\n   🎲 Чётное/Нечётное [ставка]\n   🏎 Гонки [ставка]\n   ⚔️ Бой [ставка]\n   📦 Кейсы\n\n💭 РП-команды - вывести список РП-команд\n---------------\n💥", parse_mode='html')
   elif button == 'fun':  
      await bot.send_message(call.message.chat.id, f"@{user}, развлекательные комманды:  \n💡💥 Развлекатетельное:\n   🔮 Шар\n   🧿 Шанс\n---------------\n💈 Модерация чатов:\n   🔇 .мут [время]\n   🔈 .размут\n   🛑 .бан\n   ✅ .разбан\n\n💻Донат - купить Админ/валюту", parse_mode='html')
   await bot.answer_callback_query(call.id)
      

@dp.message_handler(commands=['мут', 'mute'], commands_prefix='!?./', is_chat_admin=True)
async def mute(message):
   name1 = message.from_user.get_mention(as_html=True)
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   try:
      muteint = int(message.text.split()[1])
      mutetype = message.text.split()[2]
      comment = " ".join(message.text.split()[3:])
   except IndexError:
      await message.reply('ℹ | Не хватает аргументов!\nПример:\n<code>/мут 1 ч причина</code>')
      return
   if mutetype == "ч" or mutetype == "часов" or mutetype == "час":
      dt = datetime.now() + timedelta(hours=muteint)
      timestamp = dt.timestamp()
      await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
      await message.reply(f'👤 | Администратор: {name1}\n🛑 | Замутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | Срок: {muteint} {mutetype}\n📃 | Причина: {comment}',  parse_mode='html')
   if mutetype == "м" or mutetype == "минут" or mutetype == "минуты":
      dt = datetime.now() + timedelta(minutes=muteint)
      timestamp = dt.timestamp()
      await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
      await message.reply(f'👤 | Администратор: {name1}\n🛑 | Замутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | Срок: {muteint} {mutetype}\n📃 | Причина: {comment}',  parse_mode='html')
   if mutetype == "д" or mutetype == "дней" or mutetype == "день":
      dt = datetime.now() + timedelta(days=muteint)
      timestamp = dt.timestamp()
      await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
      await message.reply(f'👤 | Администратор: {name1}\n | 🛑Замутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | Срок: {muteint} {mutetype}\n📃 | Причина: {comment}',  parse_mode='html')

@dp.message_handler(commands=['размут', 'unmute'], commands_prefix='!?./', is_chat_admin=True)
async def unmute(message):
   name1 = message.from_user.get_mention(as_html=True)
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
   await message.reply(f'👤 | Администратор: {name1}\n🔊 | Размутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>',  parse_mode='html')

@dp.message_handler(commands=['ban', 'бан', 'кик', 'kick'], commands_prefix='!?./', is_chat_admin=True)
async def ban(message):
   name1 = message.from_user.get_mention(as_html=True)
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   comment = " ".join(message.text.split()[1:])
   await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False))
   await message.reply(f'👤 | Администратор: {name1}\n🛑 | Забанил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | Срок: навсегда\n📃 | Причина: {comment}',  parse_mode='html')

@dp.message_handler(commands=['разбан', 'unban'], commands_prefix='!?./', is_chat_admin=True)
async def unban(message):
   name1 = message.from_user.get_mention(as_html=True)
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
   await message.reply(f'👤 | Администратор: {name1}\n📲 | Разбанил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>',  parse_mode='html')

# prof_user
@dp.message_handler()
async def users(message: types.Message):

###########################################ОСНОВНЫЕ КОМАНДЫ###########################################
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
    if user_status[0] == "Blocked":
       return
    else:
       pass
    msg = message
    user_name = message.from_user.get_mention(as_html=True)
    user_id = msg.from_user.id
    win = ['🙂', '😋', '😄', '🤑', '😃']
    rwin = random.choice(win)
    loser = ['😔', '😕', '😣', '😞', '😢']
    rloser = random.choice(loser)
    ivent = cursor.execute("SELECT ivent from bot").fetchone()
    ivent = int(ivent[0])
    snow = cursor.execute("SELECT snow from users where user_id = ?",(message.from_user.id,)).fetchone()
    snow = int(snow[0])
    period = 86400
    get = cursor.execute("SELECT last_snow FROM users WHERE user_id = ?", (user_id,)).fetchone()
    last_snow = f"{int(get[0])}"
    snowtime = time.time() - float(last_snow)
    if ivent == 1:
       if snowtime > period:
          await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно собрали 2 снежинки! {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET snow = {snow + 2} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET last_snow=? WHERE user_id=?', (time.time(), user_id,))
       else:
          pass
    if ivent == 0:
       pass
    # money
    if message.text.lower() in ["баланс", "Баланс", "Б", "б"]:
       msg = message
       user_id = msg.from_user.id
       user_name = msg.from_user.full_name
       chat_id = message.chat.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       balance2 = '{:,}'.format(balance)
       bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank)
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?",(message.from_user.id,)).fetchone()
       bitcoin = round(int(bitcoin[0]))
       bitcoin2 = '{:,}'.format(bitcoin)
       c = 999999999999999999999999
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       else:
        pass
       if bank >= 999999999999999999999999:
          bank = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          bank2 = '{:,}'.format(bank) 
       else:
        pass
       if bitcoin >= 999999999999999999999999:
          bitcoin = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bitcoin = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          bitcoin2 = '{:,}'.format(bitcoin)
       else:
        pass
       await bot.send_message(message.chat.id, f"👫Ник: {user_name} \n💰Деньги: {balance2}$ \n🏦Банк: {bank2}$\n💽 Биткоины: {bitcoin2}฿")
    # nick
    if message.text.lower() in ["ник", "Ник"]:
       msg = message 
       chat_id = message.chat.id
       user_name = msg.from_user.full_name
       await bot.send_message(message.chat.id, f"🗂 Ваш ник - {user_name}")

    if message.text.lower() in ["банк", "Банк"]:
       msg = message 
       user_id = msg.from_user.id
       bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       if bank >= 999999999999999999999999:
          bank = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          bank2 = '{:,}'.format(bank) 
       else:
        pass
       msg = message 
       bank2 = '{:,}'.format(bank) 
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)
       name = msg.from_user.full_name
       await bot.send_message(message.chat.id, f"{user_name}, ваш банковский счёт:\n👫 Владелец: {name}\n💰 Деньги в банке: {bank2}$", parse_mode='html')
   
    if message.text.lower() in ["биткоин", "Биткоин"]:
       msg = message 
       user_id = msg.from_user.id
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?",(message.from_user.id,)).fetchone()
       bitcoin = round(int(bitcoin[0]))
       if bitcoin >= 999999999999999999999999:
          bitcoin = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bitcoin = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          bitcoin2 = '{:,}'.format(bitcoin) 
       else:
        pass
       msg = message 
       bitcoin2 = '{:,}'.format(bitcoin) 
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)
       await bot.send_message(message.chat.id, f"{user_name}, на вашем счету {bitcoin} BTC", parse_mode='html')

    if message.text.lower() in ["профиль", "Профиль"]:
       msg = message
       chat_id = message.chat.id
       name1 = message.from_user.get_mention(as_html=True)
       user_name = msg.from_user.full_name
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       status  = cursor.execute("SELECT status from users where user_id = ?",(message.from_user.id,)).fetchone() #add status
       bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
       games = cursor.execute("SELECT games from users where user_id = ?",(message.from_user.id,)).fetchone()
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?",(message.from_user.id,)).fetchone()
       expe = cursor.execute("SELECT expe from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       games = int(games[0])
       bank = int(bank[0])
       bitcoin = int(bitcoin[0])
       expe = int(expe[0])
       rating = int(rating[0])
       status = cursor.execute("SELECT status from users where user_id = ?",(message.from_user.id,)).fetchone()
       status = str(status[0])
       c = 999999999999999999999999
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit() 
       else:
        pass
       if int(balance) in range(0, 1000):
          balance3 = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
          balance3 = int(balance3[0])
       if int(balance) in range(1000, 999999):
          balance1 = balance / 1000
          balance2 = round(balance1)
          balance3 = f'{balance2} тыс'
       if int(balance) in range(1000000, 999999999):
          balance1 = balance / 1000000
          balance2 = round(balance1)
          balance3 = f'{balance2} млн'
       if int(balance) in range(1000000000, 999999999999):
          balance1 = balance / 1000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} млрд'
       if int(balance) in range(1000000000000, 999999999999999):
          balance1 = balance / 1000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} трлн'
       if int(balance) in range(1000000000000000, 999999999999999999):
          balance1 = balance / 1000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} квдр'
       if int(balance) in range(1000000000000000000, 999999999999999999999):
          balance1 = balance / 1000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} квнт'
       if int(balance) in range(1000000000000000000000, 999999999999999999999999):
          balance1 = balance / 1000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} скст'
       if bank >= 999999999999999999999999:
          bank = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()   
       else:
        pass
       if int(bank) in range(0, 1000):
          bank3 = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
          bank3 = int(bank3[0])
       if int(bank) in range(1000, 999999):
          bank1 = bank / 1000
          bank2 = round(bank1)
          bank3 = f'{bank2} тыс'
       if int(bank) in range(1000000, 999999999):
          bank1 = bank / 1000000
          bank2 = round(bank1)
          bank3 = f'{bank2} млн'
       if int(bank) in range(1000000000, 999999999999):
          bank1 = bank / 1000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} млрд'
       if int(bank) in range(1000000000000, 999999999999999):
          bank1 = bank / 1000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} трлн'
       if int(bank) in range(1000000000000000, 999999999999999999):
          bank1 = bank / 1000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} квдр'
       if int(bank) in range(1000000000000000000, 999999999999999999999):
          bank1 = bank / 1000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} квнт'
       if int(bank) in range(1000000000000000000000, 999999999999999999999999):
          bank1 = bank / 1000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} скст'
       if bitcoin >= 999999999999999999999999:
          bitcoin = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bitcoin = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()   
       else:
        pass
       if int(bitcoin) in range(0, 1000):
          bitcoin3 = cursor.execute("SELECT bitcoin from users where user_id = ?",(message.from_user.id,)).fetchone()
          bitcoin3 = int(bitcoin3[0])
       if int(bitcoin) in range(1000, 999999):
          bitcoin1 = bitcoin / 1000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} тыс'
       if int(bitcoin) in range(1000000, 999999999):
          bitcoin1 = bitcoin / 1000000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} млн'
       if int(bitcoin) in range(1000000000, 999999999999):
          bitcoin1 = bitcoin / 1000000000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} млрд'
       if int(bitcoin) in range(1000000000000, 999999999999999):
          bitcoin1 = bitcoin / 1000000000000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} трлн'
       if int(bitcoin) in range(1000000000000000, 999999999999999999):
          bitcoin1 = bitcoin / 1000000000000000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} квдр'
       if int(bitcoin) in range(1000000000000000000, 999999999999999999999):
          bitcoin1 = bitcoin / 1000000000000000000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} квнт'
       if int(bitcoin) in range(1000000000000000000000, 999999999999999999999999):
          bitcoin1 = bitcoin / 1000000000000000000000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} скст'
       if expe >= 999999999999999999999999:
          expe = 999999999999999999999999
          cursor.execute(f'UPDATE users SET expe = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
       else:
        pass
       if int(expe) in range(0, 1000):
          expe3 = cursor.execute("SELECT expe from users where user_id = ?",(message.from_user.id,)).fetchone()
          expe3 = int(expe3[0])
       if int(expe) in range(1000, 999999):
          expe1 = expe / 1000
          expe2 = round(expe1)
          expe3 = f'{expe2} тыс'
       if int(expe) in range(1000000, 999999999):
          expe1 = expe / 1000000
          expe2 = round(expe1)
          expe3 = f'{expe2} млн'
       if int(expe) in range(1000000000, 999999999999):
          expe1 = expe / 1000000000
          expe2 = round(expe1) 
          expe3 = f'{expe2} млрд'
       if int(expe) in range(1000000000000, 999999999999999):
          expe1 = expe / 1000000000000
          expe2 = round(expe1)
          expe3 = f'{expe2} трлн'
       if int(expe) in range(1000000000000000, 999999999999999999):
          expe1 = expe / 1000000000000000
          expe2 = round(expe1)
          bexpe3 = f'{expe2} квдр'
       if int(expe) in range(1000000000000000000, 999999999999999999999):
          expe1 = expe / 1000000000000000000
          expe2 = round(expe1)
          expe3 = f'{expe2} квнт'
       if int(expe) in range(1000000000000000000000, 999999999999999999999999):
          expe1 = expe / 1000000000000000000000
          expe2 = round(expe1)
          expe3 = f'{expe2} скст'
       if rating >= 999999999999999999999999:
          rating = 999999999999999999999999
          cursor.execute(f'UPDATE users SET rating = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
       else:
        pass
       if int(rating) in range(0, 1000):
          rating3 = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
          rating3 = int(rating3[0])
       if int(rating) in range(1000, 999999):
          rating1 = rating / 1000
          rating2 = round(rating1)
          rating3 = f'{rating2} тыс'
       if int(rating) in range(1000000, 999999999):
          rating1 = rating / 1000000
          rating2 = round(rating1)
          rating3 = f'{rating2} млн'
       if int(rating) in range(1000000000, 999999999999):
          rating1 = rating / 1000000000
          rating2 = round(rating1) 
          rating3 = f'{rating2} млрд'
       if int(rating) in range(1000000000000, 999999999999999):
          rating1 = rating / 1000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} трлн'
       if int(rating) in range(1000000000000000, 999999999999999999):
          rating1 = rating / 1000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} квдр'
       if int(rating) in range(1000000000000000000, 999999999999999999999):
          rating1 = rating / 1000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} квнт'
       if int(rating) in range(1000000000000000000000, 999999999999999999999999):
          rating1 = rating / 1000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} скст'

       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])

       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       cart = int(cart[0])

       c = int(car10) + int(car11)
       print(c)
       cars = int(car1) + int(car2) + int(car3) + int(car4) + int(car5) + int(car6) + int(car7) + int(car8) + int(car9)
       if car1 == 1:
          m1 = f"    🚗 ВАЗ 2107 - Топливо: {cart}%\n"
       if car1 == 0:
          m1 = ""
       if car2 == 1:
          m1 = f"    🚗 Lada Vesta - Топливо: {cart}%\n"
       if car2 == 0:
          m1 = ""
       if car3 == 1:
          m1 = f"    🚗 Lada XRAY Cross - Топливо: {cart}%\n"
       if car3 == 0:
          m1 = ""
       if car4 == 1:
          m1 = f"    🚗 Audi Q7 - Топливо: {cart}%\n"
       if car4 == 0:
          m1 = ""
       if car5 == 1:
          m1 = f"    🚗 BMW X6 - Топливо: {cart}%\n"
       if car5 == 0:
          m1 = ""
       if car6 == 1:
          m1 = f"    🚗 Hyundai Solaris - Топливо: {cart}%\n"
       if car6 == 0:
          m1 = ""
       if car7 == 1:
          m1 = f"    🚗 Toyota Supra - Топливо: {cart}%\n"
       if car7 == 0:
          m1 = ""
       if car8 == 1:
          m1 = f"    🚗 Lamborghini Veneno - Топливо: {cart}%\n"
       if car8 == 0:
          m1 = ""
       if car9 == 1:
          m1 = f"    🚗 Bugatti Veyron - Топливо: {cart}%\n"
       if car9 == 0:
          m1 = ""
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pets = int(pet1) + int(pet2) + int(pet3) + int(pet4) + int(pet5) + int(pet6) + int(pet7) + int(pet8) + int(pet9)
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       if pet1 == 1:
          p = f"    🐥 воробей - Имя: {pet_name}\n"
       if pet1 == 0:
          p = ""
       if pet2 == 1:
          p = f"    🐈 Акула - Имя: {pet_name}\n"
       if pet2 == 0:
          p = ""
       if pet3 == 1:
          p = f"    🐕 Скат - Имя: {pet_name}\n"
       if pet3 == 0:
          p = ""
       if pet4 == 1:
          p = f"    🦜 T-Rex - Имя: {pet_name}\n"
       if pet4 == 0:
          p = ""
       if pet5 == 1:
          p = f"    🦄 Питон - Имя: {pet_name}\n"
       if pet5 == 0:
          p = ""
       if pet6 == 1:
          p = f"    🐒 Кинг-конг - Имя: {pet_name}\n"
       if pet6 == 0:
          p = ""
       if pet7 == 1:
          p = f"    🐬 Тигр - Имя: {pet_name}\n"
       if pet7 == 0:
          p = ""
       if pet8 == 1:
          p = f"    🐅 Лев - Имя: {pet_name}\n"
       if pet8 == 0:
          p = ""
       if pet9 == 1:
          p = f"    🐉 Единорог - Имя: {pet_name}\n"
       if pet9 == 0:
          p = ""
       if int(pets) + int(cars) == 0:
          s = f"    ☹️ У вас нету имущества!\n"
       if int(pets) + int(cars) >= 1:
          s = f"{p}{m1}"
       get = cursor.execute("SELECT registr_time FROM users WHERE user_id=?", (message.from_user.id,)).fetchall()
       date_time = datetime.fromisoformat(get[0][0])
       times = date_time.strftime( "%d.%m.%Y %H:%M:%S" ) 
       await bot.send_message(message.chat.id, f"{name1}, ваш профиль: \n 🔎 ID: {user_id} \n 💰 Деньги: {balance3}$ \n 🏦 В банке: {bank3}$ \n 👑 Рейтинг: {rating3} \n 🌟 Опыт: {expe3} \n 💽 Биткоины: {bitcoin3}฿ \n 🔮 Ваш статус: {status} \n 🎲 Всего сыграно игр: {games} \n 📦 Имущество:\n {s} \n 📅 Дата регистрации: {times}",  parse_mode='html')   
    # top
    if message.text.lower() in ["топ", "Топ"]:
       list = cursor.execute(f"SELECT * FROM users ORDER BY rating DESC").fetchmany(10)
       top_list = []
       chat_id = message.chat.id
       name = message.from_user.get_mention(as_html=True)
       num = 0
       for user in list:
           if user[3] >= 999999999999999999999999:
              c6 = 999999999999999999999999
           else:
              c6 = user[3]
           num += 1
           c = Decimal(c6)
           c2 = '{:,}'.format(c)
           
           top_list.append(f"{num}. {user[19]}  — 👑{c2}")
       top = "\n".join(top_list)
       await bot.send_message(message.chat.id, f"{name}, топ 30 игроков бота:\n" + top , parse_mode='html')

    if message.text.lower() in ["ежедневный бонус", "Ежедневный бонус"]:
        msg = message
        chat_id = message.chat.id
        user_id = msg.from_user.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        period = 86400
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        get = cursor.execute("SELECT last_bonus FROM users WHERE user_id=?", (user_id,)).fetchall()
        last_bonus = f"{int(get[0][0])}"
        bonustime = time.time() - float(last_bonus)
        user_name = message.from_user.get_mention(as_html=True)
        money_bonus = random.randint(1000000000000, 5000000000000)
        money_bonus2 = '{:,}'.format(money_bonus)
        if balance >= 999999999999999999999999:
           balance = 999999999999999999999999
           cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
           connect.commit()
           balance2 = '{:,}'.format(balance) 
        if bonustime > period:
            cursor.execute(f'UPDATE users SET balance = {balance + money_bonus}  WHERE user_id = ?', (user_id,))
            cursor.execute(f'UPDATE users SET last_bonus=? WHERE user_id=?', (time.time(), user_id,))
            connect.commit()  
            await bot.send_message(message.chat.id, f"💰 | {user_name}, ты получил бонус в размере {str(money_bonus2)}$ {rwin}", parse_mode='html')
        else:
            await bot.send_message(message.chat.id, f"ℹ️ | {user_name}, ты уже получал сегодня бонус! {rloser}", parse_mode='html')

    if message.text.lower() in ["помощь", "Помощь"]:
       chat_id = message.chat.id
       name_user = message.from_user.get_mention(as_html=True)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
      #  await cmd_start(message)
       ivent = int(ivent[0])
       if ivent == 1:
          await bot.send_message(chat_id, f"{name_user} , мои команды:  \n💡 Разное:\n   📒 Профиль/профиль\n   💸 Б/Баланс\n   👨 Ник - узнать ник   \n  🏦 Банк/снять/положить [сумма]\n  🤝 Дать/дать [сумма] [команда работает ответом на сообщение]\n   💎 Топ\n   💈 Ежедневный бонус\n  💻 Работать\n   🚗 Мой гараж - узнать о своих машинах\n   📦 Беседа - вступить официальную беседу BCR\n\n  Магазин   \n---------------\n🚀 Игры:\n 🎮 Спин [ставка]\n 🎰 Казино [ставка]\n   🎲 Чётное/Нечётное [ставка]\n   🏎 Гонки [ставка]\n   ⚔️ Бой [ставка]\n   📦 Кейсы\n\n💭 РП-команды - вывести список РП-команд\n---------------\n💥 Развлекатетельное:\n   🔮 Шар\n   🧿 Шанс\n---------------\n💈 Модерация чатов:\n   🔇 .мут [время]\n   🔈 .размут\n   🛑 .бан\n   ✅ .разбан\n\n💻Донат - купить Админ/валюту", parse_mode='html')
       if ivent == 0:
          await bot.send_message(chat_id, f"{name_user} , мои команды:  \n💡 Разное:\n   📒 Профиль/профиль\n   💸 Б/Баланс\n   👨 Ник - узнать ник   \n  🏦 Банк/снять/положить [сумма]\n  🤝 Дать/дать [сумма] [команда работает ответом на сообщение]\n   💎 Топ\n   💈 Ежедневный бонус\n  💻 Работать\n   🚗 Мой гараж - узнать о своих машинах\n   📦 Беседа - вступить официальную беседу TIGLACK\n\n  Магазин  \n---------------\n🚀 Игры:\n   🎮 Спин [ставка]\n   🎰 Казино [ставка]\n   🎲 Чётное/Нечётное [ставка]\n   🏎 Гонки [ставка]\n   ⚔️ Бой [ставка]\n   📦 Кейсы\n\n💭 РП-команды - вывести список РП-команд\n---------------\n💥 Развлекатетельное:\n   🔮 Шар\n   🧿 Шанс\n---------------\n💈 Модерация чатов:\n   🔇 .мут [время]\n   🔈 .размут\n   🛑 .бан\n   ✅ .разбан\n\n💻Донат - купить Админ/валюту", parse_mode='html')

    if message.text.startswith("шар"):
       chat_id = message.chat.id
       msg = message
       name_user = message.from_user.get_mention(as_html=True)
       x = [f'я думаю - "да"','мой ответ - "нет"','я думаю - "нет"','мой ответ - "да"','может быть']
       rx = random.choice(x)
       args = message.get_args()
       await bot.send_message(chat_id, f"🎱 | {name_user} , {rx}", parse_mode='html')

    if message.text.startswith("шанс"):
       chat_id = message.chat.id
       msg = message
       name_user = message.from_user.get_mention(as_html=True)
       args = message.get_args()
       x = random.randint(0,100)
       await bot.send_message(chat_id, f"🎰 | {name_user} , шанс этого: {x}%", parse_mode='html')

    if message.text.startswith("Шар"):
       chat_id = message.chat.id
       msg = message
       name_user = message.from_user.get_mention(as_html=True)
       x = [f'я думаю - "да"','мой ответ - "нет"','я думаю - "нет"','мой ответ - "да"','может быть']
       rx = random.choice(x)
       args = message.get_args()
       await bot.send_message(chat_id, f"🎱 | {name_user} , {rx}🎱", parse_mode='html')

    if message.text.startswith("Шанс"):
       chat_id = message.chat.id
       msg = message
       name_user = message.from_user.get_mention(as_html=True)
       args = message.get_args()
       x = random.randint(0,100)
       await bot.send_message(chat_id, f"🎰 | {name_user} , шанс этого: {x}%", parse_mode='html')

    if message.text.lower() in ["донат", "Донат"]:
       user_name = message.from_user.get_mention(as_html=True)
       await bot.send_message(message.chat.id, f"💎 | {user_name}, список доната:\n\n 🛠 Aдмин - 250р/месяц\n🛠 Админ статус - 150р/месяц\n 🛒 По поводу покупки писать: @bacarty", parse_mode='html')

 # casino

    if message.text.startswith("Казино"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 110)
        rwin = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        print(f"{name} поставил в казино: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(0, 15):
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0) {rloser}', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(16, 33):
                        c = Decimal(summ - summ * 0.25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.25) {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(34, 54):
                        c = Decimal(summ * 0.5)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.5) {rloser}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(54, 62):
                        c = Decimal(summ - summ * 0.75)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.75) {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(63, 73):
                        c = summ * 1
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, ваши деньги остаются при вас {c2}$ (x1) {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(74, 83):
                        c = Decimal(summ * 1.25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.25) {rwin}', parse_mode='html')

                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.25)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(84, 90):
                        c = Decimal(summ * 1.5)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.5) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.5)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(91, 96):
                        c = Decimal(summ * 1.75)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.75) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.75)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(97, 102):
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x2) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(103, 106):
                        c = Decimal(summ * 3)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x3) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 3)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) == 110:
                        c = Decimal(summ * 50)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x5) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 5)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                    if int(rx) in range(107, 109):
                        c = Decimal(summ * 10)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x10) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 10)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return

    if message.text.startswith("казино"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 110)
        rwin = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        print(f"{name} поставил в казино: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(0, 15):
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0) {rloser}', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(16, 33):
                        c = Decimal(summ - summ * 0.25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.25) {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(34, 54):
                        c = Decimal(summ * 0.5)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.5) {rloser}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(54, 62):
                        c = Decimal(summ - summ * 0.75)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.75) {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(63, 73):
                        c = summ * 1
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, ваши деньги остаются при вас {c2}$ (x1) {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(74, 83):
                        c = Decimal(summ * 1.25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.25) {rwin}', parse_mode='html')

                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.25)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(84, 90):
                        c = Decimal(summ * 1.5)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.5) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.5)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(91, 96):
                        c = Decimal(summ * 1.75)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.75) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.75)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(97, 102):
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x2) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(103, 106):
                        c = Decimal(summ * 3)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x3) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 3)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) == 110:
                        c = Decimal(summ * 50)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x5) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 5)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                    if int(rx) in range(107, 109):
                        c = Decimal(summ * 10)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x10) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 10)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
    
 # treyd
    if message.text.startswith("Трейдвверх"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id

       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rx = random.randint(0,110)
       rwin = random.choice(win)
       rloser = random.choice(loser)

       msg = message
       name1 = message.from_user.get_mention(as_html=True)
       name = msg.from_user.last_name 
       summ = int(msg.text.split()[1])
       print(f"{name} поставил в казино: {summ} и выиграл/проиграл: {rx}")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       period = 5
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(rx) in range(0,9):
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс упал вниз {c2}$ (x0) 📉 {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()   
                   return                           
                if int(rx) in range(10,29):
                   c = Decimal(summ - summ * 0.25)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс упал вниз {c2}$ (x0.25) 📉 {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return   
                if int(rx) in range(30,44):
                   c = Decimal(summ * 0.5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс упал вниз {c2}$ (x0.5) 📉 {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return  
                if int(rx) in range(45,54):
                   c = Decimal(summ - summ * 0.75)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс упал вниз {c2}$ (x0.75) 📉 {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return  
                if int(rx) in range(55,64):
                   c = summ * 1
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс на середине {c2}$ (x1) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()
                   return 
                if int(rx) in range(65,69):
                   c = Decimal(summ * 1.25)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс поднялся вверх {c2}$ (x1.25) 📈 {rwin}', parse_mode='html')       
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.25)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()           
                   return 
                if int(rx) in range(70,74):
                   c = Decimal(summ * 1.5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс поднялся вверх {c2}$ (x1.5) 📈 {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.5)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
                if int(rx) in range(75,84):
                   c = Decimal(summ * 1.75)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс поднялся вверх {c2}$ (x1.75) 📈 {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.75)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
                if int(rx) in range(85,95):
                   c = Decimal(summ * 2)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс поднялся вверх {c2}$ (x2) 📈 {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
                if int(rx) in range(100,108):
                   c = Decimal(summ * 3)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс поднялся вверх {c2}$ (x3) 📈 {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 3)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
                if int(rx) == 109:
                   c = Decimal(summ * 5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс поднялся вверх {c2}$ (x5) 📈 {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 5)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                if int(rx) == 100:
                   c = Decimal(summ * 10)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс поднялся вверх {c2}$ (x10) 📈 {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 10)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
           await bot.send_message(chat_id, f'ℹ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
           return
            
            
    if message.text.startswith("Трейдвниз"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id

       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rx = random.randint(0,110)
       rwin = random.choice(win)
       rloser = random.choice(loser)

       msg = message
       name1 = message.from_user.get_mention(as_html=True)
       name = msg.from_user.last_name 
       summ = int(msg.text.split()[1])
       print(f"{name} поставил в казино: {summ} и выиграл/проиграл: {rx}")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       period = 5
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(rx) in range(0,9):
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс поднялся {c2}$ (x0) 📈 {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()   
                   return                           
                if int(rx) in range(10,29):
                   c = Decimal(summ - summ * 0.25)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс поднялся {c2}$ (x0.25) 📈 {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return   
                if int(rx) in range(30,44):
                   c = Decimal(summ * 0.5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс поднялся {c2}$ (x0.5) 📈 {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return  
                if int(rx) in range(45,54):
                   c = Decimal(summ - summ * 0.75)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс поднялся {c2}$ (x0.75) 📈 {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return  
                if int(rx) in range(55,64):
                   c = summ * 1
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс на середине {c2}$ (x1) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()
                   return 
                if int(rx) in range(65,69):
                   c = Decimal(summ * 1.25)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс упал {c2}$ (x1.25) 📉 {rwin}', parse_mode='html')       
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.25)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()           
                   return 
                if int(rx) in range(70,74):
                   c = Decimal(summ * 1.5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс упал {c2}$ (x1.5) 📉 {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.5)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
                if int(rx) in range(75,84):
                   c = Decimal(summ * 1.75)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс упал {c2}$ (x1.75) 📉 {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.75)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
                if int(rx) in range(85,95):
                   c = Decimal(summ * 2)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс упал {c2}$ (x2) 📉 {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
                if int(rx) in range(100,108):
                   c = Decimal(summ * 3)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс упал {c2}$ (x3) 📉 {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 3)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
                if int(rx) == 109:
                   c = Decimal(summ * 5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс упал {c2}$ (x5) 📉 {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 5)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                if int(rx) == 100:
                   c = Decimal(summ * 10)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, Курс упал {c2}$ (x10) 📉 {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 10)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
           await bot.send_message(chat_id, f'ℹ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
           return

    # spin
    if message.text.startswith("спин"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = msg.from_user.last_name
       emoji = ['🖕','🍋','🍒','🥃','💎','🍓', '🖕']
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       rwin = random.choice(win)
       re1 = random.choice(emoji)
       re2 =  random.choice(emoji)
       re3 =  random.choice(emoji)

       msg = message
       name1 = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       print( f"{user_name} поставил в спин: {summ} и выиграл/проиграл: {re1}, {re2}, {re3}")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if str(re3) == str(re2) == str(re1):
                   if str(re1) == '🖕':  #проигрыш
                               await bot.send_message(chat_id, f'{rloser} | {name1} \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
                   if str(re2) == '🖕':
                               await bot.send_message(chat_id, f'{rloser} | {name1} \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit()
                               return
                    
                   if str(re3) == '🖕':
                               await bot.send_message(chat_id, f'{rloser} | {name1} \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                   else:
                               c = Decimal(summ * 50)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| ДЖЕКПОТ! Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 50)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re1) == '🖕':  #проигрыш
                               await bot.send_message(chat_id, f'{rloser} | {name1} \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re2) == '🖕':
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit()
                               return
                  
                if str(re3) == '🖕':
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
 
                if str(re1) == '🍋': #выигрыш 1
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re2) == '🍋':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
                if str(re3) == '🍋':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re1) == '🍒': #выигрыш 2
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re2) == '🍒':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re3) == '🍒':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re1) == '🥃': #выигрыш 3
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
                if str(re2) == '🥃':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
  
                if str(re3) == '🥃':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re1) == '💎': #выигрыш 4
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re2) == '💎':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
 
                if str(re3) == '💎':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re1) == '🍓': #выигрыш 5
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re2) == '🍓':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
 
                if str(re3) == '🍓':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
           await bot.send_message(chat_id, f'ℹ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
           return

    if message.text.startswith("Спин"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = msg.from_user.last_name
       emoji = ['🖕','🍋','🍒','🥃','💎','🍓', '🖕']
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       rwin = random.choice(win)
       re1 = random.choice(emoji)
       re2 =  random.choice(emoji)
       re3 =  random.choice(emoji)

       msg = message
       name1 = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       print( f"{user_name} поставил в спин: {summ} и выиграл/проиграл: {re1}, {re2}, {re3}")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if str(re3) == str(re2) == str(re1):
                   if str(re1) == '🖕':  #проигрыш
                               await bot.send_message(chat_id, f'{rloser} | {name1} \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
                   if str(re2) == '🖕':
                               await bot.send_message(chat_id, f'{rloser} | {name1} \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit()
                               return
                    
                   if str(re3) == '🖕':
                               await bot.send_message(chat_id, f'{rloser} | {name1} \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                   else:
                               c = Decimal(summ * 50)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| ДЖЕКПОТ! Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 50)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re1) == '🖕':  #проигрыш
                               await bot.send_message(chat_id, f'{rloser} | {name1} \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re2) == '🖕':
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit()
                               return
                  
                if str(re3) == '🖕':
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
 
                if str(re1) == '🍋': #выигрыш 1
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re2) == '🍋':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
                if str(re3) == '🍋':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re1) == '🍒': #выигрыш 2
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re2) == '🍒':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re3) == '🍒':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re1) == '🥃': #выигрыш 3
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
                if str(re2) == '🥃':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
  
                if str(re3) == '🥃':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re1) == '💎': #выигрыш 4
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re2) == '💎':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
 
                if str(re3) == '💎':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re1) == '🍓': #выигрыш 5
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return

                if str(re2) == '🍓':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
 
                if str(re3) == '🍓':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1} \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               connect.commit() 
                               return
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
           await bot.send_message(chat_id, f'ℹ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
           return

    if message.text.startswith("Четное"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       name1 = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       summ = int(msg.text.split()[1])
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                cursor.execute(f'UPDATE users SET checking = {1} WHERE user_id = "{user_id}"')
                dice_message = await bot.send_dice(chat_id)
                value = dice_message.dice.value
                if value in [1, 3, 5]:
                   await asyncio.sleep(4)
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"{rloser} | {name1}, Сожалеем, выпало нечётное! \nВы проиграли: {c2} {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return
                if value in [2, 4, 6]:
                   await asyncio.sleep(4)
                   c = Decimal(summ * 1.45)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"🎉 | {name1}, Поздравляю, выпало чётное! \nВы выиграли: {c2} {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 1.45)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
           await bot.send_message(chat_id, f'ℹ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
           return

    if message.text.startswith("Нечетное"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       name1 = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       summ = int(msg.text.split()[1])
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                cursor.execute(f'UPDATE users SET checking = {1} WHERE user_id = "{user_id}"')
                dice_message = await bot.send_dice(chat_id)
                value = dice_message.dice.value
                if value in [2, 4, 6]:
                   await asyncio.sleep(4)
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"{rloser} | {name1}, Сожалеем, выпало чётное! \nВы проиграли: {c2} {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return
                if value in [1, 3, 5]:
                   await asyncio.sleep(4)
                   c = Decimal(summ * 1.45)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"🎉 | {name1}, Поздравляю, выпало нечётное! \nВы выиграли: {c2} {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 1.45)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
           await bot.send_message(chat_id, f'ℹ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
           return

    if message.text.startswith("Чётное"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       name1 = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       summ = int(msg.text.split()[1])
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                cursor.execute(f'UPDATE users SET checking = {1} WHERE user_id = "{user_id}"')
                dice_message = await bot.send_dice(chat_id)
                value = dice_message.dice.value
                if value in [1, 3, 5]:
                   await asyncio.sleep(4)
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"{rloser} | {name1}, Сожалеем, выпало нечётное! \nВы проиграли: {c2} {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return
                if value in [2, 4, 6]:
                   await asyncio.sleep(4)
                   c = Decimal(summ * 1.45)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"🎉 | {name1}, Поздравляю, выпало чётное! \nВы выиграли: {c2} {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 1.45)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
           await bot.send_message(chat_id, f'ℹ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
           return

    if message.text.startswith("Нечётное"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       name1 = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       summ = int(msg.text.split()[1])
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                cursor.execute(f'UPDATE users SET checking = {1} WHERE user_id = "{user_id}"')
                dice_message = await bot.send_dice(chat_id)
                value = dice_message.dice.value
                if value in [2, 4, 6]:
                   await asyncio.sleep(4)
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"{rloser} | {name1}, Сожалеем, выпало чётное! \nВы проиграли: {c2} {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return
                if value in [1, 3, 5]:
                   await asyncio.sleep(4)
                   c = Decimal(summ * 1.45)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"🎉 | {name1}, Поздравляю, выпало нечётное! \nВы выиграли: {c2} {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 1.45)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
           await bot.send_message(chat_id, f'ℹ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
           return

    if message.text.startswith("четное"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       name1 = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       summ = int(msg.text.split()[1])
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                cursor.execute(f'UPDATE users SET checking = {1} WHERE user_id = "{user_id}"')
                dice_message = await bot.send_dice(chat_id)
                value = dice_message.dice.value
                if value in [1, 3, 5]:
                   await asyncio.sleep(4)
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"{rloser} | {name1}, Сожалеем, выпало нечётное! \nВы проиграли: {c2} {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return
                if value in [2, 4, 6]:
                   await asyncio.sleep(4)
                   c = Decimal(summ * 1.45)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"🎉 | {name1}, Поздравляю, выпало чётное! \nВы выиграли: {c2} {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 1.45)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
           await bot.send_message(chat_id, f'ℹ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
           return

    if message.text.startswith("нечетное"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       name1 = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       summ = int(msg.text.split()[1])
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                cursor.execute(f'UPDATE users SET checking = {1} WHERE user_id = "{user_id}"')
                dice_message = await bot.send_dice(chat_id)
                value = dice_message.dice.value
                if value in [2, 4, 6]:
                   await asyncio.sleep(4)
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"{rloser} | {name1}, Сожалеем, выпало чётное! \nВы проиграли: {c2} {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return
                if value in [1, 3, 5]:
                   await asyncio.sleep(4)
                   c = Decimal(summ * 1.45)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"🎉 | {name1}, Поздравляю, выпало нечётное! \nВы выиграли: {c2} {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 1.45)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
           await bot.send_message(chat_id, f'ℹ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
           return

    if message.text.startswith("чётное"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       name1 = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       summ = int(msg.text.split()[1])
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                cursor.execute(f'UPDATE users SET checking = {1} WHERE user_id = "{user_id}"')
                dice_message = await bot.send_dice(chat_id)
                value = dice_message.dice.value
                if value in [1, 3, 5]:
                   await asyncio.sleep(4)
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"{rloser} | {name1}, Сожалеем, выпало нечётное! \nВы проиграли: {c2} {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return
                if value in [2, 4, 6]:
                   await asyncio.sleep(4)
                   c = Decimal(summ * 1.45)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"🎉 | {name1}, Поздравляю, выпало чётное! \nВы выиграли: {c2} {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 1.45)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
           await bot.send_message(chat_id, f'ℹ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
           return

    if message.text.startswith("нечётное"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       name1 = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       summ = int(msg.text.split()[1])
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                cursor.execute(f'UPDATE users SET checking = {1} WHERE user_id = "{user_id}"')
                dice_message = await bot.send_dice(chat_id)
                value = dice_message.dice.value
                if value in [2, 4, 6]:
                   await asyncio.sleep(4)
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"{rloser} | {name1}, Сожалеем, выпало чётное! \nВы проиграли: {c2} {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return
                if value in [1, 3, 5]:
                   await asyncio.sleep(4)
                   c = Decimal(summ * 1.45)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await message.answer(f"🎉 | {name1}, Поздравляю, выпало нечётное! \nВы выиграли: {c2} {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 1.45)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
           await bot.send_message(chat_id, f'ℹ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
           return



    if message.text.startswith("гонки"):
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car12 = cursor.execute("SELECT car12 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car12 = int(car12[0])
 
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       cart = int(cart[0])

       сars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car12

       msg = message
       summ = int(msg.text.split()[1])
       print(summ)
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       name1 = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       game = cursor.execute("SELECT game from users where user_id = ?",(message.from_user.id,)).fetchone()
       game = int(game[0])
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       stavka = cursor.execute("SELECT stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       stavka = int(stavka[0])
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       coff = random.randint(1,2)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(сars) >= 1:
                   if cart >= 1:
                      await bot.send_message(chat_id, f'🏎 | {name1}, вы успешно подали заявку на участие в гонках!\n⏳ | До начала гонок осталось 5 секунд!', parse_mode='html') 
                      cursor.execute(f'UPDATE users SET stavka = {stavka + summ} WHERE user_id = "{user_id}"') 
                      cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"') 
                      cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                      connect.commit() 
                      await asyncio.sleep(5)   
                      if coff == 1:
                         c = Decimal(stavka * 2)
                         c2 = round(c)
                         c2 = '{:,}'.format(c2)
                         await bot.send_message(chat_id, f'🎉 | {name1}, Вы победили в гонке! Ваш выигрыш: {c2} {rwin}', parse_mode='html')
                         cursor.execute(f'UPDATE users SET balance = {balance - stavka + (stavka * 2)} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET stavka = {stavka - stavka} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET cart = {cart - 20} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                         cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                         cursor.execute(f'UPDATE users SET checking3 = {0} WHERE user_id = "{user_id}"')
                         connect.commit() 
                         return 
                      if coff == 2:
                         c = Decimal(stavka)
                         c2 = round(c)
                         c2 = '{:,}'.format(c2)
                         await bot.send_message(chat_id, f'{rloser} | {name1}, Вы проиграли в гонке! Ваш проигрыш: {c2} {rloser}', parse_mode='html')
                         cursor.execute(f'UPDATE users SET balance = {balance - stavka} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET stavka = {stavka - stavka} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET cart = {cart - 20} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                         cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                         cursor.execute(f'UPDATE users SET checking3 = {0} WHERE user_id = "{user_id}"')
                         connect.commit()
                   if cart == 0:
                      await bot.send_message(chat_id, f'ℹ️ | {name1}, у вас закончилось топливо! {rloser}', parse_mode='html')
                if int(сars) == 0:
                   await bot.send_message(chat_id, f'ℹ️ | {name1}, у вас нету машины! {rloser}', parse_mode='html') 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ️ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
        await bot.send_message(chat_id, f'ℹ️ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
        return
       
    if message.text.startswith("Гонки"):
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car12 = cursor.execute("SELECT car12 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car12 = int(car12[0])

       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       cart = int(cart[0])

       сars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car12

       msg = message
       summ = int(msg.text.split()[1])
       print(summ)
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       name1 = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       game = cursor.execute("SELECT game from users where user_id = ?",(message.from_user.id,)).fetchone()
       game = int(game[0])
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       stavka = cursor.execute("SELECT stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       stavka = int(stavka[0])
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       coff = random.randint(1,2)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(сars) >= 1:
                   if cart >= 1:
                      await bot.send_message(chat_id, f'🏎 | {name1}, вы успешно подали заявку на участие в гонках!\n⏳ | До начала гонок осталось 5 секунд!', parse_mode='html') 
                      cursor.execute(f'UPDATE users SET stavka = {balance - summ + (summ * 2)} WHERE user_id = "{user_id}"')  
                      cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"') 
                      cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                      connect.commit() 
                      await asyncio.sleep(5)   
                      if coff == 1:
                         c = Decimal(summ * 2)
                         c2 = round(c)
                         c2 = '{:,}'.format(c2)
                         await bot.send_message(chat_id, f'🎉 | {name1}, Вы победили в гонке! Ваш выигрыш: {c2} {rwin}', parse_mode='html')
                         cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                         cursor.execute(f'UPDATE users SET stavka = {stavka - stavka} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET cart = {cart - 20} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                         cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                         cursor.execute(f'UPDATE users SET checking3 = {0} WHERE user_id = "{user_id}"')
                         connect.commit() 
                         return 
                      if coff == 2:
                         c = Decimal(summ)
                         c2 = round(c)
                         c2 = '{:,}'.format(c2)
                         await bot.send_message(chat_id, f'{rloser} | {name1}, Вы проиграли в гонке! Ваш проигрыш: {c2} {rloser}', parse_mode='html')
                         cursor.execute(f'UPDATE users SET balance = {balance - stavka} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET stavka = {stavka - stavka} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET cart = {cart - 20} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                         cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                         cursor.execute(f'UPDATE users SET checking3 = {0} WHERE user_id = "{user_id}"')
                         connect.commit()
                   if cart == 0:
                      await bot.send_message(chat_id, f'ℹ️ | {name1}, у вас закончилось топливо! {rloser}', parse_mode='html')
                if int(сars) == 0:
                   await bot.send_message(chat_id, f'ℹ️ | {name1}, у вас нету машины! {rloser}', parse_mode='html') 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ️ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
        await bot.send_message(chat_id, f'ℹ️ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
        return

       
    if message.text.lower() in ["заправка", "Заправка"]:
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       сars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9
       chat_id = message.chat.id
       name1 = message.from_user.get_mention(as_html=True)
       if int(сars) >= 1:
          await bot.send_message(chat_id, f'🧰 | {name1}, курс топлива: 2.000$ за 1% \n🛠 Чтобы заправить машину , введите: Заправить машину', parse_mode='html') 
       if int(сars) == 0:
          await bot.send_message(chat_id, f'ℹ️ | {name1}, у вас нету машины! {rloser}', parse_mode='html') 
            
    if message.text.lower() in ["заправить машину", "Заправить машину"]:
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       cart = int(cart[0])
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       name1 = message.from_user.get_mention(as_html=True)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9
       c = Decimal((100 - cart) * 2000)
       c2 = round(c)
       c2 = '{:,}'.format(c2)
       c3 = 100 - cart
       c4 = (100 - cart) * 2000
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       print(c)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(cars) == 0:
          await bot.send_message(chat_id, f'ℹ | {name1}, у вас нету автомобиля! {rloser}', parse_mode='html') 
          return
       if int(car1) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f'🧰 | {name1}, вы успешно заправили свой автомобиль за {c2}!', parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html') 
          if cart < 100:
             await bot.send_message(chat_id, f'ℹ | {name1}, у вашей машины полный бак! {rloser}', parse_mode='html') 
       if int(car2) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f'🧰 | {name1}, вы успешно заправили свой автомобиль за {c2}!', parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html') 
          if cart < 100:
             await bot.send_message(chat_id, f'ℹ | {name1}, у вашей машины полный бак! {rloser}', parse_mode='html')  
       if int(car3) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f'🧰 | {name1}, вы успешно заправили свой автомобиль за {c2}!', parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html') 
          if cart < 100:
             await bot.send_message(chat_id, f'ℹ | {name1}, у вашей машины полный бак! {rloser}', parse_mode='html') 
       if int(car4) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f'🧰 | {name1}, вы успешно заправили свой автомобиль за {c2}!', parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html') 
          if cart < 100:
             await bot.send_message(chat_id, f'ℹ | {name1}, у вашей машины полный бак! {rloser}', parse_mode='html') 
       if int(car5) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f'🧰 | {name1}, вы успешно заправили свой автомобиль за {c2}!', parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html') 
          if cart < 100:
             await bot.send_message(chat_id, f'ℹ | {name1}, у вашей машины полный бак! {rloser}', parse_mode='html') 
       if int(car6) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f'🧰 | {name1}, вы успешно заправили свой автомобиль за {c2}!', parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html') 
          if cart < 100:
             await bot.send_message(chat_id, f'ℹ | {name1}, у вашей машины полный бак! {rloser}', parse_mode='html') 
       if int(car7) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f'🧰 | {name1}, вы успешно заправили свой автомобиль за {c2}!', parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html') 
          if cart < 100:
             await bot.send_message(chat_id, f'ℹ | {name1}, у вашей машины полный бак! {rloser}', parse_mode='html') 
       if int(car8) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f'🧰 | {name1}, вы успешно заправили свой автомобиль за {c2}!', parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html') 
          if cart < 100:
             await bot.send_message(chat_id, f'ℹ | {name1}, у вашей машины полный бак! {rloser}', parse_mode='html') 
       if int(car9) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f'🧰 | {name1}, вы успешно заправили свой автомобиль за {c2}!', parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html') 
          if cart < 100:
             await bot.send_message(chat_id, f'ℹ | {name1}, у вашей машины полный бак! {rloser}', parse_mode='html') 

    if message.text.startswith("бой"):
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10

       summ = int(msg.text.split()[1])
       print(summ)
       name1 = message.from_user.get_mention(as_html=True)
       period = 5
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       game = cursor.execute("SELECT game from users where user_id = ?",(message.from_user.id,)).fetchone()
       game = int(game[0])
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       rhp = random.randint(10, 20)
       reat = random.randint(10, 20)
       rmood = random.randint(10, 20)
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       coff = random.randint(1,2)
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(pets) >= 1:
                   if pet_hp >= 20:
                      if pet_eat >= 20:
                         if pet_mood >= 20:
                            await bot.send_message(chat_id, f'⚔️ | {name1}, вы успешно подали заявку на участие в сражениях на питомцах!\n⏳ | До начала сражения осталось 5 секунд!', parse_mode='html') 
                            cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"') 
                            cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                            connect.commit() 
                            await asyncio.sleep(5)   
                            if coff == 1:
                               c = Decimal(summ * 2)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1}, ваш питомец победил в сражении! Ваш выигрыш: {c2}\n❤️ | ХП: -{rhp}\n🍗 | Сытость: -{reat}\n☀️ | Настроение: -{rmood}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 2)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_hp = {pet_hp - rhp} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_eat = {pet_eat - reat} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_mood = {pet_mood - rmood} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET checking3 = {0} WHERE user_id = "{user_id}"')
                               connect.commit() 
                               return 
                            if coff == 2:
                               c = Decimal(summ)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'{rloser} | {name1}, ваш питомец проиграл в сражении! Ваш проигрыш: {c2}\n❤️ | ХП: -{rhp}\n🍗 | Сытость: -{reat}\n☀️ | Настроение: -{rmood}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_hp = {pet_hp - rhp} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_eat = {pet_eat - reat} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_mood = {pet_mood - rmood} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET checking3 = {0} WHERE user_id = "{user_id}"')
                               connect.commit()
                         if pet_mood == 0:
                            await bot.send_message(chat_id, f'ℹ️ | {name1}, у вашего питомца нету настроения! {rloser}', parse_mode='html')
                      if pet_eat == 0:
                         await bot.send_message(chat_id, f'ℹ️ | {name1}, ваш питомец голоден! {rloser}', parse_mode='html')
                   if pet_hp == 0:
                      await bot.send_message(chat_id, f'ℹ️ | {name1}, у вашего питомца недостаточно здоровья! {rloser}', parse_mode='html')
                if int(pets) == 0:
                   await bot.send_message(chat_id, f'ℹ️ | {name1}, у вас нету питомца! {rloser}', parse_mode='html') 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ️ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
        await bot.send_message(chat_id, f'ℹ️ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
        return

    if message.text.startswith("Бой"):
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10

       summ = int(msg.text.split()[1])
       print(summ)
       name1 = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       period = 5
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       game = cursor.execute("SELECT game from users where user_id = ?",(message.from_user.id,)).fetchone()
       game = int(game[0])
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       rhp = random.randint(10, 20)
       reat = random.randint(10, 20)
       rmood = random.randint(10, 20)
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       coff = random.randint(1,2)
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(pets) >= 1:
                   if pet_hp >= 20:
                      if pet_eat >= 20:
                         if pet_mood >= 20:
                            await bot.send_message(chat_id, f'⚔️ | {name1}, вы успешно подали заявку на участие в сражениях на питомцах!\n⏳ | До начала сражения осталось 5 секунд!', parse_mode='html') 
                            cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"') 
                            cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                            connect.commit() 
                            await asyncio.sleep(5)   
                            if coff == 1:
                               c = Decimal(summ * 2)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'🎉 | {name1}, ваш питомец победил в сражении! Ваш выигрыш: {c2}\n❤️ | ХП: -{rhp}\n🍗 | Сытость: -{reat}\n☀️ | Настроение: -{rmood}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 2)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_hp = {pet_hp - rhp} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_eat = {pet_eat - reat} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_mood = {pet_mood - rmood} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET checking3 = {0} WHERE user_id = "{user_id}"')
                               connect.commit() 
                               return 
                            if coff == 2:
                               c = Decimal(summ)
                               c2 = round(c)
                               c2 = '{:,}'.format(c2)
                               await bot.send_message(chat_id, f'{rloser} | {name1}, ваш питомец проиграл в сражении! Ваш проигрыш: {c2}\n❤️ | ХП: -{rhp}\n🍗 | Сытость: -{reat}\n☀️ | Настроение: -{rmood}', parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_hp = {pet_hp - rhp} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_eat = {pet_eat - reat} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_mood = {pet_mood - rmood} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET checking3 = {0} WHERE user_id = "{user_id}"')
                               connect.commit()
                         if pet_mood == 0:
                            await bot.send_message(chat_id, f'ℹ️ | {name1}, у вашего питомца нету настроения! {rloser}', parse_mode='html')
                      if pet_eat == 0:
                         await bot.send_message(chat_id, f'ℹ️ | {name1}, ваш питомец голоден! {rloser}', parse_mode='html')
                   if pet_hp == 0:
                      await bot.send_message(chat_id, f'ℹ️ | {name1}, у вашего питомца недостаточно здоровья! {rloser}', parse_mode='html')
                if int(pets) == 0:
                   await bot.send_message(chat_id, f'ℹ️ | {name1}, у вас нету питомца! {rloser}', parse_mode='html') 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'ℹ️ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
        await bot.send_message(chat_id, f'ℹ️ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
        return

    ###########################################МАГАЗИН##########################################
    if message.text.lower() in ["Магаз", "магаз"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🏬', '🏢']
        rwin = random.choice(win)
        await bot.send_message(message.chat.id,
                               f'{user_name}, добро пожаловать в магазин Tiglack{rwin}\n\n🐾 Питомцы - узнать всю информацию про покупки питомцах \n🚘 Автосалон - Узнать всю информацию про покупки Машин , и информацию\n💥 Ивент - Узнать информацию   \n👑 Рейтинга - Узнать информацию про покупки рейтинга , и информацию\n⛽️ Запрвка - Узнать всю информацию про покупки Бензинов , и информацию\n💎 Биткоин - Узнать всю информацию про покупки биткоин , и информацию',
                               parse_mode='html')

###########################################РЕЙТИНГ###########################################
    if message.text.startswith("рейтинг продать"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
        rating = int(rating[0])
        rating2 = '{:,}'.format(summ)
        c = summ * 1000000000000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(balance) >= int(summ * 1000000000000):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы продали {rating2}👑 Рейтинга,  за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET rating = {rating - summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(balance) < int(summ * 1000000000000):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.startswith("Рейтинг продать"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
        rating = int(rating[0])
        rating2 = '{:,}'.format(summ)
        c = summ * 10000000000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(balance) >= int(summ * 1000000000000):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы продали {rating2}👑 Рейтинга,  за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET rating = {rating - summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(balance) < int(summ * 1000000000000):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.startswith("рейтинг купить"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
        rating = int(rating[0])
        rating2 = '{:,}'.format(summ)
        c = summ * 1000000000000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(balance) >= int(summ * 1000000000000):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы купили {rating2}👑 Рейтинга,  за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET rating = {rating + summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(balance) < int(summ * 1000000000000):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.startswith("Рейтинг купить"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
        rating = int(rating[0])
        rating2 = '{:,}'.format(summ)
        c = summ * 10000000000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(balance) >= int(summ * 1000000000000):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы купили {rating2}👑 Рейтинга,  за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET rating = {rating + summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(balance) < int(summ * 1000000000000):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.lower() in ["рейтинг", "Рейтинг"]:
        chat_id = message.chat.id
        user_name = message.from_user.get_mention(as_html=True)
        name1 = message.from_user.full_name
        user_id = message.from_user.id
        rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
        rating = int(rating[0])
        rating2 = '{:,}'.format(rating)
        price = 1000000000000
        price2 = '{:,}'.format(price)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот информация про Рейтинг 👑\n\n👤 Владелец: {name1}\n👑 Рейтинг : {rating}👑\n💡 Цена 1 Рейтинга 👑: {price2}$\n\nℹ Команды:\n1️⃣ Рейтинг купить [Количество] - Для покупки Рейтинга 👑\n2️⃣ Рейтинг продать [Количество] - для продажи Рейтинга 👑',
                               parse_mode='html')


 ###########################################КРИПТО###########################################
    if message.text.startswith("Биткоин продать"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        cripto = cursor.execute("SELECT cripto from users where user_id = ?", (message.from_user.id,)).fetchone()
        cripto = int(cripto[0])
        cripto2 = '{:,}'.format(summ)
        c = summ * 150000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(balance) >= int(summ * 150000):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы продали {cripto2}💾 за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cripto = {cripto - summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(balance) < int(summ * 150000):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.startswith("биткоин продать"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        cripto = cursor.execute("SELECT cripto from users where user_id = ?", (message.from_user.id,)).fetchone()
        cripto = int(cripto[0])
        cripto2 = '{:,}'.format(summ)
        c = summ * 150000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(balance) >= int(summ * 150000):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы продали {cripto2}💾 за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cripto = {cripto - summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(balance) < int(summ * 150000):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.startswith("Биткоин купить"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        cripto = cursor.execute("SELECT cripto from users where user_id = ?", (message.from_user.id,)).fetchone()
        cripto = int(cripto[0])
        cripto2 = '{:,}'.format(summ)
        c = summ * 150000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(balance) >= int(summ * 150000):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы купили {cripto2}💾 за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cripto = {cripto + summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(balance) < int(summ * 150000):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.startswith("биткоин купить"):
        msg = message
        user_id = msg.from_user.id
        user_name = message.from_user.get_mention(as_html=True)
        summ = int(msg.text.split()[2])
        chat_id = message.chat.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        cripto = cursor.execute("SELECT cripto from users where user_id = ?", (message.from_user.id,)).fetchone()
        cripto = int(cripto[0])
        cripto2 = '{:,}'.format(summ)
        c = summ * 150000
        c2 = '{:,}'.format(c)
        if summ > 0:
            if int(balance) >= int(summ * 150000):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы купили {cripto2}💾 за {c2}$! {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cripto = {cripto + summ} WHERE user_id = "{user_id}"')
                connect.commit()

            if int(balance) < int(summ * 150000):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')
        if summ <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.lower() in ["Крипто", "крипто"]:
        chat_id = message.chat.id
        user_name = message.from_user.get_mention(as_html=True)
        name1 = message.from_user.full_name
        user_id = message.from_user.id
        cripto = cursor.execute("SELECT cripto from users where user_id = ?", (message.from_user.id,)).fetchone()
        cripto = int(cripto[0])
        cripto2 = '{:,}'.format(cripto)
        price = 150000
        price2 = '{:,}'.format(price)
        await bot.send_message(message.chat.id,
                               f'{user_name},Вот информация про Крипто-Валюту💾\n\n👤 Владелец: {name1}\n💾 Крипто-Валюта: {cripto2}шт\n💡 Цена 1 Крипто-Валюты💾: {price2}$\n\nℹ Команды:\n1️⃣ Крипто купить [Количество] - Для покупки Крипто-Валюты\n2️⃣ Крипто продать [Количество] - для продажи Крипто-Валюты',
                               parse_mode='html')

###########################################БЕСЕДА#########################################
    if message.text.lower() in ["беседа", "Беседа"]:
       user_name = message.from_user.get_mention(as_html=True)
       await bot.send_message(message.chat.id, f"💎 | {user_name}, официальная беседа бота TIGLACK:\n@bacarty_444", parse_mode='html')

###########################################ЭКОНОМИКА###########################################
    # perevod        
    if message.text.startswith("дать"):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       rname =  msg.reply_to_message.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply_user_id = msg.reply_to_message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       perevod = int(msg.text.split()[1])
       perevod2 = '{:,}'.format(perevod)
       print(f"{name} перевел: {perevod} игроку {rname}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))

       if not message.reply_to_message:
          await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
          return
       
       if reply_user_id == user_id:
          await message.reply_to_message.reply(f'ℹ | Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
          return

       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       if perevod > 0:
          if balance >= perevod:  
             await message.reply_to_message.reply(f'💸 | Вы дали {perevod2}$ игроку {reply_user_name} {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
             connect.commit()    
   
          elif int(balance) <= int(perevod):
             await message.reply( f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if perevod <= 0:
          await message.reply( f'ℹ | {user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("Дать"):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       rname =  msg.reply_to_message.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply_user_id = msg.reply_to_message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       perevod = int(msg.text.split()[1])
       perevod2 = '{:,}'.format(perevod)
       print(f"{name} перевел: {perevod} игроку {rname}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))

       if not message.reply_to_message:
          await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
          return
       
       if reply_user_id == user_id:
          await message.reply_to_message.reply(f'ℹ | Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
          return

       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       if perevod > 0:
          if balance >= perevod:  
             await message.reply_to_message.reply(f'💸 | Вы отдали {perevod2}$ игроку {reply_user_name} {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
             connect.commit()    
   
          elif int(balance) <= int(perevod):
             await message.reply( f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if perevod <= 0:
          await message.reply( f'ℹ️ | {user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')  
    # bank
    if message.text.startswith("Банк положить"):
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)

       bank_p = int(msg.text.split()[2])
       print(f"{name} положил в банк: {bank_p}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_p)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       if bank_p > 0:
          if balance >= bank_p:  
             await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно положили в банк {bank2}$ {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - bank_p} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bank = {bank + bank_p} WHERE user_id = "{user_id}"') 
             connect.commit()    
   
          elif int(balance) < int(bank_p):
             await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if bank_p <= 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, нельзя положить в банк отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("Банк снять"):
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)

       bank_s = int(msg.text.split()[2])
       print(f"{name} снял с банка: {bank_s}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_s)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       if bank_s > 0:
          if bank >= bank_s:  
             await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно сняли с банковского счёта {bank2}$ {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET bank = {bank - bank_s} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance + bank_s} WHERE user_id = "{user_id}"') 
             connect.commit()    
   
          elif int(bank) < int(bank_s):
             await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств на банковском счету! {rloser}', parse_mode='html')

       if bank_s <= 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, нельзя снять с банка отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("банк положить"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       name = msg.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)

       bank_p = int(msg.text.split()[2])
       print(f"{name} положил в банк: {bank_p}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_p)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       if bank_p > 0:
          if balance >= bank_p:  
             await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно положили в банк {bank2}$ {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - bank_p} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bank = {bank + bank_p} WHERE user_id = "{user_id}"') 
             connect.commit()    
   
          elif int(balance) < int(bank_p):
             await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if bank_p <= 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, нельзя положить в банк отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("банк снять"):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)

       bank_s = int(msg.text.split()[2])
       print(f"{name} снял с банка: {bank_s}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_s)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       if bank_s > 0:
          if bank >= bank_s:  
             await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно сняли с банковского счёта {bank2}$ {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET bank = {bank - bank_s} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance + bank_s} WHERE user_id = "{user_id}"') 
             connect.commit()    
   
          elif int(bank) < int(bank_s):
             await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств на банковском счету! {rloser}', parse_mode='html')

       if bank_s <= 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, нельзя снять с банка отрицательное число! {rloser}', parse_mode='html')  

    if message.text.lower() in ["Биткоин курс", "биткоин курс"]:
       user_name = message.from_user.get_mention(as_html=True)
       chat_id = message.chat.id
       period = 30
       curs = cursor.execute("SELECT curs FROM bot").fetchall()
       curs = int(curs[0][0])
       get = cursor.execute("SELECT last_curs FROM bot").fetchall()
       last_curs = f"{get[0][0]}"
       curstime = time.time() - float(last_curs)
       new_curs = random.randint(1, 2)
       curs_bonus = random.randint(100, 500)
       four = 50000 
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if curstime > period: 
          if new_curs == 1:
             cursor.execute(f'UPDATE bot SET curs = {curs - curs_bonus}')
             cursor.execute(f'UPDATE bot SET last_curs = ?', (time.time(),)) 
             await bot.send_message(message.chat.id, f"{user_name}, на данный момент курс 1 BTC составляет - {curs}$", parse_mode='html') 
          if new_curs == 2:
             cursor.execute(f'UPDATE bot SET curs = {curs + curs_bonus}')
             cursor.execute(f'UPDATE bot SET last_curs = ?', (time.time(),)) 
             await bot.send_message(message.chat.id, f"{user_name}, на данный момент курс 1 BTC составляет - {curs}$", parse_mode='html')     
       else:
          await bot.send_message(message.chat.id, f"{user_name}, на данный момент курс 1 BTC составляет - {curs}$", parse_mode='html')

    if message.text.startswith("биткоин купить"):
       user_name = message.from_user.get_mention(as_html=True)
       curs = cursor.execute("SELECT curs FROM bot").fetchall()
       print(curs[0])
       curs2 = int(curs[0][0])
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       user_name = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[2])
       summ2 ='{:,}'.format(summ)
       print(summ2)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?", (message.from_user.id,)).fetchone()
       bitcoin = int(bitcoin[0])
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       c = summ * curs2
       c2 ='{:,}'.format(c)
       print(c2)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if summ > 0:
          if balance >= c:
             await bot.send_message(message.chat.id, f'{user_name}, вы успешно купили {summ2} BTC за {c2}$! {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"')
             connect.commit()
          else:
             await bot.send_message(message.chat.id, f'{user_name}, недостачно средств! {rloser}', parse_mode='html')
       if summ <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("биткоин продать"):
       user_name = message.from_user.get_mention(as_html=True)
       curs = cursor.execute("SELECT curs FROM bot").fetchall()
       curs2 = int(curs[0][0])
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[2])
       summ2 = '{:,}'.format(summ)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?", (message.from_user.id,)).fetchone()
       bitcoin = int(bitcoin[0])
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       c = summ * curs2
       c2 ='{:,}'.format(c)
       print(c2)
       print(summ2)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if summ > 0:
          if bitcoin >= summ:
             await bot.send_message(message.chat.id, f'{user_name}, вы успешно продали {summ2} BTC за {c2}$! {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin - summ} WHERE user_id = "{user_id}"')
             connect.commit()
          else:
             await bot.send_message(message.chat.id, f'{user_name}, недостачно BTC! {rloser}', parse_mode='html')
       if summ <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя продать отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("Биткоин купить"):
       user_name = message.from_user.get_mention(as_html=True)
       curs = cursor.execute("SELECT curs FROM bot").fetchall()
       print(curs[0])
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       curs2 = int(curs[0][0])
       user_name = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[2])
       summ2 ='{:,}'.format(summ)
       print(summ2)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?", (message.from_user.id,)).fetchone()
       bitcoin = int(bitcoin[0])
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       c = summ * curs2
       c2 ='{:,}'.format(c)
       print(c2)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if summ > 0:
          if balance >= c:
             await bot.send_message(message.chat.id, f'{user_name}, вы успешно купили {summ2} BTC за {c2}$! {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"')
             connect.commit()
          else:
             await bot.send_message(message.chat.id, f'{user_name}, недостачно средств! {rloser}', parse_mode='html')
       if summ <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("Биткоин продать"):
       user_name = message.from_user.get_mention(as_html=True)
       curs = cursor.execute("SELECT curs FROM bot").fetchall()
       curs2 = int(curs[0][0])
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[2])
       summ2 = '{:,}'.format(summ)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?", (message.from_user.id,)).fetchone()
       bitcoin = int(bitcoin[0])
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       c = summ * curs2
       c2 ='{:,}'.format(c)
       print(c2)
       print(summ2)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if summ > 0:
          if bitcoin >= summ:
             await bot.send_message(message.chat.id, f'{user_name}, вы успешно продали {summ2} BTC за {c2}$! {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin - summ} WHERE user_id = "{user_id}"')
             connect.commit()
          else:
             await bot.send_message(message.chat.id, f'{user_name}, недостачно BTC! {rloser}', parse_mode='html')
       if summ <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя продать отрицательное число! {rloser}', parse_mode='html')

###########################################АВТОМОБИЛИ###########################################
    if message.text.lower() in ["автосалон", "Автосалон"]:
       user_name = message.from_user.get_mention(as_html=True)
       chat_id = message.chat.id
       await bot.send_message(message.chat.id, f"{user_name}, доступные машины:\n🚗 1. ВАЗ 2107 - 5.000.000.000$\n🚗 2. Lada Vesta - 50.000.000.000$\n🚗 3. Lada XRAY Cross - 100.000.000.000$\n🚗 4. Audi Q7 - 500.000.000.000$\n🚗 5. BMW X6 - 750.000.000.000$\n🚗 6. Hyundai Solaris - 1.000.000.000.000$\n🚗 7. Toyota Supra - 1.500.000.000.000$\n🚗 8. Lamborghini Veneno - 3.000.000.000.000$\n🚗 9. Bugatti Veyron - 10.000.000.000.000$ \n\n🛒 Для покупки машины введите: Купить машину [номер]\nℹ Для просмотра информации о машине введите: Машина [номер] инфо", parse_mode='html')

    if message.text.lower() in ["купить машину 1", "Купить машину 1"]: 
       user_name = message.from_user.get_mention(as_html=True)
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 5000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car1 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🚗 | {user_name}, вы успешно купили ВАЗ 2107 за 5.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car1 = {car1 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')     
                return
          if car1 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный автомобиль! {rloser}', parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть автомобиль! {rloser}', parse_mode='html')  

    if message.text.lower() in ["купить машину 2", "Купить машину 2"]: 
       user_name = message.from_user.get_mention(as_html=True)
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 50000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car2 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🚗 | {user_name}, вы успешно купили Lada Vesta за 50.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car2 = {car2 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')     
                return
          if car2 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный автомобиль! {rloser}', parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть автомобиль! {rloser}', parse_mode='html')   

    if message.text.lower() in ["купить машину 3", "Купить машину 3"]: 
       user_name = message.from_user.get_mention(as_html=True)
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 100000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car3 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🚗 | {user_name}, вы успешно купили Lada XRAY Cross за 100.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car3 = {car3 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')     
                return
          if car3 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный автомобиль! {rloser}', parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть автомобиль! {rloser}', parse_mode='html')            

    if message.text.lower() in ["купить машину 4", "Купить машину 4"]: 
       user_name = message.from_user.get_mention(as_html=True)
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 500000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car4 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🚗 | {user_name}, вы успешно купили Audi Q7 за 500.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car4 = {car4 + c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"')  
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')     
                return
          if car4 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный автомобиль! {rloser}', parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть автомобиль! {rloser}', parse_mode='html')

    if message.text.lower() in ["купить машину 5", "Купить машину 5"]: 
       user_name = message.from_user.get_mention(as_html=True)
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 750000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car5 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🚗 | {user_name}, вы успешно купили BMW X6 за 750.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car5 = {car5 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')     
                return
          if car5 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный автомобиль! {rloser}', parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть автомобиль! {rloser}', parse_mode='html')              

    if message.text.lower() in ["купить машину 6", "Купить машину 6"]: 
       user_name = message.from_user.get_mention(as_html=True)
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1000000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car6 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🚗 | {user_name}, вы успешно купили Hyundai Solaris за 1.000.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car6 = {car6 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')     
                return
          if car6 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный автомобиль! {rloser}', parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть автомобиль! {rloser}', parse_mode='html')

    if message.text.lower() in ["купить машину 7", "Купить машину 7"]: 
       user_name = message.from_user.get_mention(as_html=True)
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1500000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car7 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🚗 | {user_name}, вы успешно купили Toyota Supra за 1.500.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car7 = {car7 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')     
                return
          if car7 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный автомобиль! {rloser}', parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть автомобиль! {rloser}', parse_mode='html')

    if message.text.lower() in ["купить машину 8", "Купить машину 8"]: 
       user_name = message.from_user.get_mention(as_html=True)
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 3000000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car8 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🚗 | {user_name}, вы успешно купили Lamborghini Veneno за 3.000.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car8 = {car8 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')     
                return
          if car8 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный автомобиль! {rloser}', parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть автомобиль! {rloser}', parse_mode='html')    

    if message.text.lower() in ["купить машину 9", "Купить машину 9"]: 
       user_name = message.from_user.get_mention(as_html=True)
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 10000000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car9 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🚗 | {user_name}, вы успешно купили Bugatti Veyron за 10.000.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car9 = {car9 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')     
                return
          if car9 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный автомобиль! {rloser}', parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть автомобиль! {rloser}', parse_mode='html')    

    if message.text.lower() in ["купить машину hentai", "Купить машину hentai"]:    
       user_name = message.from_user.get_mention(as_html=True)
       chat_id = message.chat.id
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       if car10 == 0:
          if int(balance) >= int(summ):
             await bot.send_message(message.chat.id, f'🚗{user_name}, вы успешно купили Hentai Solaris за 1$', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET car10 = {car10 + c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          else:
             await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')
             return
       if car10 == 1:
          await bot.send_message(message.chat.id, f'{user_name}, у вас уже есть данный автомобиль! {rloser}', parse_mode='html')     
          return
 
    if message.text.lower() in ["купить машину supra", "Купить машину Supra"]: 
       chat_id = message.chat.id  
       user_name = message.from_user.get_mention(as_html=True)
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       if car11 == 0:
          if int(balance) >= int(summ):
             await bot.send_message(message.chat.id, f'🚗{user_name}, вы успешно купили Supra Legend за 1$', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET car11 = {car11 + c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          else:
             await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')
             return
       if car11 == 1:
          await bot.send_message(message.chat.id, f'{user_name}, у вас уже есть данный автомобиль! {rloser}', parse_mode='html')     
          return

    if message.text.lower() in ["мой гараж", "Мой гараж"]:  
       user_name = message.from_user.get_mention(as_html=True)
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       car12 = cursor.execute("SELECT car12 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car12 = int(car12[0])

       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       cart = int(cart[0])
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10 + car11 + car12
       carb = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9

       c = int(car10) + int(car11) + int(car12)
       print(c)
       if car1 == 1:
          m = f"ВАЗ 2107 - 🔋 Топливо: {cart}%\n"
       if car2 == 1:
          m = f"Lada Vesta - 🔋 Топливо: {cart}%\n"
       if car3 == 1:
          m = f"Lada XRAY Cross - 🔋 Топливо: {cart}%\n"
       if car4 == 1:
          m = f"Audi Q7 - 🔋 Топливо: {cart}%\n"
       if car5 == 1:
          m = f"BMW X6 - 🔋 Топливо: {cart}%\n"
       if car6 == 1:
          m = f"Hyundai Solaris - 🔋 Топливо: {cart}%\n"
       if car7 == 1:
          m = f"Toyota Supra - 🔋 Топливо: {cart}%\n"
       if car8 == 1:
          m = f"Lamborghini Veneno - 🔋 Топливо: {cart}%\n"
       if car9 == 1:
          m = f"Bugatti Veyron - 🔋 Топливо: {cart}%\n\n"
       if carb == 0:
          m = f""


       if c >= 1:
          s = "\n💈 VIP Автомобили:\n"
       if c == 0:
          s = ""

       if car10 == 1:
          m1 = "  🏎 Hentai Solaris\n"
       if car10 == 0:
          m1 = ""
       if car11 == 1:
          m2 = "  🏎 Supra Legend\n"
       if car11 == 0:
          m2 = ""
       if car12 == 1:
          m3 = "  🚐 Сани Деда Мороза\n"
       if car12 == 0:
          m3 = ""
       if cars == 0:
          await bot.send_message(message.chat.id, f'🧰 | {user_name}, у вас нету машины', parse_mode='html')
       if cars >= 1:
          await bot.send_message(message.chat.id, f'🧰 | {user_name}, ваша машина: {m}{s}{m1}{m2}{m3}', parse_mode='html')

    if message.text.lower() in ["машина 1 инфо", "Машина 1 инфо"]:  
       user_name = message.from_user.get_mention(as_html=True)
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       if car1 == 1:
          m1 = "Данный автомобиль имеется у вас в гараже!\n"
       if car1 == 0:
          m1 = ""
       photo = open('car1.jpg', 'rb')
       await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'{user_name}, информация о машине ВАЗ 2107\n⛽️ | Макс.Скорость - 152 км/ч\n🐎 | Лошадиных сил - 140 л.с\n🛢 | Объем топливного бака - 39л\n{m1}', parse_mode='html')
  
    if message.text.lower() in ["машина 2 инфо", "Машина 2 инфо"]:
       user_name = message.from_user.get_mention(as_html=True)
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       if car2 == 1:
          m1 = "Данный автомобиль имеется у вас в гараже!\n"
       if car2 == 0:
          m1 = ""
       photo = open('car2.jpg', 'rb')
       await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'{user_name}, информация о машине Lada Vesta\n⛽️ | Макс.Скорость - 175 км/ч\n🐎 | Лошадиных сил - 106 л.с\n🛢 | Объем топливного бака - 55л\n{m1}', parse_mode='html')

    if message.text.lower() in ["машина 3 инфо", "Машина 3 инфо"]:
       user_name = message.from_user.get_mention(as_html=True)
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       if car3 == 1:
          m1 = "Данный автомобиль имеется у вас в гараже!\n"
       if car3 == 0:
          m1 = ""
       photo = open('car3.jpg', 'rb')
       await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'{user_name}, информация о машине Lada XRAY Cross\n⛽️ | Макс.Скорость - 162 км/ч\n🐎 | Лошадиных сил - 122 л.с\n🛢 | Объем топливного бака - 50л\n{m1}', parse_mode='html')

    if message.text.lower() in ["машина 4 инфо", "Машина 4 инфо"]: 
       user_name = message.from_user.get_mention(as_html=True)
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       if car4 == 1:
          m1 = "Данный автомобиль имеется у вас в гараже!\n"
       if car4 == 0:
          m1 = ""
       photo = open('car4.jpg', 'rb')
       await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'{user_name}, информация о машине Audi Q7\n⛽️ | Макс.Скорость - 225 км/ч\n🐎 | Лошадиных сил - 249 л.с\n🛢 | Объем топливного бака - 70л\n{m1}', parse_mode='html')

    if message.text.lower() in ["машина 5 инфо", "Машина 5 инфо"]:
       user_name = message.from_user.get_mention(as_html=True)
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       if car5 == 1:
          m1 = "Данный автомобиль имеется у вас в гараже!\n"
       if car5 == 0:
          m1 = ""
       photo = open('car5.jpg', 'rb')
       await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'{user_name}, информация о машине BMW X6\n⛽️ | Макс.Скорость - 250 км/ч\n🐎 | Лошадиных сил - 400 л.с\n🛢 | Объем топливного бака - 85л\n{m1}', parse_mode='html')

    if message.text.lower() in ["машина 6 инфо", "Машина 6 инфо"]:
       user_name = message.from_user.get_mention(as_html=True)
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       if car6 == 1:
          m1 = "Данный автомобиль имеется у вас в гараже!\n"
       if car6 == 0:
          m1 = ""
       photo = open('car6.jpg', 'rb')
       await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'{user_name}, информация о машине Hyundai Solaris\n⛽️ | Макс.Скорость - 185 км/ч\n🐎 | Лошадиных сил - 100 л.с\n🛢 | Объем топливного бака - 50л\n{m1}', parse_mode='html')
   
    if message.text.lower() in ["машина 7 инфо", "Машина 7 инфо"]:
       user_name = message.from_user.get_mention(as_html=True)
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       if car7 == 1:
          m1 = "Данный автомобиль имеется у вас в гараже!\n"
       if car7 == 0:
          m1 = ""
       photo = open('car7.jpg', 'rb')
       await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'{user_name}, информация о машине Toyota Supra\n⛽️ | Макс.Скорость - 250 км/ч\n🐎 | Лошадиных сил - 340 л.с\n🛢 | Объем топливного бака - 50л\n{m1}', parse_mode='html')

    if message.text.lower() in ["машина 8 инфо", "Машина 8 инфо"]:
       user_name = message.from_user.get_mention(as_html=True)      
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       if car8 == 1:
          m1 = "Данный автомобиль имеется у вас в гараже!\n"
       if car8 == 0:
          m1 = ""
       photo = open('car8.jpg', 'rb')
       await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'{user_name}, информация о машине Lamborghini Veneno\n⛽️ | Макс.Скорость - 357 км/ч\n🐎 | Лошадиных сил - 750 л.с\n🛢 |Объем топливного бака - 90л\n{m1}', parse_mode='html')

    if message.text.lower() in ["машина 9 инфо", "Машина 9 инфо"]:
       user_name = message.from_user.get_mention(as_html=True)
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       if car9 == 1:
          m1 = "Данный автомобиль имеется у вас в гараже!\n"
       if car9 == 0:
          m1 = ""
       photo = open('car9.jpg', 'rb')
       await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'{user_name}, информация о машине Bugatti Veyron\n⛽️ | Макс.Скорость - 407 км/ч\n🐎 | Лошадиных сил - 1001 л.с\n🛢 | Объем топливного бака - 100л\n{m1}', parse_mode='html')

    if message.text.lower() in ["машина 10 инфо", "Машина 10 инфо"]:
       user_name = message.from_user.get_mention(as_html=True)
       car12 = cursor.execute("SELECT car12 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car12 = int(car12[0])
       if car12 == 1:
          m1 = "Данный автомобиль имеется у вас в гараже!\n"
       if car12 == 0:
          m1 = ""
       photo = open('car12.png', 'rb')
       await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'{user_name}, информация о машине Сани Деда Мороза\n⛽️ | Макс.Скорость - 9999 км/ч\n🐎 | Лошадиных сил - 9999 л.с\n🛢 | Объем топливного бака - 9999л\n{m1}', parse_mode='html')

    if message.text.lower() in ["продать машину", "Продать машину"]:
       user_name = message.from_user.get_mention(as_html=True)
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       cart = int(cart[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9
       c = 1
       if cars == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету машины! {rloser}', parse_mode='html')
       if car1 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали свою машину за 3.750.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 3750000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car1 = {car1 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
       if car2 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали свою машину за 37.500.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 37500000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car2 = {car2 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
       if car3 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали свою машину за 75.000.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 75000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car3 = {car3 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
       if car4 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали свою машину за 375.000.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 375000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car4 = {car4 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
       if car5 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали свою машину за 562.500.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 562500000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car5 = {car5 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
       if car6 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали свою машину за 750.000.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 750000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car6 = {car6 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
       if car7 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали свою машину за 1.125.000.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 1125000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car7 = {car7 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
       if car8 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали свою машину за 2.250.000.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 2250000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car8 = {car8 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
       if car9 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали свою машину за 7.500.000.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 7500000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car9 = {car9 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"')
       if car12 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали свою машину за 22.000.000.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 22000000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car12 = {car12 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"')

###########################################АДМИН КОМАНДЫ###########################################
    if message.text.startswith("выдать"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f'💰 | Вы выдали {perevod2}$ игроку {reply_user_name} {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f'ℹ️ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')  

    if message.text.startswith("Выдать"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f'💰 | Вы выдали {perevod2}$ игроку {reply_user_name} {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f'ℹ️ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')  

    if message.text.startswith("забрать"):
       msg = message
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       user_name = message.from_user.get_mention(as_html=True)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f'💰 | Вы забрали {perevod2}$ у игрока {reply_user_name} {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f'ℹ️ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')  

    if message.text.startswith("Забрать"):
       msg = message
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       user_name = message.from_user.get_mention(as_html=True)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f'💰 | Вы забрали {perevod2}$ у игрока {reply_user_name} {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f'ℹ️ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')  

    if message.text.startswith("выдать"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Owner':
          await message.reply(f'💰 | Вы выдали {perevod2}$ игроку {reply_user_name} {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f'ℹ️ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')  

    if message.text.startswith("Выдать"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Owner':
          await message.reply(f'💰 | Вы выдали {perevod2}$ игроку {reply_user_name} {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f'ℹ️ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')  

    if message.text.startswith("забрать"):
       msg = message
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       user_name = message.from_user.get_mention(as_html=True)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Owner':
          await message.reply(f'💰 | Вы забрали {perevod2}$ у игрока {reply_user_name} {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f'ℹ️ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')  

    if message.text.startswith("Забрать"):
       msg = message
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       user_name = message.from_user.get_mention(as_html=True)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Owner':
          await message.reply(f'💰 | Вы забрали {perevod2}$ у игрока {reply_user_name} {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f'ℹ️ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')  

    if message.text.lower() in ["обнулить", "Обнулить"]:
       msg = message
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status[0] == 'Admin':
          await message.reply(f'💰 | Вы обнулили игрока {reply_user_name} {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bitcoin = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET expe = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car1 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car2 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car3 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car4 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car5 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car6 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car7 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car8 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car9 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car10 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car11 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet1 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet2 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet3 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet4 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet5 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet6 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet7 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet8 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet9 = {0} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f'ℹ️ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')

    if message.text.lower() in ["забанить", "Забанить"]:
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Blocked"
       if user_status2[0] == "Admin":
          await message.reply(f'🛑 | Вы забанили игрока: {reply_user_name}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bitcoin = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET expe = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car1 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car2 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car3 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car4 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car5 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car6 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car7 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car8 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car9 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car10 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car11 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet1 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet2 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet3 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet4 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet5 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet6 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet7 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet8 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet9 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f'ℹ️ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')
       
    if message.text.lower() in ["разбанить", "Разбанить"]:
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status = "Player"
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status2[0] == "Admin":
          await message.reply(f'✅ | Вы разбанили игрока: {reply_user_name}', parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f'ℹ️ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')
       
    if message.text.lower() in ["забанить", "Забанить"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Blocked"
       if user_status2[0] == "vip":
          await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == "Owner":
          await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')

    if message.text.lower() in ["назначить адм", "Назначить адм"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Admin"
       if user_status2[0] == "Owner":
          await message.reply(f"🛑 | Вы выдали админа бота игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()  
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       if user_status2[0] == 'Admin':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
    
    if message.text.lower() in ["разжаловать", "Разжаловать"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Player"
       if user_status2[0] == "Owner":
          await message.reply(f"🛑 | Вы забрали админа бота у игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == "vip":
          await message.reply(f"🛑 | Вы забрали админа бота у игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       if user_status2[0] == 'Admin':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       
    if message.text.lower() in ["разбанить", "Разбанить"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status = "Player"
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status2[0] == "Admin":
          await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == "vip":
          await message.reply(f"🛑 | Вы забрали админа бота у игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()  
       if user_status2[0] == "Owner":
          await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')

######################################РП КОМАНДЫ#################################################
    if message.text.lower() in ["рп-команды", "РП-команды"]:
       user_name = message.from_user.get_mention(as_html=True)
       await bot.send_message(message.chat.id, f"{user_name}, список РП-команд:\n🤗 | Обнять\n👏 | Похлопать\n👨‍💻 | Заскамить\n☕️ | Пригласить на чай\n👉👌 | Изнасиловать\n🤝 | Взять за руку\n📱 | Подарить айфон\n✋ | Дать пять\n😬 | Укусить\n🤛 | Ударить\n🤲 | Прижать\n💋 | Чмок\n💋 | Поцеловать\n😼 | Кусь\n🤲 | Прижать\n🔪 | Убить\n🤜 | Уебать\n💰 | Украсть\n🔞 | Выебать\n👅 | Отсосать\n👅 | Отлизать\n🔞 | Трахнуть\n🔥 | Сжечь", parse_mode='html')

    if message.text.lower() in ["чмок", "Чмок"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💋 | {user_name} чмокнул(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["кусь", "Кусь"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"😼 | {user_name} кусьнул(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["обнять", "Обнять"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤗 | {user_name} обнял(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["поцеловать", "Поцеловать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💋 | {user_name} поцеловал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["дать пять", "Дать пять"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"✋ | {user_name} дал(-а) пять {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["подарить айфон", "Подарить айфон"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"📱 | {user_name} подарил(-а) айфон {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["ударить", "Ударить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤛 | {user_name} ударил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["заскамить", "Заскамить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👨‍💻 | {user_name} заскамил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["прижать", "Прижать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤲 | {user_name} прижал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["укусить", "Укусить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"😬 | {user_name} укусил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["взять за руку", "Взять за руку"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤝 | {user_name} взял(-а) за руку {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["прижать", "Прижать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤲 | {user_name} прижал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["похлопать", "Похлопать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👏 | {user_name} похлопал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["изнасиловать", "Изнасиловать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👉👌 | {user_name} изнасиловал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["пригласить на чай", "Пригласить на чай"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"☕️ | {user_name} пригласил(-а) на чай {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["убить", "Убить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔪 | {user_name} убил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["уебать", "Уебать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤜 | {user_name} уебал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["украсть", "Украсть"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💰 | {user_name} украл(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["отсосать", "Отсосать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👅 | {user_name} отсосал(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["отлизать", "Отлизать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👅 | {user_name} отлизал(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["выебать", "Выебать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔞 | {user_name} выебал(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["сжечь", "Сжечь"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔥 | {user_name} сжёг {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["трахнуть", "Трахнуть"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔞 | {user_name} трахнул(-а) {reply_user_name}", parse_mode='html')

######################################ПИТОМЦЫ#################################################
    if message.text.lower() in ["питомцы", "Питомцы"]:
       user_name = message.from_user.get_mention(as_html=True)
       chat_id = message.chat.id
       await bot.send_message(message.chat.id, f"{user_name}, доступные питомцы:\n🐮 1.Корова  - 1.000.000.000.000$\n🐑 2. Овца - 10.000.000.000.000$\n🐕 3.Робопес - 50.000.000.000.000$\n🦅 4. Орёл - 100.000.000.000.000$\n🐅 5. Тигр - 500.000.000.000.000$\n🦁 6. Лев - 1.000.000.000.000.000$\n🐈‍⬛ 7. Черная пантера - 1.500.000.000.000.000$\n🦚 8.Павлин  - 2.000.000.000.000.000$\n🐊 9. Кракодил - 4.000.000.000.000.000$\n\n🛒 Для покупки питомца введите: Купить питомца [номер]\nℹ Для просмотра информации о своем питомце введите: Мой питомец", parse_mode='html')

    if message.text.lower() in ["купить питомца 1", "Купить питомца 1"]:    
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1000000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       print(pets)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet1 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🐄 | {user_name}, вы успешно купили Корова за 1.000.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet1 = {pet1 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                return
          if pet1 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html')     

    if message.text.lower() in ["купить питомца 2", "Купить питомца 2"]:    
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 10000000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       print(pets)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet2 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🐑 | {user_name}, вы успешно купили овца за 10.000.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet2 = {pet2 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                return
          if pet2 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html')     

    if message.text.lower() in ["купить питомца 3", "Купить питомца 3"]:    
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 50000000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       print(pets)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet3 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🐕 | {user_name}, вы успешно купили Робопес за 50.000.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet3 = {pet3 + c} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                return
          if pet3 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html') 

    if message.text.lower() in ["купить питомца 4", "Купить питомца 4"]:    
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 100000000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       print(pets)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet4 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🦅 | {user_name}, вы успешно купили Орла за 100.000.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet4 = {pet4 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                return
          if pet4 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html') 

    if message.text.lower() in ["купить питомца 5", "Купить питомца 5"]:    
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 500000000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       print(pets)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet5 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🐯 | {user_name}, вы успешно купили Тигр за 500.000.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet5 = {pet5 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                return
          if pet5 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html')  

    if message.text.lower() in ["купить питомца 6", "Купить питомца 6"]:    
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1000000000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       print(pets)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet6 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🦁 | {user_name}, вы успешно купили лев за 1.000.000.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet6 = {pet6 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                return
          if pet6 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html')                        

    if message.text.lower() in ["купить питомца 7", "Купить питомца 7"]:    
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1500000000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       print(pets)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet7 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🐆 | {user_name}, вы успешно купили черная пантера за 1.500.000.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet7 = {pet7 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                return
          if pet7 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html') 

    if message.text.lower() in ["купить питомца 8", "Купить питомца 8"]:    
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 20000000000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       print(pets)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet8 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'🦚 | {user_name}, вы успешно купили павлина за 2.000.000.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet8 = {pet8 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                return
          if pet8 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html') 

    if message.text.lower() in ["купить питомца 9", "Купить питомца 9"]:    
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 4000000000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       print(pets)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet9 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы успешно купили T-rex за 4.000.000.000.000.000$ 🎉', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet9 = {pet9 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                return
          if pet9 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f'ℹ️ |{user_name}, у вас уже есть питомец! {rloser}', parse_mode='html') 

    if message.text.lower() in ["мой питомец", "Мой питомец"]:        
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10
       if pets == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')    
       if pet1 == 1:
          photo = open('pet1.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'🐹 | {user_name}, ваш питомец: Корова \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')            
       if pet2 == 1:     
          photo = open('pet2.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'🐈 | {user_name}, ваш питомец: Овца \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                    
       if pet3 == 1:   
          photo = open('pet3.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'ℹ️ | {user_name}, ваш питомец: Робопес \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                            
       if pet4 == 1:           
          photo = open('pet4.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'ℹ️ | {user_name}, ваш питомец: Орел \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                            
       if pet5 == 1:
          photo = open('pet5.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'ℹ️ | {user_name}, ваш питомец: Тигр \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                                       
       if pet6 == 1:
          photo = open('pet6.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'ℹ️ | {user_name}, ваш питомец: Лев\n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                                       
       if pet7 == 1:
          photo = open('pet7.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'ℹ️ | {user_name}, ваш питомец: Черная пантера \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                                       
       if pet8 == 1:
          photo = open('pet8.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'ℹ️ | {user_name}, ваш питомец: Павлин \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                                       
       if pet9 == 1: 
          photo = open('pet9.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'ℹ️ | {user_name}, ваш питомец: Кракодил \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                                      
       if pet10 == 1:
          photo = open('pet10.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'ℹ️ | {user_name}, ваш питомец: снеговик \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                                       

    if message.text.lower() in ["вылечить питомца", "Вылечить питомца"]:  
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10
       c = Decimal((100 - pet_hp) * 1000000000000)
       c2 = (100 - pet_hp) * 1000000000000
       hp = 100 - pet_hp
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if pets == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')  
       if pet1 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
       if pet2 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
       if pet3 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
       if pet4 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
       if pet5 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
       if pet6 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
       if pet7 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
       if pet8 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
       if pet9 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')

       if pet10 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')

    if message.text.lower() in ["покормить питомца", "Покормить питомца"]:  
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10
       c = Decimal((100 - pet_eat) * 1000000000000)
       c2 = (100 - pet_eat) * 1000000000000
       eat = 100 - pet_eat
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if pets == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')  
       if pet1 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден! {rloser}', parse_mode='html')
       if pet2 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')
       if pet3 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')
       if pet4 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')
       if pet5 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден! {rloser}', parse_mode='html')
       if pet6 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')
       if pet7 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')
       if pet8 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')
       if pet9 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')

       if pet10 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')

    if message.text.lower() in ["выгулять питомца", "Выгулять питомца"]:  
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10
       c = Decimal((100 - pet_mood) * 10000)
       mood = 100 - pet_mood
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if pets == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')  
       if pet1 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
       if pet2 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
       if pet3 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
       if pet4 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
       if pet5 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
       if pet6 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
       if pet7 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
       if pet8 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
       if pet9 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')

       if pet10 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')

    if message.text.startswith("питомец имя"): 
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       name = str(message.text.split()[2])
       if pets == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')
       if pet1 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet2 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet3 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet4 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet5 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet6 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet7 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet8 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet9 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')

    if message.text.startswith("Питомец имя"): 
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       name = str(message.text.split()[2])
       if pets == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')
       if pet1 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet2 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet3 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet4 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet5 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet6 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet7 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet8 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet9 == 1:
         await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
         cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')

    if message.text.lower() in ["продать питомца", "Продать питомца"]:
       user_name = message.from_user.get_mention(as_html=True)
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       if pets == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')
       if pet1 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 750.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 500000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet1 = {pet1 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet2 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 75.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 7500000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet2 = {pet2 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet3 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 375.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 37500000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet3 = {pet3 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet4 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 750.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 75000000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet4 = {pet4 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet5 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 37.500.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 375000000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet5 = {pet5 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet6 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 75.000.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 750000000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet6 = {pet6 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"')
       if pet7 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 375.000.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet7 = {pet7 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet8 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 7.500.000.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 1500000000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet8 = {pet8 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"')
       if pet9 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 75.000.000.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 2000000000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet9 = {pet9 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet10 == 1:
          await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 22.000.000.000.000$', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 22000000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet10 = {pet10 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 

######################################РАБОТА#################################################
    if message.text.lower() in ["работать", "Работать"]:
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       chat_id = message.chat.id
       user_id = message.from_user.id
       user_name = message.from_user.get_mention(as_html=True)
       args = message.get_args()
       x = random.randint(1000000000000,5000000000000)
       work = random.randint(1,10)
       period = 3600
       get = cursor.execute("SELECT last_work FROM users WHERE user_id=?", (user_id,)).fetchall()
       last_work = f"{int(get[0][0])}"
       worktime = time.time() - float(last_work)
       x2 = '{:,}'.format(x)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       if worktime > period:
          if work == 1:
             await bot.send_message(chat_id, f"🧹 | {user_name}, ты поработал дворником и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit()   
          if work == 2:
             await bot.send_message(chat_id, f"🛎 | {user_name}, ты поработал оффициантом и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 3:
             await bot.send_message(chat_id, f"💻 | {user_name}, ты написал сайт и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 4:
             await bot.send_message(chat_id, f"📦 | {user_name}, ты поработал курьером и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 5:
             await bot.send_message(chat_id, f"🍯 | {user_name}, ты продал бабушкины заготовки и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 6:
             await bot.send_message(chat_id, f"🍎 | {user_name}, ты поработал продавцом и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 7:
             await bot.send_message(chat_id, f"🍕 | {user_name}, ты поработал доставщиком пиццы и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 8:
             await bot.send_message(chat_id, f"🔦 | {user_name}, ты поработал охранником и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 9:
             await bot.send_message(chat_id, f"🙏 | {user_name}, ты попрошайничал у людей и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
       else:
          await bot.send_message(message.chat.id, f"ℹ️ | {user_name}, вы уже работали недавно, приходите через час! {rloser}", parse_mode='html')

###########################################КЕЙСЫ###########################################
    if message.text.lower() in ["кейсы", "Кейсы"]:
       user_name = message.from_user.get_mention(as_html=True)
       case1 = cursor.execute("SELECT case1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case2 = cursor.execute("SELECT case2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case3 = cursor.execute("SELECT case3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case4 = cursor.execute("SELECT case4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case1 = int(case1[0])
       case2 = int(case2[0])
       case3 = int(case3[0])
       case4 = int(case4[0])
       c = int(case1) + int(case2) + int(case3) + int(case4)
       c = int(c)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       if c == 0:
          m = "😕 | У вас нету кейсов.\n"
          m1 = "🛒 | Для покупки кейсы введите «купить кейс [номер] [сумма]»"
       if c >= 1:
          m = "🧾 | Ваши кейсы:\n"
          m1 = "🔐 | Для открытия кейсов используйте - «Кейс открыть [1/2/3]»"
       if case1 == 0:
          s1 = ""
       if case1 >= 1:
          s1 = f"   📦 Обычный кейс - {case1}шт.\n"
       if case2 == 0:
          s2 = ""
       if case2 >= 1:
          s2 = f"   🏵 Золотой кейс - {case2}шт.\n"
       if case3 == 0:
          s3 = ""
       if case3 >= 1:
          s3 = f"   💎 Алмазный кейс - {case3}шт.\n"
       if ivent == 1:
          if case4 == 0:
             s4 = ""
          if case4 >= 1:
             s4 = f"   ❄️ Снежный кейс - {case4}шт.\n"
       print(s1)
       print(s2)
       print(s3)
       if ivent == 0:
          await bot.send_message(message.chat.id, f'{user_name}, доступные кейсы:\n🎁 1. Обычный кейс - 50 млрд.\n🎁 2. Золотой кейс - 1 трлн.\n🎁 3. Алмазный кейс - 5 трлн.\n\n{m}{s1}{s2}{s3}{m1}', parse_mode='html')
       if ivent == 1:
          await bot.send_message(message.chat.id, f'{user_name}, доступные кейсы:\n🎁 1. Обычный кейс - 50 млрд.\n🎁 2. Золотой кейс - 1 трлн.\n🎁 3. Алмазный кейс - 5 трлн.\n🎁 4. Снежный кейс - 2 трлн.\n\n{m}{s1}{s2}{s3}{s4}{m1}', parse_mode='html')

    if message.text.startswith("кdhsdgj 1"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       case1 = cursor.execute("SELECT case1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case1 = int(case1[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 50000000000 * summ
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if summ >= 1:
          if balance >= c:
             await bot.send_message(message.chat.id, f'🎁 | {user_name}, вы успешно купили {summ} обычных кейсов за {c}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case1 = {case1 + summ} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          if balance < c:
             await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
             return
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("кfjsd 2"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       case2 = cursor.execute("SELECT case2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case2 = int(case2[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 1000000000000 * summ
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if summ >= 1:
          if balance >= c:
             await bot.send_message(message.chat.id, f'🎁 | {user_name}, вы успешно купили {summ} золотых кейсов за {c}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case2 = {case2 + summ} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          if balance < c:
             await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
             return
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("кdhfiushl 3"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       case3 = cursor.execute("SELECT case3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case3 = int(case3[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 5000000000000 * summ
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if summ >= 1:
          if balance >= c:
             await bot.send_message(message.chat.id, f'🎁 | {user_name}, вы успешно купили {summ} алмазных кейсов за {c}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case3 = {case3 + summ} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          if balance < c:
             await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
             return
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("кdystf 4"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       case4 = cursor.execute("SELECT case4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case4 = int(case4[0])
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 2000000000000 * summ
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if ivent == 1:
          if summ >= 1:
             if balance >= c:
                await bot.send_message(message.chat.id, f'🎁 | {user_name}, вы успешно купили {summ} снежных кейсов за {c}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET case4 = {case4 + summ} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             if balance < c:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                return
          if summ <= 0:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался! {rloser}', parse_mode='html')

    if message.text.startswith("Кdfgks 1"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       case1 = cursor.execute("SELECT case1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case1 = int(case1[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 50000000000 * summ
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if summ >= 1:
          if balance >= c:
             await bot.send_message(message.chat.id, f'🎁 | {user_name}, вы успешно купили {summ} обычных кейсов за {c}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case1 = {case1 + summ} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          if balance < c:
             await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
             return
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("Кsdhfouihf 2"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       case2 = cursor.execute("SELECT case2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case2 = int(case2[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 1000000000000 * summ
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if summ >= 1:
          if balance >= c:
             await bot.send_message(message.chat.id, f'🎁 | {user_name}, вы успешно купили {summ} золотых кейсов за {c}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case2 = {case2 + summ} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          if balance < c:
             await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
             return
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("Кsgfiousgf 3"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       case3 = cursor.execute("SELECT case3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case3 = int(case3[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 5000000000000 * summ
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if summ >= 1:
          if balance >= c:
             await bot.send_message(message.chat.id, f'🎁 | {user_name}, вы успешно купили {summ} алмазных кейсов за {c}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case3 = {case3 + summ} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          if balance < c:
             await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
             return
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("Кdsifytg 4"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       case4 = cursor.execute("SELECT case4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case4 = int(case4[0])
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 2000000000000 * summ
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if ivent == 1:
          if summ >= 1:
             if balance >= c:
                await bot.send_message(message.chat.id, f'🎁 | {user_name}, вы успешно купили {summ} снежных кейсов за {c}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET case4 = {case4 + summ} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             if balance < c:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                return
          if summ <= 0:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен! {rloser}', parse_mode='html')

    if message.text.lower() in ["открыть кейс 1", "Открыть кейс 1"]:
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       case1 = cursor.execute("SELECT case1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case1 = int(case1[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       money = ('44000000000', '45000000000', '46000000000', '47000000000', '48000000000', '49000000000', '50000000000', '51000000000', '52000000000', '53000000000', '54000000000', '55000000000')
       rmoney = random.choice(money)
       rmoney2 = '{:,}'.format(rmoney)
       rrating = random.randint(100, 400)
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       prize = random.randint(1, 2)
       if case1 >= 1:
          if prize == 1:
             await bot.send_message(message.chat.id, f'💰 | {user_name}, вам выпало {rmoney2}$! {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + rmoney} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case1 = {case1 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()   
          if prize == 2:
             await bot.send_message(message.chat.id, f'👑 | {user_name}, вам выпало {rrating} рейтинга! {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET rating = {rating + rrating} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case1 = {case1 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()   
       if case1 <= 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету данного кейса! {rloser}', parse_mode='html')

    if message.text.lower() in ["открыть кейс 2", "Открыть кейс 2"]:
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       case2 = cursor.execute("SELECT case2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case2 = int(case2[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       money = ('950000000000', '960000000000', '970000000000', '980000000000', '990000000000', '1000000000000', '1010000000000', '1020000000000', '1030000000000', '1040000000000', '1050000000000', '1060000000000', '1070000000000', '1080000000000', '1090000000000', '1100000000000')
       rmoney = random.choice(money)
       rmoney2 = '{:,}'.format(rmoney)
       rrating = random.randint(5000, 6000)
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       prize = random.randint(1, 2)
       if case2 >= 1:
          if prize == 1:
             await bot.send_message(message.chat.id, f'💰 | {user_name}, вам выпало {rmoney2}$! {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + rmoney} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case2 = {case2 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()   
          if prize == 2:
             await bot.send_message(message.chat.id, f'👑 | {user_name}, вам выпало {rrating} рейтинга! {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET rating = {rating + rrating} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case2 = {case2 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()   
       if case2 <= 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету данного кейса! {rloser}', parse_mode='html')

    if message.text.lower() in ["открыть кейс 3", "Открыть кейс 3"]:
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       case3 = cursor.execute("SELECT case3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case3 = int(case3[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       money = ('4950000000000', '4960000000000', '4970000000000', '4980000000000', '4990000000000', '5000000000000', '50100000000000', '50200000000000', '503000000000000', '5040000000000', '50500000000000', '50600000000000', '50700000000000', '50800000000000', '50900000000000', '51000000000000')
       rmoney = random.choice(money)
       rmoney2 = '{:,}'.format(rmoney)
       rrating = random.randint(25000, 30000)
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       prize = random.randint(1, 2)
       if case3 >= 1:
          if prize == 1:
             await bot.send_message(message.chat.id, f'💰 | {user_name}, вам выпало {rmoney2}$! {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + rmoney} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case3 = {case3 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()   
          if prize == 2:
             await bot.send_message(message.chat.id, f'👑 | {user_name}, вам выпало {rrating} рейтинга! {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET rating = {rating + rrating} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case3 = {case3 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()   
       if case3 <= 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету данного кейса! {rloser}', parse_mode='html')

    if message.text.lower() in ["открыть кейс 4", "Открыть кейс 4"]:
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       case4 = cursor.execute("SELECT case4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case4 = int(case4[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       money = ('1950000000', '1960000000000', '1970000000000', '1980000000000', '1990000000000', '2000000000000', '2010000000000', '2020000000000', '2030000000000', '2040000000000', '2050000000000', '2060000000000', '2070000000000', '2080000000000', '2090000000000', '2100000000000')
       rmoney = random.choice(money)
       rrating = random.randint(1500, 2500)
       rmoney2 = '{:,}'.format(rmoney)
       rsnow = random.randint(1, 5)
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       prize = random.randint(1, 3)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       snow = cursor.execute("SELECT snow from users where user_id = ?",(message.from_user.id,)).fetchone()
       snow = int(snow[0])
       if ivent == 1:
          if case4 >= 1:
             if prize == 1:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, вам выпало {rmoney2}$! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + rmoney} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET case4 = {case4 - 1} WHERE user_id = "{user_id}"') 
                connect.commit()   
             if prize == 2:
                await bot.send_message(message.chat.id, f'👑 | {user_name}, вам выпало {rrating} рейтинга! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + rrating} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET case4 = {case4 - 1} WHERE user_id = "{user_id}"')
                connect.commit()    
             if prize == 3:
                await bot.send_message(message.chat.id, f'❄️ | {user_name}, вам выпало {rrating} снежинок! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET snow = {snow + rsnow} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET case4 = {case4 - 1} WHERE user_id = "{user_id}"') 
                connect.commit()   
          if case4 <= 0:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету данного кейса! {rloser}', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен! {rloser}', parse_mode='html')

######################################НОВОГОДНИЙ ИВЕНТ#################################################
    if message.text.lower() in ["Вес5465на", "1111111"]:
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       snow = cursor.execute("SELECT snow from users where user_id = ?",(message.from_user.id,)).fetchone()
       snow = int(snow[0])
       if ivent == 1:
          await bot.send_message(message.chat.id, f'☃️"ивент"☃️\n\n❄ Кол-во листочек: {snow}\n\n🌟 Награды:\n1. 💰 5.000.000.000.000$ - 10❄️\n2. 👑 20.000 рейтинга - 25❄️\n3. 🚐 Эксклюзивный автомобиль "Сани Деда Диора" - 50❄️\n4. ☃️ Эксклюзивный питомец "Снеговик" - 100❄️\n5. 🎆 Особый статус "New Year 2022" - 500❄️\n\nℹ️ Снежинки можно заработать открывая "Новогодние кейсы".\n📦 В кейсах можно заработать: от 1 до 5 снежинок.\n❄️ Заходя каждый день в игру вы будете получать по 2 снежинки.\nℹ️ Чтобы забрать желаемую награду введите: ивент забрать [номер].\n\n📆 Ивент продлится до: 22.01.22', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен! {rloser}', parse_mode='html')
   
    if message.text.lower() in ["ивент забрать 1", "Ивент забрать 1"]:
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       snow = cursor.execute("SELECT snow from users where user_id = ?",(message.from_user.id,)).fetchone()
       snow = int(snow[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 10
       if ivent == 1:
          if snow >= 10:
             await bot.send_message(message.chat.id, f'❄️ | {user_name}, вы обменяли свои снежинки на 5.000.000.000.000$! {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET snow = {snow - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance + 5000000000000} WHERE user_id = "{user_id}"') 
             connect.commit()   
          if snow < 10:
             await bot.send_message(message.chat.id, f'❄️ | {user_name}, недостаточно снежинок! {rloser}', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен! {rloser}', parse_mode='html')

    if message.text.lower() in ["ивент забрать 2", "Ивент забрать 2"]:
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       snow = cursor.execute("SELECT snow from users where user_id = ?",(message.from_user.id,)).fetchone()
       snow = int(snow[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = round(int(rating[0]))
       summ = 25
       if ivent == 1:
          if snow >= 25:
             await bot.send_message(message.chat.id, f'❄️ | {user_name}, вы обменяли свои снежинки на 25.000👑! {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET snow = {snow - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET rating = {rating + 25000} WHERE user_id = "{user_id}"') 
             connect.commit()   
          if snow < 25:
             await bot.send_message(message.chat.id, f'❄️ | {user_name}, недостаточно снежинок! {rloser}', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен! {rloser}', parse_mode='html')

    if message.text.lower() in ["ивент забрать 3", "Ивент забрать 3"]:
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       snow = cursor.execute("SELECT snow from users where user_id = ?",(message.from_user.id,)).fetchone()
       snow = int(snow[0])
       car12 = cursor.execute("SELECT car12 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car12 = round(int(car12[0]))
       summ = 50
       if ivent == 1:
          if snow >= 50:
             if car12 == 0:
                await bot.send_message(message.chat.id, f'❄️ | {user_name}, вы обменяли свои снежинки на автомобиль "Сани Деда Мороза"! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET snow = {snow - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car12 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()   
             if car12 == 1:
                await bot.send_message(message.chat.id, f'❄️ | {user_name}, вы уже забрали данную награду! {rloser}', parse_mode='html')
          if snow < 50:
             await bot.send_message(message.chat.id, f'❄️ | {user_name}, недостаточно снежинок! {rloser}', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен! {rloser}', parse_mode='html')

    if message.text.lower() in ["ивент забрать 4", "Ивент забрать 4"]:
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       snow = cursor.execute("SELECT snow from users where user_id = ?",(message.from_user.id,)).fetchone()
       snow = int(snow[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = round(int(pet10[0]))
       summ = 100
       if ivent == 1:
          if snow >= 100:
             if pet10 == 0:
                await bot.send_message(message.chat.id, f'❄️ | {user_name}, вы обменяли свои снежинки на питомца "Снеговик"! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET snow = {snow - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet10 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()   
             if pet10 == 1:
                await bot.send_message(message.chat.id, f'❄️ | {user_name}, вы уже забрали данную награду! {rloser}', parse_mode='html')
          if snow < 100:
             await bot.send_message(message.chat.id, f'❄️ | {user_name}, недостаточно снежинок! {rloser}', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен! {rloser}', parse_mode='html')

    if message.text.lower() in ["ивент забрать 5", "Ивент забрать 5"]:
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       snow = cursor.execute("SELECT snow from users where user_id = ?",(message.from_user.id,)).fetchone()
       snow = int(snow[0])
       status = cursor.execute("SELECT status from users where user_id = ?",(message.from_user.id,)).fetchone()
       status = str(status[0])
       stat = "New Year 2022"
       summ = 500
       if ivent == 1:
          if snow >= 500:
             if status == "Игрок":
                await bot.send_message(message.chat.id, f'❄️ | {user_name}, вы обменяли свои снежинки на статус "New Year 2022"! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET snow = {snow - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET status = \"{stat}\" WHERE user_id = "{user_id}"') 
                connect.commit()   
             if status == "New Year 2022":
                await bot.send_message(message.chat.id, f'❄️ | {user_name}, вы уже забрали данную награду! {rloser}', parse_mode='html')
          if snow < 500:
             await bot.send_message(message.chat.id, f'❄️ | {user_name}, недостаточно снежинок! {rloser}', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен! {rloser}', parse_mode='html')

    if message.text.lower() in ["начать ивент", "Начать ивент"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status[0] == "Admin":
          await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно включили новогодний ивент! {rwin}', parse_mode='html')
          cursor.execute(f"UPDATE bot SET ivent = {1}")
          connect.commit()   
       if user_status[0] == "Player":
          await bot.send_message(message.chat.id, f'ℹ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')

    if message.text.lower() in ["закончить ивент", "Закончить ивент"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status[0] == "Admin":
          await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно отключили новогодний ивент! {rwin}', parse_mode='html')
          cursor.execute(f"UPDATE bot SET ivent = {0}")
          connect.commit()   
       if user_status[0] == "Player":
          await bot.send_message(message.chat.id, f'ℹ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')
  
    if message.text.lower() in ["новогодний подарок", "Новогодний подарок"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       suprise = cursor.execute("SELECT suprise from users where user_id = ?",(message.from_user.id,)).fetchone()
       suprise = int(suprise[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if ivent == 1:
          if suprise == 0:
             await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно забрали новогодний подарок!\n🎁 Получено: 22.000.000.000.000$ {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 22000000000000} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET suprise = {1}  WHERE user_id = "{user_id}"') 
             connect.commit()   
          if suprise == 1:
             await bot.send_message(message.chat.id, f'ℹ | {user_name}, вы уже получали новогодний подарок!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["промо #tigbot", "Промо #tigbot"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo1 = cursor.execute("SELECT promo1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo1 = int(promo1[0])
       promo1_b = cursor.execute("SELECT promo1 from bot").fetchone()
       promo1_b = int(promo1_b[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if ivent == 1:
          if promo1 == 0:
             if promo1_b <= 999:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000.000.000.000$! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 10000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo1 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo1 = {promo1_b + 1}")
                connect.commit()
             if promo1_b == 1000:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo1 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["Промо #rozig", "промо #rozik"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo2 = cursor.execute("SELECT promo2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo2 = int(promo2[0])
       promo2_b = cursor.execute("SELECT promo2 from bot").fetchone()
       promo2_b = int(promo2_b[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if ivent == 1:
          if promo2 == 0:
             if promo2_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000.000.000.000$! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo2 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo2 = {promo2_b + 1}")
                connect.commit()
             if promo2_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo2 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["промо #1к", "Промо #1к"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo3 = cursor.execute("SELECT promo3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo3 = int(promo3[0])
       promo3_b = cursor.execute("SELECT promo3 from bot").fetchone()
       promo3_b = int(promo3_b[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if ivent == 1:
          if promo3 == 0:
             if promo3_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 10.000.000.000.000$! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 10000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo3 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo3 = {promo3_b + 1}")
                connect.commit()
             if promo3_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo3 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #monпаррy", "Promo #moапрапрney"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo4 = cursor.execute("SELECT promo4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo4 = int(promo4[0])
       promo4_b = cursor.execute("SELECT promo4 from bot").fetchone()
       promo4_b = int(promo4_b[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if ivent == 1:
          if promo4 == 0:
             if promo4_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000.000.000.000$! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo4 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo4 = {promo4_b + 1}")
                connect.commit()
             if promo4_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo4 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #snoпраw", "Promo #snарпow"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo5 = cursor.execute("SELECT promo5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo5 = int(promo5[0])
       promo5_b = cursor.execute("SELECT promo5 from bot").fetchone()
       promo5_b = int(promo5_b[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if ivent == 1:
          if promo5 == 0:
             if promo5_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000.000.000.000$! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo5 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo5 = {promo5_b + 1}")
                connect.commit()
             if promo5_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo5 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #saпаерапko", "Promo #sпрапiko"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo6 = cursor.execute("SELECT promo6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo6 = int(promo6[0])
       promo6_b = cursor.execute("SELECT promo6 from bot").fetchone()
       promo6_b = int(promo6_b[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if ivent == 1:
          if promo6 == 0:
             if promo6_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000.000.000.000$! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo6 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo6 = {promo6_b + 1}")
                connect.commit()
             if promo6_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo6 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #vaапраst", "Promo #vaпраst"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo7 = cursor.execute("SELECT promo7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo7 = int(promo7[0])
       promo7_b = cursor.execute("SELECT promo7 from bot").fetchone()
       promo7_b = int(promo7_b[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if ivent == 1:
          if promo7 == 0:
             if promo7_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000.000.000.000$! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo7 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo7 = {promo7_b + 1}")
                connect.commit()
             if promo7_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo7 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #vasапрbot", "Promo #vastпарапbot"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo8 = cursor.execute("SELECT promo8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo8 = int(promo8[0])
       promo8_b = cursor.execute("SELECT promo8 from bot").fetchone()
       promo8_b = int(promo8_b[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if ivent == 1:
          if promo8 == 0:
             if promo8_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000.000.000.000$! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo8 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo8 = {promo8_b + 1}")
                connect.commit()
             if promo8_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo8 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #casiапрno", "Promo #caпрапsino"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo9 = cursor.execute("SELECT promo9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo9 = int(promo9[0])
       promo9_b = cursor.execute("SELECT promo9 from bot").fetchone()
       promo9_b = int(promo9_b[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if ivent == 1:
          if promo9 == 0:
             if promo9_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000.000.000.000$! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo9 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo9 = {promo9_b + 1}")
                connect.commit()
             if promo9_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo9 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #newbапрпаot", "Promo #neрпарwbot"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo10 = cursor.execute("SELECT promo10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo10 = int(promo10[0])
       promo10_b = cursor.execute("SELECT promo10 from bot").fetchone()
       promo10_b = int(promo10_b[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if ivent == 1:
          if promo10 == 0:
             if promo10_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000.000.000.000$! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo10 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo10 = {promo10_b + 1}")
                connect.commit()
             if promo10_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo10 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')
  
    if message.text.lower() in ["promo #soпараft", "Promo #sпаапft"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo11 = cursor.execute("SELECT promo11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo11 = int(promo11[0])
       promo11_b = cursor.execute("SELECT promo11 from bot").fetchone()
       promo11_b = int(promo11_b[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if ivent == 1:
          if promo11 == 0:
             if promo11_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000.000.000.000$! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo11 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo11 = {promo11_b + 1}")
                connect.commit()
             if promo11_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo11 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #happапраy2022", "Promo #hapрапрy2022"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo12 = cursor.execute("SELECT promo12 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo12 = int(promo12[0])
       promo12_b = cursor.execute("SELECT promo12 from bot").fetchone()
       promo12_b = int(promo12_b[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if ivent == 1:
          if promo12 == 0:
             if promo12_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000.000.000.000$! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo12 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo12 = {promo12_b + 1}")
                connect.commit()
             if promo12_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo12 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #ratапрing", "Promo #ratапрапing"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo13 = cursor.execute("SELECT promo13 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo13 = int(promo13[0])
       promo13_b = cursor.execute("SELECT promo13 from bot").fetchone()
       promo13_b = int(promo13_b[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if ivent == 1:
          if promo13 == 0:
             if promo13_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000👑! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + 1000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo13 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo13 = {promo13_b + 1}")
                connect.commit()
             if promo13_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo13 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #tапраop", "Promo #tапрop"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo14 = cursor.execute("SELECT promo14 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo14 = int(promo14[0])
       promo14_b = cursor.execute("SELECT promo14 from bot").fetchone()
       promo14_b = int(promo14_b[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if ivent == 1:
          if promo14 == 0:
             if promo14_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000👑! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + 1000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo14 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo14 = {promo14_b + 1}")
                connect.commit()
             if promo14_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo14 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #xzапраshka", "Promo #xzрапраshka"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo15 = cursor.execute("SELECT promo15 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo15 = int(promo15[0])
       promo15_b = cursor.execute("SELECT promo15 from bot").fetchone()
       promo15_b = int(promo15_b[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if ivent == 1:
          if promo15 == 0:
             if promo15_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000👑! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + 1000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo15 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo15 = {promo15_b + 1}")
                connect.commit()
             if promo15_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo15 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #skroапарmnik", "Promo #skromапраnik"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo16 = cursor.execute("SELECT promo16 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo16 = int(promo16[0])
       promo16_b = cursor.execute("SELECT promo16 from bot").fetchone()
       promo16_b = int(promo16_b[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if ivent == 1:
          if promo16 == 0:
             if promo16_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000👑! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + 1000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo16 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo16 = {promo16_b + 1}")
                connect.commit()
             if promo16_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo16 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #anаапрime", "Promo #animпарапe"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo17 = cursor.execute("SELECT promo17 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo17 = int(promo17[0])
       promo17_b = cursor.execute("SELECT promo17 from bot").fetchone()
       promo17_b = int(promo17_b[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if ivent == 1:
          if promo17 == 0:
             if promo17_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000👑! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + 1000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo17 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo17 = {promo17_b + 1}")
                connect.commit()
             if promo17_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo17 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #adапрmin", "Promo #admапрапin"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo18 = cursor.execute("SELECT promo18 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo18 = int(promo18[0])
       promo18_b = cursor.execute("SELECT promo18 from bot").fetchone()
       promo18_b = int(promo18_b[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if ivent == 1:
          if promo18 == 0:
             if promo18_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000👑! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + 1000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo18 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo18 = {promo18_b + 1}")
                connect.commit()
             if promo18_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo18 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #teleапрgram", "Promo #teleаприаgram"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo19 = cursor.execute("SELECT promo19 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo19 = int(promo19[0])
       promo19_b = cursor.execute("SELECT promo19 from bot").fetchone()
       promo19_b = int(promo19_b[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if ivent == 1:
          if promo19 == 0:
             if promo19_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000👑! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + 1000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo19 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo19 = {promo19_b + 1}")
                connect.commit()
             if promo19_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo19 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #10апр00", "Promo #10рап00"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo20 = cursor.execute("SELECT promo20 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo20 = int(promo20[0])
       promo20_b = cursor.execute("SELECT promo20 from bot").fetchone()
       promo20_b = int(promo20_b[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if ivent == 1:
          if promo20 == 0:
             if promo20_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000👑! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + 1000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo20 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo20 = {promo20_b + 1}")
                connect.commit()
             if promo20_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo20 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #updапрate", "Promo #updaапрte"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo21 = cursor.execute("SELECT promo21 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo21 = int(promo21[0])
       promo21_b = cursor.execute("SELECT promo21 from bot").fetchone()
       promo21_b = int(promo21_b[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if ivent == 1:
          if promo21 == 0:
             if promo21_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000👑! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + 1000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo21 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo21 = {promo21_b + 1}")
                connect.commit()
             if promo21_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo21 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #yearапр2022", "Promo #yearпара2022"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo22 = cursor.execute("SELECT promo22 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo22 = int(promo22[0])
       promo22_b = cursor.execute("SELECT promo22 from bot").fetchone()
       promo22_b = int(promo22_b[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if ivent == 1:
          if promo22 == 0:
             if promo22_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000👑! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + 1000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo22 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo22 = {promo22_b + 1}")
                connect.commit()
             if promo22_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo22 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #resапраart", "Promo #restпараart"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo23 = cursor.execute("SELECT promo23 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo23 = int(promo23[0])
       promo23_b = cursor.execute("SELECT promo23 from bot").fetchone()
       promo23_b = int(promo23_b[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if ivent == 1:
          if promo23 == 0:
             if promo23_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000👑! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + 1000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo23 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo23 = {promo23_b + 1}")
                connect.commit()
             if promo23_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo23 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

    if message.text.lower() in ["promo #lucрпарy", "Promo #lucпрарky"]:
       user_name = message.from_user.get_mention(as_html=True)
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       promo24 = cursor.execute("SELECT promo24 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo24 = int(promo24[0])
       promo24_b = cursor.execute("SELECT promo24 from bot").fetchone()
       promo24_b = int(promo24_b[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if ivent == 1:
          if promo24 == 0:
             if promo24_b <= 19:
                await bot.send_message(message.chat.id, f'❄ | {user_name}, вы успешно активировали промокод на 1.000👑! {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + 1000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET promo24 = {1}  WHERE user_id = "{user_id}"') 
                cursor.execute(f"UPDATE bot SET promo24 = {promo24_b + 1}")
                connect.commit()
             if promo24_b == 20:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, промокод уже не действителен!', parse_mode='html')
          if promo24 == 1:
             await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, вы уже использовали этот промокод!', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, новогодний ивент еще не начался или уже закончен!', parse_mode='html')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
