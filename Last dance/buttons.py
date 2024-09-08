from telebot.types import ReplyKeyboardMarkup, KeyboardButton



def number():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    k1 = KeyboardButton('1')
    k2 = KeyboardButton('2')
    k3 = KeyboardButton('3')
    k4 = KeyboardButton('4')
    k5 = KeyboardButton('5')
    k6 = KeyboardButton('6')
    k7 = KeyboardButton('7')
    k8 = KeyboardButton('8')
    k9 = KeyboardButton('9')
    k10 = KeyboardButton('10')
    kb.add(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10)
    return kb


def register_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Поделиться контактом', request_contact=True)
    kb.add(button)
    return kb


def contacts_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Контакты', request_contact=True)
    kb.add(button)
    return kb

def menu_buttons():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('🛒Asosiy menyu')
    button3 = KeyboardButton('📥Savat')
    button4 = KeyboardButton('📞Aloqa')
    button5 = KeyboardButton('📨Xabar yuborish')
    button6 = KeyboardButton('⚙️Sozlamalar')
    button7 = KeyboardButton('ℹ️Biz haqimizda')
    keyboard.add(button1, button3, button4, button5, button6, button7)
    return keyboard

def main_menu_buttons():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button07 = KeyboardButton('Setlar')
    button8 = KeyboardButton('🌯Lavash')
    button9 = KeyboardButton('🌮Shaurma')
    button10 = KeyboardButton('🍔Burger')
    button11 = KeyboardButton('🌭Hot-dog')
    button12 = KeyboardButton('🥤Ichimliklar')
    keyboard.add(button07, button8, button9, button10, button11, button12)
    return keyboard

def settings():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button13 = KeyboardButton('🇺🇿/ru.Tilni ozgartirish')
    button14 = KeyboardButton('🗑Malumotlarni tozalash')
    button15 = KeyboardButton('🔙Orqaga qaytish')
    button2 = KeyboardButton('Вернутся в меню')
    keyboard.add(button13, button14, button15)
    return keyboard

def Sets():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button16 = KeyboardButton('🍟☕️Combo Plus Isituvchan (Qora choy)')
    button17 = KeyboardButton('🌯🧃FitCombo')
    button18 = KeyboardButton('Iftar kofte grill mol goshtidan')
    button19 = KeyboardButton('Donar boks  mol goshtidan')
    button20 = KeyboardButton('Donar boks tovuq goshtidan')
    button21 = KeyboardButton('🍟🥤COMBO+')
    button22 = KeyboardButton('Iftar strips tovuq goshtidan')
    button23 = KeyboardButton('🌭🧃🍟KidsCombo')
    button24 = KeyboardButton('🔙Orqaga qaytish')
    button200 = KeyboardButton('Вернутся в меню')
    keyboard.add(button16, button17, button18, button19, button20, button21, button22, button23, button24, button200)
    return keyboard

def La_vash():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button25 = KeyboardButton('🐮🌶🌯Mol goshtidan qalampir lavash')
    button26 = KeyboardButton('🐔🌶🌯Tovuq qoshtli qalampir lavash')
    button27 = KeyboardButton('🐮🧀🌯Mol goshtidan pishloqli lavash STANDART')
    button28 = KeyboardButton('🐔🧀🌯Tovuq goshtidan pishloqli lavash STANDART')
    button29 = KeyboardButton('FITTER')
    button30 = KeyboardButton('🐔🌯Lavash tovuq gosht')
    button31 = KeyboardButton('🐮🌯Lavash mol goshti')
    button32 = KeyboardButton('🔙Orqaga qaytish')
    button00 = KeyboardButton('Вернутся в меню')
    keyboard.add(button25, button26, button27, button28, button29, button30, button31, button32, button00)
    return keyboard

def Sha_urma():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button33 = KeyboardButton('🐮🌶🌮Mol goshtidan qalampir shaurma')
    button34 = KeyboardButton('🐔🌶🌮Tovuq goshtidan qalampir shaurma')
    button35 = KeyboardButton('🐮🌮Mol goshtidan shaurma')
    button36 = KeyboardButton('🐔🌮Tovuq goshtidan shaurma')
    button37 = KeyboardButton('🔙Orqaga qaytish')
    button99 = KeyboardButton('Вернутся в меню')
    keyboard.add(button33, button34, button35, button36, button37, button99)
    return keyboard

def Bur_ger():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button38 = KeyboardButton('🍔Gamburger')
    button39 = KeyboardButton('Double burger')
    button40 = KeyboardButton('🧀🍔Cheese burger')
    button41 = KeyboardButton('Double cheese burger')
    button42 = KeyboardButton('🔙Orqaga qaytish')
    button222 = KeyboardButton('Вернутся в меню')
    keyboard.add(button38, button39, button40, button41, button42, button222)
    return keyboard

