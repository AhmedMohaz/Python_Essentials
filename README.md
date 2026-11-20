# BIT 2118 Scientific Computing 

This repository contains a cleaned, consolidated implementation of the scientific-computing work in the supplied report. The Python source includes the numerical method, parameter-sensitivity, real-world adaptation, and visualization work .



## Files

- [`BIT2118_Python_Codes_Tasks_01_to_20.py`](BIT2118_Python_Codes_Tasks_01_to_20.py) — one executable Python source file with explicit `TASK 01` through `TASK 20` section labels.

- `graphs/` — created automatically when the Python file is run; it contains PNG figures for the numerical results.



## Setup and execution

Python 3.9 or later is recommended. Install the dependencies:

```bash
python -m pip install numpy scipy matplotlib
```

Run all tasks from the directory containing the Python file:

```bash
python BIT2118_Python_Codes_Tasks_01_to_20.py
```

The program prints representative numerical results and writes graph files to graphs. The script uses a fixed random seed where random simulation is required, so the Monte Carlo result is reproducible.

## Actual graph images

The following figures are the actual generated PNG files. Every PNG currently produced by the Python file is included below.
### Tasks 1–5

![Task 1: hourly temperature](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzAxX3RlbXBlcmF0dXJl.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekF4WDNSbGJYQmxjbUYwZFhKbC5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTcyOTI4MDB9fX1dfQ__&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIQCz0Ah3N~rFxWDjKIuIE-pPfohDgdiSXOEtaA9q2OP-LAIgTGkfr7Yfj6urUIdcsQ-1YLy0TPT8JYst2AAk~NNwUrM_)

![Task 2: vectorization benchmark](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzAyX3ZlY3Rvcml6YXRpb24.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekF5WDNabFkzUnZjbWw2WVhScGIyNC5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTcyOTI4MDB9fX1dfQ__&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIQDgZQJpqa101yLr6tOluh2uutmB68Wf91xKb8Z8HoiqNwIgKw5rcS9h~FfGYFJxuFt3Zd63jPxjFu2psq4SNGfFpfk_)

![Task 4: matrix transformation](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzA0X21hdHJpeF90cmFuc2Zvcm0.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekEwWDIxaGRISnBlRjkwY21GdWMyWnZjbTAucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk3MjkyODAwfX19XX0_&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEQCIBGo0GExQRF9lQjOo7AXVGtlbtWpFxgaVutDU9n480-FAiBRVwEb6pq4t8Xlh1DkIEl62WdFxjUAqS5ZnNZKNrh22A__)

![Task 5: quadratic curve fit](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzA1X2N1cnZlX2ZpdA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekExWDJOMWNuWmxYMlpwZEEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk3MjkyODAwfX19XX0_&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIQCtXDPrimPn2jC02PSHYcsBrgwFGYccK6hmXMmV-IesNQIgZ~w7WuTduv4kj~93Y5AeiTEwUZogk9SjlSQFqO942Gs_)

### Tasks 8–12

![Task 8: iterative convergence](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzA4X2l0ZXJhdGl2ZV9jb252ZXJnZW5jZQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekE0WDJsMFpYSmhkR2wyWlY5amIyNTJaWEpuWlc1alpRLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5NzI5MjgwMH19fV19&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEQCIEyMD8Z1UDAt1cjVASvRyQvsXxlI6gXbdcXwMNWZqRypAiBi0cayEny~hCm86bRtslMHBLE5p0YNE9xBBs5q6o8UUw__)

![Task 9: eigenvector scores](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzA5X2VpZ2VuX3Njb3Jlcw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekE1WDJWcFoyVnVYM05qYjNKbGN3LnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5NzI5MjgwMH19fV19&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEMCIF4syG8AHnCy37bYqEjOf6lOWlZmj4HLB9yl-h0OwJ2OAh9OrezVGPL6mjKBGCxNUkHV~jcntmOjpPSl3rPZl20t)

![Task 10: bisection root](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzEwX2Jpc2VjdGlvbl9yb290.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekV3WDJKcGMyVmpkR2x2Ymw5eWIyOTAucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk3MjkyODAwfX19XX0_&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIQDxwJVGezBrlTi~4l-bKH2TyM9sWTrHz3AdTJDC6ihuMgIgH-7D3sN99tsyamYLKOwa7arkkPukfcz8Aro8i8xXKQ8_)

![Task 11: IRR and NPV](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzExX2lycl9ucHY.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekV4WDJseWNsOXVjSFkucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk3MjkyODAwfX19XX0_&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIQDjBGeI1RItdYUfPbLr-OB224D8f8eq3~eoxN1E-IcWggIgfUa6fGJ~RKerr7uPeBhZe63ivEzsrYr~VrrY4yX~SGE_)

