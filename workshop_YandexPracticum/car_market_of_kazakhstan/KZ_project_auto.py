#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Описание-проекта" data-toc-modified-id="Описание-проекта-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Описание проекта</a></span><ul class="toc-item"><li><span><a href="#Описание-данных." data-toc-modified-id="Описание-данных.-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Описание данных.</a></span></li><li><span><a href="#Описание-задачи" data-toc-modified-id="Описание-задачи-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Описание задачи</a></span></li></ul></li><li><span><a href="#Общая-подготовка" data-toc-modified-id="Общая-подготовка-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Общая подготовка</a></span><ul class="toc-item"><li><span><a href="#Используем-стандартные-проверки,-с-использованием-шаблонных-функций-(заготовки-прошлых-периодов)" data-toc-modified-id="Используем-стандартные-проверки,-с-использованием-шаблонных-функций-(заготовки-прошлых-периодов)-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Используем стандартные проверки, с использованием шаблонных функций (заготовки прошлых периодов)</a></span><ul class="toc-item"><li><span><a href="#Изучим-наполнение-датасета" data-toc-modified-id="Изучим-наполнение-датасета-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Изучим наполнение датасета</a></span></li><li><span><a href="#Провека-на-очевидные-дубликаты-и-пропуски" data-toc-modified-id="Провека-на-очевидные-дубликаты-и-пропуски-2.1.2"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Провека на очевидные дубликаты и пропуски</a></span></li></ul></li><li><span><a href="#Обработка-пропусков" data-toc-modified-id="Обработка-пропусков-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Обработка пропусков</a></span><ul class="toc-item"><li><span><a href="#Объем-двигателя." data-toc-modified-id="Объем-двигателя.-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Объем двигателя.</a></span></li><li><span><a href="#Год-выпуска." data-toc-modified-id="Год-выпуска.-2.2.2"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span>Год выпуска.</a></span></li><li><span><a href="#Тип-топлива" data-toc-modified-id="Тип-топлива-2.2.3"><span class="toc-item-num">2.2.3&nbsp;&nbsp;</span>Тип топлива</a></span></li><li><span><a href="#Коробка-передач" data-toc-modified-id="Коробка-передач-2.2.4"><span class="toc-item-num">2.2.4&nbsp;&nbsp;</span>Коробка передач</a></span></li><li><span><a href="#Тип-привода" data-toc-modified-id="Тип-привода-2.2.5"><span class="toc-item-num">2.2.5&nbsp;&nbsp;</span>Тип привода</a></span></li><li><span><a href="#Итоги-чистки" data-toc-modified-id="Итоги-чистки-2.2.6"><span class="toc-item-num">2.2.6&nbsp;&nbsp;</span>Итоги чистки</a></span></li></ul></li><li><span><a href="#Обработка-типов" data-toc-modified-id="Обработка-типов-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Обработка типов</a></span><ul class="toc-item"><li><span><a href="#Кодировка-стран" data-toc-modified-id="Кодировка-стран-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Кодировка стран</a></span></li></ul></li><li><span><a href="#Анализ-данных" data-toc-modified-id="Анализ-данных-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Анализ данных</a></span><ul class="toc-item"><li><span><a href="#Визуализация-даных-для-исследования" data-toc-modified-id="Визуализация-даных-для-исследования-2.4.1"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>Визуализация даных для исследования</a></span></li><li><span><a href="#Топ-продаж-по-медиативной-цене-и-количество-проданных-авто" data-toc-modified-id="Топ-продаж-по-медиативной-цене-и-количество-проданных-авто-2.4.2"><span class="toc-item-num">2.4.2&nbsp;&nbsp;</span>Топ продаж по медиативной цене и количество проданных авто</a></span><ul class="toc-item"><li><span><a href="#Срез-для-выявления-покупок-для-частных-целей,-и-визуализация-результатов" data-toc-modified-id="Срез-для-выявления-покупок-для-частных-целей,-и-визуализация-результатов-2.4.2.1"><span class="toc-item-num">2.4.2.1&nbsp;&nbsp;</span>Срез для выявления покупок для частных целей, и визуализация результатов</a></span></li><li><span><a href="#Топ-10-бренды-по-количеству-приобретенных-авто" data-toc-modified-id="Топ-10-бренды-по-количеству-приобретенных-авто-2.4.2.2"><span class="toc-item-num">2.4.2.2&nbsp;&nbsp;</span>Топ-10 бренды по количеству приобретенных авто</a></span></li></ul></li><li><span><a href="#Динамика-продаж-по-рынку,-в-штуках-и-в-денежном-выражении." data-toc-modified-id="Динамика-продаж-по-рынку,-в-штуках-и-в-денежном-выражении.-2.4.3"><span class="toc-item-num">2.4.3&nbsp;&nbsp;</span>Динамика продаж по рынку, в штуках и в денежном выражении.</a></span></li><li><span><a href="#Посмотрим-детальнее-на-динамику,-по-типам:-брендов,-топлива,-приводу,-классу,-региону,-автоцентру-и-сегменту" data-toc-modified-id="Посмотрим-детальнее-на-динамику,-по-типам:-брендов,-топлива,-приводу,-классу,-региону,-автоцентру-и-сегменту-2.4.4"><span class="toc-item-num">2.4.4&nbsp;&nbsp;</span>Посмотрим детальнее на динамику, по типам: брендов, топлива, приводу, классу, региону, автоцентру и сегменту</a></span><ul class="toc-item"><li><span><a href="#Бренд" data-toc-modified-id="Бренд-2.4.4.1"><span class="toc-item-num">2.4.4.1&nbsp;&nbsp;</span>Бренд</a></span></li><li><span><a href="#Автоцентр" data-toc-modified-id="Автоцентр-2.4.4.2"><span class="toc-item-num">2.4.4.2&nbsp;&nbsp;</span>Автоцентр</a></span></li><li><span><a href="#Регион" data-toc-modified-id="Регион-2.4.4.3"><span class="toc-item-num">2.4.4.3&nbsp;&nbsp;</span>Регион</a></span></li><li><span><a href="#Тип-топлива" data-toc-modified-id="Тип-топлива-2.4.4.4"><span class="toc-item-num">2.4.4.4&nbsp;&nbsp;</span>Тип топлива</a></span></li><li><span><a href="#Класс" data-toc-modified-id="Класс-2.4.4.5"><span class="toc-item-num">2.4.4.5&nbsp;&nbsp;</span>Класс</a></span></li><li><span><a href="#Привод" data-toc-modified-id="Привод-2.4.4.6"><span class="toc-item-num">2.4.4.6&nbsp;&nbsp;</span>Привод</a></span></li><li><span><a href="#Сегмент" data-toc-modified-id="Сегмент-2.4.4.7"><span class="toc-item-num">2.4.4.7&nbsp;&nbsp;</span>Сегмент</a></span></li></ul></li><li><span><a href="#Исследование-средних-показателей-по-брендам-и-маркам" data-toc-modified-id="Исследование-средних-показателей-по-брендам-и-маркам-2.4.5"><span class="toc-item-num">2.4.5&nbsp;&nbsp;</span>Исследование средних показателей по брендам и маркам</a></span></li><li><span><a href="#Емкость-рынка" data-toc-modified-id="Емкость-рынка-2.4.6"><span class="toc-item-num">2.4.6&nbsp;&nbsp;</span>Емкость рынка</a></span></li><li><span><a href="#Оценим-долю-рынка-на-примере-компании-mercur-auto" data-toc-modified-id="Оценим-долю-рынка-на-примере-компании-mercur-auto-2.4.7"><span class="toc-item-num">2.4.7&nbsp;&nbsp;</span>Оценим долю рынка на примере компании mercur auto</a></span><ul class="toc-item"><li><span><a href="#Расчет-общей-доли-на-рынке-у-mercur-auto-(количественном-и-стоимостном-выражении)" data-toc-modified-id="Расчет-общей-доли-на-рынке-у-mercur-auto-(количественном-и-стоимостном-выражении)-2.4.7.1"><span class="toc-item-num">2.4.7.1&nbsp;&nbsp;</span>Расчет общей доли на рынке у mercur auto (количественном и стоимостном выражении)</a></span></li><li><span><a href="#Hасчета-доли-рынка-mercur-auto-по-маркам" data-toc-modified-id="Hасчета-доли-рынка-mercur-auto-по-маркам-2.4.7.2"><span class="toc-item-num">2.4.7.2&nbsp;&nbsp;</span>Hасчета доли рынка mercur auto по маркам</a></span></li><li><span><a href="#Рассчитаем-долю-рынка-mercur-auto-по-классам" data-toc-modified-id="Рассчитаем-долю-рынка-mercur-auto-по-классам-2.4.7.3"><span class="toc-item-num">2.4.7.3&nbsp;&nbsp;</span>Рассчитаем долю рынка mercur auto по классам</a></span></li><li><span><a href="#Общие-вывод-по-mercur-auto" data-toc-modified-id="Общие-вывод-по-mercur-auto-2.4.7.4"><span class="toc-item-num">2.4.7.4&nbsp;&nbsp;</span>Общие вывод по mercur auto</a></span></li></ul></li><li><span><a href="#Рассчет-для-mercur-auto-в-части-конкурентов" data-toc-modified-id="Рассчет-для-mercur-auto-в-части-конкурентов-2.4.8"><span class="toc-item-num">2.4.8&nbsp;&nbsp;</span>Рассчет для mercur auto в части конкурентов</a></span><ul class="toc-item"><li><span><a href="#Определение-ближайших-конкурентов-для-&quot;mercur-auto&quot;:" data-toc-modified-id="Определение-ближайших-конкурентов-для-&quot;mercur-auto&quot;:-2.4.8.1"><span class="toc-item-num">2.4.8.1&nbsp;&nbsp;</span>Определение ближайших конкурентов для "mercur auto":</a></span></li><li><span><a href="#Распределение-продаж-по-месяцам-или-годам-для-'mercur-auto'-и-их-основных-конкурентов" data-toc-modified-id="Распределение-продаж-по-месяцам-или-годам-для-'mercur-auto'-и-их-основных-конкурентов-2.4.8.2"><span class="toc-item-num">2.4.8.2&nbsp;&nbsp;</span>Распределение продаж по месяцам или годам для 'mercur auto' и их основных конкурентов</a></span></li><li><span><a href="#Распределение-продаж-по-регионам,-брендам-и-классам" data-toc-modified-id="Распределение-продаж-по-регионам,-брендам-и-классам-2.4.8.3"><span class="toc-item-num">2.4.8.3&nbsp;&nbsp;</span>Распределение продаж по регионам, брендам и классам</a></span></li></ul></li></ul></li><li><span><a href="#Итоговые-выводы" data-toc-modified-id="Итоговые-выводы-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Итоговые выводы</a></span></li></ul></li></ul></div>

