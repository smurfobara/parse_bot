import telebot
import config
bot = telebot.TeleBot(config.TOKEN)
from telebot import types
import threading
from selenium import webdriver
import time
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
path_ = webdriver.ChromeService(executable_path=binary_path)
import re
import datetime
import schedule

@bot.message_handler(commands=['test'])
def send_e(message):
    bot.send_message(message.chat.id, 'Ожидайте')
    try:
        br = webdriver.Chrome(service=path_)
        br.get('https://cbr.ru/key-indicators/')
        time.sleep(1)
        element_c_d = br.find_element(By.XPATH, "(//td[@class='value td-w-4 _bold _end mono-num _with-icon _down _green'])[2]").text
        element_c_d = element_c_d[:len(element_c_d) - 2]
        element_c_e = br.find_element(By.XPATH, "(//td[@class='value td-w-4 _bold _end mono-num _with-icon _down _green'])[3]").text
        element_c_e = element_c_e[:len(element_c_e) - 2]
    except Exception as ex:
        print(ex)
    finally:
        br.close()
        br.quit()
    try:
        br = webdriver.Chrome(service=path_)
        br.get('https://www.gismeteo.ru/weather-sortavala-3931/')
        time.sleep(1)
        element_temp = br.find_element(By.XPATH, "(//span[@class='unit unit_temperature_c'])[1]").text
        element_temp_o = br.find_element(By.XPATH, "(//span[@class='unit unit_temperature_c'])[2]").text
        element_weath_e = br.find_element(By.XPATH, "(//a[@class='weathertab weathertab-link tooltip'])[1]")
        element_weath = element_weath_e.get_attribute('data-text')
    except Exception as ex:
        print(ex)
    finally:
        br.close()
        br.quit()
    bot.send_message(message.chat.id, f'Сводка данных\n==========\n==========\n\nПогода сегодня: {element_weath}\nТемпература: {element_temp}, ощущается как: {element_temp_o}\n\n==========\n\nКурс Доллара: {element_c_d}\nКурс Евро: {element_c_e}')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Этот бот может присылать сводку информации о погоде и курсах валют ежедневно в 10:00\nЧтобы включить ежедневную отправку в этом чате напишите /enabledist')
    bot.send_message(message.chat.id, 'Чтобы бот работал в группе:\n1. Добавьте бота в группу и сделайте админом\n2. Пропишите в группе команду /start\n3. Пропишите команду /enabledist\nГотово!')

@bot.message_handler(commands=['enabledist'])
def enable_dist(message):
    with open('IDs_chats_enabled_dist.txt', 'r') as f:
        text = f.read()
        if str(message.chat.id) in text:
            bot.send_message(message.chat.id, 'Сводка уже включена!')
        else:
            with open('IDs_chats_enabled_dist.txt', 'a', encoding='utf-8') as c:
                c.write(f'{str(message.chat.id)}\n')
            bot.send_message(message.chat.id, 'Готово! Теперь сводка будет приходить сюда.')

@bot.message_handler(commands=['disabledist'])
def disable_dist(message):
    with open('IDs_chats_enabled_dist.txt', 'r') as f:
        lines = f.readlines()
    with open('IDs_chats_enabled_dist.txt', 'w') as f:
        for line in lines:
            if line.strip('\n') != str(message.chat.id):
                f.write(line)
    bot.send_message(message.chat.id, 'Теперь сводка не будет приходить в этот чат.')

print('working')

def send_sv():
    try:
        br = webdriver.Chrome(service=path_)
        br.get('https://cbr.ru/key-indicators/')
        time.sleep(1)
        element_c_d = br.find_element(By.XPATH, "(//td[@class='value td-w-4 _bold _end mono-num _with-icon _down _green'])[2]").text
        element_c_d = element_c_d[:len(element_c_d) - 2]
        element_c_e = br.find_element(By.XPATH, "(//td[@class='value td-w-4 _bold _end mono-num _with-icon _down _green'])[3]").text
        element_c_e = element_c_e[:len(element_c_e) - 2]
    except Exception as ex:
        print(ex)
    finally:
        br.close()
        br.quit()
    try:
        br = webdriver.Chrome(service=path_)
        br.get('https://www.gismeteo.ru/weather-sortavala-3931/')
        time.sleep(1)
        element_temp = br.find_element(By.XPATH, "(//span[@class='unit unit_temperature_c'])[1]").text
        element_temp_o = br.find_element(By.XPATH, "(//span[@class='unit unit_temperature_c'])[2]").text
        element_weath_e = br.find_element(By.XPATH, "(//a[@class='weathertab weathertab-link tooltip'])[1]")
        element_weath = element_weath_e.get_attribute('data-text')
    except Exception as ex:
        print(ex)
    finally:
        br.close()
        br.quit()
    with open('IDs_chats_enabled_dist.txt', 'r') as f:
        text = f.read()
        list_ = text.split()
        list_ids = []
        for i in list_:
            list_ids.append(int(i))
        print(list_ids)
    for item in list_ids:
        item = int(item)
        bot.send_message(item, f'Сводка данных\n====================\n====================\n\nПогода сегодня: {element_weath}\nТемпература: {element_temp}, ощущается как: {element_temp_o}\n\n==========\n\nКурс Доллара: {element_c_d}\nКурс Евро: {element_c_e}')

#@bot.message_handler(commands=['settime'])
#def change_time(message):
 #   if message.from_user.id == config.admin:
  #      text_list = message.text
   #     text_list = text_list.split()                                  ЗАДЕЛ ПОД НАСТРОЙКУ
    #    print(text_list)
     #   if len(text_list) != 0:
      #      pattern = re.compile("^([01]?[0-9]|2[0-3]):[0-5][0-9]$")
       #     if pattern.match(text_list[1]):
        #        bot.send_message(message.chat.id, 'all is good')
         #   else:
          #      bot.send_message(message.chat.id, 'something was wrong')

schedule.every().day.at('10:00').do(send_sv)

def loop():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    thread = threading.Thread(target=loop)
    thread.start()
    bot.polling(none_stop=True)



