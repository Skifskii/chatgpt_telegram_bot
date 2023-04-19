unknown_error_answer = """
🤖🚫
Что-то пошло не так :("""

user_not_found_error_answer = """
🤖🚫
Пользователь не найден"""

invalid_email_value_type = """
🤖🚫
Некорректный e-mail, попробуйте еще раз"""

RateLimitError_answer = """
🤖🚫
Слишком много запросов. Попробуйте повторить запрос позже"""

InvalidRequestError_answer = """
🤖🚫
Произошла ошибка. Пожалуйста, повторите запрос"""

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

Все остальные сообщения будут восприниматься как запрос в диалоговом режиме с использованием технологии нейросети.

❗️Прежде чем сменить тему общения с ботом или перейти на другой язык, нажмите /forget."""

about_answer = """
🤖
@ZhurihinAI_bot  — чат-бот с искусственным интеллектом, способный работать в диалоговом режиме, поддерживающий запросы на естественных языках c использованием технологии ChatGPT и генерировать высококачественные изображения с использованием технологии DALL-E.

@ZhurihinAI_bot  — может вести диалог, отвечать на вопросы любой сложности, писать код на разных языках программирования, искать ошибки в коде, сочинять стихи, писать сценарии и многое другое.

@ZhurihinAI_bot   —  может генерировать изображения в самых разных визуализациях — от фотореализма до картин и эмодзи.

@ZhurihinAI_bot — обучен отвечать на последовательные вопросы, признавать свои ошибки, оспаривать некорректные вводные данные и отклонять неуместные вопросы. 

@ZhurihinAI_bot — не имеет доступа к информации в интернете в режиме реального времени, в связи с этим чат-бот не может генерировать полностью оригинальные идеи и может выдавать ошибочную и неактуальную информацию. Соотвественно никакие претензии по соблюдению авторских прав и их нарушение не принимаются."""
forget_answer = """
🤖
Вы успешно очистили память бота!"""

profile_answer = """
👤 {user_name}
Статус: {user_subscription}"""

buy_no_email_answer = """
🤖
Введите адрес электронной почты для получения чеков"""

select_subscription_message = """
🤖
<b>GPT</b> - <i>100 руб.</i> - месяц безлимитного доступа к нейросети ChatGPT!   

<b>VIP</b> - <i>250 руб.</i> - месяц безлимитного доступа к нейросетям ChatGPT и DALL-E (для генерации изображений). Все запросы обрабатываются отдельно. Это повышает скорость ответа и снижает ограничение на частоту запросов!
"""

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

limit_answer = """
🤖🚫
Лимит запросов на сегодня исчерпан. Возвращайтесь завтра!"""

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

select_new_limit_answer = """
🤖
Введите число доступных пользователю запросов (в день)"""

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
⚙ `admin panel` ⚙
*
/stat - статистика
/select_user - данные пользователя
/setup_telegram_logs - настройка логов
/send_to_users (message) - рассылка
*"""

payment_link_message = """
🤖
Ссылка на оплату: {payment_link}"""

subscription_finished_message = """
🤖🚫
Срок вашей подписки истек. Если вы хотите обновить подписку, перейдите в свой профиль"""

message_to_user_message = """
🤖
Введите текст сообщения"""

message_to_user_sent_message = """
🤖
Сообщение отправлено!"""

set_new_limit_answer = """
🤖
Лимит установлен!"""
