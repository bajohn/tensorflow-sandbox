# package installed:
# install.packages("jsonlite")
#
# normalized random: x<-rnorm(10000)

library(jsonlite) #import library
message("we in here")

png(file="jsonplot.png")
data<-fromJSON("./data.json")
x<-data[,1]
y<-data[,2]
plot(x,y)

