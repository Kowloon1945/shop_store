from aiogram.dispatcher.filters.state import StatesGroup, State

class Merch(StatesGroup):
    type_merch = State()
    the_merch = State()
    size_merch = State()
    price_merch = State()

class SamovivozSPB(StatesGroup):
    delivety_type = 'Самовывоз'
    delivery_country = 'Россия'
    delivery_address = 'Питер'
    payment_type = 'Оплата при встрече'
    # payment_data = State()
    # user_id = State()
    user_tgUsername = State()

class SamovivozMSK(StatesGroup):
    delivety_type = 'Самовывоз'
    delivery_country = 'Россия'
    delivery_address = 'Москва'
    payment_type = 'Оплата при встрече'
    # payment_data = State()
    # user_id = State()
    user_tgUsername = State()

class PochtaRF(StatesGroup):
    delivety_type = 'Почта РФ'
    delivery_country = 'Россия'
    delivery_address = State()
    payment_type = 'Киви'
    # payment_data = State()
    # user_id = State()
    user_tgUsername = State()

class PochtaOtherCountry(StatesGroup):
    delivety_type = 'Почта Заграница'
    delivery_country = State()
    delivery_address = State()
    payment_type = 'Киви'
    # payment_data = State()
    # user_id = State()
    user_tgUsername = State()



