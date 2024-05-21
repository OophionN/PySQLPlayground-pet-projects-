#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[1]:


import pandas as pd 
import numpy as np
import my_func as mf
import chardet
from datetime import datetime
import glob
import datetime
from datetime import timedelta
from datetime import datetime
import os
from datetime import date
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import re
import telegram
from telegram.ext import Updater
import asyncio
from telegram import Bot
import aiohttp
from aiofiles import open as aiofiles_open
import base64
import json
from aiohttp import ClientSession, ClientTimeout
import logging



# Настройка логгера
logger = logging.getLogger('send_data_to_server')
logger.setLevel(logging.DEBUG)  # Установка уровня логирования
file_handler = logging.FileHandler(
    'C:\\Users\\****************\\log\\send_data_to_server.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)




token = "**********"
encoded_token = base64.b64encode(token.encode('utf-8')).decode('utf-8')
print(encoded_token)


# Токен бота
bot_token = '*****************************'
bot = Bot(token=bot_token)

# ID чата, куда будут отправляться файлы 
chat_ids = [*********, ***********, ***********]


# Определение директории, где хранятся папки с датами
base_dir = 'C:\\Users\\************'
# Получение списка всех файлов и папок в директории
all_files = os.listdir(base_dir)

# Фильтрация списка, чтобы оставить только папки с датами в нужном формате
date_folders = [f for f in all_files if re.match(r'\d{2}_\d{2}', f)]



current_date = datetime.now()

# Добавляем один день, чтобы получить завтрашнюю дату
tomorrow_date = current_date + timedelta(days=1)

# Форматируем дату в формат "дд_мм"
formatted_tomorrow_date = tomorrow_date.strftime("%d_%m")

print(formatted_tomorrow_date)


current_date = date.today().strftime("%d_%m")


# Преобразование названий папок в объекты datetime
dates = []
for folder in date_folders:
    try:
        dates.append(datetime.strptime(folder, "%d_%m"))
    except ValueError:
        continue  # Пропускаем названия, которые не соответствуют формату даты



def upload_rest_data(data_name, dates, base_dir):
    # Получение текущей даты в нужном формате
    current_date = date.today().strftime("%d_%m")

    # Преобразование текущей даты в объект datetime для сравнения
    current_date_dt = datetime.strptime(current_date, "%d_%m")

    # Удаление текущей даты из списка dates
    dates = [d for d in dates if d != current_date_dt]

    if dates:
        latest_date = max(dates)
        latest_date_str = latest_date.strftime("%d_%m")

        # Формирование пути к файлу с использованием последней даты
        df_staraya_path = os.path.join(
            base_dir, latest_date_str, 'остатки баз', f'rest_{data_name}_{latest_date_str}.csv')

        # Загрузка файла в DataFrame
        data_frame = pd.read_csv(df_staraya_path, low_memory=False)
        return data_frame
    else:
        print("Не найдены подходящие папки с данными.")
        return None



def google_sheets_service():
    creds = Credentials.from_authorized_user_file(r'C:\Users*********\credentials.json')
    service = build('sheets', 'v4', credentials=creds)
    return service.spreadsheets()


def upload_to_google_sheets(data, spreadsheet_id, range_name):
    # Убедитесь, что data является списком списков
    service = google_sheets_service()
    request = service.values().update(spreadsheetId=spreadsheet_id, range=range_name,
                                      valueInputOption='RAW', body={'values': data})
    response = request.execute()
    print(response)


# Выгрузка остатков баз
*******_staraya = upload_rest_data('******', dates, base_dir)


******_staraya.sample(2)



# создаем словарь


filtered_dataframes = {
    '*****': *****,
    '*****': *****
       
}



zakaz = pd.read_csv(f"C:\\Users\\**********\\{current_date}\\заказ_нарезка\\all_orders_new.csv",
                    sep=';', encoding='Windows-1251')


# Выгружаем справочник для корректировки и унификации названий регионов


sprav = pd.read_excel(r'C:\Users\******\Справочник регионов2.xlsx')


# обработка


zakaz = mf.data_preprocessing(zakaz)



count_regions=zakaz.groupby('region')['limit'].sum()



df_counts = pd.DataFrame(count_regions).reset_index()


df_counts



# справочник гео - согласован с партнером для общего использования одинаковых ID
region_id = pd.read_csv(f"C:\\Users\\********\\geo_dis.csv",
                    sep=';', encoding='Windows-1251')


region_id = mf.data_preprocessing(region_id)


df_result = pd.merge(df_counts, region_id, left_on='region', right_on='name', how='left')



df_zakaz_region = df_result[['region', 'limit', 'id']]


zakaz.rows.sum()


# используем справочник


datasets = {
    '***': ****,
    '****': *****,
    ******
}



for source, dataset in datasets.items():
    if 'unified_name' not in dataset.columns:
        print(f"В датасете от '{source}' отсутствует столбец 'unified_name'")


# подготавливаем контейнер с заказом


container = pd.DataFrame()



for index, row in zakaz.iterrows():
    region = row['region']
    source = row['source']
    num_rows = row['rows']

    if source in datasets:
        dataset = datasets[source]
        # Используем регулярное выражение для поиска точного соответствия
        mask = dataset["unified_name"].str.contains(r'\b' + region + r'\b', na=False, regex=True)
        selected_rows = dataset[mask].head(num_rows)
        dataset.drop(selected_rows.index, inplace=True)  # Удаляем выбранные строки из исходного датасета
        selected_rows['partner'] = source + '_bfl_robot'  # Добавляем столбец с источником
        selected_rows[['birthdate','amount', 'email']] = ''  # Добавляем пустые столбцы
        container = pd.concat([container, selected_rows], ignore_index=True)


# словарь для замен


replace_dict = {
    '******_bfl_robot': '*****',
    ********
}

container['partner'] = container['partner'].replace(replace_dict)


container = container.drop('region', axis=1)
container = container.rename(columns={'unified_name': 'region'})



new_order = ['first_name', 'last_name', 'middle_name', 'email', 'city', 'region', 'phone', 'partner', 'birthdate', 'amount']

container = container[new_order]


container.partner.value_counts(dropna=False)



partners = container['partner'].unique()


regions = container.region.unique()


# сохраняем файл на всякий случай
container.to_excel(
    f"C:\\Users\\******\\{current_date}\\на отправку\\unity_base_{current_date}_API.xlsx", index=False)


# функция отправки через ТГ 


async def send_document(chat_id, document, caption):
    try:
        await bot.send_document(chat_id=chat_id, document=document, caption=caption)
    except Exception as e:
        print(f"Ошибка при отправке документа: {e}")


# функция получения данных по региону


def get_region_data(region_name):
    row = df_zakaz_region[df_zakaz_region['region'] == region_name].iloc[0]
    return {
        'region_id': row['id'],
        'limit': row['limit']
    }


# функция отправки данных на сервер по API


async def send_data_to_server(region_id, limit, data, encoded_token):
    url = "https://gate.crmcalls.ru/api/base_api/apiBase/"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {token}'
    }

    modified_data = []
    for entry in data:
        fields = {
            "first_name": entry.get("first_name", ""),
            "last_name": entry.get("last_name", ""),
            "middle_name": entry.get("middle_name", ""),
            "email": entry.get("email", ""),
            "city": entry.get("city", ""),
            "region": entry.get("region", ""),
            "birthdate": entry.get("birthdate", ""),
            "amount": entry.get("amount", ""),
            "partner": entry.get("partner", "")
        }
        modified_entry = {
            "phone": entry.get("phone", ""),
            "fields": fields
        }
        modified_data.append(modified_entry)

    body = {
        'region_id': region_id,
        'limit': limit,
        'base': modified_data
    }

    timeout = ClientTimeout(total=120)

    async with ClientSession(timeout=timeout) as session:
        try:
            logger.debug(
                f"Sending data to server with region_id: {region_id} and limit: {limit}")
            logger.debug(
                f"Data: {json.dumps(body, ensure_ascii=False, indent=2)}")
            async with session.post(url, json=body, headers=headers) as response:
                response_text = await response.text()
                if response.status != 200:
                    logger.error(
                        f"Unexpected status: {response.status}; Response: {response_text}")
                    return response.status, response_text
                logger.info(
                    f"Status: {response.status}; Response: {response_text if response_text else 'No content returned'}")
                return response.status, response_text

        except asyncio.TimeoutError as e:
            logger.error(f"Timeout error occurred: {str(e)}", exc_info=True)
            return None, f"Timeout error occurred: {str(e)}"
        except Exception as e:
            logger.error(
                f"An unexpected error occurred: {str(e)}", exc_info=True)
            return None, f"An unexpected error occurred: {str(e)}"