# # Описание проекта
# 
# * Проект от Мастерской Яндекс - "Исследование авторынка Казахстана". Для исследования используются данные за 2019 год.*

# ## Описание данных.
# 
# Датасет с данными по продажам автомобилей в Казахстане за 2019 год. Данные получены из
# официальной статистики VAG, после перевода из эксель в csv обнаружились множественные
# проблемы с исходными данными: некорректные разделители десятичных разрядов, несоответствие
# данных типу данных. Дополнительной проблемой является то, что статистику собирал не один
# человек, поэтому есть неявные дубликаты - например, 4WD, 4 WD и 4-WD, а также одни и те же
# признаки могут быть записаны как на русском, так и на английском языке. Также необходимо
# очистить датасет от лишних столбцов, которые используют технические специалисты, но которые не
# нужны в управленческом учете.
# 
# 
#     - Год – год продажи (2019)
#     - Месяц – месяц продажи (январь - сентябрь)
#     - Компания – название автоцентра
#     - Бренд – название продаваемой марки автомобиля
#     - Модель – название модели автомобиля
#     - Модификация – модификация модели автомобиля (удаляем)
#     - Год выпуска – год производства автомобиля
#     - Страна-производитель – страна, где произведен автомобиль
#     - Вид топлива – бензин, дизель, электричество, гибрид
#     - Объём двиг л – объем двигателя автомобиля в литрах
#     - Коробка передач – тип коробки переключения передач (оставляем два варианта: автоматическая, механическая, то есть все что не механика ставим автомат, на DSG, S-Tronic и прочее делить не надо, равно как и количество передач)
#     - Тип привода – в итоге оставляем RWD – задний привод, FWD – передний привод, 4WD – полный привод, 2WD – все остальное (подключаемый полный привод и где нет четкого указания передний или задний это привод)
#     - Сегмент – сегмент, к которому относится авто (удаляем)
#     - Регион – регион продажи
#     - Наименование дилерского центра – совпадает с компанией – можно удалить
#     - Тип клиента – юридическое или физическое лицо (в рамках анализа не критично – можно удалить)
#     - Форма расчета – наличный и безналичный расчет (много пропусков – можно удалять)
#     - Количество – количество автомобилей в заказе
#     - Цена USD – цена автомобиля
#     - Продажа USD – цена заказа (цена авто умноженная на количество и за вычетом скидок если есть)
#     - Область – область продажи
#     - Сегментация 2013 – сегмент автомобиля актуальный
#     - Класс 2013 – класс автомобиля актуальный
#     - Сегментация Eng – английская сегментация (удаляем)
#     - Локализация производства – удаляем (совпадает со страной производителем)
# 
# Признаки-категории:
# - сегмент
# - класс
# - тип привода
# - коробка передач

# ## Описание задачи
# 
# *Вводные:* **Вы являетесь аналитиком в компании ORBIS AUTO и перед вами стоят следующие задачи при проведении исследования предоставленного датасета:**
# 
# 1. Очистить данные.
# 
# 2. Исследовательский анализ данных:
#     
#     - столбцы;
#     - Строки;
#     - Анализ дубликатов;
#     - Анализ пропусков;
#     - Проанализировать тип данных в каждом столбце, используя python типы и экспертные знания; 
#     - Изменение типа данных и кодирование переменных;
#     - Анализ числовых признаков;
#     - Анализ категориальных признаков.
# 3. Проанализировать рынок.
# 
# 4. Посчитать показатели:
#     - Прибыль и выручка
#     - Рынок
#     - Конкуренты
# 5. Сделать выводы / дать рекомендации

# # Общая подготовка
# Загрузка библиотек

# In[1]:


import pandas as pd
import numpy as np
import re
from math import ceil
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Arial"
from matplotlib.dates import DateFormatter
from matplotlib import colors
import plotly.graph_objects as go
import plotly.express as px
from scipy.stats import gaussian_kde
from plotly.subplots import make_subplots
from scipy.optimize import curve_fit
import seaborn as sns
#!pip install tabulate
from tabulate import tabulate
from scipy import stats as st
from scipy.stats import mannwhitneyu
from statistics import mode
from scipy.stats import ks_2samp
from scipy.stats import mode

from sklearn.preprocessing import LabelEncoder
#plt.close('all')
#!pip install pandas_profiling
from pandas_profiling import ProfileReport
#!pip install gdown
import gdown
import warnings
warnings.filterwarnings("ignore")


# И обновления (на всякий случай)

# In[2]:


#!pip install --upgrade pandas seaborn
#!pip install --upgrade pandas
#!pip install --upgrade seaborn


# In[3]:


try:
    data = pd.read_csv (r'C:\Users\PC_Maks\Desktop\study\workshop_yandex\kz_2019_final_all_dirt.csv',sep = ",", index_col=0)
    
except: 
    url = 'https://drive.google.com/uc?id=168eBeLZX8qZ2be1f6xdO1DXYd_GlpZT7'
    file_path = 'data.csv'

    gdown.download(url, file_path)
    data = pd.read_csv(file_path, sep=',', index_col=0)
    
    
    
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_colwidth', 1000)
plt.rcParams['figure.figsize'] = (15, 8) 


# In[4]:


data


# In[5]:


data.info()


# имеются пропуски, будем решать что с ними делать по мере проведения исследования, а вот типы данных поправим сейчас

# Для начала приведем названия столбцов к питоническому формату, а потом обработаем столбцы "год" и "месяц" 

# In[6]:


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


# In[7]:


data = data_preprocessing (data)


# In[8]:


data.info()


# In[9]:


month_dict = {
    'январь': 'January',
    'февраль': 'February',
    'март': 'March',
    'апрель': 'April',
    'май': 'May',
    'июнь': 'June',
    'июль': 'July',
    'август': 'August',
    'сентябрь': 'September',
    'октябрь': 'October',
    'ноябрь': 'November',
    'декабрь': 'December'
}

data['месяц'] = data['месяц'].map(month_dict)

data['дата'] = pd.to_datetime(data['год'].astype(str) + '-' + data['месяц'], format='%Y-%B')


# In[10]:


# удалим сразу старые столбцы 'год' и 'месяц', а также столбцы которые нам не потребуются для исследования
# "модификация", "сегмент", "наименование_дилерского_центра", "форма_расчета", "сегментация_eng", "локализация_производства"
data.drop(columns=['год', 'месяц', 'модификация', 'сегмент', 'наименование_дилерского_центра', 'форма_расчета',                   'сегментация_eng', 'тип_клиента', 'область', 'локализация_производства'], inplace=True)


# скорректируем название столбцов, для удобства

# In[11]:


data.shape


# In[12]:


data.columns


# In[13]:


data = data.rename(columns={'страна-производитель': 'страна_производитель', 'вид_топлива': 'топливо',                        'объём_двиг,_л,':'объем_двигателя', 'цена,_usd':'цена',                        'продажа,_usd':'продажа', 'сегментация_2013':'сегментация', 'класс_2013':'класс'})


# In[14]:


columns_order = ['дата', 'компания', 'бренд', 'модель', 'год_выпуска', 'страна_производитель',
       'топливо', 'объем_двигателя', 'коробка_передач', 'тип_привода',
       'регион', 'количество', 'цена', 'продажа', 'сегментация', 'класс']

data = data[columns_order]


# проведем замену названий на более удобные в использовании, с учетом питонического формата

# In[15]:


translations = {
    'дата': 'date',
    'компания': 'company',
    'бренд': 'brand',
    'модель': 'model',
    'год_выпуска': 'year_of_production',
    'страна_производитель': 'country',
    'топливо': 'fuel',
    'объем_двигателя': 'engine',
    'коробка_передач': 'transmission',
    'тип_привода': 'drive_type',
    'регион': 'region',
    'количество': 'quantity',
    'цена': 'price',
    'продажа': 'sale',
    'сегментация': 'segmentation',
    'класс': 'klass'
}

