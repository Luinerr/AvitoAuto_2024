
Запрос https://www.avito.ru/web/1/charity/ecoImpact/init

Тело для подмены ответов
```
{
    "result": {
        "blocks": {
            "personalImpact": {
                "avatarUrl": "https://i.pinimg.com/originals/e8/8f/30/e88f3028afe762960b7a2c11837b34d1.jpg",
                "data": {
                    "co2": 0,
                    "energy": 0,
                    "materials": 0,
                    "pineYears": 0,
                    "water": 0
                }
            }
        },
        "isAuthorized": true
    },
    "status": "ok"
}
```


1-AB. Не склоняется слово Тонн для датчика CO2

Шаги:

1. Перейти на страницу https://www.avito.ru/avito-care/eco-impact
2. Подменить ответ для co2 на 1000

ФР: Отображается слово Тонн

ОР: Отображается слово Тонна

Приоритет: Низкий

![image](https://github.com/Luinerr/AvitoAuto_2024/assets/43450488/4c157d0b-f996-4d2c-93f3-e51bacddfc1d)




2-AB. Для счетчика энергии при отображении млн перекрывается текст

Шаги:

1. Перейти на страницу https://www.avito.ru/avito-care/eco-impact
2. Подменить ответ для energy на 1000000

ФР: Текст съезжает и перекрывает другой текст

ОР: Текст не перекрывается

Приоритет: Низкий

![image](https://github.com/Luinerr/AvitoAuto_2024/assets/43450488/925c6aa2-c505-4056-a4a6-77c9184164df)


3-AB. Отсутствует валидация ответа от сервера микрофронтэндом

Шаги:

1. Перейти на страницу https://www.avito.ru/avito-care/eco-impact
2. Подменить ответ для счетчиков на -1

ФР: Отображается отрицательное значение для счетчика

ОР: Отображается 0 для счетчиков

Приоритет: Низкий





