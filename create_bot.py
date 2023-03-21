from pyqiwip2p import AioQiwiP2P
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token='6116938414:AAGhCOGyv-fqpaBI-r7J1FQ_VRbDrKDNkgo')
dp = Dispatcher(bot, storage=storage)

QIWI_PRIV_KEY = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjR1OGl1MS0wMCIsInVzZXJfaWQiOiI3OTk5MTY0NTAyOCIsInNlY3JldCI6IjBmZjFiZGI0OTI0NmE0MDgyMjk2YTZmYjg4MDZiMGEyOGZlNWFkZWZmZDA2MTg4MDdjOTdhMzY2YmIxYWIxZDAifX0="

p2p = AioQiwiP2P(auth_key=QIWI_PRIV_KEY)