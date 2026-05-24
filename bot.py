"""
Эндокринный эквалайзер — Telegram Bot
======================================
Зависимости: pip install python-telegram-bot==20.7

Запуск:
  1. Установи зависимости: pip install python-telegram-bot==20.7
  2. Получи токен у @BotFather в Telegram
  3. Замени BOT_TOKEN на свой токен
  4. Размести index.html на хостинге с HTTPS (см. README.md)
  5. Замени WEBAPP_URL на свой URL
  6. Запусти: python bot.py
"""

import logging
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup, MenuButtonWebApp
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ─── НАСТРОЙКИ ────────────────────────────────────────────────
BOT_TOKEN  = "ВСТАВЬ_ТОКЕН_ОТ_BOTFATHER_СЮДА"
WEBAPP_URL = "https://ВАШ_САЙТ/index.html"   # URL где лежит index.html
# ──────────────────────────────────────────────────────────────

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton(
            text="Открыть эквалайзер",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]]
    await update.message.reply_text(
        "Эндокринный эквалайзер v3.0\n\n"
        "30 параметров: гормоны, клетки крови, лейкоцитарная формула.\n"
        "Интерактивная модель взаимодействия по Верину & Иванову.\n\n"
        "Нажми кнопку ниже:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Команды:\n"
        "/start — открыть эквалайзер\n"
        "/help  — это сообщение\n\n"
        "Перемещай ползунки — система покажет каскадные эффекты.\n"
        "Пресеты: СТРЕСС, ГИПОТИРЕОЗ, СПКЯ, МЕНОПАУЗА, МЕТ.СИНДРОМ, "
        "АКРОМЕГАЛИЯ, АНЕМИЯ, ИНФЕКЦИЯ, АЛЛЕРГИЯ, ЛЕЙКОЗ, ТРОМБОЦИТОПЕНИЯ."
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help",  help_cmd))
    logger.info("Бот запущен. Нажми Ctrl+C для остановки.")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
