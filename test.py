import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5385800793:AAHmtDkREg5FIUUqQkZF65k9VTH0C9Tr8vI'

slovar = {'/Airport': ['''Международный аэропорт Иркутск (ИАТА: IKT, ИКАО: UIII) — аэропорт федерального значения с аэродромом класса «Б», расположен в Иркутске на окраине в пяти с половиной километрах от центра города. Аэропорт является местом базирования авиакомпаний Ангара и ИрАэро, а также региональным узловым аэропортом для S7 Airlines.''', 'photos/airport 1.jpg'],
          '/Angara_Icebreaker': ['''«Ангара́» — пароход-ледокол российского и советского флотов, в настоящее время корабль-музей, один из пяти дореволюционной постройки. Один из самых старых сохранившихся ледоколов в мире (наряду со шведским S/S «Bore[sv]» (1894) и финским «Tarmo» (1907)).''', 'photos/angara 1.jpg'],
          '/Kirov_Square': ['''Сквер имени Ки́рова (1669—1790-е — Кремлёвская, начало XIX века — 1935 год — Ти́хвинская, Гостинодво́рская, Гра́фа Спера́нского и другие; с 1935 года по настоящее время — сквер имени Ки́рова) — главная площадь Иркутска; расположена в Правобережном округе, в историческом центре города между улицами Ленина и Сухэ-Батора.''', 'photos/skver 2.jpg'],
          '/Moscow_Gate': ['''Моско́вские Триумфа́льные воро́та — триумфальная арка. Была сооружена в 1811 году в Иркутске в честь десятилетия восшествия на престол Александра I. Ворота располагались на пересечении улиц Московско-Ланинской и Нижней набережной Ангары при выезде из Иркутска в сторону Европейской части России — на Московский тракт. Отсюда и было получено название Московские.''', 'photos/vorota 1.jpg'],
          '/Eternal_Flame': ['''Мемориал Вечный огонь Славы в Иркутске расположен на Нижней Набережной улице города, был торжественно открыт 8 мая 1975 года, в год 30-ой годовщины Великой Победы. Главным архитектором и главным художником проекта мемориального комплекса были Владлен Федорин и Виталий Смагин, уководил строительством председатель Иркутского горисполкома Николай Салацкий.''', 'photos/ogon 1.jpg'],
          '/Monument_to_Alexander_the_Third': ['''Памятник Александру III в Иркутске был установлен в честь российского императора Александра III в 1908 году по итогам всероссийского конкурса, объявленного в 1902 году. Снесён в 1920 году на основании декрета «О памятниках республики». Восстановлен в 2003 году.''', 'photos/aleksandr 1.jpg']}


keyboard = [
        [
        InlineKeyboardButton("Аэропорт", callback_data='/Airport'),
        ],
        [
        InlineKeyboardButton("Ледокол Ангара", callback_data='/Angara_Icebreaker'),
        ],
        [
        InlineKeyboardButton("Сквер Кирова", callback_data='/Kirov_Square'),
        ],
        [
        InlineKeyboardButton("Московские ворота", callback_data='/Moscow_Gate'),
        ],
        [
        InlineKeyboardButton("Вечный огонь", callback_data='/Eternal_Flame'),
        ],
        [
        InlineKeyboardButton("Памятник Александру III", callback_data='/Monument_to_Alexander_the_Third'),
        ],
    ]
reply_markup = InlineKeyboardMarkup(keyboard, one_time_keyboard=False)


def start(update, context):
    update.message.reply_text(
        "Я бот-экскурсовод по Иркутску. О каких достопримечательностях этого города хотели бы узнать?",
        reply_markup=reply_markup
    )


def button(update, context):
    query = update.callback_query
    query.answer()
    choice = query.data
    update.callback_query.message.reply_photo(open(slovar[choice][1], 'rb'))
    update.callback_query.message.edit_text(slovar[choice][0])


def help(update, context):
    update.message.reply_text(
        "Я бот-помощник, расскажу о прекрасных местах Иркутска.")


def get_table(update, context):
    update.message.reply_photo(open('photos/angara 1.jpg', 'rb'))
    update.message.reply_photo(open('photos/angara 2.jpg', 'rb'))
    update.message.reply_photo(open('photos/aleksandr 1.jpg', 'rb'))
    update.message.reply_photo(open('photos/aleksandr 2.jpg', 'rb'))
    update.message.reply_photo(open('photos/airport 1.jpg', 'rb'))
    update.message.reply_photo(open('photos/airport 2.jpg', 'rb'))
    update.message.reply_photo(open('photos/skver 1.jpg', 'rb'))
    update.message.reply_photo(open('photos/skver 2.jpg.jpg', 'rb'))
    update.message.reply_photo(open('photos/ogon 1.jpg', 'rb'))
    update.message.reply_photo(open('photos/ogon 2.jpg', 'rb'))
    update.message.reply_photo(open('photos/vorota 1.jpg', 'rb'))
    update.message.reply_photo(open('photos/ogon 2.jpeg', 'rb'))


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()