def Hot_dog():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button43 = KeyboardButton('Hot-dog baguette')
    button44 = KeyboardButton('Hot-dog baguette double')
    button45 = KeyboardButton('👶🏻🌭Hot-dog kids')
    button46 = KeyboardButton('Hot-dog classic')
    button47 = KeyboardButton('🐔🧀Sub tovuq cheese')
    button48 = KeyboardButton('🐔Sub tovuq')
    button49 = KeyboardButton('🐮🧀Sub gosht cheese')
    button50 = KeyboardButton('🐮Sub gosht')
    button51 = KeyboardButton('🔙Orqaga qaytish')
    button211 = KeyboardButton('Вернутся в меню')
    keyboard.add(button43, button44, button45, button46, button47, button48, button49, button50, button51, button211)
    return keyboard

def Ichim_liklar():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button52 = KeyboardButton('🧃Sok dena 0,33L')
    button53 = KeyboardButton('Gazsiz suv 0,5L')
    button54 = KeyboardButton('Pepsi 0,5L')
    button55 = KeyboardButton('Pepsi 1,5L')
    button56 = KeyboardButton('🥤Quyib beriladigan pepsi')
    button57 = KeyboardButton('🥤Quyib beriladigan mirinda')
    button58 = KeyboardButton('Bliss sharbati')
    button59 = KeyboardButton('☕️Coffee Amerikano')
    button60 = KeyboardButton('☕️Coffee Latte')
    button61 = KeyboardButton('Kok choy')
    button62 = KeyboardButton('Qora choy')
    button63 = KeyboardButton('🍋Limonli kok choy')
    button64 = KeyboardButton('🔙Orqaga qaytish')
    button212 = KeyboardButton('Вернутся в меню')
    keyboard.add(button52, button53, button54, button55, button56, button57, button58, button59, button60, button61, button62, button63, button64, button212)
    return keyboard

def shirin_liklar():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button65 = KeyboardButton('🍩Donut qulupnayli')
    button66 = KeyboardButton('🍩Donut karamelli')
    button67 = KeyboardButton('Chizkeyk')
    button68 = KeyboardButton('Medovik asalim')
    button69 = KeyboardButton('🔙Orqaga qaytish')
    button213 = KeyboardButton('Вернутся в меню')
    keyboard.add(button65, button66, button67, button68, button69, button213)
    return keyboard

def Sous_va_frilar():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button70 = KeyboardButton('🍟Kartoshka fri')
    button71 = KeyboardButton('Kartoshka Po-derevenski')
    button72 = KeyboardButton('🍟🙂Kartoshka smaylik')
    button73 = KeyboardButton('🍚Guruch')
    button74 = KeyboardButton('🥙Salat')
    button75 = KeyboardButton('🥗Grecheskiy salat')
    button76 = KeyboardButton('Strips(EVOS)')
    button77 = KeyboardButton('Nagets(EVOS)')
    button78 = KeyboardButton('🧅Sarimsoq-piyozli sous')
    button79 = KeyboardButton('🍅Ketchup(Pomidorli sous)')
    button80 = KeyboardButton('Mayonez sous')
    button81 = KeyboardButton('🧀Sirniy sous')
    button82 = KeyboardButton('🌶Chili sous(Qalampirli sous)')
    button83 = KeyboardButton('🔙Orqaga qaytish')
    button214= KeyboardButton('Вернутся в меню')
    keyboard.add(button70, button71, button72, button73, button74, button75, button76, button77, button78, button79, button80, button81, button82, button83, button214)
    return keyboard



# Savat 

def buys_product():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    buys = KeyboardButton('Оплатить наличными')
    buys2 = KeyboardButton('Оплатить картой')


    keyboard.add(buys, buys2)
    return keyboard

def buy_product():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    buy = KeyboardButton('Оплатить товар')

    keyboard.add(buy)
    return keyboard


def Savat_button():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    pereyti = KeyboardButton('Перейти в корзину')

    keyboard.add(pereyti)
    return keyboard

