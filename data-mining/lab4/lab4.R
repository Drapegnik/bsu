
f<-read.table("input.txt")
colnames(f)<-c("Год", "Средняя успеваемость %")
f
mediumlevel<-mean(f[,2])
mediumlevel
result<-numeric()
for(i in 1:length(f[,2])) {
  if(f[i,2]>mediumlevel) result<-c(result, 1)
  if(f[i,2]<mediumlevel) result<-c(result, 0)
}
y<-f[,2]
result
numberofseries<-1
var<-result[1]
for(i in 2:length(result)) {
  if(result[i]!=var) {
    numberofseries<-numberofseries+1
    var<-result[i]
  }
}
numberofseries
leftpart<-as.integer((length(result)+1)/2-2*sqrt(length(result)-1)/2)
leftpart
rightpart<-as.integer((length(result)+1)/2+2*sqrt(length(result)-1)/2)
rightpart
if(leftpart<=numberofseries & numberofseries<=rightpart) {
  answer<-"Тренда нет"
} else {
  answer<-"Тренд есть"
}
answer
smoothed<-numeric()
smoothed<-c(smoothed, (5*y[1]+2*y[2]-y[3])/6)
for(i in 2:(length(f[,1])-1)) {
  smoothed<-c(smoothed, (y[i-1]+y[i]+y[i+1])/3)
}
smoothed<-c(smoothed, (5*y[length(f[,1])-1]+2*y[length(f[,1])-2]-y[length(f[,1])-3])/6)
smoothed
t<-numeric()
var<-((-1)*as.integer(length(y)/2))
as.integer(length(y)/2)
for(i in 1:length(y)) {
  t<-c(t, var)
  var<-var+1
}
f[,3]<-t
f[,4]<-t*t
f[,5]<-f[,2]*f[,3]
colnames(f)<-c("год", "успеваемость %", "t", "t^2", "y*t")
f
a0<-sum(f[,2]/length(f[,2]))
a1<-sum(f[,5])/sum(f[,4])
equation<-paste("y(t)=", a0, "+", a1, "*t")
equation
analyticsmoothed<-numeric()
for(i in 1:length(f[,2])) {
  analyticsmoothed<-c(analyticsmoothed, a0+a1*(i-as.integer(length(y)/2)))
}
ynext<-a0+a1*(max(t)+1)
ynext
fun1<-function(x) f[,2]
fun2<-function(x) smoothed
fun3<-function(x) analyticsmoothed
matplot(f[,1],cbind(fun1(x),fun2(x), fun3(x)),type="l",col=c("blue","red", "green"), xlab="year", ylab="medium progress", main="Graphic")
legend(x="topleft", y=0.92, legend=c("first", "smoothed", "analytic smoothed"), lty=c(1,1,1), lwd=c(2.5,2.5,2.5), col=c("blue", "red", "green"))