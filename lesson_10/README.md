# Проект автотестов с Page Object Pattern и Allure

Проект содержит автотесты для веб-приложений 
с использованием паттерна Page Object.

## Структура проекта

- `login_page_07.py` - Page Object для страницы авторизации
- `main_page_07.py` - Page Object для главной страницы магазина
- `cart_page_07.py` - Page Object для страницы корзины
- `checkout_page_07.py` - Page Object для страницы оформления заказа
- `calculator_page.py` - Page Object для страницы калькулятора
- `test_shopping_cart.py` - Тесты для корзины покупок
- `test_calculator.py` - Тесты для калькулятора

## Запустить тесты для формирования отчета:
pytest --alluredir=allure-results

## Просмотреть сформированный отчет:
allure serve allure-results

## Установка зависимостей

```bash
pip install -r requirements.txt