# Используем метод rename для переименования столбцов с помощью словаря translations
data.rename(columns=translations, inplace=True)


# In[16]:


data.shape


# ## Используем стандартные проверки, с использованием шаблонных функций (заготовки прошлых периодов)

# ### Изучим наполнение датасета 

# In[17]:


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


# In[18]:


check_unique(data)


# Пропусков хватает((( посмотрим внимательнее на проспуски

# ### Провека на очевидные дубликаты и пропуски 

# In[19]:


def check(data):
    """
    Проверяет DataFrame на наличие дубликатов и пропусков, выводит соответствующую информацию.
    В случае наличия дубликатов удаляет их из исходного датасета.

    Параметры:
    - data (DataFrame): DataFrame, который необходимо проверить.

    Возвращает:
    - None: Функция выводит информацию напрямую в консоль.
    Прим. Удаление дубликатов отключено в данном проекте, с учетом комментариев тимлида об уникальности данных.
    
    """
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

        #num_rows_before = len(data)
        #data.drop_duplicates(inplace=True)
        #num_rows_after = len(data)
        #num_rows_deleted = num_rows_before - num_rows_after
        #percent_deleted = round(num_rows_deleted / num_rows_before * 100, 2)
        #display(f'Удалено дубликатов: {num_rows_deleted} строк ({percent_deleted}% от всего датасета)')
        
    except Exception as e:
        print(f'ERROR: {e}')


# In[20]:


check(data)


# несмотря на, результаты проверки на дубли (15К), взяв во внимание уточнение от тех, кто формировал выгрузку, что дублей по VIN не было, считаем что все авто уникальные.
# сейчас принимаю решение попробовать заполнить пропуски с учетом имеющихся данных (взять модели авто и год выпуска, и по аналогии с имеющимися данными заполнить пропуски в топливе, объеме, типе КПП, привода), допускаю некоторую неточность, но учитывая что в указанных столбцах пропуски не превышают 6%, считаю это допустимым. но для начала нужно "причесать" столбцы с пропусками

# ## Обработка пропусков 

# ### Объем двигателя.
# Прийдется использовать функцию, но для начала подготовим данные, выставим заглушку и заменим тип на float

# In[21]:


def process_volume(volume):
    """
    Обрабатывает значения объема (двигателя), приводя их к стандартному формату.

    Функция выполняет следующие действия:
    - Убирает ненужные символы.
    - Преобразует значения, указанные в миллилитрах, в литры.
    - Заменяет пропуски или значения, равные 0, на 77.
    
    Параметры:
    - volume (str, int, float): Значение объема, которое необходимо обработать.

    Возвращает:
    - float: Обработанное значение объема в литрах с округлением до десятых.
    """
    if isinstance(volume, str):
        
        volume = re.sub(r'[^\d.,]', '', volume)
        volume = re.sub(',', '.', volume)
        if '.' not in volume and len(volume) > 3:
            volume = float(volume) / 1000
        else:
            volume = float(volume)

        volume = round(volume, 1)

    elif (isinstance(volume, int) or isinstance(volume, float)) and not np.isnan(volume):
        if volume > 100:  # Если значение указано в миллилитрах
            volume /= 1000

        volume = round(volume, 1)

    # Заменяем пропуски на значение 77
    if pd.isnull(volume) or volume == 0:
        volume = 77

    return volume


# In[22]:


data.engine = data.engine.apply(process_volume)
data.engine = data.engine.astype (float)
data.engine.unique()


# In[23]:


temp = data.engine.value_counts ().reset_index(drop=False)
temp.sort_values (by='engine', ascending = False).reset_index(drop=True).head(1)


# теперь можем приступить к заполнению пропусков (заглушек - 77)

# In[24]:


# Замена всех 77 на NaN в столбце 'объем_двигателя'
data.engine.replace(77, np.nan, inplace=True)

# Группировка данных по модели и году выпуска
grouped = data.groupby('model')

# Заполнение пропусков в столбце 'объем_двигателя' средним значением по группам
data.engine = grouped['engine'].transform(lambda x: x.fillna(x.min())).round(1)
data.engine.fillna(77, inplace=True)


# In[25]:


temp = data.engine.value_counts ().reset_index(drop=False)
temp.sort_values (by='engine', ascending = False).reset_index(drop=True).head(1)


# Удалось заполнить только 1032 (пропуски и 0) значений, что тоже не плохо, мы снизили с 5.96 до 3,4 пропуски, остальное можем срезать

# In[26]:


data = data.query('engine<50')
data.engine.unique()


# ### Год выпуска.
# Пропуски в году выпуска, менее 1%, сильной роли не сыграют, но чтобы не терять даже эти данные, заменим на минимальные значение от модели

# In[27]:


data.year_of_production.unique()


# In[28]:


data.year_of_production = data.year_of_production.replace('\xa0', ' ', regex=True)
data.year_of_production = data.year_of_production.str.replace(' ', '')


# In[29]:


data.year_of_production.fillna(77, inplace=True)
data.year_of_production = data.year_of_production.astype (int)
#data = data.query('год_выпуска != 77')


# In[30]:


grouped = data.groupby ('model')['year_of_production'].agg (mode).reset_index(inplace=False)
grouped_exploded = grouped.explode('year_of_production')

grouped_exploded.year_of_production = grouped_exploded.year_of_production.apply(lambda x: x[0])

# Оставляем только столбцы 'модель' и 'год_выпуска'
grouped_processed = grouped_exploded[['model', 'year_of_production']]
grouped_processed = grouped_processed.query ('year_of_production > 2000 and year_of_production <= 2019')
grouped_processed.year_of_production.unique()


# In[31]:


for index, row in grouped_processed.iterrows():
    # Выбираем соответствующую модель в основной таблице data
    model_fix = row['model']
    # Получаем значение года выпуска из grouped_processed
    year = row['year_of_production']
    
    # Обновляем значение года выпуска в основной таблице, если встречается 77
    data.loc[(data.model == model_fix) & (data.year_of_production == 77), 'year_of_production'] = year
    
data.year_of_production.replace(77, np.nan, inplace=True)    
    


# In[32]:


check (data)


# В результате манипуляций, количество пропусков в разделе год выпуска удалось снизить с 240 до 112, оставшиеся срезаем ( 0,35%)

# In[33]:


data = data.query ('year_of_production > 2000').reset_index (drop=True)


# In[34]:


grouped_processed.year_of_production.unique()


# ### Тип топлива
# 
# сейчас пропусков 739, или 2,33%. Используем схему, которую использовали при обработке года выпуска

# In[35]:


check (data)


# In[36]:


data.fuel.unique()


# изменять записи не нужно, только убрать пробелы

# In[37]:


data.fuel = data.fuel.str.replace(' ', '')
data.fuel.value_counts (dropna=False)


# Проведем кодировку через словарь (настало время костылей)

# In[38]:


fuel_dict = {
    'бензин': 555,
    'дизель': 777,
    'гибрид': 888,
    'газовый': 999,
    '0': 5789
}

data.fuel = data.fuel.map(fuel_dict)
data.fuel.fillna (5789, inplace=True)
data.fuel.unique()


# In[39]:


grouped = data.groupby ('model')['fuel'].agg (mode).reset_index(inplace=False)
grouped_exploded = grouped.explode('fuel')
grouped_exploded.fuel = grouped_exploded.fuel.apply(lambda x: x[0]).astype (int)


# In[40]:


list_code = [555, 777, 999, 888, 5789]
grouped_exploded = grouped_exploded.query ('fuel in @list_code')
grouped_exploded.fuel.unique()


# In[41]:


for index, row in grouped_exploded.iterrows():
    # Выбираем соответствующую модель в основной таблице data
    model_fix = row['model']
    # Получаем значение типа топлива в grouped_exploded
    fuel_fix = row['fuel']
    
    # Обновляем значение топлива выпуска в основной таблице, если встречается 77
    data.loc[(data.model == model_fix) & (data.fuel == 5789), 'fuel'] = fuel_fix
    
data.fuel.replace(5789, np.nan, inplace=True)  


# In[42]:


check (data)


# In[43]:


data= data.query ('fuel > 0')
data.fuel.value_counts (dropna=False)


# In[44]:


fuel_dict = {
    555 : 'F',
    777: 'D',
    888: 'HYB',
    999: 'E'
}

data.fuel = data.fuel.map(fuel_dict)

data.fuel.unique()


# Получилось немного заполнить пропуски в разделе топливо, из 739 (2,33%) изначальных, осталось 288 (0,91%), остальное срезали. 

# ### Коробка передач
# Сейчас имеем 721 пропуск - 2.3%, используем знакомую схему со словарем, но для начала унифицируем типы, к пропускам отнесем также не указанные значения.

# In[45]:


check (data)


# In[46]:


data.transmission.fillna('0', inplace=True)
data.transmission.isna().sum ()


# In[47]:


data.transmission.unique()


# In[48]:


# соберем в отдельный список механику - ключевые слова
mechanical_keywords = ['мт', 'mт', 'мt', 'mt', 'м/т', 'm/т', 'm/t', 'м/t',                       'мех.', 'мппк', 'мкпп', 'механика', 'механическая', 'm', 'м']
not_defined_keywords = [' -', '-', '0', 'n']


# In[49]:


test_data = data.query ('transmission in @not_defined_keywords')
test_data.transmission.value_counts (dropna=False)


# In[50]:


data.transmission.fillna('not_defined', inplace=True)

