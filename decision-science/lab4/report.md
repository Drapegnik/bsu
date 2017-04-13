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
	(v3)-0.14->(t) - [0.14]
	(v1)-4.6->(v4) - [0.3]
	(v2)-0.2->(v3) - [0.14]
	(v4)-0.5->(v3) - [0]
	(v4)-0.3->(t) - [0.3]
	(v1)-0.4->(v5) - [0]
	(v1)-3.5->(v2) - [0]
	(v2)-7.8->(v5) - [0]
```

![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab4/out/task2.gv.png)