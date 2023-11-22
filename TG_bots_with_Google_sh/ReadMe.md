<html>
<head>
    <title>Telegram Bot для Уведомлений Google Таблиц</title>
</head>
<body>
    <h1>Telegram Bot для Уведомлений Google Таблиц</h1>
    <p>Этот проект включает в себя создание бота Telegram, который отправляет уведомления при изменении данных в определенном листе Google Таблицы. Бот предназначен для уведомления пользователей о важных обновлениях в реальном времени.</p>

    <h2>Особенности</h2>
    <ul>
        <li>Автоматическая отправка уведомлений в Telegram при изменении данных.</li>
        <li>Настройка для специфического листа в Google Таблице.</li>
        <li>Уведомления включают информацию о строке, столбце и измененных данных.</li>
    </ul>

    <h2>Настройка</h2>
    <h3>Шаг 1: Создание Telegram-бота</h3>
    <ol>
        <li>Воспользуйтесь <a href="https://t.me/botfather">BotFather</a> в Telegram для создания нового бота.</li>
        <li>Следуйте инструкциям BotFather для создания бота и получите токен вашего бота.</li>
    </ol>

    <h3>Шаг 2: Настройка Google Таблицы</h3>
    <ol>
        <li>Откройте Google Таблицу, в которой необходимо отслеживать изменения.</li>
        <li>Перейдите в "Инструменты" -> "Редактор скриптов".</li>
    </ol>

    <h3>Шаг 3: Кодирование Скрипта</h3>
    <p>Напишите скрипт на языке Google Apps Script для отслеживания изменений и отправки уведомлений в Telegram. Используйте следующий код как основу:</p>
    <pre>
        <code>
        // Код функции для отслеживания изменений
function trackChanges() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = spreadsheet.getSheetByName("Матрица Ноябрь 23г.");
  if (!sheet) {
    console.log("Лист 'Матрица Ноябрь 23г' не найден");
    return;
  }

  var range = sheet.getActiveRange();
  var row = range.getRow();
  var column = range.getColumn();
  var columnHeader = sheet.getRange(1, column).getValue(); // Получение значения из первой строки столбца
  var changedValue = range.getValue(); // Получение значения измененной ячейки

  var message = 'Изменение в "Матрица Ноябрь 23г", строка: ' + row + ', столбец: ' + columnHeader + ', новое значение: ' + changedValue;
  sendTelegramMessage(message);
}


  // Код функции для отправки сообщений в Telegram
function sendTelegramMessage(message) {
  var token = 'ВАШ_ТОКЕН'; 
  var chatIds = [ВАШИ CHATID, у меня несколько пользователей];

  chatIds.forEach(function(chatId) {
    var url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chatId + '&text=' + encodeURIComponent(message);
    var options = {
      'method': 'get',
      'muteHttpExceptions': true
    };
    UrlFetchApp.fetch(url, options);
  });
}


        </code>
    </pre>

    <h3>Шаг 4: Настройка Триггера</h3>
    <ol>
        <li>Настройте триггер в редакторе скриптов, чтобы функция <code>trackChanges</code> запускалась при каждом изменении данных в таблице.</li>
    </ol>

    <h3>Шаг 5: Тестирование</h3>
    <ol>
        <li>Внесите изменения в соответствующий лист Google Таблицы.</li>
        <li>Убедитесь, что уведомления приходят в Telegram.</li>
    </ol>

    <h2>Использование</h2>
    <p>Для использования бота:</p>
    <ol>
        <li>Пользователи должны начать диалог с ботом в Telegram.</li>
        <li>После активации бота, уведомления будут автоматически отправляться при изменениях в таблице.</li>
    </ol>
</body>
</html>
