# lab6

Pazhitnykh Ivan

## task1

* Build net graphics and find all time params for:

| Job Name | time | depends of    |
| -------- | ---- | ------------- |
| `A`      | `3`  | –             |
| `B`      | `5`  | –             |
| `C`      | `7`  | –             |
| `D`      | `6`  | `A`           |
| `E`      | `3`  | `A`           |
| `F`      | `3`  | `B`, `E`      |
| `G`      | `2`  | `D`, `F`, `G` |
| `H`      | `5`  | `B`, `C`, `E` |
| `I`      | `7`  | `B`, `C`, `E` |

* result:

![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab6/task1.in.gv.png)

```
Events early terms:	Tp[0]=0.0	Tp[1]=3.0	Tp[2]=6.0	Tp[3]=7.0	Tp[4]=12.0	Tp[5]=17.0
Events late terms:	Tn[0]=0.0	Tn[1]=4.0	Tn[2]=7.0	Tn[3]=7.0	Tn[4]=12.0	Tn[5]=17.0
Events time reserves:	R[0]=0.0	R[1]=1.0	R[2]=1.0	R[3]=0.0	R[4]=0.0	R[5]=0.0

Jobs early terms start:
	Tps(0, 1) = 0.0
	Tps(0, 2) = 0.0
	Tps(0, 3) = 0.0
	Tps(1, 2) = 3.0
	Tps(1, 4) = 3.0
	Tps(2, 3) = 6.0
	Tps(2, 4) = 6.0
	Tps(3, 4) = 7.0
	Tps(3, 5) = 7.0
	Tps(4, 5) = 12.0

Jobs early terms finish:
	Tpf(0, 1) = 3.0
	Tpf(0, 2) = 5.0
	Tpf(0, 3) = 7.0
	Tpf(1, 2) = 6.0
	Tpf(1, 4) = 9.0
	Tpf(2, 3) = 6.0
	Tpf(2, 4) = 9.0
	Tpf(3, 4) = 12.0
	Tpf(3, 5) = 14.0
	Tpf(4, 5) = 17.0

Jobs late terms finish:
	Tns(0, 1) = 4.0
	Tns(0, 2) = 7.0
	Tns(0, 3) = 7.0
	Tns(1, 2) = 7.0
	Tns(1, 4) = 12.0
	Tns(2, 3) = 7.0
	Tns(2, 4) = 12.0
	Tns(3, 4) = 12.0
	Tns(3, 5) = 17.0
	Tns(4, 5) = 17.0

Jobs late terms finish:
	Tnf(0, 1) = 4.0
	Tnf(0, 2) = 7.0
	Tnf(0, 3) = 7.0
	Tnf(1, 2) = 7.0
	Tnf(1, 4) = 12.0
	Tnf(2, 3) = 7.0
	Tnf(2, 4) = 12.0
	Tnf(3, 4) = 12.0
	Tnf(3, 5) = 17.0
	Tnf(4, 5) = 17.0

Jobs summary reserves:
	Rs(0, 1) = 1.0
	Rs(0, 2) = 2.0
	Rs(0, 3) = 0.0
	Rs(1, 2) = 1.0
	Rs(1, 4) = 3.0
	Rs(2, 3) = 1.0
	Rs(2, 4) = 3.0
	Rs(3, 4) = 0.0
	Rs(3, 5) = 3.0
	Rs(4, 5) = 0.0

Jobs free reserves:
	Rf(0, 1) = 0.0
	Rf(0, 2) = 1.0
	Rf(0, 3) = 0.0
	Rf(1, 2) = 0.0
	Rf(1, 4) = 3.0
	Rf(2, 3) = 1.0
	Rf(2, 4) = 3.0
	Rf(3, 4) = 0.0
	Rf(3, 5) = 3.0
	Rf(4, 5) = 0.0

Jobs independent reserves:
	Rn(0, 1) = 0.0
	Rn(0, 2) = 1.0
	Rn(0, 3) = 0.0
	Rn(1, 2) = 0.0
	Rn(1, 4) = 2.0
	Rn(2, 3) = 0.0
	Rn(2, 4) = 2.0
	Rn(3, 4) = 0.0
	Rn(3, 5) = 3.0
	Rn(4, 5) = 0.0

Jobs guaranteed reserves:
	Rg(0, 1) = 1.0
	Rg(0, 2) = 2.0
	Rg(0, 3) = 0.0
	Rg(1, 2) = 0.0
	Rg(1, 4) = 2.0
	Rg(2, 3) = 0.0
	Rg(2, 4) = 2.0
	Rg(3, 4) = 0.0
	Rg(3, 5) = 3.0
	Rg(4, 5) = 0.0
```

