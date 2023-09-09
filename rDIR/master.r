# Install and load the "ez" package if not already installed
library(ez)
library(ggpubr)

library(rstatix)

# Load necessary libraries
library(dplyr)
library(tidyr)
library(car)

# Import your datasets (replace with actual file paths)
data_time1 <- read.csv("Baseline.csv")
data_time2 <- read.csv("PostInvervention.csv")
data_time3 <- read.csv("FollowUp.csv")

# Add a Time factor to each dataset
data_time1$Time <- "Time1"
data_time2$Time <- "Time2"
data_time3$Time <- "Time3"

# Combine the datasets into a single data frame
combined_data <- bind_rows(data_time1, data_time2, data_time3)

# Check the structure and contents of your combined dataset
# str(combined_data)
# head(combined_data)
# names(combined_data)
# col(combined_data)
# Descriptive statisticsy
# print(summary(combined_data)
# )
# Initialize an empty list to store ANOVA results
anova_results_list <- list()
for (i in colnames(combined_data)) {

    # # Repeated Measures ANOVA on combined dataset
    model <- aov(combined_data[[i]]~factor(Time)+Error(factor(Identifier)), data = combined_data)

    # Print ANOVA results for each dependent variable
    cat("ANOVA results for", i, ":\n")
    print(model)
    cat("\n")
}

#Boxplot Graphs from combined dataset
bxp <- ggboxplot(combined_data, x = "Time", y = "Average.Step.Count", add = "value")
print(bxp)

