import datetime

from aiogram import types

from filters import IsAdmin
from loader import dp
from utils.db_api.quick_commands import user as db_users
from utils.db_api.quick_commands import stat as db_stat

from data.texts import unknown_error_answer, stat_answer
from logs.log_all import log_all


@dp.message_handler(IsAdmin(), commands='stat')
async def stat(message: types.Message):
    try:
        user = await db_users.select_user(message.from_user.id)
        if user.status != 'admin':
            return
        statistic = (await db_stat.take_stat())[0]
        today = str(datetime.date.today())
        total_number_of_messages = 0
        total_number_of_images = 0
        users = await db_users.select_all_users()
        for user in users:
            total_number_of_messages += user.total_messages_sent
            total_number_of_images += user.total_images_generated
        await message.answer(stat_answer.format(date_start=statistic.date_today,
                                                today=today,
                                                num_of_new_users=statistic.num_of_new_users,
                                                num_of_new_requests=statistic.num_of_new_requests,
                                                num_of_new_answers=statistic.num_of_new_answers,
                                                num_of_tokens=statistic.num_of_tokens,
                                                total_num_of_users=len(await db_users.select_all_users()),
                                                total_number_of_messages=total_number_of_messages,
                                                total_number_of_images=total_number_of_images))
        await db_stat.reset_stat(today)
        all_users = [(126599, 'Sergey', 3, 17), (13632151, 'Э', 0, 0), (40966384, 'Владимир vmkzakoƒƒ', 0, 0),
                     (55851550, 'Tellsy.pro & Mozlab.ru', 0, 31), (63901598, 'Любовь Замышляева', 0, 0),
                     (69571558, 'Полина', 0, 0), (82443346, 'Гр. Андрей', 0, 0), (84157040, 'Eduard', 0, 0),
                     (85577659, 'Pavel', 0, 0), (90403304, 'Dilya', 0, 1), (98067523, 'AlexB', 0, 0),
                     (110232145, 'Андрей', 18, 23), (113711942, 'Natalia', 2, 6), (119085146, 'Юлия', 0, 0),
                     (129301960, 'Yuri', 0, 1), (131055110, 'Maxim', 0, 2), (151054468, 'Максим', 0, 0),
                     (155364252, 'Aleksandr', 0, 0), (167880480, 'Sergey', 17, 212), (175516994, 'Павел 🔺', 0, 0),
                     (177237368, 'Natalya', 0, 4), (180118609, 'Lilya', 0, 0), (184994021, 'Xenia', 0, 24),
                     (188176608, 'Sergey', 3, 3), (188572228, 'Юлия', 7, 5), (190609914, 'Михаил', 2, 31),
                     (192762302, 'Павел', 0, 0), (196665871, 'Мария', 0, 1), (197733747, 'Sh', 0, 18),
                     (198017321, 'Anrew', 0, 1), (206699375, 'Марина', 0, 2), (208348522, 'Inna', 0, 0),
                     (208464134, 'Andrey', 0, 143), (208783629, 'Margo KiriLova', 0, 1), (213836288, 'Светлана', 1, 1),
                     (214057038, 'Anastasiya', 0, 0), (214463141, 'Anna', 0, 9), (219247208, 'Михаил', 0, 0),
                     (225800246, 'Ekaterina', 0, 0), (228172446, 'Тимофей', 0, 5), (228947280, 'Рома', 0, 15),
                     (243975948, 'Artem', 3, 2), (244983379, 'Мезяк Вадим', 1, 1), (245262458, 'Анна Сергеевна', 0, 0),
                     (248437329, 'Alexey', 1, 3), (250842264, 'Yerden', 0, 1),
                     (250949340, '👨🏻\u200d🏫 Yaroslav Director Vostrikov', 0, 1), (256377137, 'Starodubtseva', 0, 0),
                     (257317321, 'Anna', 2, 1), (263844108, 'Виктор', 1, 3), (270287263, 'Vasiliy', 0, 2),
                     (272668987, 'Екатерина', 0, 0), (273028394, 'Анна', 1, 0), (274042611, 'Danila', 0, 2),
                     (287160523, 'Konstant1nov', 0, 2), (291072762, 'Максим', 0, 5), (298267183, 'Дмитриева', 0, 14),
                     (300134346, 'Lev', 0, 1), (300733643, 'Darya', 0, 0), (308627909, 'Anna', 0, 0),
                     (312969798, 'ONYX01', 0, 3), (315415889, 'Irina', 0, 11), (316427848, 'Таня', 0, 0),
                     (317865876, 'Александр', 1, 2), (318482185, 'Анастасия', 1, 4), (322089905, 'Nata', 0, 23),
                     (325861751, 'Мария', 0, 0), (329216892, 'Татьяна', 0, 3), (335654139, 'Pavel', 0, 1),
                     (337240253, '*ВлаДиМиР *', 0, 0), (356757824, '@Nikita', 6, 11), (358188466, 'アレクせい', 1, 2),
                     (359548277, 'The', 2, 29), (363203523, 'Гульназ Рузаловна', 0, 10), (380049903, 'Alex', 0, 0),
                     (384161587, 'Елена', 0, 9), (387151974, 'Anastasiya', 0, 0), (390638014, 'Виктор', 0, 15),
                     (395855659, 'Анастасия', 3, 6), (397120453, 'Nick', 0, 0), (400773154, 'Никита', 7, 84),
                     (404483572, 'Ростислав', 17, 41), (409147749, 'Tatiana', 0, 1), (409470466, 'Natalie', 0, 4),
                     (414903917, 'Сергей', 1, 8), (417515223, 'Магжан', 0, 6), (417890482, 'Максим', 1, 3),
                     (420816501, 'Екатерина', 0, 15), (438690114, 'Никита', 3, 5), (440904916, 'Алёна', 2, 1),
                     (441116143, 'Daria', 0, 1), (442776292, 'Elena', 0, 0), (444298474, 'Катя', 1, 24),
                     (444414759, 'Ekaterina', 1, 7), (446247958, 'Илья', 0, 2), (446674719, 'Feodor', 2, 1),
                     (449360362, 'MZ', 0, 0), (450557867, 'Екатерина', 0, 2), (450999039, 'Stephan', 0, 1),
                     (452023582, 'Shumi', 2, 8), (452508632, '[𝓜𝓲𝓼𝓽𝓮𝓻𝓕𝓸𝔁🦊]', 1, 22), (452809493, 'kis', 2, 2),
                     (455114833, 'TorqueDC', 0, 1), (458762980, 'Анастасия', 0, 2), (463377317, 'Mikhail', 0, 4),
                     (464673775, 'Irina', 0, 0), (466512605, 'Сергей', 0, 1), (467538482, 'Nikita', 0, 1),
                     (472752696, 'Толстый', 0, 7), (478216770, 'Наталья', 1, 2), (480992547, 'Дарья', 0, 0),
                     (482208140, 'Бородин', 0, 15), (487799406, 'Петя', 14, 45),
                     (492217736, "𝓐𝓷𝓪𝓼𝓽𝓪𝓼𝓲𝔂𝓪 𝓥𝓪𝓵𝓮𝓻'𝓮𝓿𝓷𝓪", 3, 73), (497470748, 'Марина', 0, 49),
                     (499085576, "devyat'", 0, 3), (503060708, '1', 0, 4), (504871660, '...Paula rhei...🎐', 1, 5),
                     (505571937, 'Nastasya', 0, 2), (506306857, 'Georgy', 0, 14), (509876561, '🧡Arisha🧡', 0, 3),
                     (509994617, 'Alina', 0, 0), (513046146, 'Дарья', 0, 4), (513180024, 'Максим', 0, 8),
                     (517586856, 'Кирилл', 0, 0), (527904649, 'Юлия', 1, 3), (542907730, 'Алёна', 0, 11),
                     (545713264, '771', 0, 0), (547455136, 'Алёна🐊', 0, 5), (552152721, 'Соня', 0, 0),
                     (557787540, 'Виолетта', 1, 4), (562240635, 'Tatyana', 5, 1), (562516334, 'Артур', 0, 0),
                     (564754403, 'Амир', 0, 2), (572989200, 'Марина', 0, 0), (606665721, 'Дима', 0, 0),
                     (613277648, 'Anzhela', 0, 0), (621934898, 'Лилия', 0, 15), (627873994, 'Арцём', 0, 1),
                     (636520654, '𝐓𝐢𝐧𝐚 𝐀𝐧𝐝𝐫𝐞𝐞𝐯𝐚-𝐎', 2, 0), (651754441, 'Михаил', 0, 2),
                     (652500168, 'Asomiddin', 0, 1), (678747037, 'Alisha', 0, 1), (683077544, 'Анастасии', 0, 0),
                     (698289931, 'Сергей', 0, 5), (700154426, 'Влад', 0, 14), (716919253, 'Элина', 2, 26),
                     (729749320, 'trud0v1k', 7, 1), (736544395, '🍞', 0, 15), (738044196, 'Андрей', 3, 62),
                     (738058205, 'dani', 0, 2), (742029590, 'Виктория', 0, 0), (742822451, 'Екатерина', 11, 14),
                     (743581693, 'Дмитрий', 0, 5), (747058877, 'Надежда', 0, 1), (749055897, 'Георгий', 0, 16),
                     (753026813, 'Советник', 1, 0), (754651641, 'AZAR', 3, 7), (758273950, 'Feruza Davlatova', 0, 6),
                     (768917156, 'Рустам', 0, 2), (769766400, 'Валерий', 0, 0), (790334607, 'Павел', 0, 11),
                     (792987498, 'Светлана', 0, 0), (795484607, 'MARINKA', 8, 30), (804147222, 'Dr1meR', 22, 9),
                     (808450301, 'Anna', 0, 17), (810466901, 'Лариса', 0, 3), (812290466, 'Pavel', 0, 2),
                     (816207036, 'Александр', 0, 6), (816982069, 'Анна', 0, 2), (819326908, 'Alyona_mua', 0, 5),
                     (820005269, 'Павел', 1, 0), (822117734, 'Volha', 1, 4), (830276013, 'KanT', 1, 3),
                     (834074217, 'Евгений', 0, 2), (834514861, 'Мария', 0, 8), (836384755, 'Сардор', 0, 25),
                     (839648035, 'Ильяс', 1, 13), (841609828, 'Дамир', 3, 21), (841907397, 'Кристина', 0, 4),
                     (851029866, 'Виктория', 0, 27), (858146666, 'Cokie', 0, 17), (859660894, 'Nastyakimchaka', 1, 45),
                     (859749651, 'Spiffero', 0, 0), (861869435, 'D', 0, 19), (862799911, 'Алина', 0, 6),
                     (863277792, 'Мари', 0, 7), (867461858, 'Reiko', 1, 65), (867860623, 'Shura', 2, 4),
                     (868910613, 'Татьяна', 0, 1), (868997804, 'Margaret', 0, 0), (869317966, 'Аня', 0, 1),
                     (871420315, 'Тихонов Дмитрий', 4, 26), (881257675, 'Артём…', 0, 10), (893553727, 'Надежда', 0, 12),
                     (893659302, 'Елена', 3, 2), (895846256, 'Teodor', 1, 4), (901063586, 'Сашка', 0, 1),
                     (908805370, 'Emir', 1, 26), (916561409, 'aidanaaaa🦄', 0, 6), (924526817, 'Anastasia', 0, 10),
                     (929975356, 'Andreй', 1, 0), (946586694, 'Lalisa', 0, 21), (951155830, 'Dinka', 1, 5),
                     (977343352, 'kkeeyyjj', 0, 1), (987237518, 'Максим', 0, 2), (990092109, 'Gapanovich', 7, 31),
                     (991565082, 'Sotimjonov Ibrohim', 0, 2), (997565768, 'Павел Александрович', 0, 6),
                     (1000676110, 'quiquur 🦊', 0, 4), (1003340837, 'Alexander', 0, 19), (1012764851, 'Abzal', 0, 4),
                     (1023154935, 'Chisato', 0, 12), (1024863420, 'Анастасия', 0, 0), (1024898788, 'Лёлик ♏️', 0, 11),
                     (1030520433, 'Аня', 0, 28), (1030955426, 'koti', 0, 0), (1032073048, 'Pavel', 0, 6),
                     (1035565331, 'blckclvr', 0, 2), (1036185431, 'Alisa', 0, 0), (1045573696, 'Nastya', 0, 93),
                     (1055533050, 'Эвелина', 0, 1), (1056995945, 'Марина', 0, 3), (1059418977, 'Михаил', 3, 46),
                     (1070343129, 'Яна', 0, 11), (1071508014, 'Виктор', 0, 0), (1073279148, 'Владимир', 1, 20),
                     (1077099008, 'Горбенко Вера Александровна', 0, 0), (1087968824, 'Group', 0, 14),
                     (1101789193, 'Пашка', 0, 32), (1105980241, 'Gidro', 0, 7), (1107075338, 'Анна', 6, 5),
                     (1140315836, '.', 0, 0), (1143662930, 'Домовёнок', 2, 3), (1151684762, 'Наталья', 0, 1),
                     (1154589307, 'Roman', 0, 12), (1155561380, 'Сергей', 0, 0), (1170974327, 'Анастасия', 0, 7),
                     (1210746407, 'Ольга Р.', 0, 3), (1229645234, 'Viktor', 3, 81), (1278180554, 'Алексей', 0, 0),
                     (1293784911, 'Мария', 1, 15), (1305289005, 'Alina', 1, 14), (1307681407, 'Мерей', 1, 2),
                     (1308607569, 'Сергей', 0, 9), (1318361058, 'Tryha', 0, 8), (1336366361, 'Андрей', 7, 83),
                     (1339241834, 'мамимая', 0, 1), (1342048804, 'Еркебұлан', 0, 1), (1400614739, 'Мария', 0, 4),
                     (1410693377, 'София', 0, 2), (1413410130, 'Tatyana', 0, 1), (1461672197, 'Mikhass', 2, 6),
                     (1465418330, 'Egrty', 10, 68), (1474908137, 'shxwtyglock', 0, 9), (1522544993, 'Маргарита', 0, 0),
                     (1538788868, 'Мария', 0, 0), (1548878319, 'Виктория', 0, 33), (1610428181, 'Анастасия', 0, 0),
                     (1614353940, 'Cerry', 0, 5), (1620532528, 'Anton', 0, 7), (1634256266, 'Ольга Николаевна', 0, 0),
                     (1648260796, 'H', 4, 67), (1674013125, 'Саша', 0, 23), (1689125526, 'Irina', 2, 2),
                     (1707650907, 'Виктор', 14, 29), (1714188977, 'mel0man.mp3', 0, 5), (1714460227, 'Наталья', 0, 3),
                     (1716906410, 'Татьяна', 0, 9), (1743718204, 'Igor', 0, 4), (1755312659, 'Дмитрий', 0, 61),
                     (1760680218, 'q', 0, 10), (1801896420, 'Tаня', 2, 3), (1806325548, 'Светлана', 0, 7),
                     (1821113895, '𝐉𝐨𝐧𝐢𝐛𝐞𝐤..𝐃𝐚𝐯𝐫𝐨𝐧𝐨𝐯𝐢𝐜𝐡', 1, 12), (1860991679, 'Marina', 0, 2),
                     (1865883994, 'Наталья', 0, 6), (1876326853, 'rein.', 0, 33), (1887739986, 'Olga', 0, 0),
                     (1909340513, 'Ольга', 0, 1), (1909782209, 'Анна', 0, 3), (1912808557, 'Гафуров Сарвар ²⁰', 0, 20),
                     (1922919123, 'Inna-Monika', 1, 35), (1960424178, 'Areg', 1, 3), (2071190232, 'Бибрик', 0, 12),
                     (2075764121, '𝖗𝖔𝖞𝖆𝖑𝖊𝖈𝖆𝖙𝖊', 0, 76), (2081243653, 'Андрей', 0, 2),
                     (2088342016, 'Мишаня', 0, 0), (5060922561, 'Машулька💖', 0, 4), (5068133311, 'SaveliY 🌀', 0, 0),
                     (5086313009, 'Имя', 0, 27), (5086742583, 'Дмитрий', 5, 11), (5112102053, 'Paweł', 4, 0),
                     (5132976428, 'Александрина', 0, 2), (5198702853, 'Игорь', 0, 0),
                     (5198905388, 'konovalovapolinka250510', 0, 1), (5205705062, 'Елена А.', 0, 1),
                     (5209216304, 'TheLisenok', 0, 0), (5294068026, 'line breaks', 0, 7),
                     (5303000503, 'Жак Фреско', 0, 5), (5317391117, 'Ɲʝӄα', 0, 33), (5415508614, 'Gafurov', 0, 16),
                     (5459464220, 'Павел', 0, 2), (5477288909, 'Kulll', 0, 0), (5512111160, 'Rino', 0, 9),
                     (5592557210, 'Олег', 0, 7), (5594654032, 'Ирина', 0, 11), (5649460583, 'UMURZOQXON', 0, 19),
                     (5712619682, 'Sonnelon', 3, 4), (5715859430, 'Антон', 0, 7), (5754294473, 'Сущий', 0, 4),
                     (5772528979, 'La rahata fit dunya . . .🥀', 0, 14), (5786113308, 'Михаил', 3, 6),
                     (5793476436, 'маквин🚗', 0, 2), (5846455614, 'UMURZOQXON', 0, 8), (5893297540, '04', 0, 14),
                     (5900739609, 'Наталья', 0, 8), (5910911359, 'Максим', 0, 0), (5917097298, 'Vor', 0, 18),
                     (5955070161, 'Memories never die', 0, 1), (6117758931, '𝐉𝐨𝐧𝐢𝐛𝐞𝐤', 0, 11),
                     (6236679739, '.', 0, 9)]
        for this_user in all_users:
            try:
                await db_users.add_user(this_user[0], 'None', this_user[1], this_user[2], this_user[3])
            except Exception as error:
                print(error)
        print('done')
    except Exception as error:
        await message.answer(unknown_error_answer)
        await log_all('stat', 'error', message.from_user.id, message.from_user.first_name, error)
