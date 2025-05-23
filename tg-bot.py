import logging
import requests
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes,
    ConversationHandler, filters
)

API_URL = "http://127.0.0.1:8001/api"
TELEGRAM_TOKEN = "7616303667:AAHPCOv8amGVMvGIaNkRulM1CUCbtEc1rz0"

LOGIN_USERNAME, LOGIN_PASSWORD, ADD_TYPE, ADD_DURATION, ADD_FOOD_NAME, ADD_FOOD_CAL, \
EDIT_WO_ID, EDIT_WO_INPUT, EDIT_FOOD_ID, EDIT_FOOD_INPUT, DEL_WO_ID, DEL_FOOD_ID = range(12)

MAIN_MENU_KB = ReplyKeyboardMarkup(
    [
        ["🏋️ Добавить тренировку", "🥗 Добавить продукт"],
        ["✏️ Редактировать тренировку", "✏️ Редактировать продукт"],
        ["❌ Удалить тренировку", "❌ Удалить продукт"],
        ["📊 Показать отчёт"]
    ],
    resize_keyboard=True
)
ACTION_KB = ReplyKeyboardMarkup([["🔙 Назад"]], resize_keyboard=True)

user_tokens = {}
logging.basicConfig(level=logging.INFO)


def headers(user_id):
    token = user_tokens.get(user_id, {}).get("access")
    return {"Authorization": f"Bearer {token}"} if token else {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Добро пожаловать! Введите /login чтобы начать.")


async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Имя пользователя:")
    return LOGIN_USERNAME


async def get_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['username'] = update.message.text
    await update.message.reply_text("Пароль:")
    return LOGIN_PASSWORD


async def get_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = context.user_data['username']
    password = update.message.text
    resp = requests.post(f"{API_URL}/auth/login/", json={"username": username, "password": password})
    if resp.status_code == 200:
        user_tokens[update.effective_user.id] = resp.json()
        await update.message.reply_text("✅ Вход выполнен. Введите /menu")
    else:
        await update.message.reply_text("❌ Ошибка входа")
    return ConversationHandler.END


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Меню:", reply_markup=MAIN_MENU_KB)


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔙 Возврат в меню.", reply_markup=MAIN_MENU_KB)
    return ConversationHandler.END


async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    u = requests.get(f"{API_URL}/auth/me/", headers=headers(user_id)).json()
    w = requests.get(f"{API_URL}/workouts/", headers=headers(user_id)).json()
    n = requests.get(f"{API_URL}/nutrition/", headers=headers(user_id)).json()
    total_dur = sum(wi['duration'] for wi in w)
    total_cal = sum(fi['calories'] for fi in n)
    await update.message.reply_text(
        f"📊 {u['username']}:\nТренировок: {len(w)} на {total_dur} мин\nПродуктов: {len(n)} на {total_cal} ккал")


# === Добавление ===
async def add_workout(update, context):
    await update.message.reply_text("Тип тренировки (Кардио, Силовая...):", reply_markup=ACTION_KB)
    return ADD_TYPE


async def get_workout_type(update, context):
    context.user_data['type'] = update.message.text
    await update.message.reply_text("Длительность (мин):", reply_markup=ACTION_KB)
    return ADD_DURATION


async def get_workout_duration(update, context):
    dur = update.message.text
    resp = requests.post(f"{API_URL}/workouts/", json={
        "workout_type": context.user_data['type'], "duration": dur
    }, headers=headers(update.effective_user.id))
    await update.message.reply_text("✅ Добавлено" if resp.status_code == 201 else "❌ Ошибка", reply_markup=MAIN_MENU_KB)
    return ConversationHandler.END


async def add_food(update, context):
    await update.message.reply_text("Название продукта:", reply_markup=ACTION_KB)
    return ADD_FOOD_NAME


async def get_food_name(update, context):
    context.user_data['food_name'] = update.message.text
    await update.message.reply_text("Калорийность:", reply_markup=ACTION_KB)
    return ADD_FOOD_CAL


async def get_food_cal(update, context):
    resp = requests.post(f"{API_URL}/nutrition/", json={
        "name": context.user_data['food_name'], "calories": update.message.text
    }, headers=headers(update.effective_user.id))
    await update.message.reply_text("✅ Добавлено" if resp.status_code == 201 else "❌ Ошибка", reply_markup=MAIN_MENU_KB)
    return ConversationHandler.END


# === Редактирование и удаление ===
async def edit_workout(update, context):
    user_id = update.effective_user.id
    workouts = requests.get(f"{API_URL}/workouts/", headers=headers(user_id)).json()
    workout_list = "\n".join(f"{w['id']}: {w['workout_type']} {w['duration']} мин" for w in workouts)
    await update.message.reply_text(f"Тренировки:\n{workout_list}\n\nВведите ID, тип, длительность через запятую:\nПример: 1, Йога, 30", reply_markup=ACTION_KB)
    return EDIT_WO_INPUT


async def handle_edit_workout(update, context):
    try:
        workout_id, new_type, new_dur = map(str.strip, update.message.text.split(","))
        response = requests.patch(
            f"{API_URL}/workouts/{workout_id}/",
            json={"workout_type": new_type, "duration": new_dur},
            headers=headers(update.effective_user.id)
        )
        if response.status_code == 200:
            await update.message.reply_text("✅ Тренировка обновлена.", reply_markup=MAIN_MENU_KB)
        else:
            await update.message.reply_text("❌ Ошибка редактирования.", reply_markup=MAIN_MENU_KB)
    except Exception:
        await update.message.reply_text("❌ Неверный формат. Пример: 1, Йога, 30", reply_markup=MAIN_MENU_KB)
    return ConversationHandler.END


async def edit_food(update, context):
    user_id = update.effective_user.id
    foods = requests.get(f"{API_URL}/nutrition/", headers=headers(user_id)).json()
    food_list = "\n".join(f"{f['id']}: {f['name']} {f['calories']} ккал" for f in foods)
    await update.message.reply_text(f"Продукты:\n{food_list}\n\nВведите ID, название, калорийность через запятую:\nПример: 1, Яблоко, 50", reply_markup=ACTION_KB)
    return EDIT_FOOD_INPUT


async def handle_edit_food(update, context):
    try:
        food_id, new_name, new_cal = map(str.strip, update.message.text.split(","))
        response = requests.patch(
            f"{API_URL}/nutrition/{food_id}/",
            json={"name": new_name, "calories": new_cal},
            headers=headers(update.effective_user.id)
        )
        if response.status_code == 200:
            await update.message.reply_text("✅ Продукт обновлён.", reply_markup=MAIN_MENU_KB)
        else:
            await update.message.reply_text("❌ Ошибка редактирования.", reply_markup=MAIN_MENU_KB)
    except Exception:
        await update.message.reply_text("❌ Неверный формат. Пример: 1, Яблоко, 50", reply_markup=MAIN_MENU_KB)
    return ConversationHandler.END


async def delete_workout(update, context):
    user_id = update.effective_user.id
    workouts = requests.get(f"{API_URL}/workouts/", headers=headers(user_id)).json()
    workout_list = "\n".join(f"{w['id']}: {w['workout_type']} {w['duration']} мин" for w in workouts)
    await update.message.reply_text(f"Удаление тренировки:\n{workout_list}\n\nВведите ID для удаления:", reply_markup=ACTION_KB)
    return DEL_WO_ID


async def handle_delete_workout(update, context):
    workout_id = update.message.text.strip()
    response = requests.delete(f"{API_URL}/workouts/{workout_id}/", headers=headers(update.effective_user.id))
    if response.status_code == 204:
        await update.message.reply_text("✅ Удалено.", reply_markup=MAIN_MENU_KB)
    else:
        await update.message.reply_text("❌ Ошибка удаления.", reply_markup=MAIN_MENU_KB)
    return ConversationHandler.END


async def delete_food(update, context):
    user_id = update.effective_user.id
    foods = requests.get(f"{API_URL}/nutrition/", headers=headers(user_id)).json()
    food_list = "\n".join(f"{f['id']}: {f['name']} {f['calories']} ккал" for f in foods)
    await update.message.reply_text(f"Удаление продукта:\n{food_list}\n\nВведите ID для удаления:", reply_markup=ACTION_KB)
    return DEL_FOOD_ID


async def handle_delete_food(update, context):
    food_id = update.message.text.strip()
    response = requests.delete(f"{API_URL}/nutrition/{food_id}/", headers=headers(update.effective_user.id))
    if response.status_code == 204:
        await update.message.reply_text("✅ Удалено.", reply_markup=MAIN_MENU_KB)
    else:
        await update.message.reply_text("❌ Ошибка удаления.", reply_markup=MAIN_MENU_KB)
    return ConversationHandler.END


if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("summary", summary))
    app.add_handler(CommandHandler("cancel", cancel))
    

    app.add_handler(ConversationHandler(
        entry_points=[CommandHandler("login", login)],
        states={
            LOGIN_USERNAME: [MessageHandler(filters.Regex("🔙 Назад"), cancel),
                             MessageHandler(filters.TEXT & ~filters.COMMAND, get_username)],
            LOGIN_PASSWORD: [MessageHandler(filters.Regex("🔙 Назад"), cancel),
                             MessageHandler(filters.TEXT & ~filters.COMMAND, get_password)],
        },
        fallbacks=[MessageHandler(filters.Regex("🔙 Назад"), cancel)]
    ))

    app.add_handler(ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("🏋️ Добавить тренировку"), add_workout)],
        states={
            ADD_TYPE: [MessageHandler(filters.Regex("🔙 Назад"), cancel),
                       MessageHandler(filters.TEXT & ~filters.COMMAND, get_workout_type)],
            ADD_DURATION: [MessageHandler(filters.Regex("🔙 Назад"), cancel),
                           MessageHandler(filters.TEXT & ~filters.COMMAND, get_workout_duration)],
        },
        fallbacks=[]
    ))

    app.add_handler(ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("🥗 Добавить продукт"), add_food)],
        states={
            ADD_FOOD_NAME: [MessageHandler(filters.Regex("🔙 Назад"), cancel),
                            MessageHandler(filters.TEXT & ~filters.COMMAND, get_food_name)],
            ADD_FOOD_CAL: [MessageHandler(filters.Regex("🔙 Назад"), cancel),
                           MessageHandler(filters.TEXT & ~filters.COMMAND, get_food_cal)],
        },
        fallbacks=[]
    ))

    app.add_handler(ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("✏️ Редактировать тренировку"), edit_workout)],
        states={
            EDIT_WO_INPUT: [MessageHandler(filters.Regex("🔙 Назад"), cancel),
                            MessageHandler(filters.TEXT & ~filters.COMMAND, handle_edit_workout)]
        },
        fallbacks=[]
    ))

    app.add_handler(ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("✏️ Редактировать продукт"), edit_food)],
        states={
            EDIT_FOOD_INPUT: [MessageHandler(filters.Regex("🔙 Назад"), cancel),
                              MessageHandler(filters.TEXT & ~filters.COMMAND, handle_edit_food)]
        },
        fallbacks=[]
    ))

    app.add_handler(ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("❌ Удалить тренировку"), delete_workout)],
        states={
            DEL_WO_ID: [MessageHandler(filters.Regex("🔙 Назад"), cancel),
                        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_delete_workout)]
        },
        fallbacks=[]
    ))

    app.add_handler(ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("❌ Удалить продукт"), delete_food)],
        states={
            DEL_FOOD_ID: [MessageHandler(filters.Regex("🔙 Назад"), cancel),
                          MessageHandler(filters.TEXT & ~filters.COMMAND, handle_delete_food)]
        },
        fallbacks=[]
    ))

    app.add_handler(MessageHandler(filters.Regex("📊 Показать отчёт"), summary))

    print("✅ Бот запущен")
    app.run_polling()
