t <- read.table ("input.txt")
plot(t,type="p",main="Диаграмма рассеивания",xlab="X", ylab="Y")
cl1 <- kmeans(t,2)
table(cl1$cluster)
cl1$centers

plot(t,col=ifelse(cl1$cluster==1,"blue","green"))
legend("topright",legend=c("1","2"),fill=c("blue","green"))

plot(t,pch=ifelse(cl1$cluster==1,1,2))
legend("topright",legend=c("1","2"),pch=c(1,2))

cl2<-kmeans(t,3)
table(cl2$cluster)
cl2$centers

plot(t,col=ifelse(cl2$cluster==1,"blue", ifelse(cl2$cluster==2, "green", "red")))
legend("topright",legend=c("1","2", "3"),fill=c("blue","green", "red"))

plot(t,pch=ifelse(cl2$cluster==1,1, ifelse(cl2$cluster==2, 2, 3)))
legend("topright",legend=c("1","2","3"),pch=c(1,2,3))