t <- read.table ("input.txt")

plot (t, main = "Correlation")

disp <- var (t[,1])   #дисперсия
deviat <- sqrt (disp) #сред кв отклонение
aver <- mean (t[,1])  #среднее


gr1 <- subset (t[,1], ((aver - deviat) < t[,1]) & (t[,1] < (aver + deviat))) 
gr2 <- subset (t[,1], ((aver - 2 * deviat) < t[,1]) & (t[,1] < (aver + 2 * deviat)))
gr3 <- subset (t[,1], ((aver - 3 * deviat) < t[,1]) & (t[,1] < (aver + 3 * deviat)))

part2 <- matrix (0, 3, 5)

part2[1:3,1] <- c (aver - deviat, aver - 2 * deviat, aver - 3 * deviat)
part2[1:3,2] <- c (aver + deviat, aver + 2 * deviat, aver+3 * deviat)
part2[1:3,3] <- c (length (gr1), length (gr2), length(gr3)) 
part2[1:3,4] <- part2[1:3,3]/length (t[,1]) * 100
part2[1:3,5] <- c (68.3, 95.4, 99.7)

range <- max (t[,1]) - min (t[,1])
k <- 1 + floor (log (length (t[,1]), 2))  #кол-во групп по Стрейджесу
h <- range / k                            #шаг

sa <- sort (t[,1])

part3 <- matrix (0, k, 5)

for (i in 0:(k-1)) {
  l <- sa[1] + i * h
  r <- sa[1] + (i + 1) * h
  gr <- subset (t[,2], l <= t[,1] & (t[,1] < r | i == k - 1 & t[,1] <= r))
  part3[i + 1, 1:5] <- c(l, r, length (gr), sum (gr), mean (gr))
}

v <- length (t[,1]) - 2
coefcor <- cor (t[,1], t[,2])                 #коэф корреляции
T <- abs (coefcor) * sqrt (v / (1 - coefcor ^2))  #расчёт значимости кк

coefcor
T
lm (t[,2]~t[,1])

six <- sqrt(sum((t[,1]-mean(t[,1]))^2)/length(t[,1]))
siy <- sqrt(sum((t[,2]-mean(t[,2]))^2)/length(t[,2]))
b <- coefcor*siy/six
b
a<-mean(t[,2])-b*mean(t[,1])
a
lines(t[,1],a+b*t[,1])

part2
part3