# Основная функция обработки и отправки данных


async def main(df_zakaz_region, container, encoded_token):
    for index, row in df_zakaz_region.iterrows():
        region_name = row['region']
        region_id = row['id']
        limit = row['limit']
        
        # Выбираем строки, соответствующие текущему региону и заменяем NaN
        region_data = container[container['region'] == region_name].fillna('')

        # Формируем данные для отправки
        data_to_send = region_data.to_dict('records')
        
        # Отправляем данные партнеру
        status, response = await send_data_to_server(region_id, limit, data_to_send, encoded_token)
        print(f"Sending data to server with region_id: {region_id} and limit: {limit}")
        #print(f"Data: {json.dumps(data_to_send, ensure_ascii=False, indent=2)}")
        print(f"Status: {status}; Response: {response}")
        
        #Отправка фойлов по регионам в бота (страховка для Ильи)
        for region in regions:
            region_data = container[container['region'] == region]
            file_path = f"C:\\Users\\maksa\\Desktop\\123finance\\заначка\\база ильи\\{current_date}\\на отправку_test\\{region}_{current_date}_for_{formatted_tomorrow_date}.xlsx"
            region_data.to_excel(file_path, index=False)
            #for chat_id in chat_ids:
                #with open(file_path, 'rb') as file:
                    #await send_document(chat_id, file, f"{region}_{current_date}_for_{formatted_tomorrow_date}.xlsx")
    



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    
    # Проверяем, запущен ли уже цикл событий
    if loop.is_running():
        loop.create_task(main(df_zakaz_region, container, encoded_token))
    else:
        loop.run_until_complete(main(df_zakaz_region, container, encoded_token))


