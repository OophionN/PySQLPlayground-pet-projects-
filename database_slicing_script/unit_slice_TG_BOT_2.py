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


# In[2]:


#!pip install python-telegram-bot
#!pip  install --upgrade python-telegram-bot


# In[2]:


# Определение директории, где хранятся папки с датами
base_dir = 'C:\\Users\\maksa\\Desktop\\123finance\\заначка\\база ильи'
# Получение списка всех файлов и папок в директории
all_files = os.listdir(base_dir)


# In[3]:


# Фильтрация списка, чтобы оставить только папки с датами в нужном формате
date_folders = [f for f in all_files if re.match(r'\d{2}_\d{2}', f)]


# In[4]:


current_date = datetime.now()

# Добавляем один день, чтобы получить завтрашнюю дату
tomorrow_date = current_date + timedelta(days=1)

# Форматируем дату в формат "дд_мм"
formatted_tomorrow_date = tomorrow_date.strftime("%d_%m")

print(formatted_tomorrow_date)


# In[5]:


current_date = date.today().strftime("%d_%m")


# In[7]:


# Преобразование названий папок в объекты datetime
dates = []
for folder in date_folders:
    try:
        dates.append(datetime.strptime(folder, "%d_%m"))
    except ValueError:
        continue  # Пропускаем названия, которые не соответствуют формату даты


# In[8]:


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


# In[9]:


def google_sheets_service():
    creds = Credentials.from_authorized_user_file(r'C:\Users\maksa\all_repo\credentials.json')
    service = build('sheets', 'v4', credentials=creds)
    return service.spreadsheets()


# In[10]:


def upload_to_google_sheets(data, spreadsheet_id, range_name):
    # Убедитесь, что data является списком списков
    service = google_sheets_service()
    request = service.values().update(spreadsheetId=spreadsheet_id, range=range_name,
                                      valueInputOption='RAW', body={'values': data})
    response = request.execute()
    print(response)


# In[11]:


fincrm_staraya = upload_rest_data('fincrm', dates, base_dir)


# In[14]:


#fincrm_staraya.drop('Unnamed: 0', axis=1, inplace=True)


# In[12]:


fincrm_staraya.sample(2)


# In[13]:


ar_base = upload_rest_data('artur', dates, base_dir)


# In[14]:


ar_base.sample(2)


# In[15]:


basis_staraya = upload_rest_data('basis', dates, base_dir)


# In[16]:


basis_staraya.sample(2)


# In[17]:


retro_base = upload_rest_data('retro', dates, base_dir)


# In[21]:


#retro_base.drop('Unnamed: 0', axis=1, inplace=True)


# In[18]:


retro_base.sample(2)


# In[19]:


fincrm_nofio_base = upload_rest_data('fincrm_no_fio', dates, base_dir)


# In[20]:


fincrm_nofio_base.sample(2)


# In[21]:


iliay_base = upload_rest_data('iliay_base', dates, base_dir)


# In[22]:


iliay_base.sample(2)


# In[23]:


cript_vov_base = upload_rest_data('cript_vov', dates, base_dir)


# In[24]:


cript_vov_base.sample(2)


# In[25]:


danila_bfl_rob_base = upload_rest_data('danila_bfl_rob', dates, base_dir)


# In[26]:


danila_bfl_rob_base.sample(2) 


# In[27]:


fincrm=fincrm_staraya.copy ()
artur=ar_base.copy()
basis=basis_staraya.copy()
retro=retro_base.copy()
fincrm_nofio=fincrm_nofio_base.copy()
iliay=iliay_base.copy ()
cript_vov=cript_vov_base.copy()
danila_bfl_rob=danila_bfl_rob_base.copy()


# In[28]:


filtered_dataframes = {
    'fincrm': fincrm,
    'artur': artur,
    'basis': basis,
    'retro': retro,
    'fincrm_nofio': fincrm_nofio,
    'iliay':iliay,
    'cript_vov':cript_vov,
    'danila_bfl_rob':danila_bfl_rob
    
}


# In[33]:


zakaz = pd.read_csv(f"C:\\Users\\maksa\\Desktop\\123finance\\заначка\\база ильи\\{current_date}\\заказ_нарезка\\all_orders.csv",
                    sep=';', encoding='Windows-1251')


# In[34]:


sprav = pd.read_excel(r'C:\Users\maksa\123fin\zanachka\Справочник регионов2.xlsx')


# In[35]:


zakaz = mf.data_preprocessing(zakaz)


# In[36]:


zakaz


# In[37]:


zakaz.rows.sum()


# In[38]:


datasets = {
    'fincrm': fincrm,
    'артур': artur,
    'основа': basis,
    'ретро': retro,
    'fincrm_no_fio':fincrm_nofio,
    'илья':iliay,
    'cript_vov':cript_vov,
    'danila':danila_bfl_rob
}


# In[39]:


for source, dataset in datasets.items():
    if 'unified_name' not in dataset.columns:
        print(f"В датасете от '{source}' отсутствует столбец 'unified_name'")


# In[40]:


container = pd.DataFrame()


# In[41]:


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


# In[42]:


container


