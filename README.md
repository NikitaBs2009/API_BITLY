# Обрезка ссылок с помощью Битли

 Код обрезает ссылки с помощью Битли и счетает клики 

### Как установить

Ключ  апи битли токен можно получить в личном кабинете  "APY_BITLY"  он выглядет как огромный набор букв и цифр

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

Затем в  скрипте нужно создать файл `".env"` и записать в него токен. `API_BITLY_TOKEN=Ваш_токен`

Для использования скрипта нужно ввести:
```
python main.py (ваша ссылка)
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).