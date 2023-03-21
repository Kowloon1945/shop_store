from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from create_bot import bot, dp, p2p
from models_merch import *
from fsm_state import Merch, SamovivozMSK, SamovivozSPB, PochtaRF, PochtaOtherCountry
from keyboards.client_kb import *
from datetime import datetime
import sqlite3

connect = sqlite3.connect('korzina_shop_store.db')
# chat_id = '-100'

async def command_start(message: types.Message):
    await bot.send_photo(message.from_user.id, types.InputFile(r'src\photo_menu.jpg'),
                         caption='Привет! Это бот для заказа футболок и худи. Перед заказом прочти, пожалуйста, дисклеймер',
                         reply_markup=open_catalog_kb)

async def command_korzina(message: types.Message):
    await bot.send_message(message.from_user.id, 'Корзина')


# async def shopping_cart(message: types.Message):
#     await bot.send_message(message.from_user.id, f'Ваши товары:{items}\nЦена:{price})
@dp.callback_query_handler(text='open_catalog')
async def open_katalog(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await bot.send_message(callback_query.from_user.id, 'Выберите категорию', reply_markup=futbolki_ili_hudi)
    await Merch.type_merch.set()

@dp.callback_query_handler(state=Merch.type_merch)
async def choice_type_merch(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'futbolki':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, 'Футболки', reply_markup=fut_kb)
        await state.update_data(type_merch=Fut.fut)
        await Merch.the_merch.set()

    elif callback_query.data == 'hudi':
        await callback_query.message.delete()
        await state.update_data(type_merch=Hud.hud)
        await bot.send_message(callback_query.from_user.id, 'Худи', reply_markup=hudi_kb)
        await Merch.the_merch.set()

    else:
        raise Exception


@dp.callback_query_handler(state=Merch.the_merch)
async def choice_the_merch(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'fut_uch':
        await callback_query.message.delete()
        await state.update_data(the_merch=FutUch.name)
        await state.update_data(price_merch=Fut.price)
        await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\fut_uch.jpg'),
                             caption='Футболка Один\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны',
                             reply_markup=futbolki_kb)
        await Merch.size_merch.set()

    elif callback_query.data == 'fut_pent':
        await callback_query.message.delete()
        await state.update_data(the_merch=FutPent.name)
        await state.update_data(price_merch=Fut.price)
        await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\fut_pent.jpg'),
                             caption='Футболка Два\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны',
                             reply_markup=futbolki_kb)
        await Merch.size_merch.set()

    elif callback_query.data == 'fut_stal':
        await callback_query.message.delete()
        await state.update_data(the_merch=FutStal.name)
        await state.update_data(price_merch=Fut.price)
        await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\fut_stal.jpg'),
                             caption='Футболка Три\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны',
                             reply_markup=futbolki_kb)
        await Merch.size_merch.set()

    elif callback_query.data == 'hudi_uch':
        await callback_query.message.delete()
        await state.update_data(the_merch=HudUch.name)
        await state.update_data(price_merch=Hud.price)
        await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\tol_uch.jpg'),
                             caption='Худи Один\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны',
                             reply_markup=the_hudi_kb)
        await Merch.size_merch.set()

    elif callback_query.data == 'hudi_pent':
        await callback_query.message.delete()
        await state.update_data(the_merch=HudPent.name)
        await state.update_data(price_merch=Hud.price)
        await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\tol_pent.jpg'),
                             caption='Худи Два\n\nДоставка: 600 рублей (почта РФ). От 800 рублей в другие страны',
                             reply_markup=the_hudi_kb)
        await Merch.size_merch.set()

    elif callback_query.data == 'back_fut_and_hudi':
        await state.finish()
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, 'Выберите категорию', reply_markup=futbolki_ili_hudi)
        await Merch.type_merch.set()

    else:
        raise Exception




