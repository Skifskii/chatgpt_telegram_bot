from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline import ikb_actions_with_user, ikb_choose_new_status
from loader import dp, bot
from states import SelectUser
from utils.db_api.quick_commands import user as db_users

from data.texts import unknown_error_answer, select_user_answer, select_new_status_answer, message_to_user_message, \
    message_to_user_sent_message, user_not_found_error_answer, set_new_limit_answer, select_new_limit_answer
from logs.log_all import log_all

from filters import IsAdmin


@dp.message_handler(IsAdmin(), commands='select_user', state=None)
async def select_user(message: types.Message):
    try:
        await message.answer(select_user_answer)
        await SelectUser.user_id.set()
    except Exception as error:
        await message.answer(unknown_error_answer)
        await log_all('select_user', 'error', message.from_user.id, message.from_user.first_name, error)


@dp.message_handler(state=SelectUser.user_id)
async def print_user_info(message: types.Message, state: FSMContext):
    try:
        user_id = message.text
        await state.update_data(user_id=int(user_id))
        user = await db_users.select_user(int(user_id))
        await message.answer(f"""
👤 Пользователь `{user_id}`

имя: *{user.firstname}*
username: *@{user.username}*
статус: *{user.status}*
лимит: *{user.limit}/{user.max_limit}*

запросов к ChatGPT: *{user.total_messages_sent}*
изображений сгенерировано: *{user.total_images_generated}*
""", reply_markup=ikb_actions_with_user)
        await SelectUser.status.set()
    except AttributeError as error:
        await message.answer(user_not_found_error_answer)
        await log_all('print_user_info', 'error', message.from_user.id, message.from_user.first_name, error)
        await state.finish()
    except Exception as error:
        await message.answer(unknown_error_answer)
        await log_all('print_user_info', 'error', message.from_user.id, message.from_user.first_name, error)
        await state.finish()


@dp.callback_query_handler(text_contains='btn_change_status', state=SelectUser.status)
async def btn_change_status(query: types.CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        await query.message.edit_text(f"""
👤 Пользователь *{data.get('user_id')}*

Выберите новый статус
""", reply_markup=ikb_choose_new_status)
        await SelectUser.select_new_status.set()
    except Exception as error:
        await query.message.answer(unknown_error_answer)
        await log_all('btn_change_status', 'error', query.message.from_user.id, query.message.from_user.first_name, error)
        await state.finish()


@dp.callback_query_handler(text_contains='btn_send_message', state=SelectUser.status)
async def btn_send_message(query: types.CallbackQuery, state: FSMContext):
    try:
        await query.message.edit_text(message_to_user_message)
        await SelectUser.message_to_user.set()
    except Exception as error:
        await query.message.answer(unknown_error_answer)
        await log_all('btn_send_message', 'error', query.message.from_user.id, query.message.from_user.first_name, error)
        await state.finish()


@dp.message_handler(state=SelectUser.message_to_user)
async def message_to_user_sent(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        await bot.send_message(data.get('user_id'), message.text)
        await message.answer(message_to_user_sent_message)
        await state.finish()
    except Exception as error:
        await message.answer(unknown_error_answer)
        await log_all('message_to_user_sent', 'error', message.from_user.id, message.from_user.first_name, error)
        await state.finish()


@dp.callback_query_handler(text_contains='btn_back', state=SelectUser.status)
async def tglog_messages_back(query: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(query.message.chat.id, query.message.message_id)
    await state.finish()


@dp.callback_query_handler(text_contains='btn_status', state=SelectUser.select_new_status)
async def select_new_limit(query: types.CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()

        user_id = data.get('user_id')
        user = await db_users.select_user(user_id)
        new_status = query.data.split('_')[-1]
        if new_status == 'unlimited':
            await db_users.reset_limit(user_id, -1)
            await db_users.reset_max_limit(user_id, -1)
        elif new_status == 'limited':
            await db_users.set_status(user_id, 'user')
            await query.message.edit_text(select_new_limit_answer)
            await SelectUser.new_limit.set()
            return
        elif new_status == 'ban':
            await db_users.set_status(user_id, 'ban')
        elif new_status == 'unban':
            await db_users.set_status(user_id, 'user')
        elif new_status == 'admin':
            await db_users.set_status(user_id, 'admin')
        await query.message.edit_text(select_new_status_answer.format(user_id=user_id, new_status=new_status))
    except Exception as error:
        await query.message.answer(unknown_error_answer)
        await log_all('btn_change_status', 'error', query.message.from_user.id, query.message.from_user.first_name,
                      error)
    await state.finish()


@dp.callback_query_handler(text_contains='btn_back', state=SelectUser.select_new_status)
async def tglog_messages_back(query: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(query.message.chat.id, query.message.message_id)
    await state.finish()


@dp.message_handler(state=SelectUser.new_limit)
async def set_new_limit(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        await db_users.reset_max_limit(data.get('user_id'), int(message.text))
        await db_users.reset_limit(data.get('user_id'), int(message.text))
        await message.answer(set_new_limit_answer)
        await state.finish()
    except Exception as error:
        await message.answer(unknown_error_answer)
        await log_all('message_to_user_sent', 'error', message.from_user.id, message.from_user.first_name, error)
        await state.finish()
