#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Описание-проекта" data-toc-modified-id="Описание-проекта-1"><span class="toc-item-num">1&nbsp;&nbsp;</span><font face="liberation serif" size="5">Описание проекта</font></a></span><ul class="toc-item"><li><span><a href="#Описание-данных." data-toc-modified-id="Описание-данных.-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span><font face="liberation serif" size="4">Описание данных.</font></a></span></li><li><span><a href="#Цели." data-toc-modified-id="Цели.-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span><font face="liberation serif" size="4">Цели.</font></a></span></li><li><span><a href="#Декомпозиция-задачи." data-toc-modified-id="Декомпозиция-задачи.-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span><font face="liberation serif" size="4">Декомпозиция задачи.</font></a></span></li></ul></li><li><span><a href="#Общая-подготовка" data-toc-modified-id="Общая-подготовка-2"><span class="toc-item-num">2&nbsp;&nbsp;</span><font face="liberation serif" size="5">Общая подготовка</font></a></span></li><li><span><a href="#Mодуль-my_func" data-toc-modified-id="Mодуль-my_func-3"><span class="toc-item-num">3&nbsp;&nbsp;</span><font face="liberation serif" size="5">Mодуль my_func</font></a></span><ul class="toc-item"><li><span><a href="#Выполним-загрузку-и-вывод-информации-через-запрос-SQL" data-toc-modified-id="Выполним-загрузку-и-вывод-информации-через-запрос-SQL-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span><font face="liberation serif" size="4">Выполним загрузку и вывод информации через запрос SQL</font></a></span></li><li><span><a href="#Корректировка-типов-данных-" data-toc-modified-id="Корректировка-типов-данных--3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span><font face="liberation serif" size="4">Корректировка типов данных </font></a></span></li><li><span><a href="#Обогащение-данных-информацией-из-файла-sp_gr_test.xlsx" data-toc-modified-id="Обогащение-данных-информацией-из-файла-sp_gr_test.xlsx-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span><font face="liberation serif" size="4">Обогащение данных информацией из файла sp_gr_test.xlsx</font></a></span></li></ul></li><li><span><a href="#Базовый-анализ-данных-(согласно-ТЗ)" data-toc-modified-id="Базовый-анализ-данных-(согласно-ТЗ)-4"><span class="toc-item-num">4&nbsp;&nbsp;</span><font face="liberation serif" size="5">Базовый анализ данных (согласно ТЗ)</font></a></span><ul class="toc-item"><li><span><a href="#Период-за-который-имеются-данные." data-toc-modified-id="Период-за-который-имеются-данные.-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span><font face="liberation serif" size="4">Период за который имеются данные.</font></a></span></li><li><span><a href="#Сколько-и-какие-именно-железные-дороги-приведены-в-таблице" data-toc-modified-id="Сколько-и-какие-именно-железные-дороги-приведены-в-таблице-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span><font face="liberation serif" size="4">Сколько и какие именно железные дороги приведены в таблице</font></a></span></li><li><span><a href="#Сколько-и-какие-именно-есть-группы-груза-в-таблице" data-toc-modified-id="Сколько-и-какие-именно-есть-группы-груза-в-таблице-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span><font face="liberation serif" size="4">Сколько и какие именно есть группы груза в таблице</font></a></span></li><li><span><a href="#Максимальный-и-минимальный-объем" data-toc-modified-id="Максимальный-и-минимальный-объем-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span><font face="liberation serif" size="4">Максимальный и минимальный объем</font></a></span></li><li><span><a href="#Выведение-дополнительной-информации" data-toc-modified-id="Выведение-дополнительной-информации-4.5"><span class="toc-item-num">4.5&nbsp;&nbsp;</span><font face="liberation serif" size="4">Выведение дополнительной информации</font></a></span></li><li><span><a href="#Возвращение-колонок-заявленному-виду" data-toc-modified-id="Возвращение-колонок-заявленному-виду-4.6"><span class="toc-item-num">4.6&nbsp;&nbsp;</span><font face="liberation serif" size="4">Возвращение колонок заявленному виду</font></a></span></li><li><span><a href="#Общий-вывод-по-подготовке,-прдварительной-обработке-и-базовому-исследованию-по-ТЗ" data-toc-modified-id="Общий-вывод-по-подготовке,-прдварительной-обработке-и-базовому-исследованию-по-ТЗ-4.7"><span class="toc-item-num">4.7&nbsp;&nbsp;</span><font face="liberation serif" size="4">Общий вывод по подготовке, прдварительной обработке и базовому исследованию по ТЗ</font></a></span></li></ul></li><li><span><a href="#Визуализация-данных" data-toc-modified-id="Визуализация-данных-5"><span class="toc-item-num">5&nbsp;&nbsp;</span><font face="liberation serif" size="5">Визуализация данных</font></a></span><ul class="toc-item"><li><span><a href="#Рейтинг-железных-дорог-(как-отправления,-так-и-назначения)-по-объему" data-toc-modified-id="Рейтинг-железных-дорог-(как-отправления,-так-и-назначения)-по-объему-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span><font face="liberation serif" size="4">Рейтинг железных дорог (как отправления, так и назначения) по объему</font></a></span></li><li><span><a href="#Топ-1-железная-дорога-по-отправлению-по-объему-(SQL)" data-toc-modified-id="Топ-1-железная-дорога-по-отправлению-по-объему-(SQL)-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span><font face="liberation serif" size="4">Топ-1 железная дорога по отправлению по объему (SQL)</font></a></span></li><li><span><a href="#Топ-типов-перевозок-по-объему" data-toc-modified-id="Топ-типов-перевозок-по-объему-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span><font face="liberation serif" size="4">Топ типов перевозок по объему</font></a></span></li><li><span><a href="#Топ-типов-перевозок-по-объему-(SQL)" data-toc-modified-id="Топ-типов-перевозок-по-объему-(SQL)-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span><font face="liberation serif" size="4">Топ типов перевозок по объему (SQL)</font></a></span></li><li><span><a href="#Топ-групп-грузов-(1-и-2-уровень)-по-объему" data-toc-modified-id="Топ-групп-грузов-(1-и-2-уровень)-по-объему-5.5"><span class="toc-item-num">5.5&nbsp;&nbsp;</span><font face="liberation serif" size="4">Топ групп грузов (1 и 2 уровень) по объему</font></a></span></li><li><span><a href="#Топ-1-группа-грузов-1-уровня-по-объему-(SQL)" data-toc-modified-id="Топ-1-группа-грузов-1-уровня-по-объему-(SQL)-5.6"><span class="toc-item-num">5.6&nbsp;&nbsp;</span><font face="liberation serif" size="4">Топ-1 группа грузов 1 уровня по объему (SQL)</font></a></span></li><li><span><a href="#Топ-1-группа-грузов-2-уровня-по-объему-(SQL)" data-toc-modified-id="Топ-1-группа-грузов-2-уровня-по-объему-(SQL)-5.7"><span class="toc-item-num">5.7&nbsp;&nbsp;</span><font face="liberation serif" size="4">Топ-1 группа грузов 2 уровня по объему (SQL)</font></a></span></li><li><span><a href="#Дополнительные-визуализации-групп-грузов-уровня-1-по-точке-отправления-и-получения-" data-toc-modified-id="Дополнительные-визуализации-групп-грузов-уровня-1-по-точке-отправления-и-получения--5.8"><span class="toc-item-num">5.8&nbsp;&nbsp;</span><font face="liberation serif" size="4">Дополнительные визуализации групп грузов уровня 1 по точке отправления и получения </font></a></span></li><li><span><a href="#Вывод-по-результатам-визуализации-по-различным-категориям" data-toc-modified-id="Вывод-по-результатам-визуализации-по-различным-категориям-5.9"><span class="toc-item-num">5.9&nbsp;&nbsp;</span>Вывод по результатам визуализации по различным категориям</a></span></li></ul></li><li><span><a href="#Общий-вывод-по-исследованию" data-toc-modified-id="Общий-вывод-по-исследованию-6"><span class="toc-item-num">6&nbsp;&nbsp;</span><font face="liberation serif" size="5">Общий вывод по исследованию</font></a></span></li><li><span><a href="#Дополнительный-материалы-по-модулю-my_func" data-toc-modified-id="Дополнительный-материалы-по-модулю-my_func-7"><span class="toc-item-num">7&nbsp;&nbsp;</span><font face="liberation serif" size="5">Дополнительный материалы по модулю my_func</font></a></span></li></ul></div>

