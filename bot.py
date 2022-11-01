import telebot
from telebot import types
from datetime import datetime as dt
import operations_complex as opCom
import operations_rational as oprat


API_TOKEN= "5488460139:AAEt4UhSUVmQsyshp3D8Pg8-YJpKeXbk8SQ"
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Калькулятор запущен')

# @bot.message_handler(commands=['button'])
# def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Комплексные числа"))
    markup.add(types.KeyboardButton("Рациональные числа"))
    bot.send_message(message.chat.id,'Выберите, с какими числами будем работать:',reply_markup=markup)

@bot.message_handler(func= lambda message: message.text =='Комплексные числа')
def message_co(message):
    bot.send_message(message.from_user.id, 'Введите первое комплексное число по образцу: 2 + 5i')
    bot.register_next_step_handler(message, message_co1)

def message_co1(message):
    global user_komplex1
    user_komplex1 = message.text
    # print("1", user_komplex1)

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("+"))
    markup.add(types.KeyboardButton("-"))
    markup.add(types.KeyboardButton("/"))
    markup.add(types.KeyboardButton("*"))

    bot.send_message(message.from_user.id, 'Выбирите фун',reply_markup=markup)
    bot.register_next_step_handler(message, message_co2)

def message_co2(message):
    global operation
    operation = message.text
    # print("2", operation)
    bot.send_message(message.from_user.id, 'Введите второе комплексное число по образцу: 2 + 5i')
    bot.register_next_step_handler(message, message_co3)

def message_co3(message):
    global user_komplex2
    user_komplex2 = message.text
    # print(user_komplex2)
    insert_co4()
    compl()

def insert_co4():
    # Функция приглашает пользователя для ввода двух комплексных чисел и операции между ними
    # print(f'"1" ({user_komplex1}){operation}({user_komplex2}) = ', end='')
    time = dt.now().strftime('%d.%m.%Y %H:%M:%S')
    with open('results.json', 'a') as data:
        data.write(f'{time} ({user_komplex1}){operation}({user_komplex2}) = ')
    data.close()
    # return [user_komplex1, user_komplex2, operation]


def compl():
    operands = [user_komplex1, user_komplex2, operation]
    # print('o',operands)
    dfg=0
    if operands[2] == "+":
        opCom.record_in_file(opCom.addition(opCom.take_rational_part(operands[0]),
                                            opCom.take_symbol(operands[0]),
                                            opCom.take_imaginary_part(operands[0]),
                                            opCom.take_rational_part(operands[1]),
                                            opCom.take_symbol(operands[1]),
                                            opCom.take_imaginary_part(operands[1])))
    elif operands[2] == "-":
        opCom.record_in_file(opCom.deduction(opCom.take_rational_part(operands[0]),
                                             opCom.take_symbol(operands[0]),
                                             opCom.take_imaginary_part(operands[0]),
                                             opCom.take_rational_part(operands[1]),
                                             opCom.take_symbol(operands[1]),
                                             opCom.take_imaginary_part(operands[1])))
    elif operands[2] == "*":
        opCom.record_in_file(opCom.multiply(opCom.take_rational_part(operands[0]),
                                            opCom.take_symbol(operands[0]),
                                            opCom.take_imaginary_part(operands[0]),
                                            opCom.take_rational_part(operands[1]),
                                            opCom.take_symbol(operands[1]),
                                            opCom.take_imaginary_part(operands[1])))
    else:
        opCom.record_in_file(opCom.division(opCom.take_rational_part(operands[0]),
                                            opCom.take_symbol(operands[0]),
                                            opCom.take_imaginary_part(operands[0]),
                                            opCom.take_rational_part(operands[1]),
                                            opCom.take_symbol(operands[1]),
                                            opCom.take_imaginary_part(operands[1])))
    print('dfg', dfg)


@bot.message_handler(func= lambda message: message.text =='Рациональные числа')

def message_vid(message):
    bot.send_message(message.from_user.id, 'Выберите первое число с плавающей точкой:')
    bot.register_next_step_handler(message, message_re)
    print(message.chat.id)
def message_re(message):
    global firstnum
    firstnum = message.text
    print("1", firstnum)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("+")), markup.add(types.KeyboardButton("-"))
    markup.add(types.KeyboardButton("/")), markup.add(types.KeyboardButton("*"))

    bot.send_message(message.from_user.id, 'Выбирите действие', reply_markup=markup)
    bot.register_next_step_handler(message, message_reply2)

def message_reply2(message):
    global operat
    operat = message.text
    print("2", operat)
    bot.send_message(message.from_user.id, 'Выберите второе число с плавающей точкой:')
    bot.register_next_step_handler(message, message_re2)

def message_re2(message):
    global secondnum
    secondnum = message.text
    print(secondnum)
    asd = oprat.mainterminal(firstnum, operat, secondnum)
    print('asd', asd)
    bot.send_message(message.from_user.id, f'Ответ: {asd}')


bot.infinity_polling()