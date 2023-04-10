from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline import ikb_buy, ikb_subscribe
from loader import dp
from utils.db_api.quick_commands import user as db_users

from data.config import subscriptions_dict
from data.texts import balance_answer, buy_no_email_answer, choose_subscription_type_answer
from logs.log_all import log_all
from states import Buy


@dp.message_handler(commands='profile')  # ToDo
async def command_profile(message: types.Message):
    try:
        user = await db_users.select_user(message.from_user.id)
        await message.answer(balance_answer.format(user_balance=user.balance, english_words=int(user.balance * 0.7)), reply_markup=ikb_buy)
    except Exception as error:
        await message.answer('Что-то пошло не так :(')
        await log_all('balance', 'error', message.from_user.id, message.from_user.first_name, error)


@dp.callback_query_handler(text_contains='btn_buy')
async def btn_buy_pressed(query: types.CallbackQuery):
    try:
        user = await db_users.select_user(query.from_user.id)
        if user.email == '':
            await query.message.edit_text(buy_no_email_answer)
            await Buy.email.set()
        else:
            pass
    except Exception as error:
        await query.message.answer('Что-то пошло не так :(')
        await log_all('btn_buy_pressed', 'error', query.message.from_user.id, query.message.from_user.first_name, error)


@dp.message_handler(state=Buy.email)
async def check_email(message: types.Message, state: FSMContext):
    try:
        user_email = message.text
        await state.update_data(email=user_email)
        await message.answer(choose_subscription_type_answer, reply_markup=ikb_subscribe)
        await Buy.subscription.set()
    except Exception as error:
        await message.answer('Что-то пошло не так :(')
        await log_all('check_email', 'error', message.from_user.id, message.from_user.first_name, error)


@dp.callback_query_handler(text_contains='btn_subscribe', state=Buy.subscription)
async def choose_subscription_type(query: types.CallbackQuery, state: FSMContext):
    try:
        subscription_type = subscriptions_dict[query.data.split('_')[-1]]
        await query.message.edit_text(f'Поздравляю! Вы оформили подписку {subscription_type}')
        await state.finish()
    except Exception as error:
        await query.message.answer('Что-то пошло не так :(')
        await log_all('choose_subscription_type', 'error', query.message.from_user.id, query.message.from_user.first_name, error)