# используем маску и меняем через регул выражения значения механики
mechanical_mask = data.transmission.str.contains('|'.join(mechanical_keywords), case=False, flags=re.IGNORECASE)
data.loc[mechanical_mask, 'transmission'] = 'mech'


# In[51]:


data.loc[data.transmission.isin(not_defined_keywords), 'transmission'] = 'not_defined'


# In[52]:


not_auto_mask = (data.transmission != 'not_defined') & ~mechanical_mask
data.loc[not_auto_mask, 'transmission'] = 'automatic'


# In[53]:


data.transmission.unique()


# In[54]:


data.transmission.value_counts (dropna=False)


# Приступим к замене не определенных типов

# In[55]:


transm_dict = {
    'automatic': 555,
    'mech': 777,
    'not_defined': 888
}
data.transmission = data.transmission.map(transm_dict)
display (data.transmission.unique())
grouped = data.groupby ('model')['transmission'].agg (mode).reset_index(inplace=False)
grouped_exploded = grouped.explode('transmission')

grouped_exploded.transmission = grouped_exploded.transmission.apply(lambda x: x[0]).astype (int)

list_code = [555, 777, 888]
grouped_exploded = grouped_exploded.query ('transmission in @list_code').reset_index(drop=True)


# In[56]:


for index, row in grouped_exploded.iterrows():
    # Выбираем соответствующую модель в основной таблице data
    model_fix = row['model']
    # Получаем значение типа топлива в grouped_exploded
    type_transm = row['transmission']
    
    # Обновляем значение топлива выпуска в основной таблице
    data.loc[(data.transmission == model_fix) & (data.transmission == 888),
             'transmission'] = type_transm


# In[57]:


grouped_exploded = grouped.explode('transmission')
grouped_exploded.transmission = grouped_exploded.transmission.apply(lambda x: x[0]).astype (int)


# In[58]:


list_code = [555, 777, 888]
grouped_exploded = grouped_exploded.query ('transmission in @list_code').reset_index(drop=True)
grouped_exploded.transmission.unique()


# In[59]:


for index, row in grouped_exploded.iterrows():
    # Выбираем соответствующую модель в основной таблице data
    model_fix = row['model']
    # Получаем значение типа топлива в grouped_exploded
    type_transm = row['transmission']
    
    # Обновляем значение топлива выпуска в основной таблице
    data.loc[(data.model == model_fix) & (data.transmission == 888),
             'transmission'] = type_transm


# In[60]:


data.transmission.value_counts (dropna=False)


# убираем неопределившихся, а остальное возращаем к исходному виду

# In[61]:


data = data.query('transmission < 800').reset_index(drop=True)


# In[62]:


transm_dict = {
    555: 'automatic',
    777: 'mech'
}
data.transmission = data.transmission.map(transm_dict)
data.transmission.unique()


# В результате корректировок, нам удалось заменить 279 записей, из 829 изначальных пропусков/не определившихся, осталось 550 (срезаем 1,6%) 

# ### Тип привода
# Осталось разобраться с типом привода, сейчас класических 643 пропуска (2,08%), нужно еще посмотреть на нестандарные описания и число неизвестных значений веротяно изменится.
# 
# 'FWD' – передний привод
# 
# '4WD' – полный привод
# 
# 'RWD' – задний привод
# 
# '2WD’ – все остальное 

# In[63]:


check (data)


# In[64]:


data.drive_type.unique()


# будем использовать следующую схему распределения 
# 
# FWD (передний привод):
# 
# 'fwd'
# 'передний'
# 'передний ' (с пробелом в конце)
# 'ff'
# 
# 4WD (полный привод):
# 
# 'quattro'
# '4wd'
# 'полный'
# 'awd'
# '4х4'
# '4x4'
# '4motion'
# 'полный ' (с пробелом в конце)
# '4х2.2'
# '4 wd'
# 'p/time'
# 
# RWD (задний привод):
# 
# 'rwd'
# 'задний'
# 'fr'
# 
# 2WD (все остальное):
# 
# '2wd'
# '2 wd'
# '4x2'
# '4х2'
# '2х4'
# 'cvt'
# '0'
# 

# In[65]:


data.drive_type = data.drive_type.str.replace(' ', '')
data.drive_type.unique()


# In[66]:


data.drive_type.fillna('0', inplace=True)
data.drive_type.isna().sum ()


# In[67]:


fwd_keywords = ['fwd', 'передний', 'ff']
wd4_keywords = ['quattro', '4wd', 'полный', 'awd', '4х4', '4x4', '4motion', '4х2.2', '4wd', 'p/time']
wd2_keywords = ['2wd', '4x2', '4х2', '2х4', 'cvt', '0']
rwd_keywords = ['rwd', 'задний', 'fr']


# In[68]:


fwd_mask = data.drive_type.str.contains('|'.join(fwd_keywords), case=False, flags=re.IGNORECASE)
data.loc[fwd_mask, 'drive_type'] = 'FWD'


# In[69]:


wd4_mask = data.drive_type.str.contains('|'.join(wd4_keywords), case=False, flags=re.IGNORECASE)
data.loc[wd4_mask, 'drive_type'] = '4WD'


# In[70]:


wd2_mask = data.drive_type.str.contains('|'.join(wd2_keywords), case=False, flags=re.IGNORECASE)
data.loc[wd2_mask, 'drive_type'] = '2WD'


# In[71]:


rwd_mask = data.drive_type.str.contains('|'.join(rwd_keywords), case=False, flags=re.IGNORECASE)
data.loc[rwd_mask, 'drive_type'] = 'RWD'


# In[72]:


data.drive_type.value_counts(dropna=False)


# Пропуски в приводе убрал.

# In[73]:


check (data)


# Осталось только удалить строки с пропускаи в столбце количество

# In[74]:


data=data.dropna().reset_index(drop=True)


# ### Итоги чистки
# 
# После всех чисток и замен, из 32854 изначальных строк, осталось 30783, или 94%. Приемлемо. Идем дальше

# ## Обработка типов 

# In[75]:


data.info()


# заменим тип в "Количество", "Цена" и "Продажа" на int, такие тоные данные, как 6 знаков после запятой, нам не обязательны. 

# In[76]:


data [['price', 'sale', 'quantity', 'year_of_production']] = data [['price', 'sale', 'quantity', 'year_of_production']].astype (int)


# In[77]:


#уберем пробелы в сегментации
data.segmentation = data.segmentation.str.strip()
data.klass = data.klass.str.strip()
data.loc[data['klass'].str.contains('suv', case=False, na=False), 'klass'] = 'suv'


# In[78]:


# А столбцы fuel, transmission, segmentation, class сделаем категориальными

data [['fuel', 'transmission', 'segmentation', 'klass']] = data [['fuel', 'transmission', 'segmentation', 'klass']].astype ('category')


# In[79]:


data.info()


# ### Кодировка стран

# In[80]:


data.country.unique ()


# In[81]:


# делаем резервную копию датасета
data2 = data.copy(deep = True)


# In[82]:


try:
    countries_codes = (pd.read_table('https://www.artlebedev.ru/country-list/', encoding='utf8')[0]
                       [['Наименование', 'Полное наименование', 'Alpha3']].\
                       rename(columns={'Наименование':'name', 'Полное наименование':'full_name'}))
    
except:
    countries_codes = pd.read_table('https://www.artlebedev.ru/country-list/tab/')


# In[83]:


countries_codes = data_preprocessing(countries_codes)


# До слияния кодировок, нужно внести правки в названия, например корея - учитывая что есть северная и июная, нужно скорректировать название.

# In[84]:


data.country = data.country.replace('корея', 'республика корея')
data.country = data.country.replace('белоруссия', 'беларусь')


# In[85]:


countries_codes_dict = {}
for i in range(len(countries_codes)):
    if countries_codes.loc[i]['name'] not in countries_codes_dict:
        countries_codes_dict[countries_codes.loc[i]['name']] = countries_codes.loc[i]['alpha3']
        
    if countries_codes.loc[i]['fullname'] not in countries_codes_dict:
        countries_codes_dict[countries_codes.loc[i]['fullname']] = countries_codes.loc[i]['alpha3']


# In[86]:


data.country = data.country.apply(lambda cell: countries_codes_dict.get(cell, cell))


# In[87]:


data.country.unique ()


# ## Анализ данных

# Учитывая датасет с которым подошли к пришло время посмотреть на числовые значения, в том числе на выбросы

# In[88]:


data.describe ()


# ### Визуализация даных для исследования

# In[89]:


def plot_distribution_and_box(data, columns):
    """
    Отображает гистограмму распределения и ящик с усами (Box plot) для указанных столбцов датасета.

    Эта функция использует Plotly для создания интерактивных графиков. Она предназначена для анализа 
    распределения значений в столбцах датасета. Для каждого указанного столбца функция выводит два графика: 
    гистограмму с линией плотности ядерной оценки (KDE) и ящик с усами.

    Параметры:
    - data (DataFrame): DataFrame, содержащий данные для анализа.
    - columns (list): Список столбцов, для которых необходимо создать графики.
    """
    for column in columns:
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig.add_trace(go.Histogram(x=data[column], nbinsx=25, histnorm='probability', name='Распределение', marker_color='steelblue'), secondary_y=False)
        fig.update_layout(title=f'Распределение значений в столбце {column}', xaxis_title=column, yaxis_title='Частота')
        fig.update_layout(xaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='lightgray'), yaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='lightgray'))
        
        kde = gaussian_kde(data[column])
        x_vals = sorted(data[column])
        y_vals = kde(x_vals)
        
        fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', line=dict(color='red', width=2), name='KDE'), secondary_y=True)
        fig.update_yaxes(title_text="Частота", secondary_y=False)
        fig.update_yaxes(title_text="Плотность", secondary_y=True)
        
        fig.show()
        
        fig = go.Figure()
        fig.add_trace(go.Box(x=data[column], name='Ящик с усами', marker_color='steelblue'))
        fig.update_layout(title=f'Ящик с усами для столбца {column}', xaxis_title=column)
        fig.update_layout(xaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='lightgray'), yaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='lightgray'))
        
        fig.show()