@dp.callback_query_handler(state=Merch.size_merch)
async def choice_size_merch(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data.startswith('size|'):
        data = callback_query.data.split('|')
        var = data[1]
        await state.update_data(size_merch=var)
        data_obj = await state.get_data()
        final_obj = data_obj['type_merch'] + ' ' + data_obj['the_merch']
        price = data_obj['price_merch']
        size = data_obj['size_merch']
        user_id = callback_query.from_user.id
        cursor = connect.cursor()
        cursor.execute('INSERT INTO korzina(items, price, size, tg_id) VALUES (?, ?, ?, ?)', (final_obj, price, size, user_id))
        cursor.close()
        connect.commit()
        await bot.send_message(callback_query.from_user.id, f'{final_obj} размера {data_obj["size_merch"]} добавлена в корзину', reply_markup=shop_cart)

    elif callback_query.data == 'back_to_futbolki':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, 'Футболки', reply_markup=fut_kb)
        await state.update_data(type_merch=Fut.fut)
        await Merch.the_merch.set()

    elif callback_query.data == 'back_to_hudi':
        await callback_query.message.delete()
        await state.update_data(type_merch=Hud.hud)
        await bot.send_message(callback_query.from_user.id, 'Худи', reply_markup=hudi_kb)
        await Merch.the_merch.set()

    elif callback_query.data == 'size_futbolki':
        await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\razmer_fut.jpg'))

    elif callback_query.data == 'size_hudi':
        await bot.send_photo(callback_query.from_user.id, types.InputFile(r'src\razmer_tol.jpg'))

    elif callback_query.data == 'korzina':
        # await state.finish()
        cursor = connect.cursor()
        products = cursor.execute('SELECT items, price, size FROM korzina WHERE tg_id=(?)', [callback_query.from_user.id]).fetchall()
        totalPrice = 0
        msg = ''
        for (item, price, size) in products:
            msg += f'-{item} {size}-{price}руб' + '\n'
            totalPrice += price
        cursor.close()
        connect.commit()
        await bot.send_message(callback_query.from_user.id, f'Ваши товары: \n{msg}\n--------------------------\nИтого: {totalPrice}руб.',
                               reply_markup=clear_shop_cart_kb)

    elif callback_query.data == 'clear_shop_cart':
        await callback_query.message.delete()
        await state.finish()
        cursor = connect.cursor()
        cursor.execute('DELETE FROM korzina WHERE tg_id=(?)', [callback_query.from_user.id])
        cursor.close()
        connect.commit()
        await bot.send_message(callback_query.from_user.id, 'корзина очищена', reply_markup=open_catalog_kb)

    elif callback_query.data == 'checkout':
        await state.finish()
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, 'Выберите доставку', reply_markup=choice_delivery)

    else:
        raise Exception


