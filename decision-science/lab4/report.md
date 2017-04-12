# lab4
Pazhitnykh Ivan

* Find maximum flows in graphs:
## task1
![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1491579189/ds-lab4-task1.png)

* find path: `(s)-[2, 2]->(v1)-[1, 1]->(v3)-[2, 2]->(t)`, with min res = 1, change flow:
```
	(s)-2->(v1) - [1]
	(v1)-1->(v3) - [1]
	(v3)-2->(t) - [1]
```

* find path: `(s)-[2, 1]->(v1)-[0, 1]->(s)-[3, 3]->(v2)-[2, 2]->(t)`, with min res = 1, change flow:
```
	(s)-2->(v1) - [1]
	(v1)-0->(s) - [-1]
	(s)-3->(v2) - [1]
	(v2)-2->(t) - [1]
```

* find path: `(s)-[2, 1]->(v1)-[0, 1]->(s)-[3, 2]->(v2)-[0, 1]->(s)-[1, 1]->(v3)-[0, 1]->(v1)-[3, 3]->(t)`, with min res = 1, change flow:
```
	(s)-2->(v1) - [1]
	(v1)-0->(s) - [-1]
	(s)-3->(v2) - [1]
	(v2)-0->(s) - [-1]
	(s)-1->(v3) - [1]
	(v3)-0->(v1) - [0]
	(v1)-3->(t) - [1]
```

* find path: `(s)-[2, 1]->(v1)-[0, 1]->(s)-[3, 2]->(v2)-[2, 1]->(t)`, with min res = 1, change flow:
```
	(s)-2->(v1) - [1]
	(v1)-0->(s) - [-1]
	(s)-3->(v2) - [2]
	(v2)-2->(t) - [2]
```

* find path: `(s)-[2, 1]->(v1)-[0, 1]->(s)-[3, 1]->(v2)-[4, 4]->(v3)-[2, 1]->(t)`, with min res = 1, change flow:
```
	(s)-2->(v1) - [1]
	(v1)-0->(s) - [-1]
	(s)-3->(v2) - [3]
	(v2)-4->(v3) - [1]
	(v3)-2->(t) - [2]
```

* find path: `(s)-[2, 1]->(v1)-[3, 2]->(t)`, with min res = 1, change flow:
```
	(s)-2->(v1) - [2]
	(v1)-3->(t) - [2]
```

* maximal flow:
```
	(v2)-4->(v3) - [1]
	(s)-2->(v1) - [2]
	(t)-0->(v1) - [-2]
	(v3)-0->(v2) - [-1]
	(v1)-3->(t) - [2]
	(v1)-0->(s) - [-2]
	(v3)-2->(t) - [2]
	(s)-3->(v2) - [3]
	(v2)-0->(v1) - [0]
	(v3)-0->(v1) - [0]
	(v1)-3->(v2) - [0]
	(v2)-0->(s) - [-3]
	(s)-1->(v3) - [1]
	(v2)-2->(t) - [2]
	(v3)-0->(s) - [-1]
	(t)-0->(v2) - [-2]
	(t)-0->(v3) - [-2]
	(v1)-1->(v3) - [0]
```

![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab4/out/task1.gv.png)

## task2
![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1491579189/ds-lab4-task2.png)

* find path: `(s)-[0.9, 0.9]->(v1)-[4.6, 4.6]->(v4)-[0.3, 0.3]->(t)`, with min res = 0.3, change flow:
```
	(s)-0.9->(v1) - [0.3]
	(v1)-4.6->(v4) - [0.3]
	(v4)-0.3->(t) - [0.3]
```

* find path: `(s)-[0.8, 0.8]->(v2)-[0.2, 0.2]->(v3)-[0.14, 0.14]->(t)`, with min res = 0.14, change flow:
```
	(s)-0.8->(v2) - [0.14]
	(v2)-0.2->(v3) - [0.14]
	(v3)-0.14->(t) - [0.14]
```

* maximal flow:
```
	(v4)-0->(v1) - [-0.3]
	(v3)-0->(v2) - [-0.14]
	(v1)-0.4->(v5) - [0]
	(v1)-0->(s) - [-0.3]
	(v4)-0.3->(t) - [0.3]
	(v4)-0.5->(v3) - [0]
	(s)-0.8->(v2) - [0.14]
	(v2)-0.2->(v3) - [0.14]
	(v2)-0->(s) - [-0.14]
	(v3)-0->(v4) - [0]
	(v5)-0->(v2) - [0]
	(v1)-3.5->(v2) - [0]
	(v5)-0->(v1) - [0]
	(v2)-7.8->(v5) - [0]
	(v2)-0->(v1) - [0]
	(t)-0->(v3) - [-0.14]
	(v1)-4.6->(v4) - [0.3]
	(t)-0->(v4) - [-0.3]
	(s)-0.9->(v1) - [0.3]
	(v3)-0.14->(t) - [0.14]
```

![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab4/out/task2.gv.png)