# In[90]:


columns_to_plot = ['price', 'engine', 'year_of_production', 'quantity']
plot_distribution_and_box(data, columns_to_plot)


# "Год производства" - в основном все машины 2018 года, 
# 
# медиативный объем двигателя 2 литра, в среднем 2.25, основная масса в пределах 3 литров, есть автомобили с объемом 17.5 (вероятно, автобусы или грузовики), 
# 
# "количество" - в основном покупают по 1 авто, но есть странные значения, в частности, 91 автомобиль (кто-то открывал такси?), большинство значений в диапазоне 1-4 
# 
# "цена" - подавляющее большинство автомобилей стоимостью в пределах 40000, аномальная высокая цена в 254958, могу пока предположить это стоимость всех авто для найденного ранее "таксопарка"
# 

# Посмотрим на распределение в части типов привода, топлива и КП и т.п.

# In[91]:


def category_plot(data, columns):
    """
    Отображает столбчатые диаграммы для категориальных переменных датасета в зависимости от их частоты.

    Эта функция использует Plotly для создания интерактивных графиков. Она предназначена для визуализации
    частоты уникальных значений категориальных переменных. Для каждого указанного столбца функция создает
    столбчатую диаграмму, отсортированную по убыванию частоты.

    Параметры:
    - data (DataFrame): DataFrame, содержащий данные для анализа.
    - columns (list): Список категориальных столбцов, для которых необходимо создать графики.
    """
    for c in columns:
        group_data = data.pivot_table(index=c, values='price', aggfunc='count').reset_index()
        group_data = group_data.sort_values(by='price', ascending=False)
        
        fig = make_subplots(specs=[[{"secondary_y": False}]])
        
        fig.add_trace(go.Bar(x=group_data[c], y=group_data['price'], name='Количество', marker_color='steelblue'))
        fig.update_layout(title=f'График распределение по типу {c}', xaxis_title=c, yaxis_title='Количество')
        fig.update_layout(xaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='lightgray'), yaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='lightgray'))
        
        fig.show()


# In[92]:


columns_to_plot = ['country', 'fuel', 'transmission', 'drive_type', 'segmentation', 'klass']
category_plot (data, columns_to_plot)


# Пока отмечаем аномалии и всплески, разбирать их будем чуть позже, сейчас займемся проверкой корреляции И расчетом ТОПов.

# ### Топ продаж по медиативной цене и количество проданных авто

# #### Срез для выявления покупок для частных целей, и визуализация результатов
# Перед расчетом, необходимо сначала исключить таксопарки, коммерческие закупки. Исходя из логики, могу сделать обоснованное предположение, что если покупается больше 2-х машин за один раз, то это маловероятно для частного использования, а также можно исключить сегмент - коммерческие автомобили, когда указано в явном виде 

# In[93]:


personal_data = data.query ('quantity <=2 and segmentation != "коммерческие автомобили"')


# In[94]:


personal_data.segmentation = personal_data.segmentation.astype ('object')
personal_data.segmentation.unique ()


# In[95]:


personal_data.klass = personal_data.klass.astype ('object')
personal_data.klass.unique ()


# In[96]:


# посмотрим еще раз на визуализацию после выделенния "частных" покупок
columns_to_plot = ['country', 'fuel', 'transmission', 'drive_type', 'segmentation', 'klass']
category_plot (personal_data, columns_to_plot)


# Как можем отметить, самые популярные - внедорожники, на втором месте легковые авто, в основном продаются автомобили на бензине, с коробкой автомат, и с полным приводом. Если смотреть на класс - то самый популярный suv - по сути внедорожник городского типа, так называемый паркетник.

# In[97]:


columns_to_plot = ['price', 'engine', 'year_of_production', 'quantity']
plot_distribution_and_box(personal_data, columns_to_plot)


# Медиативное значение объема двигателя, после фильтрации, 2 литра, 
# цена в диапазоне от 15 до 35 тысяч долларов 

# #### Топ-10 бренды по количеству приобретенных авто

# In[98]:


group_brand = personal_data.groupby ('brand').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)


# In[99]:


top_brands = group_brand.reset_index(drop=True).head (10)
top_brands


# In[100]:


top_brands_sale = group_brand.sort_values(by ='sale', ascending = False).reset_index(drop=True).head (10)
top_brands_sale


# Самая популярная марка - тойота, на втором месте хендай, и тройку лидеров замыкает ravon. 
# 
# А в части самой высокой выручки, первое место занимает ожидаемо тайота (очень большое количество продаж).

# ### Динамика продаж по рынку, в штуках и в денежном выражении.

# сначала посмотрим на общие продажи по дням

# In[101]:


def plot_dinamic (data, column1, column2, task=1):
    """
    Отображает динамику указанного столбца по датам. В зависимости от значения `task` может разделить линии по 
    значениям другого столбца или предоставить агрегированное представление.

    Эта функция использует Plotly Express для создания интерактивных линейных графиков. Она предназначена для 
    визуализации динамики указанного столбца (column2) по датам с возможностью разделения линий на основе значений 
    другого столбца (column1).

    Параметры:
    - data (DataFrame): DataFrame, содержащий данные для анализа.
    - column1 (str): Имя столбца, по которому, возможно, будет производиться разделение линий.
    - column2 (str): Имя столбца, агрегированное значение которого будет отображено на графике.
    - task (int, optional): Если равно 1, будет показана общая динамика column2. Если отличается от 1, 
                            график будет разделен по значениям column1. По умолчанию равно 1.
    """
    if task == 1:
        quantity_by_date = data.groupby(['date'])[column2].sum().reset_index()
        fig = px.line(quantity_by_date, x='date', y=column2, title=f'Распределение {column2} по месяцам')
        fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(buttons=list([
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])))
        fig.show()
    else:
        quantity_by_date = data.groupby(['date', column1])[column2].sum().reset_index()

        fig = px.line(quantity_by_date, x='date', y=column2, color=column1, title=f'Распределение {column2} по {column1} и месяцам')
        fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(buttons=list([
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])))
        fig.show()


# In[102]:


plot_dinamic (personal_data, 'quantity', 'quantity', task=1)


# Как видно из графика, пик продаж приходится на июнь 2019 года - 3467 приобретено автомобилей, а если взять более большой отрезок, то можно отметить общую активность покупателей на период с мая по сентябрь включительно. В июле значения немного снижаются, но могу предположить, что сезон отпусков и в авторынке имеет свой вес.

# In[103]:


plot_dinamic (personal_data, 'sale', 'sale', task=1)


# При анализе продаж в денежном выражении выявлена интересная динамика: в августе количество проданных автомобилей почти совпадает с их пиковым значением в июне. Однако общая стоимость приобретенных автомобилей в августе заметно ниже, даже по сравнению с маем. Это может свидетельствовать о том, что в августе покупатели приобретали автомобили более низкого ценового сегмента или модели дешевле.

# ### Посмотрим детальнее на динамику, по типам: брендов, топлива, приводу, классу, региону, автоцентру и сегменту

# #### Бренд

# In[104]:


data_subset_units = personal_data[personal_data['brand'].isin(top_brands.brand)]
plot_dinamic (data_subset_units, 'brand', 'quantity', task=2)


# In[105]:


plot_dinamic (data_subset_units, 'brand', 'sale', task=2)


# Лидеры по Продажам:
# 
#     - Toyota: Безоговорочный лидер по количеству проданных автомобилей на всем периоде наблюдения. Доход от продаж данного бренда также является наивысшим, достигая пика в более 61 млн.
#     - Hyundai: На втором месте по количеству продаж, однако по доходу занимает третье место после Toyota и Lexus. Интересно, что в апреле Hyundai уступал по доходам Lexus.
# 
# Бренды с Высоким Ценовым Сегментом:
# 
#     - Lexus: При меньшем количестве проданных автомобилей показывает высокий уровень дохода. Это говорит о том, что бренд сконцентрирован на премиум-сегменте рынка.
# 
# Бренды с Низким Ценовым Сегментом:
# 
#     - Ravon: На начальном этапе показывает внушительные продажи, однако после февраля 2019 года их продажи резко снижаются. К концу исследуемого периода продажи данного бренда практически исчезают.
# 
# 
# Общие Наблюдения:
# 
#     - Toyota имеет сильное влияние на рынок, так как общая динамика продаж автомобилей совпадает с графиком продаж данного бренда.
#     - Бренды Ravon и Lada сконцентрированы на бюджетном сегменте, так как при сравнительно высоком количестве продаж их доход меньше других брендов.
#     - Бренды JAC, Nissan, Renault, Volkswagen, и Chevrolet не показывают выдающихся результатов как по количеству, так и по доходу от продаж.
# 
# 
# Выводы показывают, что рынок автомобилей в Казахстане доминируется некоторыми ключевыми игроками, в то время как другие бренды занимают ниши или более низкие сегменты рынка. При принятии решений о запуске нового автосалона или расширении действующего бизнеса, необходимо учитывать эти данные для эффективного позиционирования и определения стратегии.

