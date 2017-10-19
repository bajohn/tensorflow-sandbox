# package installed:
# install.packages("jsonlite")
#
# normalized random: x<-rnorm(10000)

library(jsonlite) #import libraries
library(neuralnet) 
message("we in here")

png(file="batting.png")
#header = c('playerID','yearID','stint','teamID','lgID','G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP')
invisible(databack<-fromJSON("./30batting.json"))

invisible(df<-data.frame(databack))

message('data check')
invisible(dsub<-subset(df, select=c(X6:X12, X14:X22)))
invisible(dsub<-apply(dsub, 2, as.integer))
maxvals<-apply(dsub, 2, max)
minvals<-apply(dsub, 2, min)


invisible(scaledvals<-scale(dsub, center=minvals, scale=maxvals-minvals))


invisible(indices<-sample(1:nrow(scaledvals), round(0.75*nrow(scaledvals))))
invisible(trainset<-scaledvals[indices,])
invisible(testset<-scaledvals[-indices,])
n <- names(trainset)
f <- as.formula(paste("medv ~", paste(n[!n %in% "medv"], collapse = " + ")))
nn <- neuralnet(f,data=trainset,hidden=c(5,3),linear.output=T)




#apply(scaledvals, 2, max)
#subset(df, X7==716)
# ['playerID','yearID','stint','teamID','lgID','G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP'],
# x<-data[,12] # hr
# y<-data[,13] # rbi, just for fun
# plot(x,y)