## task2

* Find all time params for net graphics:
  ![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1492564649/ds-lab6-task2.png)

```
Events early terms:	Tp[0]=0.0	Tp[1]=1.0	Tp[2]=6.0	Tp[3]=8.0	Tp[4]=11.0	Tp[5]=14.0
Events late terms:	Tn[0]=0.0	Tn[1]=1.0	Tn[2]=6.0	Tn[3]=8.0	Tn[4]=12.0	Tn[5]=14.0
Events time reserves:	R[0]=0.0	R[1]=0.0	R[2]=0.0	R[3]=0.0	R[4]=1.0	R[5]=0.0

Jobs early terms start:
	Tps(0, 1) = 0.0
	Tps(0, 2) = 0.0
	Tps(0, 3) = 0.0
	Tps(1, 2) = 1.0
	Tps(1, 4) = 1.0
	Tps(2, 3) = 6.0
	Tps(2, 4) = 6.0
	Tps(3, 4) = 8.0
	Tps(3, 5) = 8.0
	Tps(4, 5) = 11.0

Jobs early terms finish:
	Tpf(0, 1) = 1.0
	Tpf(0, 2) = 5.0
	Tpf(0, 3) = 7.0
	Tpf(1, 2) = 6.0
	Tpf(1, 4) = 7.0
	Tpf(2, 3) = 8.0
	Tpf(2, 4) = 8.0
	Tpf(3, 4) = 11.0
	Tpf(3, 5) = 14.0
	Tpf(4, 5) = 13.0

Jobs late terms finish:
	Tns(0, 1) = 1.0
	Tns(0, 2) = 6.0
	Tns(0, 3) = 8.0
	Tns(1, 2) = 6.0
	Tns(1, 4) = 12.0
	Tns(2, 3) = 8.0
	Tns(2, 4) = 12.0
	Tns(3, 4) = 12.0
	Tns(3, 5) = 14.0
	Tns(4, 5) = 14.0

Jobs late terms finish:
	Tnf(0, 1) = 1.0
	Tnf(0, 2) = 6.0
	Tnf(0, 3) = 8.0
	Tnf(1, 2) = 6.0
	Tnf(1, 4) = 12.0
	Tnf(2, 3) = 8.0
	Tnf(2, 4) = 12.0
	Tnf(3, 4) = 12.0
	Tnf(3, 5) = 14.0
	Tnf(4, 5) = 14.0

Jobs summary reserves:
	Rs(0, 1) = 0.0
	Rs(0, 2) = 1.0
	Rs(0, 3) = 1.0
	Rs(1, 2) = 0.0
	Rs(1, 4) = 5.0
	Rs(2, 3) = 0.0
	Rs(2, 4) = 4.0
	Rs(3, 4) = 1.0
	Rs(3, 5) = 0.0
	Rs(4, 5) = 1.0

Jobs free reserves:
	Rf(0, 1) = 0.0
	Rf(0, 2) = 1.0
	Rf(0, 3) = 1.0
	Rf(1, 2) = 0.0
	Rf(1, 4) = 4.0
	Rf(2, 3) = 0.0
	Rf(2, 4) = 3.0
	Rf(3, 4) = 0.0
	Rf(3, 5) = 0.0
	Rf(4, 5) = 1.0

Jobs independent reserves:
	Rn(0, 1) = 0.0
	Rn(0, 2) = 1.0
	Rn(0, 3) = 1.0
	Rn(1, 2) = 0.0
	Rn(1, 4) = 4.0
	Rn(2, 3) = 0.0
	Rn(2, 4) = 3.0
	Rn(3, 4) = 0.0
	Rn(3, 5) = 0.0
	Rn(4, 5) = 0.0

Jobs guaranteed reserves:
	Rg(0, 1) = 0.0
	Rg(0, 2) = 1.0
	Rg(0, 3) = 1.0
	Rg(1, 2) = 0.0
	Rg(1, 4) = 5.0
	Rg(2, 3) = 0.0
	Rg(2, 4) = 4.0
	Rg(3, 4) = 1.0
	Rg(3, 5) = 0.0
	Rg(4, 5) = 0.0
```

![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab6/task2.in.gv.png)
