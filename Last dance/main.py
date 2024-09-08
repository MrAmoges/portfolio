import telebot
import buttons
import database


bot = telebot.TeleBot('поставте свой токен чтобы бот работал')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Добро пожаловать! Поделитесь, пожалуйста, контактом.', reply_markup=buttons.register_button())

@bot.message_handler(content_types=['contact'])
def get_contact(message):
    if message.contact:
        telegram_id = message.from_user.id
        phone_number = message.contact.phone_number

        print(f"Received contact - Telegram ID: {telegram_id}, Phone Number: {phone_number}")

        if not database.check_user(telegram_id):
            database.add_user(telegram_id, phone_number)

        bot.send_message(telegram_id, 'Вы успешно зарегистрировались', reply_markup=buttons.menu_buttons())
    else:
        bot.send_message(message.from_user.id, 'Используйте кнопку для отправки контакта', reply_markup=buttons.register_button())
        

@bot.message_handler(func=lambda message: message.text == '🛒Asosiy menyu')
def handle_main_menu(message):
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=buttons.main_menu_buttons())

@bot.message_handler(func=lambda message: message.text == '⚙️Sozlamalar')
def handle_settings(message):
    bot.send_message(message.chat.id, "Настройки:", reply_markup=buttons.settings())

@bot.message_handler(func=lambda message: message.text == '🔙Orqaga qaytish')
def handle_back(message):
    bot.send_message(message.chat.id, "Вы вернулись в главное меню.", reply_markup=buttons.menu_buttons())
    
@bot.message_handler(func=lambda message: message.text == 'Вернутся в меню')
def handle_back(message):
    bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=buttons.main_menu_buttons())

@bot.message_handler(func=lambda message: message.text == 'Перейти в корзину')
def handle_back(message):
    bot.send_message(message.chat.id, "Вы перешли в корзину", reply_markup=buttons.menu_buttons())

@bot.message_handler(func=lambda message: message.text == 'Setlar')
def handle_sets(message):
    bot.send_message(message.chat.id, "Выберите сет:", reply_markup=buttons.Sets())

@bot.message_handler(func=lambda message: message.text == '🌯Lavash')
def handle_lavash(message):
    bot.send_message(message.chat.id, "Выберите Lavash:", reply_markup=buttons.La_vash())

@bot.message_handler(func=lambda message: message.text == '🌮Shaurma')
def handle_shaurma(message):
    bot.send_message(message.chat.id, "Выберите Shaurma:", reply_markup=buttons.Sha_urma())

@bot.message_handler(func=lambda message: message.text == '🍔Burger')
def handle_burger(message):
    bot.send_message(message.chat.id, "Выберите Burger:", reply_markup=buttons.Bur_ger())

@bot.message_handler(func=lambda message: message.text == '🌭Hot-dog')
def handle_hot_dog(message):
    bot.send_message(message.chat.id, "Выберите Hot-dog:", reply_markup=buttons.Hot_dog())

@bot.message_handler(func=lambda message: message.text == '🥤Ichimliklar')
def handle_drinks(message):
    bot.send_message(message.chat.id, "Выберите напиток:", reply_markup=buttons.Ichim_liklar())

@bot.message_handler(func=lambda message: message.text == '📞Aloqa')
def handle_contact(message):
    bot.send_message(message.chat.id, "Контакты: +998 90 123 45 67")

@bot.message_handler(func=lambda message: message.text == '📥Savat')
def handle_product_selection(message):
    product_name = message.text
    user_id = message.chat.id
    
    product_amount = 1  
    total_price = get_product_price(product_name)  
    location = get_user_location(user_id)  

    success = database.add_basket(user_id, product_name, product_amount, total_price, location)
    
    if success:
        bot.send_message(user_id, f"Товар '{product_name}' добавлен в вашу корзину.", reply_markup=buttons.buy_product())
    else:
        bot.send_message(user_id, "Произошла ошибка при добавлении товара в корзину. Пожалуйста, попробуйте снова.")

def get_product_price(product_name):
    return 100  

def get_user_location(user_id):
    return "Unknown Location"


