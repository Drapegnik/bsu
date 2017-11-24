# lab3

solving partial differential Poisson's equation

## task

Решение дифференциальных уравнений в частных производных

* Разработать приложение для решения задачи Пуассона `d^2 U = f(x,y)` c
  прямоугольной границей `U(x,y)= g(x,y)` с помощью:
  * параллельного алгоритма для 1D композиции;
  * параллельного алгоритма для 2D композиции;
* Конкретный вид функций `f`, `g` определяется индивидуально.
* Решение задачи представить визуально с помощью
  [WOLFRAM MATHEMATICA](https://www.wolfram.com/mathematica/)

## requirements

* [python](https://www.python.org/)
* [numpy](http://www.numpy.org/)
* [mpi4py](http://pythonhosted.org/mpi4py/)

## solver

* **run**: `$ bash run.sh {num_of_procces} {num_of_rows} {num_of_cols}`
* [code](https://github.com/Drapegnik/bsu/blob/master/architecture/lab3-poisson/solver.py)

## results

* [report](https://drapegnik.github.io/bsu/architecture/lab3-poisson/report.pdf)
