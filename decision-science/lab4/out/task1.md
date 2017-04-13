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