@bot.message_handler(func=lambda message: message.text == '📥Добавить в корзину')
def handle_back(message):
    bot.send_message(message.chat.id, "Сколько закажете?", reply_markup=buttons.number())
  
@bot.message_handler(func=lambda message: message.text == '📨Xabar yuborish')
def handle_send_message(message):
    bot.send_message(message.chat.id, "Напишите ваше сообщение и мы с вами свяжемся.")

@bot.message_handler(func=lambda message: message.text == 'ℹ️Biz haqimizda')
def handle_about_us(message):
    bot.send_message(message.chat.id, "Мы компания, занимающаяся продажей вкусных блюд. У нас лучшие цены и качество!")

@bot.message_handler(func=lambda message: message.text == '🍩Shirinliklar')
def shirinliklar(message):
    bot.send_message(message.chat.id, "Выберите дисерт:",reply_markup=buttons.shirin_liklar())


@bot.message_handler(func=lambda message: message.text == '1')
def handle_back(message):
    bot.send_message(message.chat.id, "Вы выбрали - 1", reply_markup=buttons.Savat())

@bot.message_handler(func=lambda message: message.text == '2')
def handle_back(message):
    bot.send_message(message.chat.id, "Вы выбрали - 2", reply_markup=buttons.Savat())

@bot.message_handler(func=lambda message: message.text == '3')
def handle_back(message):
    bot.send_message(message.chat.id, "Вы выбрали - 3", reply_markup=buttons.Savat())

@bot.message_handler(func=lambda message: message.text == '4')
def handle_back(message):
    bot.send_message(message.chat.id, "Вы выбрали - 4", reply_markup=buttons.Savat())

@bot.message_handler(func=lambda message: message.text == '5')
def handle_back(message):
    bot.send_message(message.chat.id, "Вы выбрали - 5", reply_markup=buttons.Savat())

@bot.message_handler(func=lambda message: message.text == '6')
def handle_back(message):
    bot.send_message(message.chat.id, "Вы выбрали - 6", reply_markup=buttons.Savat())

@bot.message_handler(func=lambda message: message.text == '7')
def handle_back(message):
    bot.send_message(message.chat.id, "Вы выбрали - 7", reply_markup=buttons.Savat())

@bot.message_handler(func=lambda message: message.text == '8')
def handle_back(message):
    bot.send_message(message.chat.id, "Вы выбрали - 8", reply_markup=buttons.Savat())

@bot.message_handler(func=lambda message: message.text == '9')
def handle_back(message):
    bot.send_message(message.chat.id, "Вы выбрали - 9", reply_markup=buttons.Savat())

@bot.message_handler(func=lambda message: message.text == '10')
def handle_back(message):
    bot.send_message(message.chat.id, "Вы выбрали - 10", reply_markup=buttons.Savat())
    

@bot.message_handler(func=lambda message: message.text == '🍟☕️Combo Plus Isituvchan (Qora choy)')
def set1(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.combo_plus1())
    with open ('photo_2024-08-23_08-50-01.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:45000 som')       

@bot.message_handler(func=lambda message: message.text == '🌯🧃FitCombo')
def set2(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.combo_plus2())
    with open ('set2.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:35000 som')       

@bot.message_handler(func=lambda message: message.text == 'Iftar kofte grill mol goshtidan')
def set3(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.combo_plus3())
    with open ('set3.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:50000 som')       

@bot.message_handler(func=lambda message: message.text == 'Donar boks mol goshtidan')
def set4(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.combo_plus4())
    with open ('set4.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:80000 som')       

@bot.message_handler(func=lambda message: message.text == 'Donar boks tovuq goshtidan')
def set5(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.combo_plus5())
    with open ('set5.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:75000 som')         

@bot.message_handler(func=lambda message: message.text == '🍟🥤COMBO+')
def set6(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.combo_plus6())
    with open ('set6.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:60000 som')       

@bot.message_handler(func=lambda message: message.text == 'Iftar strips tovuq goshtidan')
def set7(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.combo_plus7())
    with open ('set7.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:40000 som')       

@bot.message_handler(func=lambda message: message.text == '🌭🧃🍟KidsCombo')
def set8(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.combo_plus8())
    with open ('set8.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:25000 som')       

                
