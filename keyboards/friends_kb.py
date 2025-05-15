from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_friends_keyboard(names: list[str], action: str):
   builder = InlineKeyboardBuilder()
   for name in names:
       builder.button(text=name, callback_data=f"{action}:{name}")
   # каждая кнопка в отдельной строке:
   builder.adjust(1)
   return builder.as_markup()