![Task 12: nonlinear-system intersections](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzEyX25vbmxpbmVhcl9zeXN0ZW0.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekV5WDI1dmJteHBibVZoY2w5emVYTjBaVzAucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk3MjkyODAwfX19XX0_&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIQDQ1JkhfYNkgGsVMSwo0ZQwneMNbcvjWi1TTidnzhHjMgIgcPUtBpmSEzAut~BMjA6W~r2cZleWlMVrwK8-CcUQP0A_)

### Tasks 13–20

![Task 13: interpolation](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzEzX2ludGVycG9sYXRpb24.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekV6WDJsdWRHVnljRzlzWVhScGIyNC5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTcyOTI4MDB9fX1dfQ__&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIQDX~oiYsA1-viY4BemwKxvcNTFmDDw6ersIjayF2XHsbgIgV-L3oVgIngALLJw7s13uuQge1pNXsb5sPpAR1lS2Xis_)

![Task 14: numerical differentiation](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzE0X2RpZmZlcmVudGlhdGlvbg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekUwWDJScFptWmxjbVZ1ZEdsaGRHbHZiZy5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTcyOTI4MDB9fX1dfQ__&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEQCIGxfjsvoB9642XmB6YVYlpfnu-BErjvDgamqt8fF7tAIAiAC1Lk3ERbfNgv9WQdF6AqHRBwfnpAiE8zIh81Uq-ZhQg__)

![Task 15: numerical integration](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzE1X2ludGVncmF0aW9u.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekUxWDJsdWRHVm5jbUYwYVc5dS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTcyOTI4MDB9fX1dfQ__&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIQCztaikWqUKJ8fuGE2mEOA3OAfI3IQR9MSIL~L10SQF-AIgczBCYNKg7663wka8wUVgX1V3LFAY59KryQGrotBzUN4_)

![Task 16: Euler cooling](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzE2X2V1bGVyX2Nvb2xpbmc.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekUyWDJWMWJHVnlYMk52YjJ4cGJtYy5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTcyOTI4MDB9fX1dfQ__&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEQCIDjOkF1nyHPgGW16lB~eCDbIEvqwTDz41JNi5lEsiucSAiAzjqRGYVqkPC1Du2tAFKb6fQT8NFqhwiChKNL5FLvl3Q__)

![Task 18: SciPy RC-circuit integration](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzE3X3NjaXB5X3Jj.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekUzWDNOamFYQjVYM0pqLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5NzI5MjgwMH19fV19&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIQCBaT86AnsuwM7sPL43ujpaixceXuC85Z9vIlULVcvWaAIgegrDxx8frhTqxvc61COSLROaNFuqHfXIZ-9j-dMqxB4_)

![Task 19: optimization](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzE4X29wdGltaXphdGlvbg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekU0WDI5d2RHbHRhWHBoZEdsdmJnLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5NzI5MjgwMH19fV19&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIQDEZQu8LkYJ7-fD7AGAWxjyb8dZxTIrz9q5FcK3NGBstQIgBpSAJ6yqto0JZPMmiScN6lIWHfQMu9bZ9etLdAv9QOo_)

