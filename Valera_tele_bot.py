import telebot
import pymorphy2
from telebot import types
bot = telebot.TeleBot("6141827882:AAFV3VdRzvLGqrhvMVc5PXw2VT9_t0AKVQQ", parse_mode=None)
# Для викторины:
ans = 1
hod = 0
verno = 0
neverno = 0
podskazka = 0
# Пол:
pol = ''
# Для Интересных фактов:
answer = 0
verno_F = 0
podskazka_F = 0


@bot.message_handler(commands=['start'])
def start(message):
    global pol
    markup = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton('Викторина')
    buttonP = types.KeyboardButton('Интересные факты')
    buttonU = types.KeyboardButton('Квест')
    markup.row(button, buttonP, buttonU)
    bot.send_message(message.from_user.id, f'Приветствую, {message.from_user.first_name}!👋 Меня зовут Валера. Вот функции, которые я выполняю: \n'
                                           f'~ Я могу сыграть с тобой в викторину - для этого нажми на кнопку "Викторина" \n'
                                           f'~ Я могу рассказать "Интересные факты" про города с численностью от 50000 человек - для этого нажми на кнопку "Интересные факты" \n'
                                           f'~ Мы можем сыграть в увлекательный квест - для этого нажми кнопку "Квест"',
                     reply_markup=markup)
    morph = pymorphy2.MorphAnalyzer()
    res = morph.parse(message.from_user.first_name)[0]
    if 'NOUN' in res.tag and 'femn' in res.tag:
        pol = 'ж'  # пишет боту девочка
    if 'NOUN' in res.tag and 'masc' in res.tag:
        pol = 'м'  # пишет боту мальчик


