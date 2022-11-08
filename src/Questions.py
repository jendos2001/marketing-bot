from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import config
from src.DataBase import DataBase


class MainClass:
    user_info = {}
    buttons_info = {}

    def __init__(self, token):
        self.updater = Updater(token=token, use_context=True)
        dispatcher = self.updater.dispatcher

        start_handler = CommandHandler('start', self.question1)
        dispatcher.add_handler(start_handler)

        target_audience_handler = CommandHandler('target', self.target)
        dispatcher.add_handler(target_audience_handler)

        answers_handler = CallbackQueryHandler(self.answers)
        dispatcher.add_handler(answers_handler)

    def question1(self, update, context):
        self.buttons_info[update.effective_chat.id] = dict.fromkeys(['1', '2', '3', '4', '5', '6', '7', '8'], False)
        if update.effective_chat.id not in self.user_info.keys():
            self.user_info[update.effective_chat.id] = {}
        else:
            self.user_info[update.effective_chat.id].clear()
        s = f"Привет! Это бот для сбора информации о целевой аудитории кафе быстрого питания. " \
            f"Ответь на несколько простых вопросов"
        question1 = f"Вопрос 1. Ваш пол"
        buttons = [[InlineKeyboardButton(text='Мужской', callback_data='1_Мужской')],
                   [InlineKeyboardButton(text='Женский', callback_data='1_Женский')]]
        question1_answers = InlineKeyboardMarkup(buttons)
        context.bot.send_message(chat_id=update.effective_chat.id, text=s)
        context.bot.send_message(chat_id=update.effective_chat.id, text=question1, reply_markup=question1_answers)

    @staticmethod
    def question2(update, context):
        question2 = f"Вопрос 2. Ваш возраст больше 25?"
        buttons = [[InlineKeyboardButton(text='Да', callback_data='2_Да')],
                   [InlineKeyboardButton(text='Нет', callback_data='2_Нет')]]
        question2_answers = InlineKeyboardMarkup(buttons)
        context.bot.send_message(chat_id=update.effective_chat.id, text=question2, reply_markup=question2_answers)

    @staticmethod
    def question3_1(update, context):
        question3_1 = f"Вопрос 3. Вы студент?"
        buttons = [[InlineKeyboardButton(text='Да', callback_data='3_Да')],
                   [InlineKeyboardButton(text='Нет', callback_data='3_Нет')]]
        question3_1_answers = InlineKeyboardMarkup(buttons)
        context.bot.send_message(chat_id=update.effective_chat.id, text=question3_1, reply_markup=question3_1_answers)

    @staticmethod
    def question3_2(update, context):
        question3_2 = f"Вопрос 3. Вы работаете?"
        buttons = [[InlineKeyboardButton(text='Да', callback_data='3_Да')],
                   [InlineKeyboardButton(text='Нет', callback_data='3_Нет')]]
        question3_2_answers = InlineKeyboardMarkup(buttons)
        context.bot.send_message(chat_id=update.effective_chat.id, text=question3_2, reply_markup=question3_2_answers)

    @staticmethod
    def question4(update, context):
        question4 = f"Вопрос 4. У Вас есть супруг?"
        buttons = [[InlineKeyboardButton(text='Да', callback_data='4_Да')],
                   [InlineKeyboardButton(text='Нет', callback_data='4_Нет')]]
        question4_answers = InlineKeyboardMarkup(buttons)
        context.bot.send_message(chat_id=update.effective_chat.id, text=question4, reply_markup=question4_answers)

    @staticmethod
    def question5(update, context):
        question5 = f"Вопрос 5. Ваша заработная плата больше средней заработной платы по региону?"
        buttons = [[InlineKeyboardButton(text='Да', callback_data='5_Да')],
                   [InlineKeyboardButton(text='Нет', callback_data='5_Нет')]]
        question5_answers = InlineKeyboardMarkup(buttons)
        context.bot.send_message(chat_id=update.effective_chat.id, text=question5, reply_markup=question5_answers)

    @staticmethod
    def question6(update, context):
        question6 = f"Вопрос 6. Вы покупаете еду в кафе быстрого питания чаще трёх раз в неделю?"
        buttons = [[InlineKeyboardButton(text='Да', callback_data='6_Да')],
                   [InlineKeyboardButton(text='Нет', callback_data='6_Нет')]]
        question6_answers = InlineKeyboardMarkup(buttons)
        context.bot.send_message(chat_id=update.effective_chat.id, text=question6, reply_markup=question6_answers)

    @staticmethod
    def question7(update, context):
        question7 = f"Вопрос 7. Вы готовите еду дома чаще трёх раз в неделю?"
        buttons = [[InlineKeyboardButton(text='Да', callback_data='7_Да')],
                   [InlineKeyboardButton(text='Нет', callback_data='7_Нет')]]
        question7_answers = InlineKeyboardMarkup(buttons)
        context.bot.send_message(chat_id=update.effective_chat.id, text=question7, reply_markup=question7_answers)

    @staticmethod
    def question8(update, context):
        question8 = f"Вопрос 8. Ваш средний чек в кафе быстрого питания больше 350 рублей?"
        buttons = [[InlineKeyboardButton(text='Да', callback_data='8_Да')],
                   [InlineKeyboardButton(text='Нет', callback_data='8_Нет')]]
        question8_answers = InlineKeyboardMarkup(buttons)
        context.bot.send_message(chat_id=update.effective_chat.id, text=question8, reply_markup=question8_answers)

    @staticmethod
    def question9(update, context):
        question9 = f"Вопрос 9. Ваш индекс массы тела находится в пределах нормы? " \
                    f"Индекс массы тела рассчитывается по формуле: ИМТ=масса(кг)/(рост(м) * рост(м). Норма: 18.5-24.9"
        buttons = [[InlineKeyboardButton(text='Да', callback_data='9_Да')],
                   [InlineKeyboardButton(text='Нет', callback_data='9_Нет')]]
        question9_answers = InlineKeyboardMarkup(buttons)
        context.bot.send_message(chat_id=update.effective_chat.id, text=question9, reply_markup=question9_answers)

    def answers(self, update, context):
        data = update.callback_query.data
        answer = data.split('_')
        if answer[0] == '1' and not self.buttons_info[update.effective_chat.id][answer[0]]:
            self.buttons_info[update.effective_chat.id][answer[0]] = True
            self.user_info[update.effective_chat.id][int(answer[0])] = answer[1]
            self.question2(update, context)
        elif answer[0] == '2' and not self.buttons_info[update.effective_chat.id][answer[0]]:
            self.buttons_info[update.effective_chat.id][answer[0]] = True
            self.user_info[update.effective_chat.id][int(answer[0])] = answer[1]
            if answer[1] == 'Нет':
                self.question3_1(update, context)
            else:
                self.question3_2(update, context)
        elif answer[0] == '3' and not self.buttons_info[update.effective_chat.id][answer[0]]:
            self.buttons_info[update.effective_chat.id][answer[0]] = True
            self.user_info[update.effective_chat.id][int(answer[0])] = answer[1]
            self.question4(update, context)
        elif answer[0] == '4' and not self.buttons_info[update.effective_chat.id][answer[0]]:
            self.buttons_info[update.effective_chat.id][answer[0]] = True
            self.user_info[update.effective_chat.id][int(answer[0])] = answer[1]
            self.question5(update, context)
        elif answer[0] == '5' and not self.buttons_info[update.effective_chat.id][answer[0]]:
            self.buttons_info[update.effective_chat.id][answer[0]] = True
            self.user_info[update.effective_chat.id][int(answer[0])] = answer[1]
            self.question6(update, context)
        elif answer[0] == '6' and not self.buttons_info[update.effective_chat.id][answer[0]]:
            self.buttons_info[update.effective_chat.id][answer[0]] = True
            self.user_info[update.effective_chat.id][int(answer[0])] = answer[1]
            self.question7(update, context)
        elif answer[0] == '7' and not self.buttons_info[update.effective_chat.id][answer[0]]:
            self.buttons_info[update.effective_chat.id][answer[0]] = True
            self.user_info[update.effective_chat.id][int(answer[0])] = answer[1]
            self.question8(update, context)
        elif answer[0] == '8' and not self.buttons_info[update.effective_chat.id][answer[0]]:
            self.buttons_info[update.effective_chat.id][answer[0]] = True
            self.user_info[update.effective_chat.id][int(answer[0])] = answer[1]
            self.question9(update, context)
        elif answer[0] == '9':
            self.buttons_info[update.effective_chat.id][answer[0]] = True
            self.user_info[update.effective_chat.id][int(answer[0])] = answer[1]
            data_base = DataBase(config.db_name)
            data_base.add(self.user_info[update.effective_chat.id])
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Ответ добавлен! Чтобы пройти опрос снова введите команду /start")

    @staticmethod
    def target(update, context):
        data_base = DataBase(config.db_name)
        answers = data_base.target_from_db()
        if answers[0][0] is not None:
            if answers[1][1] == 'Да':
                if answers[2][1] == 'Да':
                    status = 'Работает'
                else:
                    status = 'Безработный'
            else:
                if answers[2][1] == 'Да':
                    status = 'Студент'
                else:
                    status = 'Безработный'
            s = f"Портрет целевой аудитории:\n" \
                f"Пол: {answers[0][1]}\n" \
                f"Возраст: {'Больше 25' if answers[1][1] == 'Да' else 'Не более 25'}\n" \
                f"Статус: {status}\n" \
                f"Семейное состояние: {'В браке' if answers[3][1] == 'Да' else 'Не в браке'}\n" \
                f"Размер заработной платы: {'Больше среднего' if answers[4][1] == 'Да' else 'Меньше среднего'}\n" \
                f"Количество посещений кафе быстрого питания в неделю: " \
                f"{'Больше трёх' if answers[5][1] == 'Да' else 'Меньше трёх'}\n" \
                f"Как часто готовит еду дома: " \
                f"{'Больше трёх раз в неделю' if answers[6][1] == 'Да' else 'Меньше трёх раз в неделю'}\n" \
                f"Средний чек: {'Больше 350р' if answers[7][1] == 'Да' else 'Меньше 350р'}\n" \
                f"Индекс массы тела: {'В норме' if answers[8][1] == 'Да' else 'Не в норме'}\n"
        else:
            s = 'В базе данных нет информации!'
        context.bot.send_message(chat_id=update.effective_chat.id, text=s)

    def start(self):
        self.updater.start_polling()
        self.updater.idle()
