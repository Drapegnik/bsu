# lab4
Pazhitnykh Ivan

## task1
* Find maximum flow in graph:
![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1491579189/ds-lab4-task1.png)
* table with marks by iteration:

s | t  | v1  | v2  | v3 
--- | --- | --- | --- | --- | 
`(None, inf)` | `(v1, 2)` | `(s, 2)` | `(s, 3)` | `(s, 1)` | 
`(None, inf)` | `(v2, 2)` | `None` | `(s, 3)` | `(s, 1)` | 
`(None, inf)` | `(v3, 1)` | `None` | `None` | `(s, 1)` | 
`(None, inf)` | `None` | `None` | `None` | `None` | 

* maximal flow = 6:
```
	(s)-2->(v1) - [2]
	(s)-3->(v2) - [3]
	(s)-1->(v3) - [1]
	(v1)-1->(v3) - [0]
	(v1)-3->(t) - [2]
	(v1)-3->(v2) - [0]
	(v2)-2->(t) - [2]
	(v2)-4->(v3) - [0]
	(v3)-2->(t) - [1]
```

![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab4/out/task1.gv.png)
## task2
* Find maximum flow in graph:
![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1491579189/ds-lab4-task2.png)
* table with marks by iteration:

s | t  | v1  | v2  | v3  | v4  | v5 
--- | --- | --- | --- | --- | --- | --- | 
`(None, inf)` | `(v4, 0.3)` | `(s, 0.3)` | `(s, 0.8)` | `(v2, 0.2)` | `(v1, 0.3)` | `(v1, 0.4)` | 
`(None, inf)` | `(v3, 0.14)` | `(s, 0.6)` | `(s, 0.14)` | `(v2, 0.14)` | `(v1, 4.3)` | `(v1, 0.4)` | 
`(None, inf)` | `None` | `(s, 0.6)` | `(s, 0.66)` | `(v2, 0.06)` | `(v1, 4.3)` | `(v1, 0.4)` | 

* maximal flow = 0.44:
```
	(s)-0.9->(v1) - [0.3]
	(s)-0.8->(v2) - [0.14]
	(v1)-3.5->(v2) - [0]
	(v2)-7.8->(v5) - [0]
	(v4)-0.5->(v3) - [0]
	(v1)-4.6->(v4) - [0.3]
	(v4)-0.3->(t) - [0.3]
	(v2)-0.2->(v3) - [0.14]
	(v3)-0.14->(t) - [0.14]
	(v1)-0.4->(v5) - [0]
```

![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab4/out/task2.gv.png)
## task3
* Solve Assignment problem with coast matrix:
```
[[8 9 7 5 0 4]
 [5 8 4 4 0 3]
 [0 0 0 0 0 0]
 [5 7 6 5 0 4]
 [8 4 3 7 0 5]
 [2 4 6 8 3 7]]
```
* simplified matrix:
```
[[8 9 7 5 0 4]
 [5 8 4 4 0 3]
 [0 0 0 0 0 0]
 [5 7 6 5 0 4]
 [8 4 3 7 0 5]
 [0 2 4 6 1 5]]
```
s | s0  | s1  | s2  | s3  | s4  | s5  | t  | t0  | t1  | t2  | t3  | t4  | t5 
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
`(None, inf)` | `(t4, -1)` | `(s, 1)` | `None` | `(s, 1)` | `(s, 1)` | `None` | `None` | `None` | `None` | `None` | `None` | `(s1, 1)` | `None` | 
`(None, inf)` | `(t4, -1)` | `None` | `None` | `(s, 1)` | `None` | `None` | `None` | `None` | `None` | `None` | `None` | `(s3, 1)` | `None` | 
`(None, inf)` | `(t4, -1)` | `(t5, -1)` | `None` | `(s, 1)` | `None` | `None` | `None` | `None` | `None` | `None` | `None` | `(s3, 1)` | `(s3, 1)` | 
`(None, inf)` | `None` | `None` | `None` | `None` | `None` | `None` | `None` | `None` | `None` | `None` | `None` | `None` | `None` | 

* iteration 1, flow=3:
```
[[8 9 7 5 0 4]
 [5 8 4 4 0 3]
 [0 0 0 0 0 0]
 [5 7 6 5 0 4]
 [8 4 3 7 0 5]
 [0 2 4 6 1 5]]
```
![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab4/out/task3-1.gv.png)
* iteration 2, flow=5:
```
[[5 6 4 2 0 1]
 [2 5 1 1 0 0]
 [0 0 0 0 3 0]
 [2 4 3 2 0 1]
 [5 1 0 4 0 2]
 [0 2 4 6 4 5]]
```
![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab4/out/task3-2.gv.png)
* iteration 3, flow=5:
```
[[4 5 3 1 0 0]
 [2 5 1 1 1 0]
 [0 0 0 0 4 0]
 [1 3 2 1 0 0]
 [5 1 0 4 1 2]
 [0 2 4 6 5 5]]
```
![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab4/out/task3-3.gv.png)
* iteration 4, flow=6:
```
[[3 4 2 0 0 0]
 [1 4 0 0 1 0]
 [0 0 0 0 5 1]
 [0 2 1 0 0 0]
 [5 1 0 4 2 3]
 [0 2 4 6 6 6]]
```
![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab4/out/task3-4.gv.png)
* cost value:
```
(s0)-1->(t3)
(s1)-1->(t5)
(s2)-1->(t1)
(s3)-1->(t4)
(s4)-1->(t2)
(s5)-1->(t0)

```
`C =  5 + 4 + 4 + 7 + 0 + 4 = 24`