def Savat():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    korzina = KeyboardButton('Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(korzina, Nazad)
    return keyboard

def Savatdasan():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    delete = KeyboardButton('Удолить из корзины') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(delete, Nazad)
    return keyboard


# Lats dance


def combo_plus1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    combo1 = KeyboardButton('🍟☕️Combo Plus Isituvchan (Qora choy)')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(combo1, korzina, Nazad)
    return keyboard


def combo_plus2():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    combo3 = KeyboardButton('🌯🧃FitCombo')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(combo3, korzina, Nazad)
    return keyboard


def combo_plus3():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    combo5 = KeyboardButton('Iftar kofte grill mol goshtidan')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(combo5, korzina, Nazad)
    return keyboard


def donar_combo():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    combo7 = KeyboardButton('Donar boks mol goshtidan')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(combo7, korzina, Nazad)
    return keyboard


def combo_plus5():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    combo9 = KeyboardButton('Donar boks tovuq goshtidan')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(combo9, korzina, Nazad)
    return keyboard


def combo_plus5():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    combo9 = KeyboardButton('Donar boks tovuq goshtidan')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(combo9, korzina, Nazad)
    return keyboard


def combo_plus6():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    combo11 = KeyboardButton('🍟🥤COMBO+')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(combo11, korzina, Nazad)
    return keyboard


def combo_plus7():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    combo13 = KeyboardButton('Iftar strips tovuq goshtidan')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(combo13, korzina, Nazad)
    return keyboard


def combo_plus8():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    combo15 = KeyboardButton('🌭🧃🍟KidsCombo')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(combo15, korzina, Nazad)
    return keyboard


def Lavash_menu1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Lavash1 = KeyboardButton('🐮🌶🌯Mol goshtidan qalampir lavash')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Lavash1, korzina, Nazad)
    return keyboard


def Lavash_menu2():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Lavash2 = KeyboardButton('🐔🌶🌯Tovuq qoshtli qalampir lavash')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Lavash2, korzina, Nazad)
    return keyboard


def Lavash_menu3():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Lavash3 = KeyboardButton('🐮🧀🌯Mol goshtidan pishloqli lavash STANDART')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Lavash3, korzina, Nazad)
    return keyboard


def Lavash_menu4():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Lavash4 = KeyboardButton('🐔🧀🌯Tovuq goshtidan pishloqli lavash STANDART')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Lavash4, korzina, Nazad)
    return keyboard


def Lavash_menu5():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Lavash5 = KeyboardButton('FITTER')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Lavash5, korzina, Nazad)
    return keyboard


def Lavash_menu6():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Lavash6 = KeyboardButton('🐔🌯Lavash tovuq gosht')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Lavash6, korzina, Nazad)
    return keyboard


def Lavash_menu7():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Lavash7 = KeyboardButton('🐮🌯Lavash mol goshti')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Lavash7, korzina, Nazad)
    return keyboard


def Shaurma_menu1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Shaurma1 = KeyboardButton('🐮🌶🌮Mol goshtidan qalampir shaurma')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Shaurma1, korzina, Nazad)
    return keyboard


def Shaurma_menu2():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Shaurma2 = KeyboardButton('🐔🌶🌮Tovuq goshtidan qalampir shaurma')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Shaurma2, korzina, Nazad)
    return keyboard


def Shaurma_menu3():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Shaurma3 = KeyboardButton('🐮🌮Mol goshtidan shaurma')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Shaurma3, korzina, Nazad)
    return keyboard


def Shaurma_menu4():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Shaurma4 = KeyboardButton('🐔🌮Tovuq goshtidan shaurma')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Shaurma4, korzina, Nazad)
    return keyboard


def Burger_menu1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Burger1 = KeyboardButton('🍔Gamburger')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Burger1, korzina, Nazad)
    return keyboard


def Burger_menu2():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Burger2 = KeyboardButton('Double burger')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Burger2, korzina, Nazad)
    return keyboard


def Burger_menu3():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Burger3 = KeyboardButton('🧀🍔Cheese burger')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Burger3, korzina, Nazad)
    return keyboard


def Burger_menu4():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Burger4 = KeyboardButton('Double cheese burger')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Burger4, korzina, Nazad)
    return keyboard


def Hotdog_menu1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Hotdog1 = KeyboardButton('Hot-dog baguette')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Hotdog1, korzina, Nazad)
    return keyboard


def Hotdog_menu2():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Hotdog2 = KeyboardButton('Hot-dog baguette double')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Hotdog2, korzina, Nazad)
    return keyboard


def Hotdog_menu3():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Hotdog3 = KeyboardButton('👶🏻🌭Hot-dog kids')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Hotdog3, korzina, Nazad)
    return keyboard


def Hotdog_menu4():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Hotdog4 = KeyboardButton('Hot-dog classic')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Hotdog4, korzina, Nazad)
    return keyboard


def Hotdog_menu5():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Hotdog5 = KeyboardButton('🐔🧀Sub tovuq cheese')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Hotdog5, korzina, Nazad)
    return keyboard


def Hotdog_menu6():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Hotdog6 = KeyboardButton('🐔Sub tovuq')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Hotdog6, korzina, Nazad)
    return keyboard


def Hotdog_menu7():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Hotdog7 = KeyboardButton('🐮🧀Sub gosht cheese')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Hotdog7, korzina, Nazad)
    return keyboard


def Hotdog_menu8():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    Hotdog8 = KeyboardButton('🐮Sub gosht')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(Hotdog8, korzina, Nazad)
    return keyboard


