       X           Identifier    Average.Step.Count Average.Step.Time 
 Min.   : 1.00   Min.   : 1.00   Min.   :   56.29   Min.   :  0.5286
 1st Qu.:13.00   1st Qu.:20.00   1st Qu.: 5710.14   1st Qu.: 73.3442
 Median :25.00   Median :34.50   Median : 8175.12   Median : 92.3714
 Mean   :25.33   Mean   :38.08   Mean   : 8308.74   Mean   : 95.3504
 3rd Qu.:37.25   3rd Qu.:56.00   3rd Qu.:10203.71   3rd Qu.:119.1714
 Max.   :55.00   Max.   :76.00   Max.   :18939.43   Max.   :169.7571  
 Average.Stand.Count Average.Sitting.Time Average.Sedentary.Time
 Min.   :  1.017     Min.   : 760.3       Min.   : 760.3
 1st Qu.:147.985     1st Qu.:1011.9       1st Qu.:1011.9
 Median :191.164     Median :1063.9       Median :1063.9
 Mean   :195.061     Mean   :1060.6       Mean   :1060.6
 3rd Qu.:234.007     3rd Qu.:1116.8       3rd Qu.:1116.8
 Max.   :491.986     Max.   :1363.5       Max.   :1363.5
 Adjusted.Average.Sedentary.Time NumSitToStands   Average.Sleep
 Min.   :224.6                   Min.   : 1.571   Min.   :360.0
 1st Qu.:488.6                   1st Qu.:36.000   1st Qu.:477.9
 Median :549.4                   Median :43.000   Median :535.7
 Mean   :547.8                   Mean   :43.935   Mean   :512.8
 3rd Qu.:615.5                   3rd Qu.:52.750   3rd Qu.:535.7  
 Max.   :838.5                   Max.   :73.286   Max.   :565.7
 Weekday.Sleep   Weekend.Sleep       Time
 Min.   :360.0   Min.   :360.0   Length:148
 1st Qu.:465.0   1st Qu.:480.0   Class :character
 Median :510.0   Median :510.0   Mode  :character
 Mean   :507.1   Mean   :527.1
 3rd Qu.:540.0   3rd Qu.:600.0
 Max.   :600.0   Max.   :600.0
ANOVA results for X :

Call:
aov(formula = combined_data[[i]] ~ factor(Time) + Error(factor(Identifier)), 
    data = combined_data)

Grand Mean: 25.33108

Stratum 1: factor(Identifier)

Terms:
                factor(Time) Residuals
Sum of Squares      1144.591 28734.520
Deg. of Freedom            2        53

Residual standard error: 23.28435
Estimated effects may be unbalanced

Stratum 2: Within

Terms:
                factor(Time) Residuals
Sum of Squares     1304.5521   61.1145
Deg. of Freedom            2        90

Residual standard error: 0.8240452
Estimated effects may be unbalanced

ANOVA results for Identifier :

Call:
aov(formula = combined_data[[i]] ~ factor(Time) + Error(factor(Identifier)),
    data = combined_data)

Grand Mean: 38.08108

Stratum 1: factor(Identifier)

Terms:
                factor(Time) Residuals
Sum of Squares       3764.26  63230.77
Deg. of Freedom            2        53

Residual standard error: 34.54031
Estimated effects may be unbalanced

Stratum 2: Within

Terms:
                factor(Time)    Residuals
Sum of Squares  2.228900e-28 7.272256e-26
Deg. of Freedom            2           90

Residual standard error: 2.842584e-14
Estimated effects may be unbalanced

ANOVA results for Average.Step.Count :

Call:
aov(formula = combined_data[[i]] ~ factor(Time) + Error(factor(Identifier)),
    data = combined_data)

Grand Mean: 8308.736

Stratum 1: factor(Identifier)

Terms:
                factor(Time)  Residuals
Sum of Squares      60437132 1185580655
Deg. of Freedom            2         53

Residual standard error: 4729.635
Estimated effects may be unbalanced

Stratum 2: Within

Terms:
                factor(Time) Residuals
Sum of Squares      99451001 320225420
Deg. of Freedom            2        90

Residual standard error: 1886.282
Estimated effects may be unbalanced

ANOVA results for Average.Step.Time :

Call:
aov(formula = combined_data[[i]] ~ factor(Time) + Error(factor(Identifier)),
    data = combined_data)

Grand Mean: 95.35041

Stratum 1: factor(Identifier)

Terms:
                factor(Time) Residuals
Sum of Squares       3568.73 100855.00
Deg. of Freedom            2        53

Residual standard error: 43.62252
Estimated effects may be unbalanced

Stratum 2: Within

Terms:
                factor(Time) Residuals
Sum of Squares      10086.48  34346.42
Deg. of Freedom            2        90

Residual standard error: 19.53527
Estimated effects may be unbalanced

ANOVA results for Average.Stand.Count :

Call:
aov(formula = combined_data[[i]] ~ factor(Time) + Error(factor(Identifier)),
    data = combined_data)

Grand Mean: 195.0613