![Task 20: Monte Carlo risk](https://private-us-east-1.manuscdn.com/sessionFile/zHRHKqgdj0VQRVkVX4B47m/sandbox/8xjZBpqFnGp8gHcVoth2tx-images_1795205859858_na1fn_L2hvbWUvdWJ1bnR1L2dyYXBocy90YXNrXzE5X21vbnRlX2Nhcmxv.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvekhSSEtxZ2RqMFZRUlZrVlg0QjQ3bS9zYW5kYm94Lzh4alpCcHFGbkdwOGdIY1ZvdGgydHgtaW1hZ2VzXzE3OTUyMDU4NTk4NThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZHlZWEJvY3k5MFlYTnJYekU1WDIxdmJuUmxYMk5oY214di5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTcyOTI4MDB9fX1dfQ__&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEQCIF7UhMII1egZFMqDShkinCuUhwV7f6BaBy6VRgm9yw8oAiA6ZeFmlMh9u9bDHQvTKnD6HH4rd4YHNOghuYGjoiiIAg__)

## Task overview

| Task | Topic | Main operation | Generated graph |
| --- | --- | --- | --- |
| 1 | NumPy temperature arrays | Mean, extrema, Celsius-to-Fahrenheit transformation | `task_01_temperature.png` |
| 2 | Vectorization | Millisecond scaling and squared latency; loop benchmark | `task_02_vectorization.png` |
| 3 | Floating-point arithmetic | Equality, tolerance, absolute and relative error | — |
| 4 | Matrix algebra | Rotation, scaling, determinant, transformed coordinates | `task_04_matrix_transform.png` |
| 5 | Curve fitting | Quadratic least-squares response-time model | `task_05_curve_fit.png` |
| 6 | Linear systems | Solve `Ax=b` and residual verification | — |
| 7 | LU decomposition | Factor once and solve multiple right-hand sides | — |
| 8 | Iterative linear methods | Jacobi and Gauss–Seidel convergence | `task_08_iterative_convergence.png` |
| 9 | Eigenvalues and eigenvectors | Network-node importance scores | `task_09_eigen_scores.png` |
| 10 | Bisection and fixed point | Thermal equilibrium root | `task_10_bisection_root.png` |
| 11 | Newton–Raphson and secant | Investment IRR from NPV = 0 | `task_11_irr_npv.png` |
| 12 | Nonlinear systems | Circle/parabola intersections | `task_12_nonlinear_system.png` |
| 13 | Interpolation | Linear and cubic-spline temperature estimate | `task_13_interpolation.png` |
| 14 | Numerical differentiation | GPS position to speed | `task_14_differentiation.png` |
| 15 | Numerical integration | Power to energy using trapezoid and Simpson rules | `task_15_integration.png` |
| 16 | Euler’s method | Newton’s law of cooling | `task_16_euler_cooling.png` |
| 17 | Reserved report transition | Included in the consolidated ODE workflow | — |
| 18 | SciPy ODE integration | RC-circuit capacitor charging using `solve_ivp` | `task_17_scipy_rc.png` |
| 19 | Optimization | Continuous SLSQP and integer fleet allocation | `task_18_optimization.png` |
| 20 | Monte Carlo simulation | Construction-project budget-overrun probability | `task_19_monte_carlo.png` |

The original report presents Tasks 17 and 18 as the Euler and SciPy ODE sections. The source code keeps those methods in the same order; graph filenames are retained from the report-oriented implementation.

## Mathematical methods and interpretations

### Tasks 1–5: arrays, arithmetic, matrices, and fitting

Task 1 uses 24 hourly Celsius readings. The reproducible mean is approximately **23.1208 °C**, with a minimum of **17.50 °C** and a maximum of **29.40 °C**. Increasing the peak reading at index 12 to 35 °C raises the mean to approximately **23.3542 °C** while leaving the minimum unchanged. The Fahrenheit conversion is vectorized and preserves the order of the observations.

Task 2 compares explicit Python iteration with NumPy vectorization on one million simulated latency values. Vectorization avoids per-element Python interpreter overhead and should be substantially faster, although exact timing depends on the execution environment.

Task 3 demonstrates why `0.1 + 0.2 == 0.3` is false in binary floating-point arithmetic. `numpy.isclose` is appropriate for tolerance-based comparisons. Absolute error is

$$
|x_{true}-x_{approx}|
$$

and relative error is the absolute error divided by `|x_true|`. The same section recommends `Decimal` for currency calculations where cent-level decimal behavior matters.

Task 4 applies a 45° rotation and nonuniform scaling to the corners of a square. The determinant is approximately **3**, which means the transformation multiplies area by three. Task 5 fits a quadratic model to server response time as concurrent users increase; the curve rises more steeply at higher loads, so extrapolated predictions should be treated cautiously.

### Tasks 6–9: linear algebra

For Task 6, the system

$$
A x=b,\qquad A=\begin{bmatrix}4&2\\8&12\end{bmatrix},\quad b=\begin{bmatrix}20\\72\end{bmatrix}
$$

has solution `x = [3, 4]`. The residual `b - A @ x` verifies the result. Changing the second measurement to 96 changes the solution to approximately `[1.5, 7.0]`.

Task 7 reuses one LU factorization for several load vectors. This is efficient when `A` is fixed and many right-hand sides must be solved. Task 8 compares Jacobi with Gauss–Seidel for a diagonally dominant temperature system. Both methods converge to the direct solution, but Gauss–Seidel uses the newest values immediately and therefore reaches the tolerance in fewer iterations.

Task 9 computes the dominant eigenvector of a four-node adjacency matrix. After normalization, nodes B and C have the largest importance scores because they have stronger connectivity. The small verification norm confirms `Av ≈ λv` numerically.

```mermaid
xychart-beta
    title "Task 8: illustrative convergence trend"
    x-axis [1, 10, 20, 30, 40, 50, 60]
    y-axis "maximum change (log scale)" 0 --> 100
    line "Jacobi" [70, 28, 12, 5, 2, 0.8, 0.3]
    line "Gauss-Seidel" [65, 15, 3, 0.7, 0.15, 0.03, 0.01]
```

### Tasks 10–12: nonlinear equations

Task 10 solves

$$
f(T)=T-25-10e^{-T/20}=0
$$

with bisection and fixed-point iteration. With the equation as written in the source file, both methods converge to approximately **27.525211 °C**. Bisection has predictable halving behavior; fixed-point convergence depends on the contraction factor near the root.

Task 11 finds the internal rate of return by solving `NPV(r)=0` for cash flows `[-10000, 3000, 3500, 4000, 2500]`. Newton–Raphson uses the analytical derivative, while the secant method estimates a slope from two previous points. Both converge to approximately **11.542461%** for these cash flows and produce an NPV close to zero.

Task 12 solves the circle/parabola system

$$
x^2+y^2=4,\qquad y=x^2-1.
$$

The two symmetric intersections are approximately `(1.5175, 1.3028)` and `(-1.5175, 1.3028)`. Initial guesses influence which root is returned.

```mermaid
xychart-beta
    title "Task 11: NPV decreases through the IRR"
    x-axis [0, 5, 10, 11.49, 15, 25, 50]
    y-axis "NPV (relative scale)" -10000 --> 3500
    line [3000, 1500, 350, 0, -600, -2300, -5400]
```

### Tasks 13–15: interpolation, differentiation, and integration

Task 13 estimates the 10:30 temperature from hourly weather-station readings. Linear interpolation gives **23.250 °C**, while the cubic spline gives approximately **23.362 °C**. The difference arises because the spline uses the broader shape of the data rather than only the two neighboring values.

Task 14 estimates speed from GPS position samples. Forward, central, and backward differences are used at the beginning, interior, and end of the series. Changing the position at `t=3 s` does not change the central estimate at exactly `t=3 s`, but it does affect neighboring estimates.

Task 15 integrates smart-meter power readings. The original data give approximately **15.700 kWh** with the trapezoidal rule and **15.800 kWh** with Simpson’s rule. Raising the 6-hour power reading from 1.8 kW to 2.2 kW increases both estimates because the area under the power curve increases.

```mermaid
xychart-beta
    title "Task 13: temperature interpolation"
    x-axis [8, 9, 10, 10.5, 11, 12, 13, 14]
    y-axis "temperature (°C)" 17 --> 27
    line "linear/spline trend" [18, 20, 22.5, 23.36, 24, 25, 25.5, 25.5]
```

### Tasks 16–18: differential equations

Task 16 applies explicit Euler steps to Newton’s law of cooling,

$$
\frac{dT}{dt}=-k(T-T_{env}).
$$

The analytical solution is plotted alongside Euler solutions for several step sizes. Larger time steps produce greater truncation error; sufficiently large steps can also cause numerical instability.

Task 18 uses SciPy’s adaptive RK45 implementation through `solve_ivp` for an RC circuit:

$$
\frac{dV_C}{dt}=\frac{V_{in}-V_C}{RC}.
$$

Larger capacitance increases the time constant `τ=RC`, so the capacitor charges more slowly toward the input voltage.

### Tasks 19–20: optimization and Monte Carlo simulation

Task 19 minimizes fleet cost subject to a delivery-capacity constraint. Type A trucks cost $150 and carry 200 boxes; Type B trucks cost $250 and carry 400 boxes. The continuous solution may contain a fractional truck, so a nearby integer search is also performed. The best practical solution is **four Type B trucks**, providing 1,600 boxes at a cost of **$1,000**.

Task 20 simulates 100,000 independent construction-project cost scenarios using a fixed random seed. The three phases are normally distributed around $50,000, $80,000, and $40,000. The output estimates the probability that the total exceeds the $180,000 budget. In the supplied report, the corresponding result is approximately **23.3420%**; the exact count printed by the cleaned script is reproducible for the stated seed and NumPy version.

```mermaid
xychart-beta
    title "Task 20: Monte Carlo convergence concept"
    x-axis [10, 100, 1000, 10000, 100000]
    y-axis "estimated overrun probability (%)" 0 --> 35
    line "running estimate" [30, 18, 25, 23.0, 23.3]
    line "converged value" [23.3, 23.3, 23.3, 23.3, 23.3]
```

## Reproducibility and limitations

The timing benchmark in Task 2 varies with processor, Python version, NumPy build, and system load. Numerical outputs can differ in the final few digits across library versions. Random simulations are seeded, but normal random-number implementations should still be treated as version-sensitive. Curve fitting and extrapolation are model-dependent: a visually good fit inside the observed range does not guarantee accurate predictions outside it.

The generated PNG files are intentionally not required for running the script. They are produced locally by the source file so the repository remains easy to recreate from two primary deliverables.
