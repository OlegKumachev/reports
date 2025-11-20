# Анализ эффективности работы разработчиков

Скрипт для анализа эффективности работы разработчиков и формирования отчета. 
## Установка и запуск

1. **Клонируйте репозиторий**:

    ```bash
    git clone git@github.com:OlegKumachev/reports.git
    ```

2. **Установка зависимостей**:

    ```bash
    uv sync
    ```

4. **Запуск приложения**:

    ```bash
    uv run reports --files employees1.csv employees2.csv --report performance

5. **Пример вывода отчета**

 ![Пример запуска скрипта](/report.png)