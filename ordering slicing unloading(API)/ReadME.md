<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
   
</head>
<body>
    <h1>Проект обработки и отправки данных по API</h1>
    <p>Этот проект предназначен для обработки баз сырых строк в рамках заказа, их нарезки, отправки по API коллегам, а также сохранения остатков баз и передачи информации по остаткам строк по регионам в Google Таблицы.</p>

  <h2>Используемые библиотеки</h2>
    <ul>
        <li>pandas</li>
        <li>numpy</li>
        <li>my_func (собственный модуль)</li>
        <li>chardet</li>
        <li>datetime</li>
        <li>glob</li>
        <li>os</li>
        <li>googleapiclient</li>
        <li>google.oauth2</li>
        <li>re</li>
        <li>telegram</li>
        <li>asyncio</li>
        <li>aiohttp</li>
        <li>aiofiles</li>
        <li>base64</li>
        <li>json</li>
        <li>logging</li>
    </ul>

  <h2>Основные функции</h2>
    <p>Основные функции проекта включают:</p>
    <ul>
        <li><strong>upload_rest_data(data_name, dates, base_dir)</strong>: Загрузка данных по остаткам баз</li>
        <li><strong>google_sheets_service()</strong>: Инициализация сервиса Google Sheets</li>
        <li><strong>upload_to_google_sheets(data, spreadsheet_id, range_name)</strong>: Загрузка данных в Google Sheets</li>
        <li><strong>send_document(chat_id, document, caption)</strong>: Отправка документов через Telegram</li>
        <li><strong>get_region_data(region_name)</strong>: Получение данных по региону</li>
        <li><strong>send_data_to_server(region_id, limit, data, encoded_token)</strong>: Отправка данных на сервер по API</li>
        <li><strong>main(df_zakaz_region, container, encoded_token)</strong>: Основная функция обработки и отправки данных</li>
        <li><strong>clear_google_sheets(spreadsheet_id, sheet_name)</strong>: Очистка данных на листе Google Sheets</li>
        <li><strong>save_data_and_counts(dataset, name, current_date)</strong>: Сохранение данных и подсчет строк по регионам</li>
    </ul>

  <h2>Описание основных функций</h2>
    <h3>upload_rest_data</h3>
    <p>Эта функция загружает данные по остаткам баз из файла CSV, который находится в указанной директории и соответствует последней доступной дате.</p>

  <h3>google_sheets_service</h3>
    <p>Инициализирует и возвращает объект сервиса Google Sheets, используя учетные данные из файла.</p>

  <h3>upload_to_google_sheets</h3>
    <p>Загружает данные в указанный диапазон Google Sheets, предварительно очистив данные на листе.</p>

  <h3>send_document</h3>
    <p>Асинхронная функция для отправки документов через Telegram бот.</p>

  <h3>get_region_data</h3>
    <p>Получает данные по региону из DataFrame заказов по регионам.</p>

  <h3>send_data_to_server</h3>
    <p>Асинхронная функция для отправки данных на сервер по API с использованием библиотеки aiohttp.</p>

   <h3>main</h3>
    <p>Основная функция, которая выполняет обработку и отправку данных по регионам, а также отправку файлов через Telegram бот.</p>

   <h3>clear_google_sheets</h3>
    <p>Очищает указанный лист в Google Sheets перед загрузкой новых данных.</p>

   <h3>save_data_and_counts</h3>
    <p>Сохраняет остатки баз в формате CSV, подсчитывает количество строк по регионам и сохраняет их в Excel, а также загружает данные в Google Sheets.</p>

   <h2>Пример использования</h2>
    <p>Основной скрипт запускается с помощью asyncio:</p>
    <pre>
        <code>
if __name__ == '__main__':
    loop = asyncio.get_event_loop()

   ### Проверяем, запущен ли уже цикл событий
   if loop.is_running():
        loop.create_task(main(df_zakaz_region, container, encoded_token))
    else:
        loop.run_until_complete(main(df_zakaz_region, container, encoded_token))
        </code>
    </pre>
    
<h2>Для получения более детальной информации, пожалуйста, ознакомьтесь с кодом в репозитории.</h2>
    <p><a href="https://github.com/OophionN/PySQLPlayground-pet-projects-/blob/main/parser/parser.py">Основной скрипт для запуска </a></p>
</body>
</html>