@bot.message_handler(func=lambda message: message.text == '🐮🌶🌯Mol goshtidan qalampir lavash')
def lavash1(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Lavash_menu1())
    with open ('lavash1.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:24000 som')       

@bot.message_handler(func=lambda message: message.text == '🐔🌶🌯Tovuq qoshtli qalampir lavash')
def lavash2(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Lavash_menu2())
    with open ('lavash2.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:24000 som')       

@bot.message_handler(func=lambda message: message.text == '🐮🧀🌯Mol goshtidan pishloqli lavash STANDART')
def lavash3(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Lavash_menu3())
    with open ('lavash3.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:22000 som')       

@bot.message_handler(func=lambda message: message.text == '🐔🧀🌯Tovuq goshtidan pishloqli lavash STANDART')
def lavash4(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Lavash_menu4())
    with open ('lavash4.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:20000 som')       

@bot.message_handler(func=lambda message: message.text == 'FITTER')
def lavash5(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Lavash_menu5())
    with open ('lavash5.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:36000 som') 

@bot.message_handler(func=lambda message: message.text == '🐔🌯Lavash tovuq gosht')
def lavash6(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Lavash_menu6())
    with open ('lavash6.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:26000 som')       

@bot.message_handler(func=lambda message: message.text == '🐮🌯Lavash mol goshti')
def lavash7(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Lavash_menu7())
    with open ('lavash7.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:27000 som') 



@bot.message_handler(func=lambda message: message.text == '🐮🌶🌮Mol goshtidan qalampir shaurma')
def shaurma1(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Shaurma_menu1())
    with open ('shaurma1.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:32000 som')       

@bot.message_handler(func=lambda message: message.text == '🐔🌶🌮Tovuq goshtidan qalampir shaurma')
def shaurma2(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Shaurma_menu2())
    with open ('shaurma2.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:30000 som') 

@bot.message_handler(func=lambda message: message.text == '🐮🌮Mol goshtidan shaurma')
def shaurma3(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Shaurma_menu3())
    with open ('shaurma3.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:28000 som')       

@bot.message_handler(func=lambda message: message.text == '🐔🌮Tovuq goshtidan shaurma')
def shaurma4(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Shaurma_menu4())
    with open ('shaurma4.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:29000 som') 


@bot.message_handler(func=lambda message: message.text == '🍔Gamburger')
def burger1(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Burger_menu1())
    with open ('burger1.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:35000 som')       

@bot.message_handler(func=lambda message: message.text == 'Double burger')
def burger2(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Burger_menu2())
    with open ('burger2.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:50000 som') 

@bot.message_handler(func=lambda message: message.text == '🧀🍔Cheese burger')
def burger3(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Burger_menu3())
    with open ('burger3.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:40000 som')       

@bot.message_handler(func=lambda message: message.text == 'Double cheese burger')
def burger4(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Burger_menu4())
    with open ('burger4.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:30000 som') 


@bot.message_handler(func=lambda message: message.text == 'Hot-dog baguette')
def hotdog1(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Hotdog_menu1())
    with open ('hotdog1.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:30000 som')       

@bot.message_handler(func=lambda message: message.text == 'Hot-dog baguette double')
def hotdog2(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Hotdog_menu2())
    with open ('hotdog2.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:35000 som')       

@bot.message_handler(func=lambda message: message.text == '👶🏻🌭Hot-dog kids')
def hotdog3(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Hotdog_menu3())
    with open ('hotdog3.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:12000 som')       

@bot.message_handler(func=lambda message: message.text == 'Hot-dog classic')
def hotdog4(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Hotdog_menu4())
    with open ('hotdog4.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:16000 som')       

@bot.message_handler(func=lambda message: message.text == '🐔🧀Sub tovuq cheese')
def hotdog5(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Hotdog_menu5())
    with open ('hotdog5.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:26000 som')         

@bot.message_handler(func=lambda message: message.text == '🐔Sub tovuq')
def hotdog6(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Hotdog_menu6())
    with open ('hotdog6.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:27000 som')       

@bot.message_handler(func=lambda message: message.text == '🐮🧀Sub gosht cheese')
def hotdog7(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Hotdog_menu7())
    with open ('hotdog7.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:25000 som')       

