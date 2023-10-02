# Load necessary libraries
required_packages <- c("dplyr", "tidyr", "car", "ez", "ggpubr", "rstatix", "readxl", "DescTools")

for (package in required_packages) {
  if (!require(package, character.only = TRUE)) {
    install.packages(package)
  }
  library(package, character.only = TRUE)
}

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

# Function to winsorize all numeric columns except "X" and "Identifier" and log the original and winsorized values
winsorize_data <- function(data) {
  numeric_cols <- sapply(data, is.numeric)
  numeric_cols_to_winsorize <- colnames(data)[numeric_cols & colnames(data) != "X" & colnames(data) != "Identifier"]
  original_data <- data  # Create a copy of the original data
  data[numeric_cols_to_winsorize] <- lapply(data[numeric_cols_to_winsorize],function(x)
  {winsorized_values <- DescTools::Winsorize(x)
  return(winsorized_values)})
  return(list(Original = original_data, Winsorized = data))
}

# Winsorize numeric variables in the combined dataset, excluding "X" and "Identifier" columns
winsorized_data_list <- winsorize_data(combined_data)
combined_data_winsorized <- winsorized_data_list$Winsorized


# for (i in colnames(combined_data_winsorized)) {

#     # Repeated Measures ANOVA on winsorized combined dataset
#     model <- aov(combined_data_winsorized[[i]] ~ factor(Time) + Error(factor(Identifier)), data = combined_data_winsorized)

#     # Print ANOVA results for each dependent variable
#     cat("ANOVA results for", i, ":\n")
#     print(model)
#     cat("\n")
# }

# You can also save the original and winsorized data to CSV files if needed
write.csv(winsorized_data_list$Original, "original_data.csv", row.names = FALSE)
write.csv(combined_data_winsorized, "winsorized_data.csv", row.names = FALSE)