# # <font face='liberation serif' size=5>Описание проекта</font>
# 
# <font face='liberation serif' size=4>*Проект от 123Finance - "Объемные показатели по ЖД". Для исследования используются данные предоставленые заказчиком.*</font>

# ## <font face='liberation serif' size=4>Описание данных.</font>
# 
# <font face='liberation serif' size=4>Данные включают в себя информацию о датах, годах, месяцах, кодах групп груза, дорогах отправления и назначения, виде перевозки и самом объеме.
#     Структура файла 'df_test':
#     
#     - 'Дата',
#     - 'Год',
#     - 'Месяц',
#     - 'Код_группа_груза_ур_2',
#     - 'Код_группа_груза_ур_1',
#     - 'Дорога_отправления',
#     - 'Дорога_назначения',
#     - 'Вид_перевозки',
#     - 'Объём'
# </font>

# ## <font face='liberation serif' size=4>Цели.</font>
# 
# <font face='liberation serif' size=4>
# Обзор данных: Изучение основных характеристик датасета, таких как размер, типы данных и статистические показатели.
# Предобработка данных: Очистка данных от пропусков и аномалий, а также преобразование типов данных при необходимости.
# Базовый анализ: Исследование распределений, зависимостей между переменными и других статистических характеристик.
# Визуализация данных: Построение графиков и диаграмм для наглядного представления информации.
# Выводы: Суммирование основных находок и интерпретация результатов.</font>

