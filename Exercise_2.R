#Rscript Exercise_2.R
#description: this generates a vector of 100 random numbers with mean 3.8 and stdev 4.6
#then outputs the mean, median and stdev to stdout
#usage: Rscript Exercise_2.R

data<-rnorm(100, mean=3.8, sd = 4.6)
cat("the mean is: ")
cat(mean(data))
cat("\nthe median is: ")
cat(median(data))
cat("\nthe standard deviation is: ")
cat(sd(data))
cat("\n")
