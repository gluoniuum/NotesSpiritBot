from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
## DICT - cb - callback
start_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'Древняя Тайна Цветка Жизни 🌺', callback_data = 'flower_cb')],
        [InlineKeyboardButton(text = 'Книга Мудрости часть II 📗', callback_data = 'second_wisdom_cb')],
        [InlineKeyboardButton(text = 'Книга Мудрости часть I 📕', callback_data = 'first_wisdom_cb')],
        [InlineKeyboardButton(text = 'Книга Здоровья 📘', callback_data = 'health_cb')],
        [InlineKeyboardButton(text = 'Кибалион 📙', callback_data = 'kibalion_cb')],
        [InlineKeyboardButton(text = 'Бесплатные Книги 📚', callback_data = 'free_books_cb')],
        [InlineKeyboardButton(text = 'Донат ⚪', callback_data = 'donat_cb')],
        [InlineKeyboardButton(text = 'Связь 🛰', callback_data = 'support_cb')],
        ])

free_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = 'Хатха Йога Прадипика', callback_data = 'flower_cb')],
        [InlineKeyboardButton(text = 'Атмосфера Человека', callback_data = 'health_cb')],
        [InlineKeyboardButton(text = 'Личный Магнетизм', callback_data = 'second_wisdom_cb')],
        [InlineKeyboardButton(text = 'Книга Медиумов', callback_data = 'first_wisdom_cb')],
        [InlineKeyboardButton(text = 'Сила Формы', callback_data = 'health_cb')],
        [InlineKeyboardButton(text = 'Чакры', callback_data = 'health_cb')],
])