# ## <font face='liberation serif' size=4>Декомпозиция задачи.</font>
# 
# <font face='liberation serif' size=4>
# Этап 1: Обзор данных:
#     
#     - Загрузка данных.
#     - Первичный осмотр структуры данных.
# 
# Этап 2: Предобработка данных:
# 
#     - Обработка/исследование пропущенных значений.
#     - Преобразование типов данных.
#     - обогащение данных информацией из файла sp_gr_test.xlsx
#     
# Этап 3: Базовый анализ данных (согласно ТЗ):
#     
#     - за какой период имеются данные;
#     - сколько и какие именно железные дороги приведены в таблице;
#     - сколько и какие именно есть группы груза в таблице;
#     - максимальный и минимальный объем
# 
# Этап 4: Визуализация данных:
#     
#     - Построение гистограмм. 
#     - Построение графиков.
# 
# 
# Этап 6: Выводы:
#     
#     - Суммирование основных находок.
#     
#     
#     
# Все этапы будут выполнены в среде Jupyter Notebook с использованием языка программирования Python. SQL запросы будут выполнены средствами Python.
# 
# </font>

# # <font face='liberation serif' size=5>Общая подготовка
# <font face='liberation serif' size=4>Установка библиотек</font>

# In[1]:


#!pip install tabulate
#plt.close('all')
#!pip install pandas_profiling
#!pip install gdown


# <font face='liberation serif' size=4>Обновление библиотек</font>

# In[2]:


#!pip install -qU pandas seaborn
#!pip install -qU pandas
#!pip install -qU seaborn


# <font face='liberation serif' size=4>Загрузка библиотек</font>

# In[3]:


import pandas as pd
import numpy as np
import re
### модуль используется мной локально, для его использования ниже будет ссылка на модуль и описание процесса установки
### прим. в проекте использовал свои стандартные функции предъобработки и исследования, модуль ускоряет процесс работы
import my_func as mf 
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib import colors
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
from tabulate import tabulate
import gdown
import sqlite3
import gc ### файл большой, может потребоваться свалка


# # <font face='liberation serif' size=5>Mодуль my_func</font>
#     
# Сам модуль и инструкцию по установке фукнции можно найти по [ссылке](https://github.com/OophionN/PySQLPlayground-pet-projects-/tree/main/my_func)
# 
# или использовать сами функции непосредственно в блокноте
# 
# 
# [Переход](#Перейти_к_функциям)
# 

# <font face='liberation serif' size=4>Загрузка датасета</font>

# In[4]:


try:
    df = pd.read_pickle("C:\\Users\\PC_Maks\\Desktop\\123finance\\df_test.uu")
    
except:
    url = 'https://drive.google.com/uc?id=1TUAeOnxdSr4E07xfg_AjbujnfufC5Tdx'
    file_path = 'df_test_downlowd_gd.csv'
    gdown.download(url, file_path)
    df = pd.read_pickle(file_path)


# In[5]:


df.sample (10)


# In[6]:


##вывод первых и последних 10 строк датасета 

display (df.head (10))
display (df.tail (10))


# In[7]:


df.info()


# In[8]:


help (mf)


# In[9]:


mf.data_preprocessing(df)


# In[10]:


mf.check (df, drop_dupl=False) ## пока проверим без удаления


# Всего 100 дубликатов, объемом менее 0,1% от датасета, пропуски имеются в столбцах дата и год. Дубли пока оставим как есть, пропуски посмотрим внимательнее.

# In[11]:


rows_with_na = df[df.isna().any(axis=1)]
rows_with_na.sample(10)


# В столбце дата зашифрованы год и месяц, можно конечно сплитом заменить пропуски, пропусков менее 0,05%, , в соответствии с ТЗ заполним пропуски, самый простой способ через сплит даты

# In[12]:


df[['year_str', 'month_str']] = df['date'].str.split('/', expand=True)

df['year'].fillna(df['year_str'].astype(float), inplace=True)
df['month'].fillna(df['month_str'].astype(float), inplace=True)

df.drop(columns=['year_str', 'month_str'], inplace=True)


# In[13]:


mf.check_unique (df)


