"""
Лабораторная работа 2: Численные вычисления и анализ данных с использованием NumPy.

Выполнение базовых и матричных операций, статистический анализ
и визуализация данных.
"""

import os
from typing import Dict, Union
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# ============================================================
# 1. СОЗДАНИЕ И ОБРАБОТКА МАССИВОВ
# ============================================================

def create_vector() -> np.ndarray:
    """Создает массив от 0 до 9 включительно."""
    return np.arange(10)


def create_matrix() -> np.ndarray:
    """Создает матрицу 5x5 со случайными числами в интервале [0, 1)."""
    return np.random.rand(5, 5)


def reshape_vector(vec: np.ndarray) -> np.ndarray:
    """Преобразует вектор формы (10,) в матрицу формы (2, 5)."""
    return vec.reshape(2, 5)


def transpose_matrix(mat: np.ndarray) -> np.ndarray:
    """Транспонирует входную матрицу."""
    return mat.T


# ============================================================
# 2. ВЕКТОРНЫЕ ОПЕРАЦИИ
# ============================================================

def vector_add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Выполняет поэлементное сложение двух векторов одинаковой длины."""
    return a + b


def scalar_multiply(vec: np.ndarray, scalar: Union[int, float]) -> np.ndarray:
    """Умножает вектор на скалярное число."""
    return vec * scalar


def elementwise_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Выполняет поэлементное умножение массивов."""
    return a * b


def dot_product(a: np.ndarray, b: np.ndarray) -> Union[int, float, np.number]:
    """Вычисляет скалярное произведение двух векторов."""
    return np.dot(a, b)


# ============================================================
# 3. МАТРИЧНЫЕ ОПЕРАЦИИ
# ============================================================

def matrix_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Выполняет матричное умножение."""
    return a @ b


def matrix_determinant(a: np.ndarray) -> float:
    """Вычисляет определитель квадратной матрицы."""
    return float(np.linalg.det(a))


def matrix_inverse(a: np.ndarray) -> np.ndarray:
    """Вычисляет обратную матрицу."""
    return np.linalg.inv(a)


def solve_linear_system(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Решает систему линейных алгебраических уравнений Ax = b."""
    return np.linalg.solve(a, b)


# ============================================================
# 4. СТАТИСТИЧЕСКИЙ АНАЛИЗ
# ============================================================

def load_dataset(path: str = "data/students_scores.csv") -> np.ndarray:
    """Загружает CSV-файл с данными и возвращает NumPy массив."""
    df = pd.read_csv(path)
    return df.to_numpy()


def statistical_analysis(data: np.ndarray) -> Dict[str, float]:
    """Рассчитывает основные статистические показатели для одномерного массива."""
    return {
        "mean": float(np.mean(data)),
        "median": float(np.median(data)),
        "std": float(np.std(data)),
        "min": float(np.min(data)),
        "max": float(np.max(data)),
        "percentile_25": float(np.percentile(data, 25)),
        "percentile_75": float(np.percentile(data, 75))
    }


def normalize_data(data: np.ndarray) -> np.ndarray:
    """Выполняет Min-Max нормализацию массива в диапазон [0, 1]."""
    min_val = np.min(data)
    max_val = np.max(data)
    if max_val == min_val:
        return np.zeros_like(data, dtype=float)
    return (data - min_val) / (max_val - min_val)


# ============================================================
# 5. ВИЗУАЛИЗАЦИЯ
# ============================================================

def plot_histogram(data: np.ndarray, save_path: str = "plots/histogram.png") -> None:
    """Строит и сохраняет гистограмму распределения оценок."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=10, color='skyblue', edgecolor='black')
    plt.title("Распределение оценок по математике")
    plt.xlabel("Баллы")
    plt.ylabel("Количество студентов")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig(save_path)
    plt.close()


def plot_heatmap(matrix: np.ndarray, save_path: str = "plots/heatmap.png") -> None:
    """Строит и сохраняет тепловую карту корреляции."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Тепловая карта корреляции")
    plt.savefig(save_path)
    plt.close()


def plot_line(x: np.ndarray, y: np.ndarray, save_path: str = "plots/line_plot.png") -> None:
    """Строит и сохраняет линейный график зависимости."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title("Зависимость: студент -> оценка по математике")
    plt.xlabel("Номер студента")
    plt.ylabel("Оценка")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig(save_path)
    plt.close()