Telegram Bot для Уведомлений Google Таблиц

Этот проект включает в себя создание бота Telegram, который отправляет уведомления при изменении данных в определенном листе Google Таблицы. Бот предназначен для уведомления пользователей о важных обновлениях в реальном времени.
Особенности

    Автоматическая отправка уведомлений в Telegram при изменении данных.
    Настройка для специфического листа в Google Таблице.
    Уведомления включают информацию о строке, столбце и измененных данных.

Настройка
Шаг 1: Создание Telegram-бота

    Воспользуйтесь BotFather в Telegram для создания нового бота.
    Следуйте инструкциям BotFather для создания бота и получите токен вашего бота.

Шаг 2: Настройка Google Таблицы

    Откройте Google Таблицу, в которой необходимо отслеживать изменения.
    Перейдите в "Инструменты" -> "Редактор скриптов".

Шаг 3: Кодирование Скрипта

    Напишите скрипт на языке Google Apps Script для отслеживания изменений и отправки уведомлений в Telegram.

    Используйте следующий код как основу:

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



function sendTelegramMessage(message) {
  var token = 'ВАШ_ТОКЕН'; 
  var chatIds = [chatid пользователей];//у меня несколько пользователей 

  chatIds.forEach(function(chatId) {
    var url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chatId + '&text=' + encodeURIComponent(message);
    var options = {
      'method': 'get',
      'muteHttpExceptions': true
    };
    UrlFetchApp.fetch(url, options);
  });
}


Шаг 4: Настройка Триггера

    Настройте триггер в редакторе скриптов, чтобы функция trackChanges запускалась при каждом изменении данных в таблице.

Шаг 5: Тестирование

    Внесите изменения в соответствующий лист Google Таблицы.
    Убедитесь, что уведомления приходят в Telegram.

Использование

Для использования бота:

    Пользователи должны начать диалог с ботом в Telegram.
    После активации бота, уведомления будут автоматически отправляться при изменениях в таблице.