# Странный пункт назначения и получаения - #, посмотрим сколько таких записей

# In[14]:


filtered_df = df[
    df['дорога_отправления'].str.contains('#', na=False) | 
    df['дорога_назначения'].str.contains('#', na=False)
]
filtered_df


# 111 строк- не так много, удаляем 

# In[15]:


df.drop(
    df[
        df['дорога_отправления'].str.contains('#', na=False) | 
        df['дорога_назначения'].str.contains('#', na=False)
    ].index, inplace=True
)


# Явно нужно скорректировать форматы данных. займемся на следующих шагах

# ## <font face='liberation serif' size=4>Выполним загрузку и вывод информации через запрос SQL</font>

# In[16]:


### Создадим подключение к датасету 

conn = sqlite3.connect("test_db.sqlite")
df.to_sql("railroad_data", conn, if_exists="replace")


# In[17]:


# Формируем SQL-запрос
query = '''
SELECT *
FROM railroad_data
'''

result_df_sql = pd.read_sql_query(query, conn)

### закрывать пока не будем, так как еще будем к нему обращаться 
#conn.close()

print(result_df_sql.head())


# In[18]:


# SQL-запрос для первых 10 строк достаточно обычного LIMIT
query_first_10 = '''
SELECT *
FROM railroad_data
LIMIT 10
'''
### Для последних 10 строк, возьмем общее количество строк и от них отталкнемся 
total_rows = pd.read_sql_query("SELECT COUNT(*) FROM railroad_data", conn).iloc[0,0]
query_last_10 = f'''
SELECT *
FROM railroad_data
LIMIT 10 OFFSET {total_rows - 10}
'''


result_first_10 = pd.read_sql_query(query_first_10, conn)
result_last_10 = pd.read_sql_query(query_last_10, conn)


display("Первые 10 строк:")
display(result_first_10)
display ()
display("Последние 10 строк:")
display(result_last_10)


# ## <font face='liberation serif' size=4>Корректировка типов данных </font>

# Перед обогащением, с учетом объема исходного датасета и ограниченного объема памяти, скорректируем типы данных в датасетах

# In[19]:


df = df.astype({
    'year': 'Int32',
    'month': 'Int32',
    'код_группа_груза_ур_2': 'Int32',
    'код_группа_груза_ур_1': 'Int32',
    'v': 'Int32'
})


# скорректируем названия для удобства обработки

# In[20]:


old_cols=df.columns.tolist()
new_cols = ['date',
 'year',
 'month',
 'code_cargo_2',
 'code_cargo_1',
 'departure_road',
 'destination_road',
 'type_trans',
 'volume'
]

cols_change_dict = {i: v for i, v in zip (old_cols, new_cols)}
df.rename(columns=cols_change_dict, inplace=True)


# In[21]:


df.info ()


# ## <font face='liberation serif' size=4>Обогащение данных информацией из файла sp_gr_test.xlsx</font>

# Загрузим справочник

# In[22]:


try:
    sp_gr_test_df = pd.read_excel("C:\\Users\\PC_Maks\\Desktop\\123finance\\sp_gr_test.xlsx")
except:
    url = 'https://drive.google.com/uc?id=1gQPiJ0HQHgP7r_zbKm3M3kGY9WZD71I2'
    output = 'sp_gr_test_downloaded.xlsx'
    gdown.download(url, output, quiet=False)

    sp_gr_test_df = pd.read_excel(output)


# In[23]:


display(sp_gr_test_df.sample(10))


# Так как уровень детализации основного датасета только до уровня 2, произведем обогащение только до данного уровня.

# In[24]:


## ограним таблицу-справочник
selected_columns = ['Код_группа_груза_ур_1', 'Группа_груза_ур_1', 'Код_группа_груза_ур_2', 'Группа_груза_ур_2']
sp_gr_test_df_selected = sp_gr_test_df[selected_columns]


# In[25]:


mf.data_preprocessing (sp_gr_test_df_selected)


# скорректируем названия

# In[26]:


old_cols=sp_gr_test_df_selected.columns.tolist()
new_cols = ['code_cargo_1',
 'group_cargo_1',
 'code_cargo_2',
 'group_cargo_2'
]

cols_change_dict = {i: v for i, v in zip (old_cols, new_cols)}
sp_gr_test_df_selected.rename(columns=cols_change_dict, inplace=True)


# In[27]:


sp_gr_test_df_selected = sp_gr_test_df_selected.astype({
    'code_cargo_1': 'Int32',
    'code_cargo_2': 'Int32'    
})


# In[28]:


### так как работаем со справочником, уберем лишнее
mf.check(sp_gr_test_df_selected)


# In[29]:


sp_gr_test_df_selected.info()


