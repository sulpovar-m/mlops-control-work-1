# MLOps. Контрольная работа №1

Прогноз отмены бронирования отеля. Python 3.12.

- **46:** `train.ipynb`, выполненный ноутбук с анализом данных, сравнением моделей и оценкой на тесте.
- **47:** `Dockerfile`, `predict.py` и готовая модель `model.joblib`.
- **48:** раздел 4 ноутбука, эксперименты и логирование параметров, метрик и моделей в MLflow. Итоговые метрики и порог сохраняются в разделе 7.

Данные: [Hotel Booking Demand, Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand). CSV включён в проект. Источник: N. Antonio, A. de Almeida, L. Nunes, [Hotel booking demand datasets](https://doi.org/10.1016/j.dib.2018.11.126), 2019, CC BY 4.0.

## Повторный запуск

Из папки проекта:

```bash
pip install -r requirements.txt
pip install notebook
jupyter notebook train.ipynb
```

Выполнить все ячейки. Результаты уже сохранены в ноутбуке. Локальная база MLflow создаётся при повторном запуске:

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Интерфейс: http://127.0.0.1:5000.

## Контейнер

```bash
docker build -t hotel-cancellations .
docker run --rm hotel-cancellations
```

Вывод: вероятность отмены и класс для пяти строк `example.csv`. Для своего CSV с такими же колонками:

```bash
docker run --rm -v "$(pwd)/bookings.csv:/app/bookings.csv" hotel-cancellations bookings.csv
```
