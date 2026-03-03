# Statistical Modeling Projects

This folder contains statistical modeling projects developed in the context of quantitative and variationist linguistics.

All analyses are implemented in R using RMarkdown.

## Methods Used

- Linear regression  
- Logistic regression  
- Mixed-effects models (lmer)  
- Model comparison  
- Diagnostic checks  
- Interpretation of fixed and random effects  

Main packages:

- tidyverse  
- broom  
- car  
- languageR  
- lme4  

---

## Projects

### Linguistic Diversity Regression

Multiple linear regression modeling linguistic diversity.

Includes:

- Log-transformation  
- Multicollinearity diagnostics (VIF)  
- Model interpretation  
- Confidence intervals and visualization  

File:  
`linguistic_diversity_regression_analysis.Rmd`

---

### Dative Alternation – Logistic Regression

Binomial logistic regression predicting PP vs NP realization in English dative constructions.

Predictors:

- Animacy of recipient  
- Length of recipient  

Includes probability estimation and visualization of predicted effects.

File:  
`dative_alternation_logistic_regression.Rmd`

---

### That-Omission Analysis

Variationist analysis of that-omission in English complement clauses.

This project replicates a quantitative approach inspired by Tagliamonte, using logistic regression to model the effect of linguistic predictors on the presence or absence of *that*.

File:  
`That_omission_analysis.Rmd`

---

### Mixed-Effects Model Analysis

Mixed-effects modeling using random intercepts (and slopes where applicable), including model comparison and interpretation of fixed and random effects.

File:  
`mixed_effects_model_analysis.Rmd`
