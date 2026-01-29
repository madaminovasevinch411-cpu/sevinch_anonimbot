from aiogram import Bot, Dispatcher, executor, types
import logging

API_TOKEN = 7949219655:AAGZXzdpIQAJGitzJWbf5EjVnR23UILvgBw

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

users = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    args = message.get_args()
    if args:
        users[message.from_user.id] = int(args)
        await message.answer("✉️ Xabaringizni yozing, u anonim yuboriladi.")
    else:
        link = f"https://t.me/sevinch_anonimbot?start={message.from_user.id}"
        await message.answer(
            "Salom 👋\n\n"
            "Bu bot orqali sizga anonim xabar yuborish mumkin.\n\n"
            f"📩 Sizning shaxsiy linkingiz:\n{link}\n\n"
            "Linkni bio yoki story’ga joylang."
        )

@dp.message_handler()
async def send_anon(message: types.Message):
    if message.from_user.id in users:
        target = users[message.from_user.id]
        await bot.send_message(
            target,
            f"📩 Sizga yangi anonim xabar:\n\n{message.text}"
        )
        await message.answer("✅ Xabar anonim yuborildi.")
        users.pop(message.from_user.id)
    else:
        await message.answer("❗ Xabar yuborish uchun shaxsiy link orqali kiring.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
