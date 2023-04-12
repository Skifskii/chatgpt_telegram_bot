unknown_error_answer = """
🤖🚫
Что-то пошло не так :("""

start_answer = """
🤖
Привет, {first_name} 👋
Я персональный чат-бот с искусственным интеллектом, способный работать в диалоговом режиме, повторяющий возможности ChatGPT.
Нажми /help, чтобы получить информацию о моих командах."""

help_answer = """
🤖
Команды:

/about - обо мне.
/profile - профиль пользователя.
/forget - очистить память нейросети.
/image - сгенерировать изображение по текстовому запросу.

Все остальные сообщения будут восприниматься как запрос к ChatGPT.

❗️Прежде чем сменить тему общения с ботом или перейти на другой язык, нажмите /forget."""

about_answer = """
🤖
ChatGPT — чат-бот с искусственным интеллектом, способный работать в диалоговом режиме, поддерживающий запросы на естественных языках.
ChatGPT может вести диалог, отвечать на вопросы любой сложности, писать код на разных языках программирования, искать ошибки в коде, сочинять стихи, писать сценарии и многое другое.
ChatGPT может использовать в общении разные языки, но мы рекомендуем вести общение на английском. Так бот будет работать более корректно, а вы сможете сэкономить свои токены (1000 токенов ~ 700 английских слов или 150 слов другого языка)."""

forget_answer = """
🤖
Вы успешно очистили память бота!"""

profile_answer = """
👤 {user_name}
Подписка: {user_subscription}"""

buy_no_email_answer = """
🤖
Введите адрес электронной почты для получения чеков"""

check_email_answer = """
🤖
Выберите тип подписки"""

choose_subscription_type_answer = """
🤖
Поздравляю! Вы оформили подписку {subscription_type}"""

while_answer_is_generating_answer = """
🤖 Генерирую ответ..."""

telegram_logs_permission_symbols = ['❌', '✅']

ask_gpt_without_subscribe_answer = """
🤖🚫
Вы не можете отправлять запросы без подписки. Если вы хотите оформить подписку, перейдите в свой профиль, нажав /profile"""

ban_answer = """
🤖🚫
Вы были забанены администратором."""

ask_dalle_without_subscribe_answer = """
🤖🚫
Вы не можете генерировать изображения без подписки VIP. Если вы хотите оформить подписку, перейдите в свой профиль, нажав /profile"""

image_command_answer = """
🤖
Введите текст запроса"""

choose_image_size_message = """
🤖
Выберите качество изображения"""

generating_image_message = """
🤖 Генерирую изображение..."""

openai_dalle_error_message = """
🤖🚫
Произошла ошибка на сервере DALL-E :(\nПопробуйте повторить запрос"""

openai_dalle_bad_request_error_message = """
🤖🚫
Ошибка! Введенный вами запрос является некорректным с точки зрения DALL-E.\nПопробуйте повторить запрос, изменив формулировку"""

select_user_answer = """
🤖
Введите id пользователя"""

select_new_status_answer = """
🤖
Статус пользователя {user_id} изменен на {new_status}"""

stat_answer = """
🤖
Статистика, собранная в период
От   {date_start}
До   {today}

- Новых пользователей: {num_of_new_users}
- Запросов отправлено: {num_of_new_requests}
- Ответов получено: {num_of_new_answers}
- Токенов потрачено: {num_of_tokens}

Общая статистика:
- Пользователи: {total_num_of_users}
- Количество запросов: {total_number_of_messages}
- Сгенерированные изображения: {total_number_of_images}"""

admin_funcs_info_answer = """
⚙ admin panel ⚙

/stat - статистика
/select_user - данные пользователя
/setup_telegram_logs - настройка логов
/send_to_users (message) - рассылка
"""