# In[30]:


df = pd.merge(df, sp_gr_test_df_selected, on=['code_cargo_2', 'code_cargo_1'], how='left')


# In[31]:


df.info()


# Таблицы объедленили. можем перейти к оценки дублей, пропусков и чистке. 

# In[32]:


mf.check(df, drop_dupl=False)


# Учитывая не значительное количество дубликатов - удаляем их

# In[33]:


mf.check(df, drop_dupl=True)


# # <font face='liberation serif' size=5>Базовый анализ данных (согласно ТЗ)</font>

# Предварительную обработку и объединение мы закончили, удалили дубли, пропуски, собрали одну таблицу, пора ответить на вопросы.
# 
#     - за какой период имеются данные;
#     - сколько и какие именно железные дороги приведены в таблице;
#     - сколько и какие именно есть группы груза в таблице;
#     - максимальный и минимальный объем

# ## <font face='liberation serif' size=4>Период за который имеются данные.</font>

# In[34]:


### Чтобы опять не собирать новый столбце с годами и месяцами (таблица массивная, памяти требуется много)
### сгруппируем по мин и макс, и посмотрим на даты

grouped_by_year = df.groupby('year')['month'].agg(['min', 'max'])


min_year = grouped_by_year.index.min()
max_year = grouped_by_year.index.max()

min_month_for_min_year = grouped_by_year.loc[min_year, 'min']
max_month_for_max_year = grouped_by_year.loc[max_year, 'max']

print(f"Данные имеются за период с {min_month_for_min_year} месяца {min_year} года по {max_month_for_max_year} месяц {max_year} года.")


# Данные за период с января 2009 года по март 2023 года. Идем дальше

# ## <font face='liberation serif' size=4>Сколько и какие именно железные дороги приведены в таблице</font>

# Эти и остальные значения мы в приницпе выводили модульной функцией check_unique, но выведем нужные значения в явном виде

# In[35]:


unique_roads = df['departure_road'].unique()
num_unique_roads = len(unique_roads)
print(f"В таблице приведены данные по {num_unique_roads} железным дорогам - пунктам отправления: {unique_roads}")


# In[36]:


unique_roads = df['destination_road'].unique()
num_unique_roads = len(unique_roads)
print(f"В таблице приведены данные по {num_unique_roads} железным дорогам - пунктам получения: {unique_roads}")


# ## <font face='liberation serif' size=4>Сколько и какие именно есть группы груза в таблице</font>

# In[37]:


unique_cargo_groups = df['group_cargo_1'].unique()
num_unique_cargo_groups = len(unique_cargo_groups)
print(f"В таблице приведены данные по {num_unique_cargo_groups} группам груза: {unique_cargo_groups}")


# ## <font face='liberation serif' size=4>Максимальный и минимальный объем</font>

# In[38]:


max_volume = df['volume'].max()
min_volume = df['volume'].min()
print(f"Максимальный объем: {max_volume}, минимальный объем: {min_volume}")


# ## <font face='liberation serif' size=4>Выведение дополнительной информации</font>
# Для вывдения информации одной компандой - info (), для выведения списка колонок columns

# In[39]:


df.info()


# In[40]:


df.columns


# ## <font face='liberation serif' size=4>Возвращение колонок заявленному виду</font>

# In[41]:


old_cols=df.columns.tolist()
new_cols = ['Дата',
            'Год',
            'Месяц',
            'Код_группа_груза_ур_2',
            'Код_группа_груза_ур_1',
            'Дорога_отправления',
            'Дорога_назначения',
            'Вид_перевозки',
            'Объём',
            'Группа_грузов_ур_1',
            'Группа_грузов_ур_2'
]

cols_change_dict = {i: v for i, v in zip (old_cols, new_cols)}
df.rename(columns=cols_change_dict, inplace=True)


# In[42]:


### проведем контрольную проверку на пропуски и дубли

mf.check (df)


# Все хорошо. 

# ## <font face='liberation serif' size=4>Общий вывод по подготовке, прдварительной обработке и базовому исследованию по ТЗ</font>

