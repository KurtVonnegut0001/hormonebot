# Эндокринный эквалайзер — Telegram Bot

## Что внутри

```
index.html   — само приложение (полный HTML, работает автономно)
bot.py       — Telegram-бот на Python (20 строк, без сервера)
requirements.txt
README.md    — этот файл
```

---

## Шаг 1 — Разместить index.html (бесплатно за 5 минут)

### Вариант А: GitHub Pages (рекомендую)

1. Зайди на https://github.com и создай новый репозиторий
   - Назови, например: `hormone-eq`
   - Поставь галку "Public"

2. Загрузи `index.html` в репозиторий
   - Нажми "Add file" → "Upload files"

3. Включи GitHub Pages:
   - Settings → Pages → Source: "Deploy from a branch"
   - Branch: `main`, папка: `/ (root)` → Save

4. Через 2–3 минуты сайт будет доступен по адресу:
   ```
   https://ТВО_ИМЯ.github.io/hormone-eq/
   ```
   Это и есть твой `WEBAPP_URL`.

### Вариант Б: Netlify (drag & drop)

1. Зайди на https://netlify.com
2. Перетащи папку с `index.html` в браузер
3. Получи URL вида `https://случайное-имя.netlify.app`

### Вариант В: Vercel

```bash
npm i -g vercel
vercel --name hormone-eq
```

---

## Шаг 2 — Создать бота у @BotFather

1. Открой Telegram, найди @BotFather
2. Отправь `/newbot`
3. Придумай имя и username (например `HormoneEqBot`)
4. Скопируй токен вида `1234567890:AAF...`

---

## Шаг 3 — Настроить и запустить bot.py

1. Установи зависимости:
   ```bash
   pip install python-telegram-bot==20.7
   ```

2. Открой `bot.py` и замени:
   ```python
   BOT_TOKEN  = "1234567890:AAFxxxxxxx"          # токен от BotFather
   WEBAPP_URL = "https://твой-сайт.github.io/hormone-eq/"  # URL из шага 1
   ```

3. Запусти:
   ```bash
   python bot.py
   ```

4. Найди своего бота в Telegram, отправь `/start` — появится кнопка.

---

## Шаг 4 (опционально) — Держать бота включённым 24/7

### Бесплатно на Railway.app

1. Зайди на https://railway.app
2. "New Project" → "Deploy from GitHub repo"
3. Подключи репозиторий с `bot.py`
4. Добавь переменные окружения:
   - `BOT_TOKEN` = твой токен
   - `WEBAPP_URL` = твой URL
5. Измени `bot.py` чтобы читать из env:
   ```python
   import os
   BOT_TOKEN  = os.environ["BOT_TOKEN"]
   WEBAPP_URL = os.environ["WEBAPP_URL"]
   ```

### На своём VPS (systemd)

```bash
# /etc/systemd/system/hormone-bot.service
[Unit]
Description=Hormone EQ Bot

[Service]
ExecStart=/usr/bin/python3 /opt/hormone-eq-bot/bot.py
Restart=always
Environment=BOT_TOKEN=xxx
Environment=WEBAPP_URL=https://...

[Install]
WantedBy=multi-user.target
```

```bash
systemctl enable hormone-bot
systemctl start hormone-bot
```

---

## Требования к хостингу

- Обязательно **HTTPS** (Telegram не открывает WebApp по HTTP)
- GitHub Pages, Netlify, Vercel — все дают HTTPS бесплатно
- Файл `index.html` должен быть доступен напрямую по URL

---

## Важно

Приложение образовательное. Не использовать для самодиагностики.