@dp.callback_query_handler(text='clear_shop_cart')
async def clear_shop_cart(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    cursor = connect.cursor()
    cursor.execute('DELETE FROM korzina WHERE user_id=(?)', [callback_query.from_user.id])
    cursor.close()
    connect.commit()
    await bot.send_message(callback_query.from_user.id, 'корзина очищена', reply_markup=open_catalog_kb)

@dp.callback_query_handler(text='checkout')
async def checkout(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Выберите доставку', reply_markup=choice_delivery)

@dp.callback_query_handler(text='samovivoz')
async def samovivoz(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Самовывоз возможен только из следующих городов', reply_markup=samovivoz_kb)

@dp.callback_query_handler(text='pochta')
async def russia_or_other(callback_query : types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Выберите страну',
                           reply_markup=Russia_or_other)


# Самовывоз МСК
@dp.callback_query_handler(text='msk')
async def samovivoz_msk(callback_query : types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           'Введите контактную информацию, чтобы мы могли с вами связаться')
    await SamovivozMSK.user_tgUsername.set()

@dp.message_handler(state=SamovivozMSK.user_tgUsername)
async def samik_msk(message: types.Message, state: FSMContext):
    await state.update_data(user_tgUsername=message.text)
    data = await state.get_data()
    await state.finish()
    date = datetime.utcnow()
    cursor = connect.cursor()
    products = cursor.execute('SELECT items, size FROM korzina WHERE tg_id=(?)', [message.from_user.id]).fetchall()
    msg = ''
    for (item, size) in products:
        msg += f'{item} {size}; '
    # productsWithoutTuple = [i[0] for i in products]
    # finalProductsList = [str(item) for item in productsWithoutTuple]
    # products_final = ', '.join(finalProductsList)
    amount_price = cursor.execute('SELECT SUM(price) FROM korzina WHERE tg_id=(?)',
                                  [message.from_user.id]).fetchall()
    amount_priceWithoutTuple = [i[0] for i in amount_price]
    finalPriceList = [int(item) for item in amount_priceWithoutTuple]
    finalPriceWithoutList = finalPriceList[0]
    del_type = str(SamovivozMSK.delivety_type)
    del_country = str(SamovivozMSK.delivery_country)
    del_address = str(SamovivozMSK.delivery_address)
    pay_type = str(SamovivozMSK.payment_type)
    delivery_state = 'Не доставлено'
    cursor.execute(
        'INSERT INTO orders(products, products_price, delivery_type, delivery_country, delivery_address, payment_type, payment_data, user_id, user_info, delivery_state) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (msg, finalPriceWithoutList, del_type,
         del_country, del_address, pay_type,
         date, message.from_user.id,
         data['user_tgUsername'], delivery_state))
    order = cursor.execute('SELECT * FROM orders WHERE tg_id=(?)', [message.from_user.id]).fetchall()
    await bot.send_message(message.from_user.id, 'Отлично! Ждите, мы с вами свяжемся')
    await bot.send_message(chat_id, f'{order}')
    cursor.close()
    connect.commit()



# Самовывоз из СПБ
@dp.callback_query_handler(text='spb')
async def samovivoz_spb(callback_query : types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, 'Введите контактную информацию, чтобы мы могли с вами связаться')
    await SamovivozSPB.user_tgUsername.set()

@dp.message_handler(state=SamovivozSPB.user_tgUsername)
async def samik_spb(message: types.Message, state: FSMContext):
    await state.update_data(user_tgUsername=message.text)
    data = await state.get_data()
    await state.finish()
    date = datetime.utcnow()
    cursor = connect.cursor()
    products = cursor.execute('SELECT items, size FROM korzina WHERE tg_id=(?)', [message.from_user.id]).fetchall()
    msg = ''
    for (item, size) in products:
        msg += f'{item} {size}; '
    # productsWithoutTuple = [i[0] for i in products]
    # finalProductsList = [str(item) for item in productsWithoutTuple]
    # products_final = ', '.join(finalProductsList)
    amount_price = cursor.execute('SELECT SUM(price) FROM korzina WHERE tg_id=(?)',
                                  [message.from_user.id]).fetchall()
    amount_priceWithoutTuple = [i[0] for i in amount_price]
    finalPriceList = [int(item) for item in amount_priceWithoutTuple]
    finalPriceWithoutList = finalPriceList[0]
    del_type = str(SamovivozSPB.delivety_type)
    del_country = str(SamovivozSPB.delivery_country)
    del_address = str(SamovivozSPB.delivery_address)
    pay_type = str(SamovivozSPB.payment_type)
    delivery_state = 'Не доставлено'
    cursor.execute('INSERT INTO orders(products, products_price, delivery_type, delivery_country, delivery_address, payment_type, payment_data, user_id, user_info, delivery_state) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (msg, finalPriceWithoutList, del_type,
                    del_country, del_address,pay_type,
                    date, message.from_user.id,
                    data['user_tgUsername'], delivery_state))
    cursor.close()
    connect.commit()
    await bot.send_message(message.from_user.id, 'Отлично! Ждите, мы с вами свяжемся')



# Доставка почтой РФ
@dp.callback_query_handler(text='russia')
async def pochta_rf_address(callback_query : types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, 'Введите область, город, улицу, дом, почтовый индекс')
    await PochtaRF.delivery_address.set()

@dp.message_handler(state=PochtaRF.delivery_address)
async def pochta_rf_info(message: types.Message, state: FSMContext):
    await state.update_data(delivery_address=message.text)
    await bot.send_message(message.from_user.id, 'Введите контактную информацию для связи')
    await PochtaRF.user_tgUsername.set()

@dp.message_handler(state=PochtaRF.user_tgUsername)
async def pochta_rf_info2(message: types.Message, state: FSMContext):
    await state.update_data(user_tgUsername=message.text)
    data = await state.get_data()
    await state.finish()
    date = datetime.utcnow()
    cursor = connect.cursor()
    products = cursor.execute('SELECT products, size FROM korzina WHERE tg_id=(?)', [message.from_user.id]).fetchall()
    msg = ''
    for (item, size) in products:
        msg += f'{item} {size}; '
    # productsWithoutTuple = [i[0] for i in products]
    # finalProductsList = [str(item) for item in productsWithoutTuple]
    # products_final = ', '.join(finalProductsList)
    amount_price = cursor.execute('SELECT SUM(price) FROM korzina WHERE tg_id=(?)',
                                  [message.from_user.id]).fetchall()
    amount_priceWithoutTuple = [i[0] for i in amount_price]
    finalPriceList = [int(item) for item in amount_priceWithoutTuple]
    finalPriceWithoutList = finalPriceList[0]
    del_type = str(PochtaRF.delivety_type)
    del_country = str(PochtaRF.delivery_country)
    pay_type = str(PochtaRF.payment_type)
    pay_state = 'Не оплачено'
    delivery_state = 'Не доставлено'
    new_bill = await p2p.bill(amount=finalPriceWithoutList, lifetime=45)
    bill_id = new_bill.bill_id
    cursor.execute(
        'INSERT INTO orders(products, products_price, delivery_type, delivery_country, delivery_address, payment_type, payment_data, user_id, user_info, pay_state, delivery_state, bill_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (msg, finalPriceWithoutList, del_type,
         del_country, data['delivery_address'], pay_type,
         date, message.from_user.id,
         data['user_tgUsername'], pay_state, delivery_state, bill_id))
    cursor.close()
    connect.commit()
    new_bill = await p2p.bill(amount=finalPriceWithoutList, lifetime=45)
    await bot.send_message(message.from_user.id, new_bill.pay_url)
    if (await p2p.check(bill_id=new_bill.bill_id)).status is True:
        await bot.send_message(message.from_user.id, 'Ваш заказ оплачен')


