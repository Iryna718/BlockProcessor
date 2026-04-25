# Проєкт BlockProcessor (Лабораторні роботи 2-6)

Проєкт присвячений розробці системи обробки даних (блоків та голосів) з використанням механізмів валідації та збереженням у реляційну базу даних.

## Структура проєкту

Відповідно до завдань лабораторних робіт 2-6, проєкт складається з наступних компонентів:

* **SQL Backend (Labs 2-4)**:
    * Використання SQLite для зберігання структурованих даних.
    * Реалізація схем таблиць `Blocks` та `Votes`.
    * Скрипти для імпорту та оновлення даних із CSV-файлів.
* **Object Model (Lab 5)**:
    * Опис бізнес-логіки проєкту через класи Python.
    * Перехід від сирих даних до об'єктного представлення сутностей.
* **Validation & Testing (Lab 6)**:
    * `models.py` — реалізація моделей даних на базі бібліотеки Pydantic. Включає перевірку типів, використання регулярних виразів для IP-адрес та ідентифікаторів, а також контроль числових діапазонів.
    * `test_lab6.py` — набір автоматизованих тестів Pytest для верифікації моделей та перевірки коректної обробки помилок (ValidationError).

## Технологічний стек
* Мова програмування: Python 3.13
* Бібліотека валідації: Pydantic
* Фреймворк для тестування: Pytest
* Система керування базами даних: SQLite3

## Діаграма процесу обробки даних

Схема взаємодії компонентів проєкту:

```mermaid
graph TD
    subgraph Input [Вхідні дані]
        CSV[CSV Files] --> Stream[Data Stream]
    end

    subgraph Validation [Валідація Pydantic]
        Stream --> ModelCheck{Перевірка моделей}
        ModelCheck -- Valid --> CleanData[Валідовані дані]
        ModelCheck -- Invalid --> Error[ValidationError]
    end

    subgraph Storage [Persistence Layer]
        CleanData --> DB[(SQLite DB)]
        DB --> T1[Table: Blocks]
        DB --> T2[Table: Votes]
    end

    subgraph QA [Quality Assurance]
        DB -.-> Tests[Pytest Suite]
        Tests --> Summary[7 Passed]
    end