@bot.message_handler(func=lambda message: message.text == '🐮Sub gosht')
def hotdog8(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Hotdog_menu8())
    with open ('hotdog8.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:22000 som')  


@bot.message_handler(func=lambda message: message.text == '🍩Donut qulupnayli')
def shirinlik1(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.shirinliklar_menu1())
    with open ('donut1.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:20000 som')       

@bot.message_handler(func=lambda message: message.text == '🍩Donut karamelli')
def shirinlik2(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.shirinliklar_menu2())
    with open ('donut2.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:20000 som') 

@bot.message_handler(func=lambda message: message.text == 'Chizkeyk')
def shirinlik3(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.shirinliklar_menu3())
    with open ('chizkeyk.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:35000 som')       

@bot.message_handler(func=lambda message: message.text == 'Medovik asalim')
def shirinlik4(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.shirinliklar_menu4())
    with open ('medovik.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:25000 som') 


@bot.message_handler(func=lambda message: message.text == '🧃Sok dena 0,33L')
def ichimlik1(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Ichimlik_menu1())
    with open ('ichimlik1.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:10000 som')       

@bot.message_handler(func=lambda message: message.text == 'Gazsiz suv 0,5L')
def ichimlik2(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Ichimlik_menu2())
    with open ('ichimlik2.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:3000 som')       

@bot.message_handler(func=lambda message: message.text == 'Pepsi 0,5L')
def ichimlik3(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Ichimlik_menu3())
    with open ('ichimlik3.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:7000 som')       

@bot.message_handler(func=lambda message: message.text == 'Pepsi 1,5L')
def ichimlik4(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Ichimlik_menu4())
    with open ('ichimlik4.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:13000 som')       

@bot.message_handler(func=lambda message: message.text == '🥤Quyib beriladigan pepsi')
def ichimlik5(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Ichimlik_menu5())
    with open ('ichimlik5.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:90000 som')         

@bot.message_handler(func=lambda message: message.text == '🥤Quyib beriladigan mirinda')
def ichimlik6(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Ichimlik_menu6())
    with open ('ichimlik6.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:8000 som')       

@bot.message_handler(func=lambda message: message.text == 'Bliss sharbati')
def ichimlik7(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Ichimlik_menu7())
    with open ('ichimlik7.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:10000 som')       

@bot.message_handler(func=lambda message: message.text == '☕️Coffee Amerikano')
def ichimlik8(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Ichimlik_menu8())
    with open ('ichimlik8.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:25000 som') 
        
@bot.message_handler(func=lambda message: message.text == '☕️Coffee Latte')
def ichimlik9(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Ichimlik_menu9())
    with open ('ichimlik9.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:20000 som')         

@bot.message_handler(func=lambda message: message.text == 'Kok choy')
def ichimlik10(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Ichimlik_menu10())
    with open ('ichimlik10.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:5000 som')       

@bot.message_handler(func=lambda message: message.text == 'Qora choy')
def ichimlik11(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Ichimlik_menu11())
    with open ('ichimlik11.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:5000 som')

@bot.message_handler(func=lambda message: message.text == '🍋Limonli kok choy')
def ichimlik12(message):
    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=buttons.Ichimlik_menu12())
    with open ('ichimlik12.jpg', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo, caption='Narxi:7000 som') 

# Savat


@bot.message_handler(func=lambda message: message.text == 'Добавить в корзину')
def ichimlik12(message):
    bot.send_message(message.chat.id, "Добавить в корзину", reply_markup=buttons.Savat_button())

@bot.message_handler(func=lambda message: message.text == 'Оплатить товар')
def ichimlik12(message):
    bot.send_message(message.chat.id, "Нажмите на кнопку", reply_markup=buttons.buys_product())


@bot.message_handler(func=lambda message: message.text == 'Оплатить наличными')
def ichimlik12(message):
    bot.send_message(message.chat.id, "Вы оплатили наличными", reply_markup=buttons.menu_buttons())

@bot.message_handler(func=lambda message: message.text == 'Оплатить картой')
def ichimlik12(message):
    bot.send_message(message.chat.id, "Вы оплатили картой", reply_markup=buttons.menu_buttons())




bot.polling()




