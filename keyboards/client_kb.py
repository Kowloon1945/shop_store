from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

shop_cart = InlineKeyboardMarkup(row_width=2)
shop_cart_btn = InlineKeyboardButton('Корзина', callback_data='korzina')
shop_cart.add(shop_cart_btn)

clear_shop_cart_kb = InlineKeyboardMarkup(row_width=2)
clear_shop_cart_btn = InlineKeyboardButton('Очистить корзину', callback_data='clear_shop_cart')
checkout = InlineKeyboardButton('Оформить заказ', callback_data='checkout')
clear_shop_cart_kb.add(clear_shop_cart_btn).add(checkout)


open_catalog_kb = InlineKeyboardMarkup(row_width=2)
open_katalog = InlineKeyboardButton('Открыть каталог', callback_data='open_catalog')
open_catalog_kb.add(open_katalog)

futbolki_ili_hudi = InlineKeyboardMarkup(row_width=2)
futbolki = InlineKeyboardButton('Футболки', callback_data='futbolki')
hudi = InlineKeyboardButton('Худи', callback_data='hudi')
futbolki_ili_hudi.add(futbolki).add(hudi)

# размеры
size_kb = InlineKeyboardMarkup(row_width=2)
size_xs = InlineKeyboardButton('XS', callback_data='size|XS')
size_s = InlineKeyboardButton('S', callback_data='size|S')
size_m = InlineKeyboardButton('M', callback_data='size|M')
size_l = InlineKeyboardButton('L', callback_data='size|L')
size_xl = InlineKeyboardButton('XL', callback_data='size|XL')
size_2xl = InlineKeyboardButton('2XL', callback_data='size|2XL')
size_3xl = InlineKeyboardButton('3XL', callback_data='size|3XL')
size_4xl = InlineKeyboardButton('4XL', callback_data='size|4XL')
size_5xl = InlineKeyboardButton('5XL', callback_data='size|5XL')
size_kb.add(size_xs).row(size_s, size_m).row(size_l, size_xl).row(size_2xl, size_3xl).row(size_4xl, size_5xl)


# клавивтура для футболок
futbolki_kb = InlineKeyboardMarkup(row_width=2)
back_to_futbolki = InlineKeyboardButton('Назад', callback_data='back_to_futbolki') # кнопка нахад в футболки
size_futbolki = InlineKeyboardButton('Размеры', callback_data='size_futbolki')
futbolki_kb.add(size_xs).row(size_s, size_m).row(size_l, size_xl).row(size_2xl, size_3xl).row(size_4xl, size_5xl).add(back_to_futbolki, size_futbolki)

# Футболки
fut_kb = InlineKeyboardMarkup(row_width=2)
fut_uch = InlineKeyboardButton('Футболка Учение', callback_data='fut_uch')
fut_pent = InlineKeyboardButton('Футболка Пентаграмма', callback_data='fut_pent')
fut_stal = InlineKeyboardButton('Футболка Сталинеш', callback_data='fut_stal')
back_fut_and_hudi = InlineKeyboardButton('Назад', callback_data='back_fut_and_hudi') #общая для футболок и худи кнопка назад
fut_kb.add(fut_uch).add(fut_pent).add(fut_stal).add(back_fut_and_hudi)




# Худи
hudi_kb = InlineKeyboardMarkup(row_width=2)
hudi_uch = InlineKeyboardButton('Худи Учение', callback_data='hudi_uch')
hudi_pent = InlineKeyboardButton('Худи Пентаграмма', callback_data='hudi_pent')
hudi_kb.add(hudi_uch).add(hudi_pent).add(back_fut_and_hudi)

# клавиатура для худи
the_hudi_kb = InlineKeyboardMarkup(row_width=2)
back_to_hudi = InlineKeyboardButton('Назад', callback_data='back_to_hudi') # кнопка назад в худи
size_hudi = InlineKeyboardButton('Размеры', callback_data='size_hudi')
the_hudi_kb.add(size_xs).row(size_s, size_m).row(size_l, size_xl).row(size_2xl, size_3xl).row(size_4xl, size_5xl).add(back_to_hudi, size_hudi)

# тест кб
test_size = ['XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL', '5XL']
test_kb = InlineKeyboardMarkup(row_width=2)
test_kb.add(*[InlineKeyboardButton(name, callback_data=f'{name}') for name in test_size])


choice_delivery = InlineKeyboardMarkup(row_width=2)
choice_delivery_samovivoz = InlineKeyboardButton('Самовывоз', callback_data='samovivoz')
choice_delivery_pochta = InlineKeyboardButton('Почтой', callback_data='pochta')
choice_delivery.row(choice_delivery_samovivoz, choice_delivery_pochta)

samovivoz_kb = InlineKeyboardMarkup(row_width=2)
msk = InlineKeyboardButton('Москва', callback_data='msk')
spb = InlineKeyboardButton('Спб', callback_data='spb')
samovivoz_kb.add(msk).add(spb)

Russia_or_other = InlineKeyboardMarkup(row_width=2)
russia = InlineKeyboardButton('Россия', callback_data='russia')
other = InlineKeyboardButton('Другая страна', callback_data='other')
Russia_or_other.add(russia).add(other)