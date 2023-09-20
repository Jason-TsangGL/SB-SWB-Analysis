# Load necessary libraries
library(ez)
library(ggpubr)
library(rstatix)
library(dplyr)
library(tidyr)
library(car)
library(beeswarm)

# Import your datasets (replace with actual file paths)
data_time1 <- read.csv("Baseline.csv")
data_time2 <- read.csv("PostIntervention.csv")
data_time3 <- read.csv("FollowUp.csv")

# Add a Time factor to each dataset
data_time1$Time <- "Time1"
data_time2$Time <- "Time2"
data_time3$Time <- "Time3"

# Combine the datasets into a single data frame
combined_data <- bind_rows(data_time1, data_time2, data_time3)
print(names(combined_data))
# 
# print(boxplot(Average.Step.Count ~ Time, data=combined_data, cex.lab=1.5, cex.axis=1.5, xlab='Baseline, Post-Intervention, Follow-Up', ylab=''))
# print(boxplot(Average.Stand.Count ~ Time, data=combined_data, cex.lab=1.5, cex.axis=1.5, xlab='Baseline, Post-Intervention, Follow-Up', ylab=''))
# print(boxplot(Average.Sitting.Time ~ Time, data=combined_data, cex.lab=1.5, cex.axis=1.5, xlab='Baseline, Post-Intervention, Follow-Up', ylab=''))


# #Test homework for normality
# shapiro.test(classdata$homework)
#t-test
for (i in colnames(combined_data)) {
    print(t.test(combined_data[[i]] ~ Time, data=combined_data, var.equal=TRUE)) #Pooled Variance 
}