# Доставка почтой в другую страну
@dp.callback_query_handler(text='other')
async def pochta_other_address(callback_query : types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, 'Введите страну')
    await PochtaOtherCountry.delivery_country.set()
@dp.message_handler(state=PochtaOtherCountry.delivery_country)
async def pochta_other_address(message: types.Message, state: FSMContext):
    await state.update_data(delivery_country=message.text)
    await bot.send_message(message.from_user.id, 'Введите область, город, улицу, дом, почтовый индекс')
    await PochtaOtherCountry.delivery_address.set()

@dp.message_handler(state=PochtaOtherCountry.delivery_address)
async def pochta_other_info(message: types.Message, state: FSMContext):
    await state.update_data(delivery_address=message.text)
    await bot.send_message(message.from_user.id, 'Введите контактную информацию для связи')
    await PochtaOtherCountry.user_tgUsername.set()

@dp.message_handler(state=PochtaOtherCountry.user_tgUsername)
async def pochta_other_info2(message: types.Message, state: FSMContext):
    await state.update_data(user_tgUsername=message.text)
    data = await state.get_data()
    await state.finish()
    date = datetime.utcnow()
    cursor = connect.cursor()
    products = cursor.execute('SELECT products, size FROM korzina WHERE tg_id=(?)', [message.from_user.id]).fetchall()
    msg = ''
    for (item, size) in products:
        msg += f'{item} {size}; '
    # productsWithoutTuple = [i[0] for i in products]
    # finalProductsList = [str(item) for item in productsWithoutTuple]
    # products_final = ', '.join(finalProductsList)
    amount_price = cursor.execute('SELECT SUM(price) FROM korzina WHERE tg_id=(?)',
                                  [message.from_user.id]).fetchall()
    amount_priceWithoutTuple = [i[0] for i in amount_price]
    finalPriceList = [int(item) for item in amount_priceWithoutTuple]
    finalPriceWithoutList = finalPriceList[0]
    del_type = str(PochtaOtherCountry.delivety_type)
    pay_type = str(PochtaOtherCountry.payment_type)
    pay_state = 'Не оплачено'
    delivery_state = 'Не доставлено'
    new_bill = await p2p.bill(amount=finalPriceWithoutList, lifetime=45)
    bill_id = new_bill.bill_id
    cursor.execute(
        'INSERT INTO orders(products, products_price, delivery_type, delivery_country, delivery_address, payment_type, payment_data, user_id, user_info, pay_state, delivery_state, bill_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (msg, finalPriceWithoutList, del_type,
         data['delivery_country'], data['delivery_address'], pay_type,
         date, message.from_user.id,
         data['user_tgUsername'], pay_state, delivery_state, bill_id))
    await bot.send_message(message.from_user.id, new_bill.pay_url)
    if (await p2p.check(bill_id=bill_id)).status is True:
        await bot.send_message(message.from_user.id, 'Ваш заказ оплачен')
    cursor.close()
    connect.commit()



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    # dp.register_message_handler(command_korzina, commands=['korzina'])