# #### Автоцентр

# In[106]:


group_brand = personal_data.groupby ('company').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)
group_brand.sale = group_brand.sale.round (1)
top_company = group_brand.reset_index(drop=True).head (10)
top_company


# Ожидаемый лидер - официальный дилер тойота - почти 30% всех продаж, с целью более корректного исследования, исключим данного дилера из рейтинга 

# In[107]:


group_brand_no_toyota = group_brand.query ('company != "toyota motor kazakhstan"')
top_company_units = group_brand_no_toyota.reset_index(drop=True).head (10)
top_company_units


# In[108]:


data_subset_units = personal_data[personal_data.company.isin(top_company_units.company)]

plot_dinamic (data_subset_units, 'company', 'quantity', task=2)
plot_dinamic (data_subset_units, 'company', 'sale', task=2)


# Динамика продаж:
# 
# Узавто-Казахстан: Начинает как лидер продаж, однако со временем их продажи резко снижаются. Это указывает на возможные внутренние или внешние проблемы у компании.
# Astana-motors: С января 2019 года становится непререкаемым лидером рынка и удерживает это положение до сентября 2019 года. Отставание остальных участников составляет в 2-3 раза по выручке. Пик продаж этой компании приходится на май 2019 года с выручкой более 18 млн.
# Внешние факторы:
# 
# По данным из сети, Узавто-Казахстан сменил свою политику, увеличив экспорт популярных моделей, таких как Chevrolet Cobalt, даже при наличии спроса на внутреннем рынке. Это может объяснить снижение их продаж в Казахстане.
# Медианный чек:
# 
# Subaru Kazakhstan лидирует среди всех участников рынка по медианному чеку, достигая пика в 2,77 млн. 
# 
# Прим. удалось найти в сети информацию, что политика компании Узавто-Казахстан менялась, а именно был увеличен экспорт самых популярных моделей - шевроле кобальт, несмотря на, очереди на внутреннм рынке, могу предположить, что снижение продаж на рынке Казахстана связано именно с данными изменениями. 
# 

# #### Регион

# In[109]:


group_brand = personal_data.groupby ('region').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)

top_company_units = group_brand.reset_index(drop=True).head (10)
display (top_company_units)

data_subset_units = personal_data[personal_data.region.isin(top_company_units.region)]


# In[110]:


plot_dinamic (data_subset_units, 'region', 'quantity', task=2)
plot_dinamic (data_subset_units, 'region', 'sale', task=2)


# Лидеры продаж:
# 
# Алматы и Астана являются абсолютными лидерами по продажам автомобилей на изучаемом отрезке. Эти города существенно превосходят другие регионы как по количеству продаж, так и по их объему в денежном выражении.
# Сравнивая их с другими участниками рейтинга, объем продаж в Алматы и Астане вместе взятых превышает объем продаж в остальных городах из ТОПа.
# Характеристика рынков:
# 
# Алматы: Наиболее активный регион с точки зрения продаж. Высокие показатели, вероятно, обусловлены большим населением, активной экономикой и большим количеством бизнесов.
# Астана: Второй по величине рынок автомобилей с высоким уровнем экономической активности.
# Шымкент, Костанай и Атырау: Заметный рынок, но меньше по объемам, чем в Алматы и Астане.
# Другие города: Регионы, такие как Караганда, Уральск, Актау, Усть-Каменогорск и Актобе, имеют существенное количество продаж, хотя и в меньших объемах.
# 

# #### Тип топлива

# In[111]:


group_brand = personal_data.groupby ('fuel').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)
top_fuel = group_brand.reset_index(drop=True).head (10)
top_fuel


# In[112]:


data_subset_units = personal_data[personal_data.fuel.isin(top_fuel.fuel)]
plot_dinamic (data_subset_units, 'fuel', 'quantity', task=2)
plot_dinamic (data_subset_units, 'fuel', 'sale', task=2)


# Результат ожидаемый - явный лидер - бензиновый двигатель

# #### Класс

# In[113]:


group_brand = personal_data.groupby ('klass').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)
top_klass = group_brand.reset_index(drop=True).head (10)
display (top_klass)
data_subset_units = personal_data[personal_data.klass.isin(top_klass.klass)]
plot_dinamic (data_subset_units, 'klass', 'quantity', task=2)
plot_dinamic (data_subset_units, 'klass', 'sale', task=2)


# Парткетники лидирует как в количестве так и в денежном выражении, а вот картина со вторым местом в рейтинге в штуках и в объемах продаж немного отличается, в количественном выражении лидерует Б класс, иногда уступая Е классу, но не сильно, а в денежном выражении Е класс вырывается на второе место с марта 2019 года и сохраняет лидерскую позицию до конца.
# 
# SUV (внедорожники) являются самым популярным классом автомобилей как по объему продаж (sale), так и по количеству проданных автомобилей (quantity). Это может быть связано с повышенной потребностью в автомобилях этого класса из-за их универсальности, пространства и проходимости.
# 
# Автомобили класса B занимают второе место по популярности среди покупателей, что может быть обусловлено их доступностью и практичностью для городской езды.
# 
# Автомобили класса E и C также имеют значительное количество продаж и проданных единиц, что говорит о спросе на более премиальные или большие автомобили.
# 
# Пикапы (pick-ups) и автомобили класса A и D также представлены в данных, но их продажи и количество значительно меньше, что может говорить о более ограниченном спросе или меньшей доступности этих типов автомобилей.
# 
# Классы автомобилей F, полноразмерные минивэны и компактвэны наименее представлены в продажах. Это может быть связано с меньшей популярностью этих типов автомобилей, их стоимостью или недостаточным предложением на рынке.

# #### Привод

# In[114]:


group_brand = personal_data.groupby ('drive_type').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)
top_drive_type = group_brand.reset_index(drop=True).head (10)
display (top_drive_type)
data_subset_units = personal_data[personal_data.drive_type.isin(top_drive_type.drive_type)]
plot_dinamic (data_subset_units, 'drive_type', 'quantity', task=2)
plot_dinamic (data_subset_units, 'drive_type', 'sale', task=2)


# Переднеприводные автомобили лидировали вплоть до марта 2019 года, и занимали на март 2019 г. первое место с 1172 продажами, но с апреля 2019  начинают уступать первое место полноприводным авто с продажами на пике в августе 2019 - 1703 шт.
# Динамика продаж в денежном выражении более равномерная в части лидерства - первое место полноприводные авто, с пиком в июне в размере 65 млн.
# 
# Самым популярным типом привода является 4WD (полный привод), как по объему продаж (sale), так и по количеству проданных автомобилей (quantity). Это может говорить о высоком спросе на автомобили с полным приводом, что может быть связано с условиями дорожного движения, климатическими условиями или предпочтениями покупателей.
# 
# Вторым по популярности является FWD (передний привод). По объему продаж он уступает 4WD, хотя разница в количестве проданных автомобилей не так велика. Это может говорить о том, что автомобили с передним приводом в среднем дешевле автомобилей с полным приводом.
# 
# RWD (задний привод) является наименее популярным типом привода, продажи которого составляют всего лишь небольшую долю от общего числа продаж. Это может быть связано с тем, что автомобили с задним приводом часто ассоциируются с спортивными или премиальными автомобилями, которые обычно имеют более ограниченный рынок.
# 
# Привод 2WD также имеет значительное количество продаж и количество проданных автомобилей, что говорит о том, что эти автомобили также находятся в спросе, хотя и уступают по популярности автомобилям с полным и передним приводом.

# #### Сегмент

# In[115]:


group_brand = personal_data.groupby ('segmentation').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)
top_segmentation = group_brand.reset_index(drop=True).head (10)
display (top_segmentation)
data_subset_units = personal_data[personal_data.segmentation.isin(top_segmentation.segmentation)]
plot_dinamic (data_subset_units, 'segmentation', 'quantity', task=2)
plot_dinamic (data_subset_units, 'segmentation', 'sale', task=2)


# В части количества проданных авто, внедорожники уверенно лидирует с июня 2019 года и на пике имеют 2118 проданных авто, второе место занимаю легкоые авто. В денежном выражении внедорожники удерживают лидерскую позицию на всем исследуемомо отрезке, и имеют пиковое значение почти в 71 млн.

# ### Исследование средних показателей по брендам и маркам

# Бренды уже рассматривали, там беззаговорочный лидер Tayota. теперь посмотрим по моделям

# In[116]:


group_brand = personal_data.groupby('model').agg({
    'price':'mean',
    'quantity':'sum',
    'klass':lambda x: x.mode()[0] if len(x.mode()) > 0 else None
}).reset_index().sort_values(by='price', ascending=False)

group_brand.price=group_brand.price.round (1)
top_brands = group_brand.reset_index(drop=True).head (10)
top_brands