def Ichimlik_menu1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    ichimlik1 = KeyboardButton('🧃Sok dena 0,33L')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(ichimlik1, korzina, Nazad)
    return keyboard


def Ichimlik_menu2():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    ichimlik2 = KeyboardButton('Gazsiz suv 0,5L')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(ichimlik2, korzina, Nazad)
    return keyboard


def Ichimlik_menu3():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    ichimlik3 = KeyboardButton('Pepsi 0,5L')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(ichimlik3, korzina, Nazad)
    return keyboard


def Ichimlik_menu4():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    ichimlik4 = KeyboardButton('Pepsi 1,5L')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(ichimlik4, korzina, Nazad)
    return keyboard


def Ichimlik_menu5():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    ichimlik5 = KeyboardButton('🥤Quyib beriladigan pepsi')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(ichimlik5, korzina, Nazad)
    return keyboard


def Ichimlik_menu6():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    ichimlik6 = KeyboardButton('🥤Quyib beriladigan mirinda')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(ichimlik6, korzina, Nazad)
    return keyboard


def Ichimlik_menu7():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    ichimlik7 = KeyboardButton('Bliss sharbati')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(ichimlik7, korzina, Nazad)
    return keyboard


def Ichimlik_menu8():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    ichimlik8 = KeyboardButton('☕️Coffee Amerikano')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(ichimlik8, korzina, Nazad)
    return keyboard


def Ichimlik_menu9():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    ichimlik9 = KeyboardButton('☕️Coffee Latte')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(ichimlik9, korzina, Nazad)
    return keyboard


def Ichimlik_menu10():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    ichimlik10 = KeyboardButton('Kok choy')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(ichimlik10, korzina, Nazad)
    return keyboard


def Ichimlik_menu11():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    ichimlik11 = KeyboardButton('Qora choy')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(ichimlik11, korzina, Nazad)
    return keyboard


def Ichimlik_menu12():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    ichimlik12 = KeyboardButton('🍋Limonli kok choy')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(ichimlik12, korzina, Nazad)
    return keyboard


def shirinliklar_menu1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    shirinlik1 = KeyboardButton('🍩Donut qulupnayli')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(shirinlik1, korzina, Nazad)
    return keyboard


def shirinliklar_menu2():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    shirinlik2 = KeyboardButton('🍩Donut karamelli')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(shirinlik2, korzina, Nazad)
    return keyboard


def shirinliklar_menu3():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    shirinlik3 = KeyboardButton('Chizkeyk')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(shirinlik3, korzina, Nazad)
    return keyboard


def shirinliklar_menu4():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    shirinlik4 = KeyboardButton('Medovik asalim')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(shirinlik4, korzina, Nazad)
    return keyboard


def sous_menu1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sous1 = KeyboardButton('🍟Kartoshka fri')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(sous1, korzina, Nazad)
    return keyboard


def sous_menu2():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sous2 = KeyboardButton('Kartoshka Po-derevenski')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(sous2, korzina, Nazad)
    return keyboard


def sous_menu3():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sous3 = KeyboardButton('🍟🙂Kartoshka smaylik')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(sous3, korzina, Nazad)
    return keyboard


def sous_menu4():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sous4 = KeyboardButton('🍚Guruch')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(sous4, korzina, Nazad)
    return keyboard


def sous_menu5():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sous5 = KeyboardButton('🥙Salat')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(sous5, korzina, Nazad)
    return keyboard


def sous_menu6():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sous6 = KeyboardButton('🥗Grecheskiy salat')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(sous6, korzina, Nazad)
    return keyboard


def sous_menu7():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sous7 = KeyboardButton('Strips(EVOS)')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(sous7, korzina, Nazad)
    return keyboard


def sous_menu8():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sous8 = KeyboardButton('Nagets(EVOS)')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(sous8, korzina, Nazad)
    return keyboard


def sous_menu9():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sous9 = KeyboardButton('🧅Sarimsoq-piyozli sous')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(sous9, korzina, Nazad)
    return keyboard


def sous_menu10():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sous10 = KeyboardButton('🍅Ketchup(Pomidorli sous')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(sous10, korzina, Nazad)
    return keyboard


def sous_menu11():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sous11 = KeyboardButton('Mayonez sous')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(sous11, korzina, Nazad)
    return keyboard


def sous_menu12():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sous12 = KeyboardButton('🧀Sirniy sous')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(sous12, korzina, Nazad)
    return keyboard


def sous_menu13():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    sous13 = KeyboardButton('🌶Chili sous(Qalampirli sous)')
    korzina = KeyboardButton('📥Добавить в корзину') 
    Nazad = KeyboardButton('Вернутся в меню')

    keyboard.add(sous13, korzina, Nazad)
    return keyboard
