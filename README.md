## Инструкция по запуску автотестов
### **Требования**
1. Для запуска проекта требуется: 

  - Python 3.7 или выше.
  - Google Chrome последней версии

2. Склонировать репозиторий:
```
git clone https://github.com/Luinerr/AvitoAutoTestCase.git
```
3. В папке проекта установить виртуальное окружение
```
python -m venv venv
```
```
source venv/Script/activate
```
4. Устновить pytest/playwright
```
pip install pytest-playwright
playwright install
```
5. Запустить тесты
```
pytest tests.py
```
