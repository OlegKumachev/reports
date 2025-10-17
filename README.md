# Система учёта работников компании

Скрипт для анализа рейтингов товаров по брендам из CSV-файлов. Формирует отчёт **average-rating**, выводит средний рейтинг каждого бренда и сортирует бренды по рейтингу.

## Установка и запуск

1. **Клонируйте репозиторий**:

    ```bash
    git clone git@github.com:OlegKumachev/kiout-test-backend.git
    ```

2. **Установка зависимостей**:

    ```bash
    poetry install
    ```

4. **Запуск приложения**:

    ```bash
    poetry run python main.py --files product1.csv product2.csv --report average-rating.

5. **Пример вывода отчета**

 ![Пример запуска скрипта](/screenshot.png)