# В основном представлены автомобили класса F и SUV. Это свидетельствует о предпочтении покупателей премиум-сегмента именно этих классов автомобилей.
# 
# Модель LX отличается от других наличием большого количества продаж (404 единицы), что говорит о ее популярности среди покупателей, несмотря на высокую среднюю цену.
# 
# С другой стороны, модели 911 Carrera S, G-class, LC и Genesis G90 продались в очень маленьком количестве (от 1 до 2 единиц), что может говорить о их эксклюзивности, либо о меньшей популярности среди покупателей по каким-то причинам.
# 
# Самой дорогой моделью является 911 Carrera S, что может свидетельствовать о её высоком статусе или ограниченной доступности.
# 
# Самым продаваемым автомобилем из списка является LX, несмотря на то что его цена значительно выше среднего.

# ### Емкость рынка

# In[117]:


total_sales = personal_data['quantity'].sum()
display ('Общий объем продаж:', total_sales)


# In[118]:


company_sales = personal_data.groupby('company')['quantity'].sum().sort_values(ascending=False)
display ('Продажи по салонам', company_sales)


# In[119]:


region_sales = personal_data.groupby('region')['quantity'].sum().sort_values(ascending=False)
display('Продажи по регионам', region_sales)


# In[120]:


sale_by_date = personal_data.groupby('date')['sale'].sum().reset_index()
sale_by_date


# Чуть раньше уже проводился анализ данных направлений в срезе Топов, но если обобщить 
# 
# Объем продаж: Всего было продано 27 155 единиц товара.
# 
# Продажи по компаниям:
# 
# Наибольший объем продаж приходится на компанию 'Toyota Motor Kazakhstan' с 10 440 проданными единицами.
# За ней следует 'Astana Motors' с 5 703 проданными единицами.
# 'Бипэк Авто' и 'Узавто-Казахстан' также показали значительные продажи - 2 728 и 1 727 единиц соответственно.
# Наименьшие показатели у компаний 'Sivi Finance Consulting' и 'SMC' - 4 и 1 единица соответственно.
# Продажи по регионам:
# 
# Наибольший объем продаж был в Алматы (8 013 единиц), затем в Астане (5 881 единица).
# Другие крупные города, такие как Шымкент, Костанай и Атырау, также показали значительные показатели продаж.
# Наименьшие объемы продаж были в Щучинске (3 единицы).
# В общем, продажи сконцентрированы в крупных городах и у крупных автомобильных дистрибьюторов. Вероятно, это связано с наличием у этих дистрибьюторов большего количества автосалонов в крупных городах и лучшим доступом к ресурсам, таким как реклама и распределение.
# 
# Меньшие продажи в некоторых регионах и у некоторых дистрибьюторов могут указывать на необходимость усилить маркетинговые усилия или присмотреться к спросу в этих регионах.
# 
# Динамика продаж:
# Судя по данным, продажи варьируются от месяца к месяцу.
# Наименьший объем продаж был в январе 2019 года (60 426 429), а наибольший - в июне 2019 года (113 785 455).
# Отмечается общий тренд к росту продаж с начала года: с января по июнь продажи почти удвоились.
# После июня 2019 года продажи немного снизились (в июле), но затем снова увеличились и стабилизировались на уровне около 103-105 млн в августе и сентябре.
# В общем, данная динамика может быть связана с сезонностью или другими факторами, влияющими на спрос. Так, например, рост продаж в первой половине года может быть связан со снижением стоимости автомобилей из-за модельного года или с покупкой автомобилей перед летними каникулами, перед отпусками и т.п.

# ### Оценим долю рынка на примере компании mercur auto

# #### Расчет общей доли на рынке у mercur auto (количественном и стоимостном выражении)

# In[121]:


total_quantity = data.quantity.sum()
total_sales = data.sale.sum()

mercur_quantity = data[data.company == 'mercur auto']['quantity'].sum()
mercur_sales = data[data.company == 'mercur auto']['sale'].sum()

quantity_market_share = (mercur_quantity / total_quantity) * 100
sales_market_share = (mercur_sales / total_sales) * 100

display (f"Количественная доля рынка компании 'mercur auto': {quantity_market_share:.2f}%")
display (f"Стоимостная доля рынка компании 'mercur auto': {sales_market_share:.2f}%")


# #### Hасчета доли рынка mercur auto по маркам

# In[122]:


total_sales_by_brand = data.groupby('brand')['sale'].sum()

mercur_sales_by_brand = data[data.company == 'mercur auto'].groupby('brand')['sale'].sum()

brand_market_share = (mercur_sales_by_brand / total_sales_by_brand) * 100

display ("Доли рынка компании 'mercur auto' по маркам:")
display (brand_market_share)


# #### Рассчитаем долю рынка mercur auto по классам

# In[123]:


total_sales_by_klass = data.groupby('klass')['sale'].sum()

mercur_sales_by_klass = data[data.company == 'mercur auto'].groupby('klass')['sale'].sum()

klass_market_share = (mercur_sales_by_klass / total_sales_by_klass) * 100

display ("Доли рынка компании 'mercur auto' по классам:")
display (klass_market_share)


# #### Общие вывод по mercur auto
# 
# *Общая доля рынка:* 
# 
# Компания 'mercur auto' занимает 2,83% рынка по количеству проданных автомобилей и 3,18% рынка по стоимости продаж. Это указывает на то, что средняя стоимость автомобиля, проданного компанией, выше среднего уровня по рынку.
# 
# *Доля рынка по маркам:*
# 
# Компания 'mercur auto' полностью доминирует на рынке брендов Audi, Porsche и Volkswagen, занимая 100% долю продаж по этим маркам. Это может указывать на эксклюзивные права на продажу или очень сильное присутствие в этом сегменте.
# По другим маркам у компании нет продаж, что может указывать на специализированный характер деятельности компании или на наличие эксклюзивных договоров с определенными производителями.
# 
# *Доля рынка по классам:*
# 
# Наибольшую долю рынка 'mercur auto' занимает в сегменте "спортивные автомобили", составляющую 84,04%. Это может говорить о том, что компания специализируется на продаже спортивных автомобилей или имеет выдающееся предложение в этом сегменте.
# Другие выдающиеся сегменты, в которых компания имеет заметное присутствие, включают "полноразмерные минивэны" с долей 18,41% и "микроавтобусы" с долей 9,71%.
# В некоторых классах, таких как "а класс", "большие автобусы", "компактвэн" и других, у компании нет продаж, что может говорить о целевой специализации компании или о стратегическом решении не работать с этими сегментами.
# Общий вывод: Компания 'mercur auto', вероятно, является специализированным дилером, сосредоточенным на определенных марках и классах автомобилей. Её присутствие особенно заметно в сегменте спортивных автомобилей, полноразмерных минивэнов и микроавтобусов. Это может указывать на то, что компания выбрала стратегию дифференциации и фокусируется на конкретных нишах рынка.

# ### Рассчет для mercur auto в части конкурентов

# In[124]:


company_ranking = data.groupby('company')['sale'].sum().sort_values(ascending=False)

display ("Лидеры рынка по объему продаж:")
display (company_ranking.head())


# Ранее мы уже смотрели на топ рынка по продажам, и отмечали лидирующие позиции toyota motor kazakhstan, теперь посмотрим на топ-5 в сравнении с mercur auto

# #### Определение ближайших конкурентов для "mercur auto":

# In[125]:


mercur_regions = data[data.company == 'mercur auto']['region'].unique()
mercur_brands = data[data.company == 'mercur auto']['brand'].unique()
mercur_klasses = data[data.company == 'mercur auto']['klass'].unique()

competitor_data = data[(data.region.isin(mercur_regions)) & 
                     (data.brand.isin(mercur_brands)) & 
                     (data.klass.isin(mercur_klasses))]


competitor_ranking = competitor_data.groupby('company')['sale'].sum().sort_values(ascending=False)

# Исключим "mercur auto" из списка, чтобы увидеть конкурентов
competitor_ranking = competitor_ranking[competitor_ranking.index != 'mercur auto']

display ("Ближайшие конкуренты 'mercur auto' по объему продаж:")
display (competitor_ranking.head())


# Странно, якобы никого нет, нужно проверить, исключая по очереди наши параметры

# In[126]:


regional_competitor_data = data[data.region.isin(mercur_regions)]
regional_competitor_ranking = regional_competitor_data.groupby('company')['sale'].sum().sort_values(ascending=False)
regional_competitor_ranking = regional_competitor_ranking[regional_competitor_ranking.index != 'mercur auto']
display ("Конкуренты 'mercur auto' по объему продаж в регионах:")
display (regional_competitor_ranking.head())


# По регионам явно проблем нет с поиском конкурентов 

# In[127]:


brand_competitor_data = data[data.brand.isin(mercur_brands)]
brand_competitor_ranking = brand_competitor_data.groupby('company')['sale'].sum().sort_values(ascending=False)
brand_competitor_ranking = brand_competitor_ranking[brand_competitor_ranking.index != 'mercur auto']
display ("Конкуренты 'mercur auto' по объему продаж среди брендов:")
display (brand_competitor_ranking.head())

klass_competitor_data = data[data.klass.isin(mercur_klasses)]
klass_competitor_ranking = klass_competitor_data.groupby('company')['sale'].sum().sort_values(ascending=False)
klass_competitor_ranking = klass_competitor_ranking[klass_competitor_ranking.index != 'mercur auto']
display ("Конкуренты 'mercur auto' по объему продаж в классах машин:")
display (klass_competitor_ranking.head())


# #### Распределение продаж по месяцам или годам для 'mercur auto' и их основных конкурентов

# In[128]:


# соберем данные по месяцам:
monthly_sales = data.groupby(['company', data['date'].dt.to_period('M')])['sale'].sum().reset_index()
# лидеров рынка по классам машин и mercur auto
list_of_competitors = ['mercur auto', 'toyota motor kazakhstan', 'бипэк авто', 'astana motors',                       'nissan manufacturing rus', 'автоцентр-бавария']
monthly_sales = monthly_sales.query('company == @ list_of_competitors')


# In[129]:


monthly_sales['date'] = monthly_sales['date'].astype(str)
fig = px.line(monthly_sales, x='date', y='sale', color='company', title='Распределение продаж по месяцам')
fig.update_xaxes(rangeslider_visible=True)
fig.show()


# *Лидеры рынка по регионам:*
# 
# Как уже отмечалось, компания "toyota motor kazakhstan" является абсолютным лидером рынка с продажами, превышающими 415 миллионов.
# Следом идут компании "бипэк авто" и "astana motors" с продажами около 117 и 115 миллионов соответственно.
# "вираж" и "nissan manufacturing rus" также находятся в списке лидеров, но их продажи значительно меньше — 45 и 42 миллиона соответственно.
# 
# *По брендам:*
# 
# На основе предоставленных данных 'mercur auto' является единственной компанией, предлагающей некоторые из рассматриваемых брендов. Это может указывать на эксклюзивное право 'mercur auto' на продажу этих брендов или на то, что конкуренты не работают с этими конкретными брендами.
# 
# *По классам машин:*
# 
# Снова, "toyota motor kazakhstan" лидирует с продажами более 468 миллионов.
# "бипэк авто" и "astana motors" следуют за ней с продажами 149 и 124 миллиона соответственно.
# "nissan manufacturing rus" и "автоцентр-бавария" замыкают пятерку лидеров с продажами 43 и 23 миллиона соответственно.
# 
# 
# *Общие выводы:*
# 
# "toyota motor kazakhstan" является ключевым игроком на рынке в рассматриваемых регионах и классах машин.
# 'mercur auto' имеет уникальное преимущество в определенных брендах, что может служить конкурентным преимуществом.
# Хотя 'mercur auto' может не иметь такого большого объема продаж, как некоторые из лидеров рынка, уникальные бренды и возможное эксклюзивное право на их продажу могут дать возможность для стратегического позиционирования и разработки маркетинговых кампаний. Посмотрим более детально на продажи по регионам, брендам и классам, в срезе лидеров рынка и mercur auto

# #### Распределение продаж по регионам, брендам и классам

# In[130]:


def plot_sales_by_category(data, category, list_of_competitors):
    """
    Составляет график продаж по заданной категории.

    Аргументы:
    - данные (pd.DataFrame): набор данных.
    - категория (str): категория, по которой следует группировать продажи (например, "бренд", "класс", "регион").
    - list_of_competitors (список): список конкурентов для фильтрации данных.

    Что возвращает:
    - ничего: отображает график.
    """
    grouped_data = data.groupby([category, 'company'])['sale'].sum().reset_index()
    filtered_data = grouped_data[grouped_data['company'].isin(list_of_competitors)]
    fig = px.bar(filtered_data, x=category, y='sale', color='company', title=f'Продажи по {category}')
    fig.show()


# In[131]:


plot_sales_by_category(data, 'brand', list_of_competitors)
plot_sales_by_category(data, 'klass', list_of_competitors)
plot_sales_by_category(data, 'region', list_of_competitors)


# **Если кратко обобщить результаты визуализации**
# 
# Бренды:
# 
# Toyota является абсолютным лидером, причем их дистрибьютор 'Toyota Motor Kazakhstan' контролирует наибольшую долю рынка. Другие выдающиеся бренды включают Lada, Hyundai, Lexus, и Kia.
# С другой стороны, 'Mercur Auto' предоставляет такие бренды как Audi, Porsche и Volkswagen. Несмотря на то, что Volkswagen имеет заметные продажи в 20,438,224, другие бренды этого дистрибьютора, такие как Audi и Porsche, имеют относительно меньший объем продаж.
# Категории транспортных средств:
# 
# 'Toyota Motor Kazakhstan' и 'Astana Motors' доминируют в ряде высокодоходных категорий, таких как SUV, E класс и коммерческие транспортные средства.
# В то время как 'Mercur Auto' занимает значимые позиции в категориях F класс и микроавтобусы. Однако, в целом, их доля на рынке в этих категориях меньше по сравнению с 'Toyota Motor Kazakhstan' и 'Astana Motors'.
# Сравнение с 'Mercur Auto':
# 
# Несмотря на то, что 'Mercur Auto' представляет несколько высококачественных брендов, их общий объем продаж ниже, чем у ключевых лидеров рынка.
# Они занимают ведущие позиции в определенных нишевых категориях, но их общий рыночный охват и разнообразие представленных категорий меньше по сравнению с главными игроками рынка.
# В заключении, 'Mercur Auto' является активным участником рынка, предоставляя ряд премиальных брендов и занимая лидирующие позиции в некоторых категориях. Однако, по общему объему продаж и разнообразию представленного транспорта, они уступают таким гигантам рынка, как 'Toyota Motor Kazakhstan' и 'Astana Motors'.

# ## Итоговые выводы

# **Общие выводы:**
# 
#     Объем продаж: Всего было продано 27 155 единиц товара.
# 
#     Продажи по компаниям:
# 
# 'Toyota Motor Kazakhstan' является лидером рынка с 10 440 проданными единицами.
# 'Astana Motors' и 'Бипэк Авто' также являются ключевыми игроками с 5 703 и 2 728 проданными единицами соответственно.
# Компании 'Sivi Finance Consulting' и 'SMC' показали наименьший объем продаж - 4 и 1 единица соответственно.
# Между тем, компания "mercur auto" занимает долю рынка в размере 2.83% по количеству и 3.18% по стоимости.
# 
#     Продажи по регионам:
# 
# Алматы и Астана являются ключевыми регионами с продажами 8 013 и 5 881 единиц соответственно.
# Города Шымкент, Костанай и Атырау также показали значительные показатели.
# Щучинск стоит выделить как регион с наименьшим объемом продаж - всего 3 единицы.
# Динамика продаж: Продажи имеют тенденцию к росту с января по июнь, вероятно, из-за сезонности или экономических факторов.
# 
#     Классы автомобилей:
# 
# Самыми популярными являются автомобили класса F и SUV. В частности, "mercur auto" особенно сильно представлено в классе F (39.05%) и классе спортивных автомобилей (84.04%).
# Модель LX наиболее популярна среди покупателей, продавшись в количестве 404 единиц.
# Модели 911 Carrera S, G-class, LC и Genesis G90 менее популярны, с продажами в диапазоне от 1 до 2 единиц.
# 
# **Выводы по компании Mercur Auto**
# 
#     - Рыночное положение: 
#     
# 'Mercur Auto' обладает количественной долей рынка в 2.83% и стоимостной долей в 3.18%. Это показывает, что хотя их общий объем продаж может быть меньше, чем у некоторых других игроков, они, вероятно, продавали автомобили более высокого класса или стоимости.
# 
#     - По маркам: 
#     
# 'Mercur Auto' является единственным представителем марок Audi, Porsche и Volkswagen на рынке. Это дает им уникальное конкурентное преимущество в этих категориях.
# 
#     - По классам: 
#     
# 'Mercur Auto' занимает лидирующие позиции в классе F (39.05%), полноразмерных минивэнах (18.41%) и спортивных автомобилях (84.04%). Это подтверждает их присутствие в премиум-сегменте.
# 
# **Рекомендации:**
# 
#     - По классам:
#         
#         - F класс: Учитывая высокую долю рынка в 39.05%, Mercur Auto должна продолжать активное продвижение и укрепление своего положения в этом классе.
# 
#         - Полноразмерный минивэн: С долей рынка 18.41% следует рассмотреть возможность увеличения ассортимента и предложений в этой категории.
# 
#         - Спортивные автомобили: Огромная доля рынка в 84.04% указывает на доминирование компании в этом сегменте. Необходимо сохранить этот статус и возможно расширить ассортимент или предложить специальные акции.
# 
#     - По городам:
# 
#         - Алматы: Учитывая его статус крупнейшего города и экономического центра страны, Mercur Auto должна активизировать свои усилия в этом регионе. Возможно, учитывая спрос на премиум-сегмент, стоит расширить присутствие в городе.
#         - Астана (Нур-Султан): Как столица страны, Астана представляет собой еще один важный регион для укрепления присутствия.
#         - Шымкент и другие крупные города: Предложить пробные поездки или провести рекламные кампании, чтобы привлечь больше клиентов из этих регионов.
#         
#     - Маркетинговые усилия: Рассмотреть возможность усилить рекламные кампании в регионах с меньшими продажами, а также провести исследование потребительских предпочтений в этих регионах.
# 
#     - Анализ конкурентов: Важно учитывать действия ключевых конкурентов, таких как 'Toyota Motor Kazakhstan' и 'Astana Motors', чтобы определить возможные стратегические шаги для увеличения доли рынка "mercur auto".
# 
#     Учитывая вышеуказанные выводы и рекомендации, Mercur Auto имеет все шансы на успешное развитие на рынке. С учетом их уникального присутствия в определенных марках и классах автомобилей, важно сосредоточить усилия на сохранении этих позиций, а также на расширении присутствия в стратегически важных регионах.