# <font face='liberation serif' size=4>По результатм первичного исследования датасета установлено:</font>
#     
# 
# <font face='liberation serif' size=4>
# 
# - **Полные дубликаты:** 100 строк (менее 0.1%). **Действие:** Удалены.
#   
# - **Пропуски в столбце "year":** 35 (менее 0.02%). **Действие:** Заменены на основе данных из столбца 'date'.
#   
# - **Пропуски в столбце "month":** 39 (менее 0.02%). **Действие:** Заменены на основе данных из столбца 'date'.
#   
# - **Символ "#" в столбцах отправления и прибытия:** 111 значений. **Действие:** Удалены.
#   
# - **Некорректные названия столбцов:** Разный тип раскладки, прописные и строчные буквы. **Действие:** Корректировка.
#   
# - **Несоответствие типов данных:** Заменены типы данных для полей "year" и "month" с float на int32.
#   
# - **Объединение со справочником:** Проведено после исключения дублей из последнего.
#   
# - **Период данных:** с января 2009 по март 2023 года.
#   
# - **Железные дороги:** Данные по 20 пунктам отправления и 19 пунктам получения.
#   
# - **Максимальный и минимальный объем:** 6040944 и 0 соответственно.
#   
# - **Группы груза:** 11 различных групп.
#   
# </font>
# 
# **Датасет готов к этапу визуализации и тонкого исследования.**
# 
# 

# # <font face='liberation serif' size=5>Визуализация данных</font>

# ## <font face='liberation serif' size=4>Рейтинг железных дорог (как отправления, так и назначения) по объему</font>

# In[43]:


### Вывод аналогичного графика несколько раз - значит сделаем функцию 

def plot_top_from_column(df, column_name):
    grouped_df = df.groupby(column_name)['Объём'].sum().reset_index()
    sorted_df = grouped_df.sort_values(by='Объём', ascending=False).head()
    plt.figure(figsize=(15, 6))
    barplot = sns.barplot(x=column_name, y='Объём', data=sorted_df, palette='viridis')
    
    plt.title(f'Топ по столбцу {column_name} по объему', fontsize=16)
    plt.xlabel(column_name, fontsize=14)
    plt.ylabel('Объём', fontsize=14)
    
    for p in barplot.patches:
        barplot.annotate(f'{int(p.get_height())}', 
                         (p.get_x() + p.get_width() / 2., p.get_height()), 
                         ha='center', va='center', fontsize=12, color='black', xytext=(0, 5), 
                         textcoords='offset points')
    
    plt.show()


# In[44]:


plot_top_from_column(df, 'Дорога_отправления')


# In[45]:


plot_top_from_column(df, 'Дорога_назначения')


# ## <font face='liberation serif' size=4>Топ-1 железная дорога по отправлению по объему (SQL)</font>

# In[46]:


#данную операцию (вывод топа) делать нужно несколько раз, напишем функцию, так проще
def get_leader_from_column(column_name):
    conn = sqlite3.connect("test_db.sqlite")
    
    query = f'''
    SELECT {column_name}, SUM(Объём) AS total_volume
    FROM new_railroad_data
    GROUP BY {column_name}
    ORDER BY total_volume DESC
    LIMIT 1;
    '''
    
    result_df = pd.read_sql_query(query, conn)
    conn.close()
    
    return result_df


# In[47]:


get_leader_from_column('Дорога_отправления')


# ## <font face='liberation serif' size=4>Топ типов перевозок по объему</font>

# In[48]:


plot_top_from_column(df, 'Вид_перевозки')


# ## <font face='liberation serif' size=4>Топ типов перевозок по объему (SQL)</font>

# In[49]:


get_leader_from_column('Вид_перевозки')


# ## <font face='liberation serif' size=4>Топ групп грузов (1 и 2 уровень) по объему</font>

# In[50]:


plot_top_from_column(df, 'Группа_грузов_ур_1')


# In[51]:


plot_top_from_column(df, 'Группа_грузов_ур_2')


# ## <font face='liberation serif' size=4>Топ-1 группа грузов 1 уровня по объему (SQL)</font>

# In[52]:


get_leader_from_column('Группа_грузов_ур_1')


# ## <font face='liberation serif' size=4>Топ-1 группа грузов 2 уровня по объему (SQL)</font>

# In[53]:


get_leader_from_column('Группа_грузов_ур_2')


# ## <font face='liberation serif' size=4>Дополнительные визуализации групп грузов уровня 1 по точке отправления и получения </font>

# In[54]:


top_departure_roads = df.groupby('Дорога_отправления')['Объём'].sum().sort_values(ascending=False).index[:1]

plt.figure(figsize=(15, 6))
ax = sns.barplot(data=df[df['Дорога_отправления'].isin(top_departure_roads)],                 x='Дорога_отправления', y='Объём', hue='Группа_грузов_ур_1', palette="tab20")
plt.title('Распределение групп грузов внутри лидера по отправке')
plt.xlabel('Дорога отправления')
plt.ylabel('Объём')


for p in ax.patches:
    ax.annotate(f"{p.get_height():.0f}",
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='baseline',
                xytext=(0, 10),
                textcoords='offset points')

plt.show()


# In[55]:


top_destination_roads = df.groupby('Дорога_назначения')['Объём'].sum().sort_values(ascending=False).index[:1]


