library(MASS)
x1<-rnorm(10,mean = 0,sd = 8/3)
y1<-rnorm(10,0,8/3)
x2<-rnorm(20,8,8/3)
y2<-rnorm(20,8,8/3)
xy<-cbind(c(x1, x2),c(y1, y2))
xy

n<-30
n.train<-floor(n*0.7)            #обучающая выборка
n.test<-n-n.train                #тестовая выборка

idx.train<-sample(1:n,n.train)   #случайный выбор индексов
idx.test<-(1:n)[!(1:n %in% idx.train)]

data.train<-xy[idx.train,]       #выбираем данные по индексам
data.test<-xy[idx.test,] 

cl<-kmeans(xy,2)
cl.cluster<-cl$cluster

cl.train<-cl.cluster[idx.train]
cl.test<-cl.cluster[idx.test]

mod<-qda(data.train, cl.train)               #обучение тестовой выборки
cl.test_est<-predict(mod, data.test)$class   #классификация получ данных
sum(cl.test_est!=cl.test)/n.test             #вычисляем ошибку
idx<-idx.test[cl.test_est!=cl.test]          #индексы не соответсв истинной

plot(xy, type="n")
points(data.train,pch=24, col=ifelse(cl.train==1,"blue","green"))
legend("topleft",legend=c("train - 1","train - 2"),pch=24,col=c("blue","green"))
points(data.test,pch=21, col=ifelse(cl.test==1,"blue","green"))
legend("bottomright",legend=c("test - 1","test - 2"),pch=21,col=c("blue","green"))
if (length(idx)==1){			             #костыль, чтобы работало
  points(xy[idx,1],xy[idx,2],col="red", pch=4) 
}else
  points(xy[idx,],col="red", pch=4)
legend("bottom",legend=c("wrong"),pch=4,col="red")

idd<-sample(1:n.train,n.train * 0.2)         #выбираем индексы 20% обучающей
for(i in idd) 
  cl.train[i]=ifelse(cl.train[i]==1,2,1)     #инверсируем номера кластеров

mod2<-qda(data.train, cl.train)              #обучение тестовой выборки
cl.test_est<-predict(mod2, data.test)$class  #классификация получ данных
sum(cl.test_est!=cl.test)/n.test             #вычисляем ошибку
idx2<-idx.test[cl.test_est!=cl.test]         #индексы не соответсв истинной

plot(xy, type="n")
points(data.train,pch=24, col=ifelse(cl.train==1,"blue","green"))
legend("topleft",legend=c("train - 1","train - 2"),pch=24,col=c("blue","green"))
points(data.test,pch=21, col=ifelse(cl.test==1,"blue","green"))
legend("bottomright",legend=c("test - 1","test - 2"),pch=21,col=c("blue","green"))

if (length(idx2)==1){ 			             #костыль, чтобы работало
  points(xy[idx2,1],xy[idx2,2],col="red", pch=4) 
}else
  points(xy[idx2,],col="red", pch=4)
legend("bottom",legend=c("wrong"),pch=4,col="red")