# Очистка данных на листе Google Sheets


def clear_google_sheets(spreadsheet_id, sheet_name):
    service = google_sheets_service()
    # Для очистки всего листа, используем имя листа без указания диапазона ячеек
    # Пример range_name: '{name}' вместо '{name}!A1'
    full_range_name = sheet_name  # sheet_name - это переменная с именем листа
    request = service.values().clear(spreadsheetId=spreadsheet_id, range=full_range_name, body={})
    response = request.execute()
    print(f"Cleared data from: {full_range_name}")


# Сохранение данных и подсчет строк по регионам


def save_data_and_counts(dataset, name, current_date):
    # Сохраняем остатки базы в формате CSV
    dataset.to_csv(
        f"C:\\Users\\*************\\{current_date}\\остатки баз\\rest_{name}_{current_date}.csv", index=False)

    # Подсчитываем количество строк по регионам и сохраняем в формате EXCEL
    region_counts = dataset['unified_name'].value_counts()
    region_counts.to_excel(
        f"C:\\Users\\**********\\{current_date}\\потенциал\\{name}_{current_date}_poten_rest.xlsx")

    # Преобразовываем данные для загрузки в Google Sheets
    region_counts_df = region_counts.reset_index()
    region_counts_df.columns = ['Region', 'Count']
    data = region_counts_df.values.tolist()

    spreadsheet_id = '****************'
    range_name = f'{name}!A1'  # Диапазон для вставки данных
    
    #лист для очистки
    sheet_name = name

    # Очистка данных на листе перед загрузкой новых
    clear_google_sheets(spreadsheet_id, sheet_name)

    # Загрузка новых данных
    upload_to_google_sheets(data, spreadsheet_id, range_name)


# Вызываем функцию для каждого источника
save_data_and_counts(******, '*****', current_date)