plt.figure(figsize=(15, 6))
ax = sns.barplot(data=df[df['Дорога_назначения'].isin(top_destination_roads)],            x='Дорога_назначения', y='Объём', hue='Группа_грузов_ур_1', palette="tab20")
plt.title('Распределение групп грузов внутри лидера по назначению')
plt.xlabel('Дорога назначения')
plt.ylabel('Объём')

for p in ax.patches:
    ax.annotate(f"{p.get_height():.0f}",
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='baseline',
                xytext=(0, 10),
                textcoords='offset points')

plt.show()


# <h2>Вывод по результатам визуализации по различным категориям</h2>
# 
# <font face='liberation serif' size=4>Дорога отправления</font>
# <ul>
#     <li><strong>ЗСБ (Западно-Сибирская дорога)</strong> является лидером по объему отправления с показателем 4,185,282,960.</li>
#     <li><strong>СВР (Северо-Восточная дорога)</strong> занимает второе место с объемом 1,930,358,951.</li>
#     <li>Далее следуют <strong>ЮУР (Южно-Уральская дорога)</strong>, <strong>ОКТ (Октябрьская дорога)</strong> и <strong>ЮВС (Южно-Восточная дорога)</strong>.</li>
# </ul>
# 
# <font face='liberation serif' size=4>Дорога назначения</font>
# <ul>
#     <li><strong>ОКТ (Октябрьская дорога)</strong> занимает первое место по объему назначения с 3,156,406,995.</li>
#     <li><strong>СКВ (Северо-Кавказская дорога)</strong> и <strong>ДВС (Дальневосточная дорога)</strong> также имеют высокие показатели.</li>
# </ul>
# 
# <font face='liberation serif' size=4>Вид перевозки</font>
# <ul>
#     <li>Внутренние перевозки доминируют с объемом 11,654,023,133, что значительно превышает другие виды перевозок.</li>
#     <li>Экспорт занимает второе место с 6,190,685,416, а импорт и транзит имеют значительно меньший объем.</li>
# </ul>
# 
# <font face='liberation serif' size=4>Группа грузов 1 уровня</font>
# <ul>
#     <li><strong>Каменный уголь</strong> является самым перевозимым товаром с объемом 5,209,012,097.</li>
#     <li><strong>Нефтяные грузы</strong> и <strong>минерально-строительные материалы</strong> также занимают верхние строчки в рейтинге.</li>
# </ul>
# 
# <font face='liberation serif' size=4>Группа грузов 1 уровня</font>
# <ul>
#     <li><strong>Каменный уголь</strong> и <strong>нефть и нефтепродукты</strong> занимают первые два места.</li>
#     <li><strong>Строительные грузы</strong>, <strong>руда железная и марганцевая</strong>, и <strong>черные металлы</strong> также входят в топ-5.</li>
# </ul>
# 

# # <font face='liberation serif' size=5>Общий вывод по исследованию</font>
# 
# <font face='liberation serif' size=4>По итогам комплексного исследования датасета по объемам перевозок железнодорожного транспорта можно сделать следующие ключевые выводы:</font>
# 
# 1. Этап предобработки и первого исследования
# <font face='liberation serif' size=4>Предобработка данных включала в себя удаление дубликатов, заполнение пропусков, корректировку названий столбцов и типов данных. По окончании этапа, датасет был готов для визуализации и тонкого исследования. Проанализированы данные по 20 пунктам отправления и 19 пунктам получения с января 2009 по март 2023 года. Определены 11 различных групп грузов.</font>
# 
# 2. Этап визуализации и исследования по различным категориям
# Дорога отправления
# <font face='liberation serif' size=4>Лидером по объему отправления является <strong>ЗСБ (Западно-Сибирская дорога)</strong> с показателем 4,185,282,960. <strong>СВР (Северо-Восточная дорога)</strong> занимает второе место с объемом 1,930,358,951.</font>
# 
# Дорога назначения
# <font face='liberation serif' size=4><strong>ОКТ (Октябрьская дорога)</strong> лидирует по объему назначения с 3,156,406,995.</font>
# 
# Вид перевозки
# <font face='liberation serif' size=4>Внутренние перевозки доминируют с объемом 11,654,023,133, что значительно превышает другие виды перевозок.</font>
# 
# Группа грузов 1 уровня
# <font face='liberation serif' size=4><strong>Каменный уголь</strong> является самым перевозимым товаром с объемом 5,209,012,097. Далее следуют <strong>нефтяные грузы</strong> и <strong>минерально-строительные материалы</strong>.</font>
# 
# <font face='liberation serif' size=4>Все вышеуказанные выводы формируют общую картину и позволяют сделать интегрированные выводы для стратегического и тактического планирования в сфере железнодорожных перевозок. Данный анализ является полезным инструментом для принятия управленческих решений.</font>