@bot.message_handler(content_types=['text'])
def scenari(message):
    global ans, hod, verno, neverno, podskazka, pol, answer, verno_F, podskazka_F
    numbers = ['1', '2', '3']
    if message.text.lower() == 'главная':
        markup = types.ReplyKeyboardMarkup()
        button = types.KeyboardButton('Викторина')
        buttonP = types.KeyboardButton('Интересные факты')
        buttonU = types.KeyboardButton('Квест')
        markup.row(button, buttonP, buttonU)
        bot.send_message(message.from_user.id,
                         f'Приветствую, {message.from_user.first_name}!👋 Меня зовут Валера. Вот функции, которые я выполняю: \n'
                         f'~ Я могу сыграть с тобой в викторину - для этого нажми на кнопку "Викторина" \n'
                         f'~ Я могу рассказать "Интересные факты" про города с численностью от 50000 человек - для этого нажми на кнопку "Интересные факты" \n'
                         f'~ Мы можем сыграть в увлекательный квест - для этого нажми кнопку "Квест"',
                         reply_markup=markup)
    if message.text.lower() == '/help':
        bot.send_message(message.from_user.id,
                         'Я могу подсказать три раза за всю игру! Напиши свой запрос вот так: \n'
                         '"Вопрос №" и добавь номер через пробел вот так: "Вопрос № 1"')
    if message.text.lower() == 'викторина':
        bot.send_message(message.from_user.id, 'Итак, викторина. Но это необычная викторина. Представьте обычную настольную игру, в которой бросаешь кубик и ходишь. \n'
                                               'Нашей игре правила чуть-чуть другие: \n'
                                               '~ Я задаю вопрос, если правильно отвечаешь, то передвигаешься на два хода вперед, если неправильно - на один \n'
                                               '~ Отвечать нужно точно также как записан вариант ответа(в такой же падежной форме) \n'
                                               '~ Всегда можешь вернуться к спику игр при помощи функции "Главная" \n'
                                               '~ Если нужна помощь, то набери функцию /help \n'
                                               '~ Если хочешь досрочно завершить игру ты также можешь набрать функции /stop_play или Главная \n'
                                               'Если правила ясны, то скорее пиши "Начинаем"')
    if message.text.lower() == 'начинаем' or message.text.lower() == 'повторить викторину':
        bot.send_message(message.from_user.id,
                         'Вопрос №1')
        bot.send_message(message.from_user.id,
                         'В честь кого назван Санкт-Петербург? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Петра Первого \n'
                         '2) Апостола Петра \n'
                         '3) Петра Вяземского \n')
        ans = 1
    if ans == 1 and message.text.lower() == 'апостола петра':
        bot.send_message(message.from_user.id,
                         'И это правильный ответ! А вот краткая информация: \n'
                         'Санкт-Петербург назван в честь святого апостола Петра, так как он был основан '
                         'Петром I в 1703 году на месте крепости Ниеншанц, захваченной шведами в 1617 году. '
                         'Петр I выбрал это место, так как оно обладало удобным географическим положением для развития '
                         'торговли и обороны северных границ России. \n')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fistmira.com%2Fuploads%2Fposts%2F2022-04%2Fpetru-ic-biz-s15-in.webp&lr=11091&pos=1&rpt=simage&text=Апостола%20Петра')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №3 ')
        bot.send_message(message.from_user.id,
                         'Какой из этих городов находится на реке Ангара? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Иркутск \n'
                         '2) Якутск \n'
                         '3) Новый Уренгой \n')
        hod += 1
        ans += 2
        verno += 1
    if ans == 1 and (message.text.lower() == 'петра первого' or message.text.lower() == 'петра вяземского'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Апостола Петра \n'
                         '\n'
                         'Санкт-Петербург назван в честь святого апостола Петра, так как он был основан '
                         'Петром I в 1703 году на месте крепости Ниеншанц, захваченной шведами в 1617 году. '
                         'Петр I выбрал это место, так как оно обладало удобным географическим положением для развития '
                         'торговли и обороны северных границ России. \n')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fistmira.com%2Fuploads%2Fposts%2F2022-04%2Fpetru-ic-biz-s15-in.webp&lr=11091&pos=1&rpt=simage&text=Апостола%20Петра')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №2')
        bot.send_message(message.from_user.id,
                         'В каком городе находится этот памятник Сергею Есенину? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Тверь \n'
                         '2) Москва \n'
                         '3) Рязань \n')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9068028%2FyOt7yYbynD2ZZWOffhlbHg3845&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Ffs.tonkosti.ru%2Fsized%2Fc420x200%2F7c%2Flr%2F7clruxfo18soo4cow8scg44gk.jpg&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9068028%2FyOt7yYbynD2ZZWOffhlbHg3845%2Forig')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 2 and message.text.lower() == 'рязань':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'В центре Рязани по соседству с кремлем находится памятник великому русскому поэту  '
                         'Сергею Есенину  - уроженцу Рязанской области. Скульптура была установлена в день 80-летия '
                         'со дня рождения лирика — 2 октября 1975 года.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9068028%2FyOt7yYbynD2ZZWOffhlbHg3845&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Ffs.tonkosti.ru%2Fsized%2Fc420x200%2F7c%2Flr%2F7clruxfo18soo4cow8scg44gk.jpg&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9068028%2FyOt7yYbynD2ZZWOffhlbHg3845%2Forig')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №4 ')
        bot.send_message(message.from_user.id,
                         'Какой из этих городов находится за Полярным Северным кругом? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Охотск \n'
                         '2) Мурманск \n'
                         '3) Красноярск \n')
        hod += 1
        ans += 2
        verno += 1
    if ans == 2 and (message.text.lower() == 'тверь' or message.text.lower() == 'москва'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Рязань \n'
                         '\n'
                         'В центре Рязани по соседству с кремлем находится памятник великому русскому поэту  '
                         'Сергею Есенину  - уроженцу Рязанской области. Скульптура была установлена в день 80-летия '
                         'со дня рождения лирика — 2 октября 1975 года.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9068028%2FyOt7yYbynD2ZZWOffhlbHg3845&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Ffs.tonkosti.ru%2Fsized%2Fc420x200%2F7c%2Flr%2F7clruxfo18soo4cow8scg44gk.jpg&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9068028%2FyOt7yYbynD2ZZWOffhlbHg3845%2Forig')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №3')
        bot.send_message(message.from_user.id,
                         'Какой из этих городов находится на реке Ангара? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Иркутск \n'
                         '2) Якутск \n'
                         '3) Новый Уренгой \n')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 3 and message.text.lower() == 'иркутск':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции про этот город:\n'
                         '\n'
                         'Иркутск – старинный город в России, расположившийся на востоке Сибири, в живописной долине '
                         'реки Ангары. Он является административным центром Иркутской области и одноименного района, '
                         'одним из наиболее развитых в экономической, культурной и научной сферах городов '
                         'Восточно-Сибирского региона.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fvyvoz.org%2Fblog%2Fwp-content%2Fuploads%2F2020%2F10%2Ffederalnyy-proekt-sohranenie-ozera-baykal.jpg&lr=11091&nomisspell=1&pos=0&rpt=simage&source=related-query-serp&text=иркутск%20природа%20байкал')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №5 ')
        bot.send_message(message.from_user.id,
                         'Какой российский город называют "городом невест"? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Кострома \n'
                         '2) Владимир \n'
                         '3) Иваново')
        hod += 1
        ans += 2
        verno += 1
    if ans == 3 and (message.text.lower() == 'якутск' or message.text.lower() == 'новый уренгой'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Иркутск \n'
                         '\n'
                         'Иркутск – старинный город в России, расположившийся на востоке Сибири, в живописной долине '
                         'реки Ангары. Он является административным центром Иркутской области и одноименного района, '
                         'одним из наиболее развитых в экономической, культурной и научной сферах городов '
                         'Восточно-Сибирского региона.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fvyvoz.org%2Fblog%2Fwp-content%2Fuploads%2F2020%2F10%2Ffederalnyy-proekt-sohranenie-ozera-baykal.jpg&lr=11091&nomisspell=1&pos=0&rpt=simage&source=related-query-serp&text=иркутск%20природа%20байкал')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №4')
        bot.send_message(message.from_user.id,
                         'Какой из этих городов находится за Полярным Северным кругом? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Охотск \n'
                         '2) Мурманск \n'
                         '3) Красноярск \n')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 4 and message.text.lower() == 'мурманск':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции про этот город:\n'
                         '\n'
                         'Мурманск – административный центр Мурманской области, расположенной в северо-западном регионе '
                         'России. Город находится на Кольском полуострове, у скалистого побережья одноименного залива, '
                         'принадлежащего к акватории Баренцева моря. Мурманск известен как крупнейший незамерзающий порт '
                         'арктического побережья РФ и самый большой из всех городов в мире, выстроенных за Северным '
                         'полярным кругом.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fimg-fotki.yandex.ru%2Fget%2F39232%2F414616.5c0%2F0_e7757_8ea24cc8_orig.jpg&lr=11091&pos=1&rpt=simage&text=мурманск')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №6 ')
        bot.send_message(message.from_user.id,
                         ' Го́род-геро́й  — высшая степень отличия, которой удостоены двенадцать городов Советского '
                         'Союза, прославившихся своей героической обороной во время Великой Отечественной войны '
                         '1941—1945 годов. На данный момент 9 из них находятся на территории России. '
                         'Укажите российский город, который НЕ является городом-героем. \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Москва \n'
                         '2) Тверь \n'
                         '3) Керчь')
        hod += 1
        ans += 2
        verno += 1
    if ans == 4 and (message.text.lower() == 'охотск' or message.text.lower() == 'красноярск'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Мурманск \n'
                         '\n'
                         'Мурманск – административный центр Мурманской области, расположенной в северо-западном регионе '
                         'России. Город находится на Кольском полуострове, у скалистого побережья одноименного залива, '
                         'принадлежащего к акватории Баренцева моря. Мурманск известен как крупнейший незамерзающий порт '
                         'арктического побережья РФ и самый большой из всех городов в мире, выстроенных за Северным '
                         'полярным кругом.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fimg-fotki.yandex.ru%2Fget%2F39232%2F414616.5c0%2F0_e7757_8ea24cc8_orig.jpg&lr=11091&pos=1&rpt=simage&text=мурманск')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №5')
        bot.send_message(message.from_user.id,
                         'Какой российский город называют "городом невест"? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Кострома \n'
                         '2) Владимир \n'
                         '3) Иваново')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 5 and message.text.lower() == 'иваново':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Город невест — широко распространённое неофициальное название города Иваново.  '
                         'Образ Иванова как города с преобладающим женским населением появился с развитием '
                         'текстильной промышленности. На предприятиях по изготовлению и обработке тканей работало '
                         'большое количество женщин. После Великой Отечественной войны вследствие убыли мужского '
                         'населения демографический перекос усугубился. '
                         'Окончательно прозвище «город невест» закрепилось благодаря песне «Ну чем мы не пара», '
                         'исполненной Андреем Мироновым в фильме «Честный, умный, неженатый…», вышедшем на экраны '
                         'в 1981 году.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fxn--80adbv1agb.xn--p1ai%2Fupload%2Fiblock%2Fd0c%2Fd0ce323cf40d3c744a6411211c425e65.jpg&lr=11091&pos=0&rpt=simage&text=иваново')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №7 ')
        bot.send_message(message.from_user.id,
                         'В какой город, согласно пословице, не стоит ехать со своим самоваром? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Уфу \n'
                         '2) Самару \n'
                         '3) Тулу \n')
        hod += 1
        ans += 2
        verno += 1
    if ans == 5 and (message.text.lower() == 'кострома' or message.text.lower() == 'владимир'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Иваново \n'
                         '\n'
                         'Город невест — широко распространённое неофициальное название города Иваново.  '
                         'Образ Иванова как города с преобладающим женским населением появился с развитием '
                         'текстильной промышленности. На предприятиях по изготовлению и обработке тканей работало '
                         'большое количество женщин. После Великой Отечественной войны вследствие убыли мужского '
                         'населения демографический перекос усугубился. '
                         'Окончательно прозвище «город невест» закрепилось благодаря песне «Ну чем мы не пара», '
                         'исполненной Андреем Мироновым в фильме «Честный, умный, неженатый…», вышедшем на экраны '
                         'в 1981 году.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fxn--80adbv1agb.xn--p1ai%2Fupload%2Fiblock%2Fd0c%2Fd0ce323cf40d3c744a6411211c425e65.jpg&lr=11091&pos=0&rpt=simage&text=иваново')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №6')
        bot.send_message(message.from_user.id,
                         ' Го́род-геро́й  — высшая степень отличия, которой удостоены двенадцать городов Советского '
                         'Союза, прославившихся своей героической обороной во время Великой Отечественной войны '
                         '1941—1945 годов. На данный момент 9 из них находятся на территории России. '
                         'Укажите российский город, который НЕ является городом-героем. \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Москва \n'
                         '2) Тверь \n'
                         '3) Керчь')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 6 and message.text.lower() == 'тверь':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Тверь  не является Городом-героем, но имеет почётное звание "Город воинской славы".')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fcdn.culture.ru%2Fimages%2F0a9776ce-84f1-53cc-8a80-88343fefad2c&lr=11091&pos=0&rpt=simage&text=тверь')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №8 ')
        bot.send_message(message.from_user.id,
                         'Какой из этих городов расположен НЕ на Волге? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Ярославль \n'
                         '2) Киров\n'
                         '3) Чебоксары')
        ans += 2
        hod += 1
        verno += 1
    if ans == 6 and (message.text.lower() == 'москва' or message.text.lower() == 'керчь'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Тверь \n'
                         '\n'
                         'Тверь  не является Городом-героем, но имеет почётное звание "Город воинской славы".'
                         'в 1981 году.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fcdn.culture.ru%2Fimages%2F0a9776ce-84f1-53cc-8a80-88343fefad2c&lr=11091&pos=0&rpt=simage&text=тверь')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №7')
        bot.send_message(message.from_user.id,
                         'В какой город, согласно пословице, не стоит ехать со своим самоваром? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Уфу \n'
                         '2) Самару \n'
                         '3) Тулу \n')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 7 and message.text.lower() == 'тулу':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Впервые это выражение использовал в 1915 году Корней Чуковский в книге '
                         '"О Чехове: человек и мастер" в следующем виде: "Ехать с женой в Париж все равно, что ехать в '
                         'Тулу со своим самоваром."')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fstorage.yandexcloud.net%2Fstorage.yasno.media%2Fnat-geo%2Fimages%2F2019%2F10%2F11%2Fd7cb94233c28455aac96be9344e1fab8.max-1200x800.jpg&lr=11091&pos=0&rpt=simage&text=тула')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №9 ')
        bot.send_message(message.from_user.id,
                         'Герб какого города вы видите? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Ярославля \n'
                         '2) Твери \n'
                         '3) Ставрополя')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=8963679%2FV1hWpAfkNDmWsezRzTNE6A7485&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fyoursticker.ru%2Fwp-content%2Fuploads%2F2021%2F12%2Fgerb-yaroslavlya.jpg&pos=1&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F8963679%2FV1hWpAfkNDmWsezRzTNE6A7485%2Forig')
        ans += 2
        hod += 1
        verno += 1
    if ans == 7 and (message.text.lower() == 'уфу' or message.text.lower() == 'самару'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Тулу \n'
                         '\n'
                         'Впервые это выражение использовал в 1915 году Корней Чуковский в книге '
                         '"О Чехове: человек и мастер" в следующем виде: "Ехать с женой в Париж все равно, что ехать в '
                         'Тулу со своим самоваром."')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fstorage.yandexcloud.net%2Fstorage.yasno.media%2Fnat-geo%2Fimages%2F2019%2F10%2F11%2Fd7cb94233c28455aac96be9344e1fab8.max-1200x800.jpg&lr=11091&pos=0&rpt=simage&text=тула')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №8')
        bot.send_message(message.from_user.id,
                         'Какой из этих городов расположен НЕ на Волге? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Ярославль \n'
                         '2) Киров\n'
                         '3) Чебоксары')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 8 and message.text.lower() == 'киров':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Город Киров расположен на реке Вятке.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fi7.photo.2gis.com%2Fimages%2Fgeo%2F0%2F30258560054875358_0c1a.jpg&lr=11091&pos=0&rpt=simage&text=киров')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №10 ')
        bot.send_message(message.from_user.id,
                         'Продолжите ставшее крылатым выражение из грибоедовского «Горя от ума»: "В деревню, к тетке, в глушь, в ..." \n'
                         '\n '
                         'Варианты ответов:\n'
                         '1) Ростов \n'
                         '2) Саратов \n'
                         '3) Реутов')
        ans += 2
        hod += 1
        verno += 1
    if ans == 8 and (message.text.lower() == 'ярославль' or message.text.lower() == 'чебоксары'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Киров \n'
                         '\n'
                         'Город Киров расположен на реке Вятке.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fi7.photo.2gis.com%2Fimages%2Fgeo%2F0%2F30258560054875358_0c1a.jpg&lr=11091&pos=0&rpt=simage&text=киров')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №9')
        bot.send_message(message.from_user.id,
                         'Герб какого города вы видите? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Ярославля \n'
                         '2) Твери \n'
                         '3) Ставрополя')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=8963679%2FV1hWpAfkNDmWsezRzTNE6A7485&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fyoursticker.ru%2Fwp-content%2Fuploads%2F2021%2F12%2Fgerb-yaroslavlya.jpg&pos=1&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F8963679%2FV1hWpAfkNDmWsezRzTNE6A7485%2Forig')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 9 and message.text.lower() == 'ярославля':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Медведь становится символом Ярославля и Ярославской земли с середины XVII века. Гербовый медведь считался символом предусмотрительности и силы.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=8963679%2FV1hWpAfkNDmWsezRzTNE6A7485&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fyoursticker.ru%2Fwp-content%2Fuploads%2F2021%2F12%2Fgerb-yaroslavlya.jpg&pos=1&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F8963679%2FV1hWpAfkNDmWsezRzTNE6A7485%2Forig')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №11 ')
        bot.send_message(message.from_user.id,
                         'Назовите столицу Чувашской Республики. \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Чебоксары \n'
                         '2) Уфа \n'
                         '3) Ульяновск')
        ans += 2
        hod += 1
        verno += 1
    if ans == 9 and (message.text.lower() == 'твери' or message.text.lower() == 'ставрополя'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Ярославля \n'
                         '\n'
                         'Медведь становится символом Ярославля и Ярославской земли с середины XVII века. Гербовый медведь считался символом предусмотрительности и силы.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=8963679%2FV1hWpAfkNDmWsezRzTNE6A7485&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fyoursticker.ru%2Fwp-content%2Fuploads%2F2021%2F12%2Fgerb-yaroslavlya.jpg&pos=1&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F8963679%2FV1hWpAfkNDmWsezRzTNE6A7485%2Forig')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №10')
        bot.send_message(message.from_user.id,
                         'Продолжите ставшее крылатым выражение из грибоедовского «Горя от ума»: "В деревню, к тетке, в глушь, в ..." \n'
                         '\n '
                         'Варианты ответов:\n'
                         '1) Ростов \n'
                         '2) Саратов \n'
                         '3) Реутов')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 10 and message.text.lower() == 'саратов':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'В пьесе один из главных героев Фамусов обращается к своей дочери со словами: \n'
                         '«Не быть тебе в Москве, не жить тебе с людьми; \n'
                         'Подалее от этих хватов. \n'
                         'В деревню, к тетке, в глушь, в Саратов, \n'
                         'Там будешь горе горевать. \n'
                         'За пяльцами сидеть, за святцами зевать».')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fkartinkin.net%2Fpics%2Fuploads%2Fposts%2F2022-08%2F1660187251_23-kartinkin-net-p-most-saratov-engels-krasivo-foto-27.jpg&lr=11091&pos=7&rpt=simage&text=саратов')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №12 ')
        bot.send_message(message.from_user.id,
                         'Какой из этих городов НЕ был присоединен к территории Руси во время правления Ивана Грозного? \n'
                         '\n'
                         '1) Казань \n'
                         '2) Оренбург \n'
                         '3) Астрахань')
        ans += 2
        hod += 1
        verno += 1
    if ans == 10 and (message.text.lower() == 'ростов' or message.text.lower() == 'реутов'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Саратов \n'
                         '\n'
                         'В пьесе один из главных героев Фамусов обращается к своей дочери со словами: \n'
                         '«Не быть тебе в Москве, не жить тебе с людьми; \n'
                         'Подалее от этих хватов. \n'
                         'В деревню, к тетке, в глушь, в Саратов, \n'
                         'Там будешь горе горевать. \n'
                         'За пяльцами сидеть, за святцами зевать».')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fkartinkin.net%2Fpics%2Fuploads%2Fposts%2F2022-08%2F1660187251_23-kartinkin-net-p-most-saratov-engels-krasivo-foto-27.jpg&lr=11091&pos=7&rpt=simage&text=саратов')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №11')
        bot.send_message(message.from_user.id,
                         'Назовите столицу Чувашской Республики. \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Чебоксары \n'
                         '2) Уфа \n'
                         '3) Ульяновск')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 11 and message.text.lower() == 'чебоксары':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Чебокса́ры  (на чувашском языке - Шупашкар) — город в России, '
                         'столица Чувашской Республики, речной порт на правом берегу реки Волги, при впадении '
                         'в неё реки Чебоксарки.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fputdor.ru%2Fupload%2Fiblock%2Fd4a%2Fd4a52c9beed74f2197431b55961c63e5.jpg&lr=11091&pos=1&rpt=simage&text=чебоксары')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №13 ')
        bot.send_message(message.from_user.id,
                         '')
        ans += 2
        hod += 1
        verno += 1
    if ans == 11 and (message.text.lower() == 'уфа' or message.text.lower() == 'ульяновск'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Чебоксары \n'
                         '\n'
                         'Чебокса́ры  (на чувашском языке - Шупашкар) — город в России, '
                         'столица Чувашской Республики, речной порт на правом берегу реки Волги, при впадении '
                         'в неё реки Чебоксарки.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fputdor.ru%2Fupload%2Fiblock%2Fd4a%2Fd4a52c9beed74f2197431b55961c63e5.jpg&lr=11091&pos=1&rpt=simage&text=чебоксары')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №12')
        bot.send_message(message.from_user.id,
                         'Какой из этих городов НЕ был присоединен к территории Руси во время правления Ивана Грозного? \n'
                         '\n'
                         '1) Казань \n'
                         '2) Оренбург \n'
                         '3) Астрахань')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 12 and message.text.lower() == 'оренбург':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Иван Грозный не захватывал  Оренбург . Город был основан значительно позже - в 1735 году.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fmultiurok.ru%2Fimg%2F132450%2Fimage_5e333ef1cb272.jpg&lr=11091&pos=10&rpt=simage&text=оренбург')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №14 ')
        bot.send_message(message.from_user.id,
                         'О каком городе говорят: "деревянные печи, золотые ворота, железные церкви"? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Владимир \n'
                         '2) Калуга \n'
                         '3) Сочи \n')
        ans += 2
        hod += 1
        verno += 1
    if ans == 12 and (message.text.lower() == 'казань' or message.text.lower() == 'астрахань'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Оренбург \n'
                         '\n'
                         'Иван Грозный не захватывал  Оренбург . Город был основан значительно позже - в 1735 году.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fmultiurok.ru%2Fimg%2F132450%2Fimage_5e333ef1cb272.jpg&lr=11091&pos=10&rpt=simage&text=оренбург')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №13')
        bot.send_message(message.from_user.id,
                         'Какой российский город изображен на купюре достоинством 500 рублей? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Москва \n'
                         '2) Ярославль \n'
                         '3) Архангельск \n')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 13 and message.text.lower() == 'архангельск':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Банкнота посвящена  Архангельску . '
                         'На лицевой стороне банкноты изображен памятник Петру Великому и парусник на фоне морского '
                         'и речного вокзала, а на обратной — панорама Соловецкого монастыря.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=8245426%2FUSqPc53L91T3Rr0ugIyikw9187&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fimgprx.livejournal.net%2Fd5d6bc02a9f8c022e225aaa318402b82ebee871c%2FCJEsUd8f1KH2eqsRxPBAEP58uN9IHfBv7ABrOgkpWDlPL_wD_6SHP9w4RAIlJJKNN4uUHGwll7eeNdCbsVTZqTy48aWX14lwLtHwQ1Zgf0T4CsnxUWnxOuTqxqltzUzkbsYwVyXZgEY6IhpbKPRy6g&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F8245426%2FUSqPc53L91T3Rr0ugIyikw9187%2Forig')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №15 ')
        bot.send_message(message.from_user.id,
                         'Какой российский город  с 7 октября 1932 по 22 октября 1990 года назывался Го́рький? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Загорск \n'
                         '2) Нижний Новгород \n'
                         '3) Киров \n')
        ans += 2
        hod += 1
        verno += 1
    if ans == 13 and (message.text.lower() == 'москва' or message.text.lower() == 'ярославль'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Архангельск \n'
                         '\n'
                         'Банкнота посвящена  Архангельску . '
                         'На лицевой стороне банкноты изображен памятник Петру Великому и парусник на фоне морского '
                         'и речного вокзала, а на обратной — панорама Соловецкого монастыря.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=8245426%2FUSqPc53L91T3Rr0ugIyikw9187&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fimgprx.livejournal.net%2Fd5d6bc02a9f8c022e225aaa318402b82ebee871c%2FCJEsUd8f1KH2eqsRxPBAEP58uN9IHfBv7ABrOgkpWDlPL_wD_6SHP9w4RAIlJJKNN4uUHGwll7eeNdCbsVTZqTy48aWX14lwLtHwQ1Zgf0T4CsnxUWnxOuTqxqltzUzkbsYwVyXZgEY6IhpbKPRy6g&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F8245426%2FUSqPc53L91T3Rr0ugIyikw9187%2Forig')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №14')
        bot.send_message(message.from_user.id,
                         'О каком городе говорят: "деревянные печи, золотые ворота, железные церкви"? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Владимир \n'
                         '2) Калуга \n'
                         '3) Сочи \n')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 14 and message.text.lower() == 'владимир':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Эта пословица о  Владимире . Деревянная печь была в '
                         'архиерейском доме Успенского собора, Золотые ворота - самый известный символ города, а '
                         'железная церковь была у Рождественского монастыря.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fstorage.rentride.ru%2Fuploads%2Fposts%2F2022%2F12%2FQPgZmdNaGcQLICYeYDlecV1hPLCC3WFJZnKjn9rE.webp&lr=11091&pos=0&rpt=simage&text=владимир%20город')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №16 ')
        bot.send_message(message.from_user.id,
                         'В каком городе находится картинная галерея имени И. К. Айвазовского? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Москва \n'
                         '2) Феодосия \n'
                         '3) Севастополь \n')
        ans += 2
        hod += 1
        verno += 1
    if ans == 14 and (message.text.lower() == 'калуга' or message.text.lower() == 'сочи'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Владимир \n'
                         '\n'
                         'Эта пословица о  Владимире . Деревянная печь была в '
                         'архиерейском доме Успенского собора, Золотые ворота - самый известный символ города, а '
                         'железная церковь была у Рождественского монастыря.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fstorage.rentride.ru%2Fuploads%2Fposts%2F2022%2F12%2FQPgZmdNaGcQLICYeYDlecV1hPLCC3WFJZnKjn9rE.webp&lr=11091&pos=0&rpt=simage&text=владимир%20город')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №15')
        bot.send_message(message.from_user.id,
                         'Какой российский город  с 7 октября 1932 по 22 октября 1990 года назывался Го́рький? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Загорск \n'
                         '2) Нижний Новгород \n'
                         '3) Киров \n')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 15 and message.text.lower() == 'нижний новогород':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         '7 октября 1932 года, в ознаменование 40-летней литературной деятельности советского '
                         'писателя Максима Горького, уроженца этого города,  Нижний Новгород был переименован в '
                         'Горький. 22 октября 1990 года  городу было возвращено историческое название.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fmykaleidoscope.ru%2Fx%2Fuploads%2Fposts%2F2022-09%2F1663390645_1-mykaleidoscope-ru-p-nizhnii-novgorod-stolitsa-privolzhya-pinte-1.jpg&lr=11091&pos=0&rpt=simage&text=нижний%20новогород')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №17 ')
        bot.send_message(message.from_user.id,
                         'Какой из этих город находится в России? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Караганда́ \n'
                         '2) Баку́ \n'
                         '3) Махачкала́')
        ans += 2
        hod += 1
        verno += 1
    if ans == 15 and (message.text.lower() == 'загорск' or message.text.lower() == 'киров'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Нижний Новгород \n'
                         '\n'
                         '7 октября 1932 года, в ознаменование 40-летней литературной деятельности советского '
                         'писателя Максима Горького, уроженца этого города,  Нижний Новгород был переименован в '
                         'Горький. 22 октября 1990 года  городу было возвращено историческое название.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fmykaleidoscope.ru%2Fx%2Fuploads%2Fposts%2F2022-09%2F1663390645_1-mykaleidoscope-ru-p-nizhnii-novgorod-stolitsa-privolzhya-pinte-1.jpg&lr=11091&pos=0&rpt=simage&text=нижний%20новогород')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №16')
        bot.send_message(message.from_user.id,
                         'В каком городе находится картинная галерея имени И. К. Айвазовского? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Москва \n'
                         '2) Феодосия \n'
                         '3) Севастополь \n')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 16 and message.text.lower() == 'феодосия':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Этот знаменитый музей маринистической живописи находится в Крыму, в городе  '
                         'Феодосия , где родился и жил Иван Константинович Айвазовский.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fregion82.su%2Fwp-content%2Fuploads%2F2018%2F07%2Fimage.jpg&lr=11091&pos=0&rpt=simage&text=галерея%20имени%20И.%20К.%20Айвазовского%3F')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №18 ')
        bot.send_message(message.from_user.id,
                         'В каком городе был убит русский поэт Михаил Юрьевич Лермонтов? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Армавир \n'
                         '2) Пятигорск \n'
                         '3) Владикавказ')
        ans += 2
        hod += 1
        verno += 1
    if ans == 16 and (message.text.lower() == 'москва' and message.text.lower() == 'севастополь'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Феодосия \n'
                         '\n'
                         'Этот знаменитый музей маринистической живописи находится в Крыму, в городе  '
                         'Феодосия , где родился и жил Иван Константинович Айвазовский.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fregion82.su%2Fwp-content%2Fuploads%2F2018%2F07%2Fimage.jpg&lr=11091&pos=0&rpt=simage&text=галерея%20имени%20И.%20К.%20Айвазовского%3F')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №17')
        bot.send_message(message.from_user.id,
                         'Какой из этих город находится в России? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Караганда́ \n'
                         '2) Баку́ \n'
                         '3) Махачкала́')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 17 and message.text.lower() == 'махачкала':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Караганда́ — город в Казахстане. Баку́ – это столица Азербайджана. '
                         'А  Махачкала́  — город на юге России, столица Республики Дагестан.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Friaderbent.ru%2Fwp-content%2Fuploads%2F2021%2F05%2Fbe0b3367ea9b46b3afa7848f5709b9a6.max-1200x800-1.jpg&lr=11091&pos=1&rpt=simage&text=махачкала')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №19 ')
        bot.send_message(message.from_user.id,
                         'В каком из этих городов России больше миллиона жителей? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Новосибирск \n'
                         '2) Саратов \n'
                         '3) Магадан')
        ans += 2
        hod += 1
        verno += 1
    if ans == 17 and (message.text.lower() == 'караганда' or message.text.lower() == 'баку'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Махачкала \n'
                         '\n'
                         'Караганда́ — город в Казахстане. Баку́ – это столица Азербайджана. '
                         'А  Махачкала́  — город на юге России, столица Республики Дагестан.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Friaderbent.ru%2Fwp-content%2Fuploads%2F2021%2F05%2Fbe0b3367ea9b46b3afa7848f5709b9a6.max-1200x800-1.jpg&lr=11091&pos=1&rpt=simage&text=махачкала')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №18')
        bot.send_message(message.from_user.id,
                         'В каком городе был убит русский поэт Михаил Юрьевич Лермонтов? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Армавир \n'
                         '2) Пятигорск \n'
                         '3) Владикавказ')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 18 and message.text.lower() == 'пятигорск':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Летом 1841 года в  Пятигорске  между Лермонтовым и майором в отставке Николаем Мартыновым '
                         'произошла ссора. Состоялась дуэль. По основной версии, Лермонтов выстрелил вверх, а '
                         'Мартынов — прямо в грудь поэту. 16 (28) августа 1889 в Пятигорске открыли самый первый в '
                         'России памятник поэту.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9661928%2F3NW1M9qkQ2jXfmj0VP9jNw619&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F3%2F3d%2F%25D0%259F%25D0%25B0%25D0%25BC%25D1%258F%25D1%2582%25D0%25BD%25D0%25B8%25D0%25BA_%25D0%259C.%25D0%25AE.%25D0%259B%25D0%25B5%25D1%2580%25D0%25BC%25D0%25BE%25D0%25BD%25D1%2582%25D0%25BE%25D0%25B2%25D1%2583%252C_%25D0%259F%25D1%258F%25D1%2582%25D0%25B8%25D0%25B3%25D0%25BE%25D1%2580%25D1%2581%25D0%25BA%252C_%25D0%25B8%25D1%258E%25D0%25BB%25D1%258C_2015%25D0%25B3%252C.jpg&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9661928%2F3NW1M9qkQ2jXfmj0VP9jNw619%2Forig')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №20 ')
        bot.send_message(message.from_user.id,
                         'Из всех городов России только этот город является единственным, расположенным в субтропической зоне. Какой? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Сочи \n'
                         '2) Геленджик \n'
                         '3) Севастополь')
        ans += 2
        hod += 1
        verno += 1
    if ans == 18 and (message.text.lower() == 'армавир' or message.text.lower() == 'владкавказ'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Пятигорск \n'
                         '\n'
                         'Летом 1841 года в  Пятигорске  между Лермонтовым и майором в отставке Николаем Мартыновым '
                         'произошла ссора. Состоялась дуэль. По основной версии, Лермонтов выстрелил вверх, а '
                         'Мартынов — прямо в грудь поэту. 16 (28) августа 1889 в Пятигорске открыли самый первый в '
                         'России памятник поэту.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9661928%2F3NW1M9qkQ2jXfmj0VP9jNw619&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F3%2F3d%2F%25D0%259F%25D0%25B0%25D0%25BC%25D1%258F%25D1%2582%25D0%25BD%25D0%25B8%25D0%25BA_%25D0%259C.%25D0%25AE.%25D0%259B%25D0%25B5%25D1%2580%25D0%25BC%25D0%25BE%25D0%25BD%25D1%2582%25D0%25BE%25D0%25B2%25D1%2583%252C_%25D0%259F%25D1%258F%25D1%2582%25D0%25B8%25D0%25B3%25D0%25BE%25D1%2580%25D1%2581%25D0%25BA%252C_%25D0%25B8%25D1%258E%25D0%25BB%25D1%258C_2015%25D0%25B3%252C.jpg&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9661928%2F3NW1M9qkQ2jXfmj0VP9jNw619%2Forig')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №19')
        bot.send_message(message.from_user.id,
                         'В каком из этих городов России больше миллиона жителей? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Новосибирск \n'
                         '2) Саратов \n'
                         '3) Магадан')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 19 and message.text.lower() == 'новосибирск':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Новосибирск  является городом-миллионером. Численность населения на 2022 год составляет '
                         '1 621 330 человека. Всего на данный момент в России 16 городов с численностью населения '
                         'более миллиона: Волгоград, Воронеж, Екатеринбург, Казань, Краснодар, Красноярск, Москва, '
                         'Нижний Новгород, Новосибирск, Омск, Пермь, Ростов-на-Дону, Самара, Санкт-Петербург, Уфа, '
                         'Челябинск.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fimg.geliophoto.com%2Fnsk2020w%2F43_nsk2020w.jpg&lr=11091&pos=0&rpt=simage&text=новосибирск')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №21 ')
        bot.send_message(message.from_user.id,
                         'В каком из этих городов России НЕТ метрополитена? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Казань \n'
                         '2) Омск \n'
                         '3) Екатеринбург')
        ans += 2
        hod += 1
        verno += 1
    if ans == 19 and (message.text.lower() == 'саратов' or message.text.lower() == 'магадан'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Новосибирск \n'
                         '\n'
                         'Новосибирск  является городом-миллионером. Численность населения на 2022 год составляет '
                         '1 621 330 человека. Всего на данный момент в России 16 городов с численностью населения '
                         'более миллиона: Волгоград, Воронеж, Екатеринбург, Казань, Краснодар, Красноярск, Москва, '
                         'Нижний Новгород, Новосибирск, Омск, Пермь, Ростов-на-Дону, Самара, Санкт-Петербург, Уфа, '
                         'Челябинск.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fimg.geliophoto.com%2Fnsk2020w%2F43_nsk2020w.jpg&lr=11091&pos=0&rpt=simage&text=новосибирск')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №20')
        bot.send_message(message.from_user.id,
                         'Из всех городов России только этот город является единственным, расположенным в субтропической зоне. Какой? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Сочи \n'
                         '2) Геленджик \n'
                         '3) Севастополь')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 20 and message.text.lower() == 'сочи':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Тёплый субтропический климат - один из важнейших факторов, который привлекает отдыхающих в  Сочи.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fa.d-cd.net%2FcAAAAgOEY-A-1920.jpg&lr=11091&pos=0&rpt=simage&text=сочи')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №22 ')
        bot.send_message(message.from_user.id,
                         'Этот город называют "Ювелирной столицей России", "Сырной столицей России" и "Льняной столицей России". О каком городе речь? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Костроме \n'
                         '2) Вологде \n'
                         '3) Егорьевске')
        ans += 2
        hod += 1
        verno += 1
    if ans == 20 and (message.text.lower() == 'геленджик' or message.text.lower() == 'севастополь'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Сочи \n'
                         '\n'
                         'Тёплый субтропический климат - один из важнейших факторов, который привлекает отдыхающих в  Сочи.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fa.d-cd.net%2FcAAAAgOEY-A-1920.jpg&lr=11091&pos=0&rpt=simage&text=сочи')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №21')
        bot.send_message(message.from_user.id,
                         'В каком из этих городов России НЕТ метрополитена? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Казань \n'
                         '2) Омск \n'
                         '3) Екатеринбург')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 21 and message.text.lower() == 'омск':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'О́мский метрополите́н  — недостроенная и законсервированная система метрополитена. '
                         'Метро в Омске начали строить в 1992 году, но затем строительство неоднократно откладывалось,'
                         'а в мае 2018 года было окончательно прекращено. \n'
                         'Всего в России  семь городов  с действующим метрополитеном: Москва, '
                         'Санкт-Петербург, Нижний Новгород, Казань, Екатеринбург, Новосибирск и Самара.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fbarcaffe.ru%2Fwp-content%2Fuploads%2F2021%2F03%2F04_omsk2020.jpg&lr=11091&pos=7&rpt=simage&text=омск')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №23 ')
        bot.send_message(message.from_user.id,
                         'Назовите самый южный город России. \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Адлер \n'
                         '2) Дербент \n'
                         '3) Грозный')
        ans += 2
        hod += 1
        verno += 1
    if ans == 21 and (message.text.lower() == 'казань' or message.text.lower() == 'екатеренбург'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Омск \n'
                         '\n'
                         'О́мский метрополите́н  — недостроенная и законсервированная система метрополитена. '
                         'Метро в Омске начали строить в 1992 году, но затем строительство неоднократно откладывалось,'
                         'а в мае 2018 года было окончательно прекращено. \n'
                         'Всего в России  семь городов  с действующим метрополитеном: Москва, '
                         'Санкт-Петербург, Нижний Новгород, Казань, Екатеринбург, Новосибирск и Самара.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fbarcaffe.ru%2Fwp-content%2Fuploads%2F2021%2F03%2F04_omsk2020.jpg&lr=11091&pos=7&rpt=simage&text=омск')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №22')
        bot.send_message(message.from_user.id,
                         'Этот город называют "Ювелирной столицей России", "Сырной столицей России" и "Льняной столицей России". О каком городе речь? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Костроме \n'
                         '2) Вологде \n'
                         '3) Егорьевске')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 22 and message.text.lower() == 'костроме':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Все эти туристические бренды относятся к  Костроме. \n'
                         'Кострому называют ювелирной столицей России, т.к. в течение нескольких столетий здесь '
                         'развивался ювелирный промысел. Почти 80% ювелирных изделий, продаваемых на прилавках в других '
                         'российских городах, – продукция костромского и красносельского производства. \n'
                         'Сырами Кострома славится со второй половины XIX века, когда здесь открылась '
                         'первая сыроварня. Сейчас в Костромской области насчитывают порядка 11 крупных сырных производств.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fi.pinimg.com%2Foriginals%2Fa1%2F47%2F7b%2Fa1477bf29f20cff85cfb139984002237.jpg&lr=11091&pos=0&rpt=simage&text=кострома')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №24 ')
        bot.send_message(message.from_user.id,
                         'Какой из этих городов основал НЕ Юрий Долгорукий? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Москва \n'
                         '2) Переславль \n'
                         '3) Углич')
        ans += 2
        hod += 1
        verno += 1
    if ans == 22 and (message.text.lower() == 'вологде' or message.text.lower() == 'егорьевске'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Костроме \n'
                         '\n'
                         'Все эти туристические бренды относятся к  Костроме. \n'
                         'Кострому называют ювелирной столицей России, т.к. в течение нескольких столетий здесь '
                         'развивался ювелирный промысел. Почти 80% ювелирных изделий, продаваемых на прилавках в других '
                         'российских городах, – продукция костромского и красносельского производства. \n'
                         'Сырами Кострома славится со второй половины XIX века, когда здесь открылась '
                         'первая сыроварня. Сейчас в Костромской области насчитывают порядка 11 крупных сырных производств.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fi.pinimg.com%2Foriginals%2Fa1%2F47%2F7b%2Fa1477bf29f20cff85cfb139984002237.jpg&lr=11091&pos=0&rpt=simage&text=кострома')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №23')
        bot.send_message(message.from_user.id,
                         'Назовите самый южный город России. \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Адлер \n'
                         '2) Дербент \n'
                         '3) Грозный')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 23 and message.text.lower() == 'дербент':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Дербе́нт - это город на юге России в Республике Дагестан. '
                         'Город расположен на западном побережье Каспийского моря и является самым южным в России.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fi.siteapi.org%2FwRh250WJXzRLeb3d7Jq3Fi2ueAM%3D%2F0x0%3A1100x703%2Fs.siteapi.org%2F6d8a5ead61a49b5%2Fimg%2F5aq7mic35yscoswkk08swcokokksc8&lr=11091&pos=2&rpt=simage&text=дербент')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №25 ')
        bot.send_message(message.from_user.id,
                         'Какой российский город называют "колыбелью космонавтики"? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Курск \n'
                         '2) Тверь \n'
                         '3) Калугу')
        ans += 2
        hod += 1
        verno += 1
    if ans == 23 and (message.text.lower() == 'адлер' or message.text.lower() == 'грозный'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Костроме \n'
                         '\n'
                         'Дербе́нт - это город на юге России в Республике Дагестан. '
                         'Город расположен на западном побережье Каспийского моря и является самым южным в России.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fi.siteapi.org%2FwRh250WJXzRLeb3d7Jq3Fi2ueAM%3D%2F0x0%3A1100x703%2Fs.siteapi.org%2F6d8a5ead61a49b5%2Fimg%2F5aq7mic35yscoswkk08swcokokksc8&lr=11091&pos=2&rpt=simage&text=дербент')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №24')
        bot.send_message(message.from_user.id,
                         'Какой из этих городов основал НЕ Юрий Долгорукий? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Москва \n'
                         '2) Переславль \n'
                         '3) Углич')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 24 and message.text.lower() == 'углич':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Углич основан в 937 году родственником княгини Ольги Киевской - Яном Плесковичем.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Ftop7travel.ru%2Fwp-content%2Fuploads%2F2021%2F12%2FUglich.jpg&lr=11091&pos=0&rpt=simage&text=углич')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №26 ')
        bot.send_message(message.from_user.id,
                         '')
        ans += 2
        hod += 1
        verno += 1
    if ans == 24 and (message.text.lower() == 'москва' or message.text.lower() == 'переславль'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Углич \n'
                         '\n'
                         'Углич основан в 937 году родственником княгини Ольги Киевской - Яном Плесковичем.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Ftop7travel.ru%2Fwp-content%2Fuploads%2F2021%2F12%2FUglich.jpg&lr=11091&pos=0&rpt=simage&text=углич')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №25')
        bot.send_message(message.from_user.id,
                         'Какой российский город называют "колыбелью космонавтики"? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Курск \n'
                         '2) Тверь \n'
                         '3) Калугу')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 25 and message.text.lower() == 'калугу':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         '"Колыбелью космонавтики" называют  Калугу , т.к. с 1892 по '
                         '1935 год в этом городе жил и работал теоретик космонавтики, выдающийся изобретатель '
                         'К. Э. Циолковский.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9642991%2F_ftktfvW7_Bn6MD0Ppg9cw5844&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fbelator.ru%2Fwp-content%2Fuploads%2F2021%2F09%2Fbfa95a23f9ba4c35eebe441bbeb4f716-150x150.jpg&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9642991%2F_ftktfvW7_Bn6MD0Ppg9cw5844%2Forig')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №27 ')
        bot.send_message(message.from_user.id,
                         'В каком городе России находится мечеть Кул-Шариф? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Уфа \n'
                         '2) Казань \n'
                         '3) Йошкар-Ола')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9635807%2FJqXn6RdryFF8EouL4mgRkw6241&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fallovertheus.ru%2Fwp-content%2Fuploads%2F2020%2F01%2Fistoriya-i-osobennosti-mecheti-kul-sharif-v-kazanskom-kremle-scaled.jpg&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9635807%2FJqXn6RdryFF8EouL4mgRkw6241%2Forig')
        ans += 2
        hod += 1
        verno += 1
    if ans == 25 and (message.text.lower() == 'курск' or message.text.lower() == 'тверь'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Калугу \n'
                         '\n'
                         '"Колыбелью космонавтики" называют  Калугу , т.к. с 1892 по '
                         '1935 год в этом городе жил и работал теоретик космонавтики, выдающийся изобретатель '
                         'К. Э. Циолковский.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9642991%2F_ftktfvW7_Bn6MD0Ppg9cw5844&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fbelator.ru%2Fwp-content%2Fuploads%2F2021%2F09%2Fbfa95a23f9ba4c35eebe441bbeb4f716-150x150.jpg&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9642991%2F_ftktfvW7_Bn6MD0Ppg9cw5844%2Forig')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №26')
        bot.send_message(message.from_user.id,
                         'Какой город НЕ входит в "Золотое Кольцо России"? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Кострома \n'
                         '2) Пенза \n'
                         '3) Ярославль')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 26 and message.text.lower() == 'пенза':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Золото́е кольцо́ Росси́и  — туристический маршрут, проходящий по древним городам '
                         'Северо-Восточной Руси, в которых сохранились уникальные памятники истории и культуры '
                         'России и центры народных ремёсел. Автор термина и самой идеи кольцевого маршрута — '
                         'журналист и литератор Юрий Бычков. В Золотое кольцо традиционно включают восемь основных '
                         'городов — Сергиев Посад, Переславль-Залесский, Ростов, Ярославль, Кострома, Иваново, Суздаль '
                         'и Владимир. Включение других городов является дискуссионным. \n'
                         'Пенза в Золотое кольцо не входит, её кандидатура даже не рассматривается.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?img_url=http%3A%2F%2Fcs11.pikabu.ru%2Fpost_img%2Fbig%2F2020%2F12%2F02%2F4%2F1606888758159075111.jpg&lr=11091&pos=0&rpt=simage&text=пенза')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №28 ')
        bot.send_message(message.from_user.id,
                         'Город Екатеринбург назван в честь... \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Екатерины I \n'
                         '2) Екатерины II \n'
                         '3) Екатерины Медичи')
        ans += 2
        hod += 1
        verno += 1
    if ans == 26 and (message.text.lower() == 'кострома' or message.text.lower() == 'ярославль'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Пенза \n'
                         '\n'
                         'Золото́е кольцо́ Росси́и  — туристический маршрут, проходящий по древним городам '
                         'Северо-Восточной Руси, в которых сохранились уникальные памятники истории и культуры '
                         'России и центры народных ремёсел. Автор термина и самой идеи кольцевого маршрута — '
                         'журналист и литератор Юрий Бычков. В Золотое кольцо традиционно включают восемь основных '
                         'городов — Сергиев Посад, Переславль-Залесский, Ростов, Ярославль, Кострома, Иваново, Суздаль '
                         'и Владимир. Включение других городов является дискуссионным. \n'
                         'Пенза в Золотое кольцо не входит, её кандидатура даже не рассматривается.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?img_url=http%3A%2F%2Fcs11.pikabu.ru%2Fpost_img%2Fbig%2F2020%2F12%2F02%2F4%2F1606888758159075111.jpg&lr=11091&pos=0&rpt=simage&text=пенза')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №27')
        bot.send_message(message.from_user.id,
                         'В каком городе России находится мечеть Кул-Шариф? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Уфа \n'
                         '2) Казань \n'
                         '3) Йошкар-Ола')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9635807%2FJqXn6RdryFF8EouL4mgRkw6241&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fallovertheus.ru%2Fwp-content%2Fuploads%2F2020%2F01%2Fistoriya-i-osobennosti-mecheti-kul-sharif-v-kazanskom-kremle-scaled.jpg&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9635807%2FJqXn6RdryFF8EouL4mgRkw6241%2Forig')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 27 and message.text.lower() == 'казань':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Мечеть «Кул-Шариф»  — главная соборная джума-мечеть республики Татарстан и '
                         'города Казани. Расположена на территории Казанского кремля. Является одной из главных '
                         'достопримечательностей города.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9635807%2FJqXn6RdryFF8EouL4mgRkw6241&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fallovertheus.ru%2Fwp-content%2Fuploads%2F2020%2F01%2Fistoriya-i-osobennosti-mecheti-kul-sharif-v-kazanskom-kremle-scaled.jpg&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9635807%2FJqXn6RdryFF8EouL4mgRkw6241%2Forig')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №29 ')
        bot.send_message(message.from_user.id,
                         'В кремле этого города снимали сцены старой Москвы в фильме "Иван Васильевич меняет профессию". Назовите этот город. \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Дмитров \n'
                         '2) Ростов \n'
                         '3) Коломна')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9610900%2FAN5QDdPyuRJz6i-0vd_OMA6898&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fextraguide.ru%2Fimages%2Fsp%2Ffed3fed6c2dd0f74985b0ec37f7b4fc9d529310e.jpg&pos=1&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9610900%2FAN5QDdPyuRJz6i-0vd_OMA6898%2Forig')
        ans += 2
        hod += 1
        verno += 1
    if ans == 27 and (message.text.lower() == 'уфа' or message.text.lower() == 'йошкар-ола'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Казань \n'
                         '\n'
                         'Мечеть «Кул-Шариф»  — главная соборная джума-мечеть республики Татарстан и '
                         'города Казани. Расположена на территории Казанского кремля. Является одной из главных '
                         'достопримечательностей города.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9635807%2FJqXn6RdryFF8EouL4mgRkw6241&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fallovertheus.ru%2Fwp-content%2Fuploads%2F2020%2F01%2Fistoriya-i-osobennosti-mecheti-kul-sharif-v-kazanskom-kremle-scaled.jpg&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9635807%2FJqXn6RdryFF8EouL4mgRkw6241%2Forig')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №28')
        bot.send_message(message.from_user.id,
                         'Город Екатеринбург назван в честь... \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Екатерины I \n'
                         '2) Екатерины II \n'
                         '3) Екатерины Медичи')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 28 and message.text.lower() == 'екатерины I':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Весной 1723 года по указу императора Петра I на берегах реки Исети развернулось строительство '
                         'крупнейшего в России железоделательного завода. Завод-крепость нарекли Екатеринбургом  '
                         'в честь императрицы Екатерины I , супруги Петра I.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?img_url=http%3A%2F%2Fxn--e1adcaacuhnujm.xn--p1ai%2Fwp-content%2Fuploads%2F2019%2F11%2F1_ekaterina-1.jpg&lr=11091&pos=1&rpt=simage&text=екатерина%201')
        bot.send_message(message.from_user.id,
                         'И ты переходишь на два хода вперед! А это значит ты пропускаешь одну клетку = один вопрос')
        bot.send_message(message.from_user.id,
                         'Вопрос №30 ')
        bot.send_message(message.from_user.id,
                         'В каком городе находится этот памятник? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Ростов-на-Дону \n'
                         '2) Волгоград \n'
                         '3) Краснодар')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9148391%2FaASL_U0iAvGQUsOepdh7eQ7185&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fmockva.ru%2Fwp-content%2Fuploads%2F2021%2F01%2Fsnimok-ekrana-2-1-770x400.png&pos=7&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9148391%2FaASL_U0iAvGQUsOepdh7eQ7185%2Forig')
        ans += 2
        hod += 1
        verno += 1
    if ans == 28 and (message.text.lower() == 'екатерины II' or message.text.lower() == 'екатерины медичи'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Екатерины I \n'
                         '\n'
                         'Весной 1723 года по указу императора Петра I на берегах реки Исети развернулось строительство '
                         'крупнейшего в России железоделательного завода. Завод-крепость нарекли Екатеринбургом  '
                         'в честь императрицы Екатерины I , супруги Петра I.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?img_url=http%3A%2F%2Fxn--e1adcaacuhnujm.xn--p1ai%2Fwp-content%2Fuploads%2F2019%2F11%2F1_ekaterina-1.jpg&lr=11091&pos=1&rpt=simage&text=екатерина%201')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №29')
        bot.send_message(message.from_user.id,
                         'В кремле этого города снимали сцены старой Москвы в фильме "Иван Васильевич меняет профессию". Назовите этот город. \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Дмитров \n'
                         '2) Ростов \n'
                         '3) Коломна')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9610900%2FAN5QDdPyuRJz6i-0vd_OMA6898&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fextraguide.ru%2Fimages%2Fsp%2Ffed3fed6c2dd0f74985b0ec37f7b4fc9d529310e.jpg&pos=1&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9610900%2FAN5QDdPyuRJz6i-0vd_OMA6898%2Forig')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 29 and message.text.lower() == 'ростов':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Фильм Леонида Гайдая «Иван Васильевич меняет профессию» снимался в  Ростовском кремле . '
                         'Главное участие в фильме принимала звонница – там снимали сцену погони.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=2225081%2FPS2uv44EBVWlq20pKzqcLQ7035&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fcs9.pikabu.ru%2Fpost_img%2Fbig%2F2017%2F08%2F19%2F8%2F1503148329131253862.png&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F2225081%2FPS2uv44EBVWlq20pKzqcLQ7035%2Forig')
        bot.send_message(message.from_user.id,
                         'Итак, остался последний вопрос!')
        bot.send_message(message.from_user.id,
                         'Вопрос №30 ')
        bot.send_message(message.from_user.id,
                         'В каком городе находится этот памятник? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Ростов-на-Дону \n'
                         '2) Волгоград \n'
                         '3) Краснодар')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9148391%2FaASL_U0iAvGQUsOepdh7eQ7185&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fmockva.ru%2Fwp-content%2Fuploads%2F2021%2F01%2Fsnimok-ekrana-2-1-770x400.png&pos=7&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9148391%2FaASL_U0iAvGQUsOepdh7eQ7185%2Forig')
        ans += 2
        hod += 1
        verno += 1
    if ans == 29 and (message.text.lower() == 'дмитров' or message.text.lower() == 'коломна'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Екатерины I \n'
                         '\n'
                         'Фильм Леонида Гайдая «Иван Васильевич меняет профессию» снимался в  Ростовском кремле . '
                         'Главное участие в фильме принимала звонница – там снимали сцену погони.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=2225081%2FPS2uv44EBVWlq20pKzqcLQ7035&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fcs9.pikabu.ru%2Fpost_img%2Fbig%2F2017%2F08%2F19%2F8%2F1503148329131253862.png&pos=0&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F2225081%2FPS2uv44EBVWlq20pKzqcLQ7035%2Forig')
        bot.send_message(message.from_user.id,
                         'Ты переходишь на один ход вперед! Следующий вопрос...\n'
                         'Вопрос №30')
        bot.send_message(message.from_user.id,
                         'В каком городе находится этот памятник? \n'
                         '\n'
                         'Варианты ответов: \n'
                         '1) Ростов-на-Дону \n'
                         '2) Волгоград \n'
                         '3) Краснодар')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9148391%2FaASL_U0iAvGQUsOepdh7eQ7185&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fmockva.ru%2Fwp-content%2Fuploads%2F2021%2F01%2Fsnimok-ekrana-2-1-770x400.png&pos=7&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9148391%2FaASL_U0iAvGQUsOepdh7eQ7185%2Forig')
        ans += 1
        hod += 1
        neverno += 1
    if ans == 30 and message.text.lower() == 'волгоград':
        bot.send_message(message.from_user.id,
                         'Правильно! А вот немного информции:\n'
                         '\n'
                         'Скульпту́ра «Ро́дина-мать зовёт!»  — композиционный центр памятника-ансамбля '
                         '«Героям Сталинградской битвы» на Мамаевом кургане в  Волгограде . '
                         'Это одна из самых высоких статуй мира - ее высота 85 м.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9148391%2FaASL_U0iAvGQUsOepdh7eQ7185&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fmockva.ru%2Fwp-content%2Fuploads%2F2021%2F01%2Fsnimok-ekrana-2-1-770x400.png&pos=7&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9148391%2FaASL_U0iAvGQUsOepdh7eQ7185%2Forig')
        ans += 2
        hod += 1
        verno += 1
        if pol == 'ж':
            bot.send_message(message.from_user.id,
                             f'Молодец, викторина окончена, а сейчас подведем итоги. \n'
                             f'Количество вопросов, на которые ты ответила верно: {verno} \n'
                             f'Количество вопросов, на которые ты ответила неверно: {neverno} \n'
                             f'Количество ходов, сделанных за игру: {hod} \n'
                             f'Количество использованных подсказок: {podskazka} \n'
                             f'Если захочешь повторить, то пиши "Повторить викторину"')
        if pol == 'м':
            bot.send_message(message.from_user.id,
                             f'Молодец, викторина окончена, а сейчас подведем итоги. \n'
                             f'Количество вопросов, на которые ты ответил верно: {verno} \n'
                             f'Количество вопросов, на которые ты ответил неверно: {neverno} \n'
                             f'Количество ходов, сделанных за игру: {hod} \n'
                             f'Количество использованных подсказок: {podskazka} \n'
                             f'Если захочешь повторить, то пиши "Повторить викторину"')
        hod = 0
        verno = 0
        neverno = 0
        ans = 1
        podskazka = 0
    if ans == 30 and (message.text.lower() == 'ростов-на-дону' or message.text.lower() == 'краснодар'):
        bot.send_message(message.from_user.id,
                         'К сожалению, ты ответил неверно... Правильный ответ: Волгоград \n'
                         '\n'
                         'Скульпту́ра «Ро́дина-мать зовёт!»  — композиционный центр памятника-ансамбля '
                         '«Героям Сталинградской битвы» на Мамаевом кургане в  Волгограде . '
                         'Это одна из самых высоких статуй мира - ее высота 85 м.')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?cbir_id=9148391%2FaASL_U0iAvGQUsOepdh7eQ7185&cbir_page=similar&cbird=5&img_url=http%3A%2F%2Fmockva.ru%2Fwp-content%2Fuploads%2F2021%2F01%2Fsnimok-ekrana-2-1-770x400.png&pos=7&rpt=imageview&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F9148391%2FaASL_U0iAvGQUsOepdh7eQ7185%2Forig')
        ans += 1
        hod += 1
        neverno += 1
        if pol == 'ж':
            bot.send_message(message.from_user.id,
                             f'Молодец, викторина окончена, а сейчас подведем итоги. \n'
                             f'Количество вопросов, на которые ты ответила верно: {verno} \n'
                             f'Количество вопросов, на которые ты ответила неверно: {neverno} \n'
                             f'Количество ходов, сделанных за игру: {hod} \n'
                             f'Количество использованных подсказок: {podskazka} \n'
                             f'Если захочешь повторить, то пиши "Повторить викторину"')
        if pol == 'м':
            bot.send_message(message.from_user.id,
                             f'Молодец, викторина окончена, а сейчас подведем итоги. \n'
                             f'Количество вопросов, на которые ты ответил верно: {verno} \n'
                             f'Количество вопросов, на которые ты ответил неверно: {neverno} \n'
                             f'Количество ходов, сделанных за игру: {hod} \n'
                             f'Количество использованных подсказок: {podskazka} \n'
                             f'Если захочешь повторить, то пиши "Повторить викторину"')
        hod = 0
        verno = 0
        neverno = 0
        ans = 1
        podskazka = 0
    if message.text.lower() == '/stop_play':
        if pol == 'ж':
            bot.send_message(message.from_user.id,
                             f'Жалко, что ты уже уходишь. Ну чтож итоги: \n'
                             f'Количество вопросов, на которые ты ответила верно: {verno} \n'
                             f'Количество вопросов, на которые ты ответила неверно: {neverno} \n'
                             f'Количество ходов, сделанных за игру: {hod} \n'
                             f'Количество использованных подсказок: {podskazka} \n'
                             f'Если захочешь повторить, то пиши "Повторить викторину"')
        if pol == 'м':
            bot.send_message(message.from_user.id,
                             f'Жалко, что ты уже уходишь. Ну чтож итоги: \n'
                             f'Количество вопросов, на которые ты ответил верно: {verno} \n'
                             f'Количество вопросов, на которые ты ответил неверно: {neverno} \n'
                             f'Количество ходов, сделанных за игру: {hod} \n'
                             f'Количество использованных подсказок: {podskazka} \n'
                             f'Если захочешь повторить, то пиши "Повторить викторину"')
        hod = 0
        verno = 0
        neverno = 0
        ans = 1
        podskazka = 0
    if message.text.lower() == 'вопрос № 1':
        bot.send_message(message.from_user.id,
                         'Ответ: Апостола Петра')
        podskazka += 1
    if message.text.lower() == 'вопрос № 2':
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Рязань')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Рязань')
            podskazka += 1
    if message.text.lower() == 'вопрос № 3':
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Иркутск')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Иркутск')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Иркутск')
            podskazka += 1
    if message.text.lower() == 'вопрос № 4':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Мурманск')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Мурманск')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Мурманск')
            podskazka += 1
    if message.text.lower() == 'вопрос № 5':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Иваново')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Иваново')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Иваново')
            podskazka += 1
    if message.text.lower() == 'вопрос № 6':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Тверь')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Тверь')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Тверь')
            podskazka += 1
    if message.text.lower() == 'вопрос № 7':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Тулу')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Тулу')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Тулу')
            podskazka += 1
    if message.text.lower() == 'вопрос № 8':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Киров')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Киров')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Киров')
            podskazka += 1
    if message.text.lower() == 'вопрос № 9':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Ярославля')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Ярославля')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Ярославля')
            podskazka += 1
    if message.text.lower() == 'вопрос № 10':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Саратов')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Саратов')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Саратов')
            podskazka += 1
    if message.text.lower() == 'вопрос № 11':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Чебоксары')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Чебоксары')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Чебоксары')
            podskazka += 1
    if message.text.lower() == 'вопрос № 12':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Оренбург')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Оренбург')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Оренбург')
            podskazka += 1
    if message.text.lower() == 'вопрос № 13':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Архангельск')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Архангельск')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Архангельск')
            podskazka += 1
    if message.text.lower() == 'вопрос № 14':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Владимир')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Владимир')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Владимир')
            podskazka += 1
    if message.text.lower() == 'вопрос № 15':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Нижний Новгород')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Нижний Новгород')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Нижний Новгород')
            podskazka += 1
    if message.text.lower() == 'вопрос № 16':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Феодосия')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Феодосия')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Феодосия')
            podskazka += 1
    if message.text.lower() == 'вопрос № 17':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Махачкала')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Махачкала')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Махачкала')
            podskazka += 1
    if message.text.lower() == 'вопрос № 18':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Пятигорск')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Пятигорск')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Пятигорск')
            podskazka += 1
    if message.text.lower() == 'вопрос № 19':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Новосибирск')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Новосибирск')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Новосибирск')
            podskazka += 1
    if message.text.lower() == 'вопрос № 20':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Сочи')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Сочи')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Сочи')
            podskazka += 1
    if message.text.lower() == 'вопрос № 21':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Омск')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Омск')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Омск')
            podskazka += 1
    if message.text.lower() == 'вопрос № 22':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Костроме')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Костроме')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Костроме')
            podskazka += 1
    if message.text.lower() == 'вопрос № 23':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Дербент')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Дербент')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Дербент')
            podskazka += 1
    if message.text.lower() == 'вопрос № 24':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Углич')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Углич')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Углич')
            podskazka += 1
    if message.text.lower() == 'вопрос № 25':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Калугу')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Калугу')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Калугу')
            podskazka += 1
    if message.text.lower() == 'вопрос № 26':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Пенза')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Пенза')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Пенза')
            podskazka += 1
    if message.text.lower() == 'вопрос № 27':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Казань')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Казань')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Казань')
            podskazka += 1
    if message.text.lower() == 'вопрос № 28':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Екатерины I')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Екатерины I')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Екатерины I')
            podskazka += 1
    if message.text.lower() == 'опрос № 29':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Ростов')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Ростов')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Ростов')
            podskazka += 1
    if message.text.lower() == 'вопрос № 30':
        if podskazka == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились подсказки...')
        if podskazka == 2:
            bot.send_message(message.from_user.id,
                             'Ответ: Волгоград')
            podskazka += 1
        if podskazka == 1:
            bot.send_message(message.from_user.id,
                             'Ответ: Волгоград')
            podskazka += 1
        if podskazka == 0:
            bot.send_message(message.from_user.id,
                             'Ответ: Волгоград')
            podskazka += 1
    if message.text in numbers:
        bot.send_message(message.from_user.id,
                         'Отвечать нужно точно также как записан вариант ответа(в такой же падежной форме)')
    if message.text.lower() == 'интересные факты' or message.text.lower() == 'повторить интересные факты':
        if pol == 'ж':
            bot.send_message(message.from_user.id,
                             '"Интересные факты". Простые правила использования: \n'
                             '~ Я рассказываю про любой город РФ \n'
                             '~ Ты должена догадаться о каком городе идет речь \n'
                             '~ На всю игру тебе даются 3 подсказки и чтобы ее полчить напиши: "Помоги"\n'
                             '~ Ты можешь досрочно закончить игру написав: "/stop_fact" или "Главная" \n'
                             '~ Если ты вводишь неверно название, то я буду ждать пока ты назовешь верное \n'
                             'Если готова, то скорее пиши: "Готова"')
        if pol == 'м':
            bot.send_message(message.from_user.id,
                             '"Интересные факты". Простые правила использования: \n'
                             '~ Я рассказываю про любой город РФ \n'
                             '~ Ты должен догадаться о каком городе идет речь \n'
                             '~ На всю игру тебе даются 3 подсказки и чтобы ее полчить напиши: "Помоги"\n'
                             '~ Ты можешь досрочно закончить игру написав: "/stop_fact" или "Главная" \n'
                             '~ Если ты вводишь неверно название, то я буду ждать пока ты назовешь верное \n'
                             'Если готов, то скорее пиши: "Готов"')
    if message.text.lower() == 'готов' or message.text.lower() == 'готова':
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fkrot.info%2Fuploads%2Fposts%2F2021-12%2F1640788740_2-krot-info-p-abakan-stolitsa-krasivo-foto-2.jpg&lr=11091&pos=0&rpt=simage&text=абакан')
        bot.send_message(message.from_user.id,
                         'Город №1: \n'
                         'Находится на 53-й параллели северной широты. То есть — на одной параллели с Минском, Гамбургом и Магнитогорском. \n'
                         'Он входит в популярный туристический маршрут «Саянское кольцо». \n'
                         'Официально основан в 1931 году \n'
                         'Здесь проживает всего порядка 180 тысяч человек. Из них около 12% составляют хакасы (коренное население). \n'
                         'Находится единственная в Сибири детско-юношеская школа ЦСКА.')
        answer += 1
    if answer == 1 and message.text.lower() == 'абакан':
        bot.send_message(message.from_user.id,
                            'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fklintsy.ru%2Ffoto%2Fbfoto%2F11859_342795.jpg&lr=11091&pos=0&rpt=simage&text=клинцы')
        bot.send_message(message.from_user.id,
                         'Город №2: \n'
                         'Современная территория города находилась под управлением Польши, Украины. \n'
                         'Именно поэтому город называли «Манчестером Черниговской губернии». \n'
                         'Город был яблочной провинцией. \n'
                         'Автокраны этого города первыми проехали по мосту через Керченский пролив.\n')
        verno_F += 1
        answer += 1
    if answer == 2 and message.text.lower() == 'клинцы':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fsdelanounas.ru%2Fi%2Fa%2Fw%2F1%2Ff_aW1nLmdlbGlvcGhvdG8uY29tL2JpeXNrLzA3X2JpeXNrLmpwZz9fX2lkPTE0ODA0MA%3D%3D.jpeg&lr=11091&pos=0&rpt=simage&text=бийск')
        bot.send_message(message.from_user.id,
                         'Город №3: \n'
                         'Входит в число шести городов России, которые построили по личному указу Петра I. \n'
                         'Располагается уникальный памятник Владимиру Ленину — его особенность в том, что вождь изображен в пальто и зимней шапке. \n'
                         'Привокзальная площадь города засветилась в советском черно-белом фильме Василия Шукшина «Печки-лавочки». \n'
                         'Упоминается в серии романов «Академия вампиров» Райчел Мид как родина одного из главных персонажей — вампира русского происхождения Дмитрия Беликова. \n')
        verno_F += 1
        answer += 1
    if answer == 3 and message.text.lower() == 'бийск':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fpicworld.ru%2Fwp-content%2Fuploads%2F2020%2F04%2F752366-3.jpg&lr=11091&pos=1&rpt=simage&text=архангельск')
        bot.send_message(message.from_user.id,
                         'Город №4: \n'
                         'В области никогда не было крепостного права. \n'
                         'Этот город - родина российского триколора. \n'
                         'В 1781 году в городе по указу Екатерины Великой была открыта первая в России мореходная школа. \n'
                         'Ленин не любил этот город. \n')
        verno_F += 1
        answer += 1
    if answer == 4 and message.text.lower() == 'архангельск':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fstatic.tildacdn.com%2Ftild3065-3237-4638-a161-633337646638%2F36_tumen.jpg&lr=11091&pos=6&rpt=simage&text=тюмень')
        bot.send_message(message.from_user.id,
                         'Город №5: \n'
                         'Это первый русский город в Сибири. \n'
                         'В 1960-х годах в окрестностях города нашли нефть. \n'
                         'Самый высокий памятник Владимиру Ильичу, отлитый из бронзы, расположен здесь. \n'
                         'В области были рождены такие люди, как Дмитрий Менделеев и Григорий Распутин. \n')
        verno_F += 1
        answer += 1
    if answer == 5 and message.text.lower() == 'тюмень':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fi5.photo.2gis.com%2Fimages%2Fgeo%2F0%2F30258560054944179_a9ad.jpg&lr=11091&pos=5&rpt=simage&text=кумертау')
        bot.send_message(message.from_user.id,
                         'Город №6: \n'
                         'Название города происходит от башк. - "угловая гора". \n'
                         'Возник в 1947 как посёлок Бабай с началом промышленного освоения Верхнее-Бабаевского месторождения Южно-Уральского буроугольного бассейна. \n'
                         'Здесь находится стела, посвящённая строителям крылатых машин \n'
                         'Памятник жертвам радиационных аварий и катастроф. \n')
        verno_F += 1
        answer += 1
    if answer == 6 and message.text.lower() == 'кумертау':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fwozap.ru%2Fuploads%2Fposts%2F2016-11%2F1480346119908.jpeg&lr=11091&pos=1&rpt=simage&text=астрахань')
        bot.send_message(message.from_user.id,
                         'Город №7: \n'
                         'За 2 века до официального основания города в середине XVI века здесь находился ордынский город Хаджи-Тархан. \n'
                         'В 1858 году здесь побывал знаменитый французский писатель Александр Дюма. \n'
                         'Здесь есть фермы по разведению верблюдов, а каждый год проводятся выставки этих животных. \n'
                         'Город растянут вдоль побережья Волги на целых 45 километров. \n')
        verno_F += 1
        answer += 1
    if answer == 7 and message.text.lower() == 'астрахань':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fic.pics.livejournal.com%2Fzdorovs%2F16627846%2F1706777%2F1706777_original.jpg&lr=11091&pos=10&rpt=simage&text=Балаково')
        bot.send_message(message.from_user.id,
                         'Город №8: \n'
                         'В год основания города (1762) скончались российская императрица Елизавета Петровна и император Петр III. \n'
                         'Протяженность города вдоль Волги составляет примерно 11 км. \n'
                         'Первая телефонная сеть общего пользования, открытая купцом В. И. Бердниковым, появилась в городе в 1908 году. \n'
                         'С 1850 по 1928 годы город входил в состав Самарской губернии. \n')
        verno_F += 1
        answer += 1
    if answer == 8 and message.text.lower() == 'балаково':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fimg.tourister.ru%2Ffiles%2F2%2F7%2F0%2F5%2F4%2F0%2F5%2F9%2Foriginal.jpg&lr=11091&pos=2&rpt=simage&text=Ессентуки')
        bot.send_message(message.from_user.id,
                         'Город №9: \n'
                         'Этот город самый молодой курорт Кавминвод и основан в 1825г. \n'
                         'С 2007 г. на центральной площади города работает самый большой «Поющий фонтан» на юге страны. \n'
                         'Крупнейший концертный зал КМВ также находится здесь. \n'
                         'Между Кисловодском и этим городом 20 км. \n')
        verno_F += 1
        answer += 1
    if answer == 9 and message.text.lower() == 'ессентуки':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fstatic.mk.ru%2Fupload%2Fentities%2F2022%2F08%2F23%2F10%2Farticles%2FfacebookPicture%2Fa5%2F3c%2Fa4%2F46%2F2f1c61fb342407fb3253b84f179a8b90.jpg&lr=11091&pos=1&rpt=simage&text=Серпухов')
        bot.send_message(message.from_user.id,
                         'Город №10: \n'
                         'Город распложен в Московской области. \n'
                         'В 1374 году в городе был выстроен дубовый кремль. \n'
                         'Троицкий собор, что на соборной горке, является старейшим городским храмом города. \n'
                         'Через город протекает река Нара и два её притока — река Серпейка и река Чавра. \n')
        verno_F += 1
        answer += 1
    if answer == 10 and message.text.lower() == 'серпухов':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fsdelanounas.ru%2Fi%2Fa%2Fw%2F1%2Ff_aW1nLmdlbGlvcGhvdG8uY29tL2tyc25kci8yMV9rcnNuZHIuanBnP19faWQ9MTQzNTc5.jpeg&lr=11091&pos=13&rpt=simage&text=Краснодар')
        bot.send_message(message.from_user.id,
                         'Город №11: \n'
                         'До победы красных город был столицей белогвардейского юга России. \n'
                         'В городе есть ипподром, и он один из старейших в России и был основан в 1864 году. \n'
                         'Первый глава Екатеринодара трудился на благо города бесплатно. \n'
                         'Изначально город был основан черноморскими казаками в качестве военной крепости. \n')
        verno_F += 1
        answer += 1
    if answer == 11 and message.text.lower() == 'краснодар':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fkartinkin.net%2Fuploads%2Fposts%2F2022-12%2F1670596563_29-kartinkin-net-p-ulyanovsk-kartinki-krasivo-29.jpg&lr=11091&pos=0&rpt=simage&text=Ульяновск')
        bot.send_message(message.from_user.id,
                         'Город №12: \n'
                         'Этот город называют городом на 7 холмах и 7 ветрах. \n'
                         'Этот город занимает 1-е место в России по производству гражданских самолётов. \n'
                         'До 1944 года на территории современной улицы Автозаводской располагался колхоз «Родина Ильича». \n'
                         'В 80-е годы XVIII века по указу императрицы Екатерины II в Симбирске началось преподавание грамматики, арифметики и естественной истории (географии). \n')
        verno_F += 1
        answer += 1
    if answer == 12 and message.text.lower() == 'ульяновск':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fcdn.fishki.net%2Fupload%2Fpost%2F2018%2F09%2F24%2F2713661%2F7379274adea4f286fb64a18d5e3b3c96.jpg&lr=11091&pos=6&rpt=simage&text=Нерюнгри')
        bot.send_message(message.from_user.id,
                         'Город №13: \n'
                         'А в районе города добывают не только простой уголь, но и коксующийся. \n'
                         'Кроме панельных домов в городе можно посмотреть на крупную технику. \n'
                         'Население второго по численности города Якутии составляет чуть больше 57 тысяч человек. \n'
                         'Возле города в непосредственной близости находятся три поселка: Беркакит, Серебряный Бор и Чульман. \n')
        verno_F += 1
        answer += 1
    if answer == 13 and message.text.lower() == 'нерюнгри':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fsun9-10.userapi.com%2Fimpg%2Fgr727ddMS7quv2SwgbMVokDFvxikkAzS4e3tmg%2FUKYnFZPV3l8.jpg%3Fsize%3D1280x853%26quality%3D96%26sign%3Dc26f8ad33f86b7d800de7eeb20a220a8%26c_uniq_tag%3D4XV070mCSZfhp4ob7KbdsykT490ZB0Frx35cjG-Qqvc%26type%3Dalbum&lr=11091&pos=0&rpt=simage&text=Елец')
        bot.send_message(message.from_user.id,
                         'Город №14: \n'
                         'Город на один год старше Москвы. \n'
                         'С 1995 года тут установлен один из памятников писателю Ивану Бунину. \n'
                         'Город находится в Липецкой области. \n'
                         'В прошлом город входил в состав Черниговского и Рязанского княжеств, а затем был частью Орловской и Воронежской областей. \n')
        verno_F += 1
        answer += 1
    if answer == 14 and message.text.lower() == 'елец':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fpicworld.ru%2Fwp-content%2Fuploads%2F2017%2F11%2Fkemerovo-2.jpeg&lr=11091&pos=9&rpt=simage&text=Кемерово')
        bot.send_message(message.from_user.id,
                         'Город №15: \n'
                         'Среди всех городов, построенных на могучей реке Томь,город занимает второе место по численности население. \n'
                         'Город является одним из основных мировых центров угольной промышленности ещё с дореволюционных времён. \n'
                         'Город входит в топ-10 городов России по уровню жизни. \n'
                         'Здесь был пожар в 2018 году в ТЦ "Зимняя вишня". \n')
        verno_F += 1
        answer += 1
    if answer == 15 and message.text.lower() == 'кемерово':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fvtspb.ru%2Fupload%2Fiblock%2F190%2Fvstrecha_novogo_goda_v_vologde_.jpg&lr=11091&pos=19&rpt=simage&text=Вологда')
        bot.send_message(message.from_user.id,
                         'Город №16: \n'
                         'С конца XIV века город стала уделом московских князей. \n'
                         'В период 1911-1912 годов в городе отбывал ссылку Иосиф Сталин. \n'
                         'Город был одним из важнейших транзитных центров в торговле России с Англией, Голландией и другими западными странами по Беломорскому пути и в торговле с Сибирью по рекам Сухоне и Вычегде. \n'
                         'В городе есть памятник – писающая на фонарный столб дворняга. \n')
        verno_F += 1
        answer += 1
    if answer == 16 and message.text.lower() == 'вологда':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fdomremont24.ru%2Fassets%2Fimg%2F%25D1%2585%25D0%25B8%25D0%25BC%25D0%25BA%25D0%25B8.jpg&lr=11091&pos=4&rpt=simage&text=Химки')
        bot.send_message(message.from_user.id,
                         'Город №17: \n'
                         'С 1830-х годов на территории современного города активно строили дачи. \n'
                         'Во второй трети XX века из-за роста крупной промышленности город получил статус рабочего поселка. \n'
                         'В 1937 году закончилось строительство канала имени Москвы и Северного речного порта в городе. \n'
                         'В 1812 году в городе расположился французский авангард корпуса Эжена де Богарне — пасынка Наполеона. \n')
        verno_F += 1
        answer += 1
    if answer == 17 and message.text.lower() == 'химки':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fxn--80adbv1agb.xn--p1ai%2Fupload%2Fiblock%2Fd0c%2Fd0ce323cf40d3c744a6411211c425e65.jpg&lr=11091&pos=0&rpt=simage&text=Иваново')
        bot.send_message(message.from_user.id,
                         'Город №18: \n'
                         'С момента учреждения “Золотого кольца России” этот город входит в его состав. \n'
                         'Среди всех городов Золотого кольца город уступает по численности населения лишь Ярославлю. \n'
                         'Несмотря на стремительный отток населения, город до сих пор входит в 50 крупнейших городов России. \n'
                         'Щудровская палатка, возведённая в XVII столетии – самое древнее здание во всём городе. \n')
        verno_F += 1
        answer += 1
    if answer == 18 and message.text.lower() == 'иваново':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fi7.photo.2gis.com%2Fimages%2Fgeo%2F0%2F30258560054875358_0c1a.jpg&lr=11091&pos=0&rpt=simage&text=Киров')
        bot.send_message(message.from_user.id,
                         'Город №19: \n'
                         'Среди всех городов, основанных славянами во времена Древней Руси, он был самым восточным. \n'
                         'При основании город назывался по-другому – Вятка. \n'
                         'Основан город был новгородцами. \n'
                         'Новгородцы в 1174 году захватили марийский город Кокшаров и поменяли его название на Котельнич. \n')
        verno_F += 1
        answer += 1
    if answer == 19 and message.text.lower() == 'киров':
        bot.send_message(message.from_user.id,
                         'Да это верно!')
        bot.send_photo(message.from_user.id,
                       'https://yandex.ru/images/search?from=tabbar&img_url=http%3A%2F%2Fsdelanounas.ru%2Fi%2Fa%2Fw%2F1%2Ff_aW1nLmdlbGlvcGhvdG8uY29tL21heWtvcC9tYXlrb3BfMDAuanBnP19faWQ9MTQ0Mzcx.jpeg&lr=11091&pos=1&rpt=simage&text=майкоп')
        bot.send_message(message.from_user.id,
                         'Город №20: \n'
                         'В 1897 году ученые обнаружили на территории города курган с богатым захоронением эпохи раннего бронзового века, ставший известным как «Могила вождя». \n'
                         'Город выстроен на холмистом плато в предгорьях Северного Кавказа. \n'
                         'У юго-западной черты города в Белую впадает река Фортепьянка. \n'
                         'На улицах многоконфессионального и мультинационального города слышны призывы к молитве, доносящиеся с минаретов Соборной мечети. \n')
        verno_F += 1
        answer += 1
    if answer == 20 and message.text.lower() == 'майкоп':
        if pol == 'ж':
            bot.send_message(message.from_user.id,
                             f'Молодец! Ты прошла эту игру. Итоги: \n'
                             f'Ты отгадала: 20 из 20 городов \n'
                             f'Количество использованных подсказок: {podskazka_F} \n'
                             f'Ты можешь начать сначала, для этого напиши: "Повторить Интересные Факты"')
        if pol == 'м':
            bot.send_message(message.from_user.id,
                             f'Молодец! Ты прошл эту игру. Итоги: \n'
                             f'Ты отгадал: 20 из 20 городов \n'
                             f'Количество использованных подсказок: {podskazka_F} \n'
                             f'Ты можешь начать сначала, для этого напиши: "Повторить Интересные Факты"')
    if message.text.lower() == '/stop_fact':
        if pol == 'ж':
            bot.send_message(message.from_user.id,
                             f'Жалко, что ты уже уходишь.... Итак итоги: \n'
                             f'Количество правильных введенных названий: {verno_F} из 20 \n'
                             f'Количество использованных подсказок: {podskazka_F} \n')
        if pol == 'м':
            bot.send_message(message.from_user.id,
                             f'Жалко, что ты уже уходишь.... Итак итоги: \n'
                             f'Количество правильных введенных названий: {verno_F} из 20 \n'
                             f'Количество использованных подсказок: {podskazka_F}')
    if message.text.lower() == 'помоги':
        bot.send_message(message.from_user.id,
                         f'Я могу помочь всего 3 раза за игру. Для этого напиши так: \n'
                         f'"Город № " и далее номер города, который нужен')
    if message.text.lower() == 'город № 1':
        bot.send_message(message.from_user.id,
                         'Правильный ответ: Абакан')
        podskazka_F += 1
    if message.text.lower() == 'город № 2':
        bot.send_message(message.from_user.id,
                             'Правильный ответ: Клинцы')
        podskazka_F += 1
    if message.text.lower() == 'город № 3':
        bot.send_message(message.from_user.id,
                         'Правильный ответ: Бийск')
        podskazka_F += 1
    if message.text.lower() == 'город № 4':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Архангельск')
            podskazka_F += 1
    if message.text.lower() == 'город № 5':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Тюмень')
            podskazka_F += 1
    if message.text.lower() == 'город № 6':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Кумертау')
            podskazka_F += 1
    if message.text.lower() == 'город № 7':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Астрахань')
            podskazka_F += 1
    if message.text.lower() == 'город № 8':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Балаково')
            podskazka_F += 1
    if message.text.lower() == 'город № 9':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Ессентуки')
            podskazka_F += 1
    if message.text.lower() == 'город № 10':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Серпхув')
            podskazka_F += 1
    if message.text.lower() == 'город № 11':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Краснодар')
            podskazka_F += 1
    if message.text.lower() == 'город № 12':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Ульяновск')
            podskazka_F += 1
    if message.text.lower() == 'город № 13':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Нерюнгри')
            podskazka_F += 1
    if message.text.lower() == 'город № 14':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Елец')
            podskazka_F += 1
    if message.text.lower() == 'город № 15':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Кемерово')
            podskazka_F += 1
    if message.text.lower() == 'город № 16':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Вологда')
            podskazka_F += 1
    if message.text.lower() == 'город № 17':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Химки')
            podskazka_F += 1
    if message.text.lower() == 'город № 18':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Иваново')
            podskazka_F += 1
    if message.text.lower() == 'город № 19':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Киров')
            podskazka_F += 1
    if message.text.lower() == 'город № 20':
        if podskazka_F == 3:
            bot.send_message(message.from_user.id,
                             'У тебя закончились все подсказки')
        else:
            bot.send_message(message.from_user.id,
                             'Правильный ответ: Майкоп')
            podskazka_F += 1


bot.polling(none_stop=True, interval=0)