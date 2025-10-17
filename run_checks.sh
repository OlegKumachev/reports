#!/bin/bash

# Проверка форматирования
black --check .

# Линтинг
flake8 . --exclude .venv

# Запуск тестов
python -m pytest --cov
