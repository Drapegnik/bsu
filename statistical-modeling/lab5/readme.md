# lab5

Система массового обслуживания **GPSS**

## 20. Моделирование процесса функционирования вычислительного центра.

### Исходные данные:

1.  Вычислительный центр, оснащенный тремя однотипными ЭВМ, обслуживает сеть активных терминалов.
2.  Задачи пользователей образуют пуассоновский поток с зад/сек, а время выполнения задачи в ЭВМ имеет экспоненциальное распределение с математическим ожиданием сек.
3.  Программа-диспетчер обрабатывает задачу, выбирая для нее свободную ЭВМ. Время обработки равномерно распределено на интервале **`[a ± Δ]`**. Если все ЭВМ заняты, то задача направляется в очередь, которая на данный момент является минимальной.
4.  После выполнения в ЭВМ, задача возвращается на соответствующий терминал, причем **`30%`** задач обслуживается в АЦПУ **`[b ± ε]`** сек.

### Цель:

Разработать **GPSSV**-модель для анализа процесса функционирования вычислительного центра в течение одного часа.

### Первоначальный перечень экспериментов:

- `λ = 0.2`
- `µ = 12`
- `a = 2`
- `Δ = 1`
- `b = 12`
- `ε = 8`

## Решение:

> source code of [`lab5.gps`](https://github.com/Drapegnik/bsu/tree/master/statistical-modeling/lab5/lab5.gps)

```asm
input_flow_mean		VARIABLE 	0.2	; lambda
manager_mean		VARIABLE	2	; a
manager_max_delta	VARIABLE	1	; delta
computers_mean		VARIABLE	12	; mu
print_probability	VARIABLE	0.3	; percent of task to printing
printer_mean		VARIABLE 	12	; b
printer_max_delta	VARIABLE 	8	; epsilon

Computers 		STORAGE 	3

POISS	FUNCTION	RN1,C24 (Poisson Process)
0.0,0.0/0.1,0.104/0.2,0.222/0.3,0.355/0.4,0.509/0.5,0.69/
0.6,0.915/0.7,1.2/0.75,1.38/0.8,1.6/0.84,1.83/0.88,7.12/
0.9,2.3/0.92,2.52/0.94,2.81/0.95,2.99/0.96,3.2/0.97,3.5/
0.98,3.9/0.99,4.6/0.995,5.3/0.998,6.2/0.999,7/0.9997,8

; ---------------------------------------------------------------

	GENERATE V$input_flow_mean,FN$POISS 				; Input flow: lambda*PoissonDistr()

	QUEUE GeneralQueue

	QUEUE ManagerQueue
	SEIZE Manager
	DEPART ManagerQueue
	  ADVANCE V$manager_mean,V$manager_max_delta 		; Processing by task manager
	RELEASE Manager

	ENTER Computers
	  ADVANCE (Exponential(1, 0, V$computers_mean)) 	; General Computations
	LEAVE Computers

	TRANSFER V$print_probability,FINISH,PRINT			; 30% on PRINT, 70$ on FINISH

	PRINT	QUEUE PrinterQueue
	SEIZE Printer
	DEPART PrinterQueue
	  ADVANCE V$printer_mean,V$printer_max_delta		; Printing
	RELEASE Printer

	FINISH	DEPART GeneralQueue
	TERMINATE

; ---------------------------------------------------------------

	GENERATE 3600						; 1 hr = 60*60 = 3600 s
	TERMINATE 1
	START 2
```