Stratum 1: factor(Identifier)

Terms:
                factor(Time) Residuals
Sum of Squares       18613.3  645327.9
Deg. of Freedom            2        53

Residual standard error: 110.3449
Estimated effects may be unbalanced

Stratum 2: Within

Terms:
                factor(Time) Residuals
Sum of Squares      13903.64 156505.83
Deg. of Freedom            2        90

Residual standard error: 41.70076
Estimated effects may be unbalanced

ANOVA results for Average.Sitting.Time :

Call:
aov(formula = combined_data[[i]] ~ factor(Time) + Error(factor(Identifier)),
    data = combined_data)

Grand Mean: 1060.594

Stratum 1: factor(Identifier)

Terms:
                factor(Time) Residuals
Sum of Squares       41058.5  971050.4
Deg. of Freedom            2        53

Residual standard error: 135.3577
Estimated effects may be unbalanced

Stratum 2: Within

Terms:
                factor(Time) Residuals
Sum of Squares       40907.8  321689.1
Deg. of Freedom            2        90

Residual standard error: 59.78564
Estimated effects may be unbalanced

ANOVA results for Average.Sedentary.Time :

Call:
aov(formula = combined_data[[i]] ~ factor(Time) + Error(factor(Identifier)),
    data = combined_data)

Grand Mean: 1060.594

Stratum 1: factor(Identifier)

Terms:
                factor(Time) Residuals
Sum of Squares       41058.5  971050.4
Deg. of Freedom            2        53

Residual standard error: 135.3577
Estimated effects may be unbalanced

Stratum 2: Within

Terms:
                factor(Time) Residuals
Sum of Squares       40907.8  321689.1
Deg. of Freedom            2        90

Residual standard error: 59.78564
Estimated effects may be unbalanced

ANOVA results for Adjusted.Average.Sedentary.Time :

Call:
aov(formula = combined_data[[i]] ~ factor(Time) + Error(factor(Identifier)),
    data = combined_data)

Grand Mean: 547.8

Stratum 1: factor(Identifier)

Terms:
                factor(Time) Residuals
Sum of Squares       33686.1  988229.2
Deg. of Freedom            2        53

Residual standard error: 136.5497
Estimated effects may be unbalanced

Stratum 2: Within

Terms:
                factor(Time) Residuals
Sum of Squares      228891.7  419002.2
Deg. of Freedom            2        90

Residual standard error: 68.23181
Estimated effects may be unbalanced

ANOVA results for NumSitToStands :

Call:
aov(formula = combined_data[[i]] ~ factor(Time) + Error(factor(Identifier)),
    data = combined_data)

Grand Mean: 43.93511

Stratum 1: factor(Identifier)

Terms:
                factor(Time) Residuals
Sum of Squares       451.602 17934.991
Deg. of Freedom            2        53

Residual standard error: 18.39554
Estimated effects may be unbalanced

Stratum 2: Within

Terms:
                factor(Time) Residuals
Sum of Squares      268.5332 2939.2314
Deg. of Freedom            2        90

Residual standard error: 5.714729
Estimated effects may be unbalanced

ANOVA results for Average.Sleep :

Call:
aov(formula = combined_data[[i]] ~ factor(Time) + Error(factor(Identifier)),
    data = combined_data)

Grand Mean: 512.7944

Stratum 1: factor(Identifier)

Terms:
                factor(Time) Residuals
Sum of Squares        533.12  65406.35
Deg. of Freedom            2        53

Residual standard error: 35.1295
Estimated effects may be unbalanced

Stratum 2: Within

Terms:
                factor(Time) Residuals
Sum of Squares     154357.43  94158.13
Deg. of Freedom            2        90

Residual standard error: 32.34504
Estimated effects may be unbalanced

ANOVA results for Weekday.Sleep :

Call:
aov(formula = combined_data[[i]] ~ factor(Time) + Error(factor(Identifier)),
    data = combined_data)

Grand Mean: 507.0608

Stratum 1: factor(Identifier)

Terms:
                factor(Time) Residuals
Sum of Squares       2166.43  98667.52
Deg. of Freedom            2        53

Residual standard error: 43.14686
Estimated effects may be unbalanced

Stratum 2: Within

Terms:
                factor(Time) Residuals
Sum of Squares      272364.9  157647.6
Deg. of Freedom            2        90

Residual standard error: 41.8526
Estimated effects may be unbalanced

ANOVA results for Weekend.Sleep :

Call:
aov(formula = combined_data[[i]] ~ factor(Time) + Error(factor(Identifier)), 
    data = combined_data)

Grand Mean: 527.1284

Stratum 1: factor(Identifier)

Terms:
                factor(Time) Residuals
Sum of Squares      32156.68  66885.38
Deg. of Freedom            2        53

Residual standard error: 35.52448
Estimated effects may be unbalanced

Stratum 2: Within

Terms:
                factor(Time) Residuals
Sum of Squares      282742.2  109620.3
Deg. of Freedom            2        90

Residual standard error: 34.89991
Estimated effects may be unbalance