# # <font face='liberation serif' size=5>Дополнительный материалы по модулю my_func</font>
# 
# <a id="Перейти_к_функциям"></a>
# 
# <font face='liberation serif' size=4>Чтобы не устанавливать модуль в переменную среду на локальный ПК, можно использовать код функций напрямую (нужно скопировать код в ячейку после загрузки датасета.</font>
# 

# In[56]:


def data_preprocessing(data):
    """
    Производит предварительную обработку данных, модифицируя заголовки столбцов и строковые значения.

    Параметры:
    - data (DataFrame): исходный DataFrame, который требуется предобработать.

    Основные шаги функции:
    1. Преобразует заголовки столбцов к нижнему регистру и заменяет пробелы на нижние подчеркивания.
    2. Преобразует строковые значения всех столбцов к нижнему регистру.

    Возвращает:
    - DataFrame: предобработанный DataFrame с модифицированными заголовками столбцов и строковыми значениями.

    Пример:
    >>> data = pd.DataFrame({"First Name": ["John", "JANE"], "Last Name": ["DOE", "SMITH"]})
    >>> data_preprocessing(data)
       first_name last_name
    0       john       doe
    1       jane     smith
    """

    data.columns = data.columns.str.lower().str.replace(' ', '_')
    data = data.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

    return data
    
    
    


# In[57]:


def check_unique(data):
    """
    Выводит уникальные значения и их количество для строковых столбцов, 
    диапазон значений для числовых и даты/времени столбцов, а также уникальные значения 
    для числовых столбцов, где уникальных значений не более 10.

    Параметры:
    - data (DataFrame): DataFrame, значения которого необходимо проверить.

    Возвращает:
    - None: Функция выводит информацию напрямую в ячейку выполнения кода.

        """
    for col in data.select_dtypes(include=['object']):
        print(f"Уникальные значения в столбце {col}:")
        print(data[col].unique())
        print(f"Количество уникальных значений: {data[col].nunique()}")
        print('---------------------')

    for col in data.select_dtypes(include=['datetime64', 'float64', 'int64']):
        print(f"Диапазон значений в столбце {col}:")
        print(f"Минимальное значение: {data[col].min()}")
        print(f"Максимальное значение: {data[col].max()}")
        print('---------------------')

    for col in data.select_dtypes(include=['int64', 'float64']):
        if len(data[col].unique()) > 10:
            print(f"В столбце {col} более 10 уникальных значений")
        else:
            print(f"Уникальные значения в столбце {col}:")
            print(data[col].unique())
        print(f"Количество уникальных значений: {data[col].nunique()}")
        print('---------------------')
        


# In[58]:


def check(data, drop_dupl=True):
    """
    Проверяет DataFrame на наличие дубликатов и пропусков и выводит соответствующую информацию.
    При обнаружении дубликатов имеется возможность их удалить.

    Параметры:
    - data (DataFrame): DataFrame, который необходимо проверить.
    - drop_dupl (bool, по умолчанию True): Если True, дубликаты будут удалены из DataFrame.

    Возвращает:
    - None: Функция выводит информацию напрямую в консоль. 
            Если были обнаружены дубликаты и параметр drop_dupl установлен в True, то из исходного DataFrame дубликаты будут удалены.
            Если дубликаты найдены, но drop_dupl установлен в False, то дубликаты не удаляются.

    """
    if drop_dupl:
        try:
            display('Проверка на дубликаты:')
            duplicates = data.duplicated()
            duplicate_rows = data.loc[duplicates]
            display(duplicate_rows.info())
            display(duplicate_rows)
            display('----------------------')
            display('Пропуски:')
            display(data.isna().sum())
            display('Пропуски в процентном отношении к всему датасету:')
            display(data.isna().sum() / len(data) * 100)

            num_rows_before = len(data)
            data.drop_duplicates(inplace=True)
            num_rows_after = len(data)
            num_rows_deleted = num_rows_before - num_rows_after
            percent_deleted = round(num_rows_deleted / num_rows_before * 100, 2)
            display(f'Удалено дубликатов: {num_rows_deleted} строк ({percent_deleted}% от всего датасета)')
        
        except Exception as e:
            print(f'ERROR: {e}')
    else:
        try:
            display('Проверка на дубликаты:')
            duplicates = data.duplicated()
            duplicate_rows = data.loc[duplicates]
            display(duplicate_rows.info())
            display(duplicate_rows.sample())
            display('----------------------')
            display('Пропуски:')
            display(data.isna().sum())
            display('Пропуски в процентном отношении к всему датасету:')
            display(data.isna().sum() / len(data) * 100)
        
        except Exception as e:
            print(f'ERROR: {e}')

