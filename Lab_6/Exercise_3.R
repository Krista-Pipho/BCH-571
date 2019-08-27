#Rscript Exercise_3.R
#description: Reads the input file tmp_python_out.csv, performs a t.test, and writes the results to tmp_R_out.txt
#usage: Rscript Exercise_3.R


#set working directoy if necessary
#setwd("")

#read in the csv file 
data<-read.csv('tmp_python_out.csv',head = T, sep = '\t')

#redirect output from R to a text file
sink('tmp_R_out.txt')
cat("==============================\n")
cat("T-test between A and B\n")
cat("==============================\n")
#perform t test
t.test(data$A,data$B)
#stop writing to file
sink()
