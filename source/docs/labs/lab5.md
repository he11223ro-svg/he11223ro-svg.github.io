\# Отчет по лабораторной работе №5



\*\*Тема:\*\* Регрессия с применением Scikit-Learn (Predict House Price)  

\*\*Выполнил:\*\* Альшухайед Рами



\---



\## 1. Цель работы

Освоение методов регрессии с использованием библиотеки \*\*Scikit-Learn\*\*, проведение сравнительного анализа алгоритмов прогнозирования непрерывных значений (Linear Regression, Ridge, Lasso, SVR, Gradient Boosting, Random Forest), а также исследование способов оптимизации гиперпараметров для снижения ошибки предсказания.



\---



\## 2. Ссылка на Google Colab

Полный рабочий ноутбук с исходным кодом и результатами экспериментов:  

👉 \*\*\[Открыть Google Colab: Predict House Price Tasks](https://colab.research.google.com/drive/1jU0Yj5oBnMaM-Kraq4V6uZtWl9lsN2ib?usp=sharing)\*\* \*(доступ открыт по ссылке)\*



\---



\## 3. Результаты экспериментов и сравнение моделей



В ходе выполнения самостоятельной работы были обучены и протестированы различные модели регрессии на датасете `California Housing` с предварительным масштабированием признаков (`StandardScaler`):



| Модель | MSE | RMSE | R2-Score |

| :--- | :---: | :---: | :---: |

| \*\*Linear Regression\*\* | 0.555 | 0.745 | 0.575 |

| \*\*Ridge Regression\*\* | 0.555 | 0.745 | 0.575 |

| \*\*Lasso Regression\*\* | 0.887 | 0.942 | -0.001 |

| \*\*Support Vector Regressor (SVR)\*\* | 0.354 | 0.595 | 0.730 |

| \*\*Gradient Boosting\*\* | 0.239 | 0.489 | 0.817 |

| \*\*Random Forest (Tuned)\*\* | \*\*0.205\*\* | \*\*0.453\*\* | \*\*0.844\*\* |



\### Анализ результатов и тюнинг Random Forest:

Оптимизация гиперпараметров ансамблевого алгоритма \*\*Random Forest Regressor\*\* (увеличение числа деревьев `n\_estimators=150` и ограничение глубины `max\_depth=15`) позволила добиться наименьшей среднеквадратичной ошибки (\*\*RMSE = 0.453\*\*) и высокого коэффициента детерминации (\*\*R2 = 0.844\*\*), что превосходит базовые линейные модели.



\---



\## 4. Обзор современных алгоритмов регрессии

На основе анализа передовых практик Machine Learning:

1\. \*\*Gradient Boosting Frameworks:\*\* Ансамбли \*\*CatBoost\*\*, \*\*LightGBM\*\* и \*\*XGBoost\*\* демонстрируют исключительную производительность и точность на структурированных и регрессионных задачах.

2\. \*\*Neural Networks for Regression:\*\* Полносвязные нейронные сети с правильной регуляризацией (Dropout, Batch Normalization) успешно применяются для сложных нелинейных зависимостей.



\---



\## 5. Пошаговый алгоритм интеграции регрессионной модели с веб-сервисом (FastAPI)



1\. \*\*Сохранение обученной модели:\*\*

&#x20;  ```python

&#x20;  import joblib

&#x20;  joblib.dump(model, 'house\_price\_model.pkl')

2\. \*\*Создание REST API (FastAPI):\*\*

&#x20;  ```python

&#x20;  from fastapi import FastAPI

&#x20;  import joblib

&#x20;  import numpy as np



&#x20;  app = FastAPI()

&#x20;  model = joblib.load('house\_price\_model.pkl')



&#x20;  @app.post("/predict\_price")

&#x20;  def predict\_price(features: list):

&#x20;      data = np.array(features).reshape(1, -1)

&#x20;      predicted\_price = model.predict(data)

&#x20;      return {"estimated\_price": float(predicted\_price\[0])}

3\. \*\*Контейнеризация:\*\* Упаковка приложения в `Dockerfile`.



4\. \*\*Развертывание (Deployment):\*\* Деплой сервиса на облачную платформу для удаленного доступа.


