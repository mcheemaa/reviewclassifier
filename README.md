# Naïve Bayesian Classification

## Introduction

Naïve Bayes Classifier that categorizes movie reviews as positive or negative based off of the text in the review. 



### The Naïve Bayes Algorithm

The probability of a review being positive given a set of features $f$ can be calculated as:

$$P(positive \ | \ f) = P(positive) * \prod^n_{i=1} P(f_i \ | \ positive)$$

Since probabilities can become very small, the product of these numbers can result in underflow. To get around this, we use *log-probabilities* (in which case products become sums).


## Evaluation

To evaluate how well your classifier perfoms, we will train and test your classifier on the given dataset and calculate an f-score for each of the two class (positive and negative). 