# In[43]:


replace_dict = {
    'fincrm_bfl_robot': 'fin_crm_robot',
    'артур_bfl_robot': 'artur_bfl_robot',
    'основа_bfl_robot': 'osnova_robot',
    'ретро_bfl_robot': 'retro_bfl_robot',
    'fincrm_no_fio_bfl_robot':'fincrm_no_fio_bfl_robot',
    'илья_bfl_robot':'fedor_robot',
    'cript_vov_bfl_robot':'kripta_rob',
    'danila_bfl_robot':'danila_bfl_rob'
}

container['partner'] = container['partner'].replace(replace_dict)


# In[44]:


container


# In[45]:


container.region.value_counts()


# In[46]:


container = container.drop('region', axis=1)
container = container.rename(columns={'unified_name': 'region'})


# In[47]:


new_order = ['first_name', 'last_name', 'middle_name', 'email', 'city', 'region', 'phone', 'partner', 'birthdate', 'amount']

container = container[new_order]


# In[48]:


container.partner.value_counts()


# In[49]:


container.phone.count()


# In[50]:


partners = container['partner'].unique()


# In[51]:


container.to_excel(
    f"C:\\Users\\maksa\\Desktop\\123finance\\заначка\\база ильи\\{current_date}\\на отправку\\unity_base_{current_date}.xlsx", index=False)


# In[52]:


# Токен бота
bot_token = '6467070962:AAG15Y-3tMol2-fGQ_kU9d5pA03_QTR3fqI'
bot = Bot(token=bot_token)

# ID чата, куда будут отправляться файлы 
chat_ids = [415338551, 389809710, 545727398]
#, -4005852353


# In[53]:


async def send_document(chat_id, document, caption):
    try:
        await bot.send_document(chat_id=chat_id, document=document, caption=caption)
    except Exception as e:
        print(f"Ошибка при отправке документа: {e}")


# In[54]:


async def main():
    for partner in partners:
        partner_data = container[container['partner'] == partner]
        file_path = f"C:\\Users\\maksa\\Desktop\\123finance\\заначка\\база ильи\\{current_date}\\на отправку\\{partner}_{current_date}_for_{formatted_tomorrow_date}.xlsx"
        partner_data.to_excel(file_path, index=False)
        for chat_id in chat_ids:
            with open(file_path, 'rb') as file:
                await send_document(chat_id, file, f"{partner}_{current_date}_for_{partner}_{current_date}_for_{formatted_tomorrow_date}.xlsx")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    if loop.is_running():
        # Для сред, где цикл уже запущен
        loop.create_task(main())
    else:
        # Стандартный запуск асинхронной функции
        loop.run_until_complete(main())


# In[55]:


def clear_google_sheets(spreadsheet_id, sheet_name):
    service = google_sheets_service()
    # Для очистки всего листа, используем имя листа без указания диапазона ячеек
    # Пример range_name: '{name}' вместо '{name}!A1'
    full_range_name = sheet_name  # sheet_name - это переменная с именем листа
    request = service.values().clear(spreadsheetId=spreadsheet_id, range=full_range_name, body={})
    response = request.execute()
    print(f"Cleared data from: {full_range_name}")


# In[56]:


def save_data_and_counts(dataset, name, current_date):
    # Сохраняем остатки базы в формате CSV
    dataset.to_csv(
        f"C:\\Users\\maksa\\Desktop\\123finance\\заначка\\база ильи\\{current_date}\\остатки баз\\rest_{name}_{current_date}.csv", index=False)

    # Подсчитываем количество строк по регионам и сохраняем в формате EXCEL
    region_counts = dataset['unified_name'].value_counts()
    region_counts.to_excel(
        f"C:\\Users\\maksa\\Desktop\\123finance\\заначка\\база ильи\\{current_date}\\потенциал\\{name}_{current_date}_poten_rest.xlsx")

    # Преобразовываем данные для загрузки в Google Sheets
    region_counts_df = region_counts.reset_index()
    region_counts_df.columns = ['Region', 'Count']
    data = region_counts_df.values.tolist()

    spreadsheet_id = '1xGrphQs_Y_9qZQ6FpSz_JsIj2RkWNttm_fEq4kCCzls'
    range_name = f'{name}!A1'  # Диапазон для вставки данных
    
    #лист для очистки
    sheet_name = name

    # Очистка данных на листе перед загрузкой новых
    clear_google_sheets(spreadsheet_id, sheet_name)

    # Загрузка новых данных
    upload_to_google_sheets(data, spreadsheet_id, range_name)


# In[57]:


# Вызываем функцию для каждого источника
save_data_and_counts(fincrm, 'fincrm', current_date)
save_data_and_counts(artur, 'artur', current_date)
save_data_and_counts(basis, 'basis', current_date)
save_data_and_counts(retro, 'retro', current_date)
save_data_and_counts(fincrm_nofio, 'fincrm_no_fio', current_date)
save_data_and_counts(iliay, 'iliay_base', current_date)
save_data_and_counts(cript_vov, 'cript_vov', current_date)
save_data_and_counts(danila_bfl_rob, 'danila_bfl_rob', current_date)

