# Load necessary libraries
required_packages <- c("dplyr", "tidyr", "car", "ez", "ggpubr", "rstatix", "readxl", "DescTools","grephl")
for (package in required_packages) {
  if (!require(package, character.only = TRUE)) {
    install.packages(package)
  }
  library(package, character.only = TRUE)
}

# Import your datasets (replace with actual file paths)
initialdata <- read_excel("draftdata.xlsx")
initialdata[, grepl("Total Baseline|Total Post-Int|Total Follow-Up", names(initialdata))]


