library(ez)
library(ggpubr)
library(rstatix)
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

# Descriptive statistics
print(summary(combined_data)
)
# Iterate between Factors to calculate Repeated Measures ANOVA results
for (i in colnames(combined_data)) {

    # Repeated Measures ANOVA on combined dataset
    model <- aov(combined_data[[i]]~factor(Time)+Error(factor(Identifier)), data = combined_data)

    # Print ANOVA results for each dependent variable
    cat("ANOVA results for", i, ":\n")
    print(model)
    cat("\n")
}
