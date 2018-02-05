# Chapter 7 : Statistical Data Analysis

In this chapter, we will cover the following topics:

* [7.1. Exploring a dataset with pandas and matplotlib](01_pandas.md)
* [7.2. Getting started with statistical hypothesis testing — a simple z-test](02_z_test.md)
* [7.3. Getting started with Bayesian methods](03_bayesian.md)
* [7.4. Estimating the correlation between two variables with a contingency table and a chi-squared test](04_correlation.md)
* [7.5. Fitting a probability distribution to data with the maximum likelihood method](05_mlfit.md)
* [7.6. Estimating a probability distribution nonparametrically with a kernel density estimation](06_kde.md)
* [7.7. Fitting a Bayesian model by sampling from a posterior distribution with a Markov Chain Monte Carlo method](07_pymc.md)
* [7.8. Analyzing data with the R programming language in the Jupyter Notebook](08_r.md) *

In the previous chapters, we reviewed technical aspects of high-performance interactive computing in Python. We now begin the second part of this book by illustrating a variety of scientific questions that can be tackled with Python.

In this chapter, we introduce statistical methods for data analysis. In addition to covering statistical packages such as pandas, statsmodels, and PyMC3, we will explain the basics of the underlying mathematical principles. Therefore, this chapter will be most profitable if you have basic experience with probability theory and calculus.

The next chapter, *Chapter 8, Machine Learning*, is closely related; the underlying mathematics is very similar, but the goals are slightly different. In this chapter, we show how to gain insight into real-world data and how to make informed decisions in the presence of uncertainty. In the next chapter, the goal is to learn from data, that is, to generalize and to predict outcomes from partial observations.

In this introduction, we will give a broad, high-level overview of the methods we will see in this chapter.

## What is statistical data analysis?

The goal of statistical data analysis is to understand a complex, real-world phenomenon from partial and uncertain observations. The uncertainty in the data results in uncertainty in the knowledge we get about the phenomenon. A major goal of the theory is to *quantify* this uncertainty.

It is important to make the distinction between the mathematical theory underlying statistical data analysis, and the decisions made after conducting an analysis. The former is perfectly rigorous; perhaps surprisingly, mathematicians were able to build an exact mathematical framework to deal with uncertainty. Nevertheless, there is a subjective part in the way statistical analysis yields actual human decisions. Understanding the risk and the uncertainty behind statistical results is critical in the decision-making process.

In this chapter, we will see the basic notions, principles, and theories behind statistical data analysis, covering in particular how to make decisions with a quantified risk. Of course, we will always show how to implement these methods with Python.

## A bit of vocabulary

There are many terms that need introduction before we get started with the recipes. These notions allow us to classify statistical techniques within multiple dimensions.

### Exploration, Inference, Decision, Prediction

**Exploratory methods** allow us to get a preliminary look at a dataset through basic statistical aggregates and interactive visualization. We covered these basic methods in the first chapter of this book and in the prequel book *IPython for Interactive Computing and Data Visualization, Second Edition*, Packt Publishing. The first recipe of this chapter, *Exploring a dataset with pandas and matplotlib*, shows another example.

**Statistical inference** consists of getting information about an unknown process through partial and uncertain observations. In particular, **estimation** entails obtaining approximate quantities for the mathematical variables describing this process. Three recipes in this chapter deal with statistical inference:

* The *Fitting a probability distribution to data with the maximum likelihood method* recipe
* The *Estimating a probability distribution nonparametrically with a kernel density estimation* recipe
* The *Fitting a Bayesian model by sampling from a posterior distribution with a Markov chain Monte Carlo method* recipe

**Decision theory** allows us to make decisions about an unknown process from random observations, with a controlled risk. The following two recipes show how to make statistical decisions:

* The *Getting started with statistical hypothesis testing – a simple z-test* recipe
* The *Estimating the correlation between two variables with a contingency table and a chi-squared test* recipe

**Prediction** consists of learning from data, that is, predicting the outcomes of a random process based on a limited number of observations. This is the topic of the next chapter, *Chapter 8, Machine Learning*.

### Univariate and Multivariate methods

In most cases, you can consider two dimensions in your data:

* **Observations** (or **samples**, for machine learning people)
* **Variables** (or **features**)

Typically, observations are independent realizations of the same random process. Each observation is made of one or several variables. Most of the time, variables are either numbers, or elements belonging to a finite set (that is, taking a finite number of values). The first step in an analysis is to understand what your observations and variables are.

Your problem is **univariate** if you have one variable. It is **bivariate** if you have two variables and **multivariate** if you have at least two variables. Univariate methods are typically simpler. That being said, univariate methods may be used on multivariate data, using one dimension at a time. Although interactions between variables cannot be explored in that case, it is often an interesting first approach.

### Frequentist and Bayesian methods

There are at least two different ways of considering uncertainty, resulting in two different classes of methods for inference, decision, and other statistical questions. These are called **frequentist and Bayesian methods**. Some people prefer frequentist methods, while others prefer Bayesian methods.

Frequentists interpret a probability as a *statistical average* across many independent realizations (law of large numbers). Bayesians interpret it as a *degree of belief* (no need for many realizations). The Bayesian interpretation is very useful when only a single trial is considered. In addition, Bayesian theory takes into account our **prior knowledge** about a random process. This prior probability distribution is updated into a posterior distribution as we get more and more data.

Both frequentist and Bayesian methods have their advantages and disadvantages. For instance, one could say that frequentist methods might be easier to apply than Bayesian methods, but more difficult to interpret. For classic misuses of frequentist methods, see http://www.refsmmat.com/statistics/.

In any case, if you are a beginner in statistical data analysis, you probably want to learn the basics of both approaches before choosing sides. This chapter introduces you to both types of methods.

The following recipes are exclusively Bayesian:

* The *Getting started with Bayesian methods* recipe
* The *Fitting a Bayesian model by sampling from a posterior distribution with a Markov chain Monte Carlo method* recipe

Jake Vanderplas has written several blog posts about frequentism and Bayesianism, with examples in Python. The first post of the series is available at http://jakevdp.github.io/blog/2014/03/11/frequentism-and-bayesianism-a-practical-intro/.

### Parametric and non-parametric inference methods

In many cases, you base your analysis on a **probabilistic model**. This model describes how your data is generated. A probabilistic model has no reality; it is only a mathematical object that guides you in your analysis. A good model can be helpful, whereas a bad model may misguide you.

With a **parametric method**, you assume that your model belongs to a known family of probability distributions. The model has one or multiple numerical *parameters* that you can *estimate*.

With a **nonparametric model**, you do not make such an assumption in your model. This gives you more flexibility. However, these methods are typically more complicated to implement and to interpret.

The following recipes are parametric and nonparametric, respectively:

* The *Fitting a probability distribution to data with the maximum likelihood method* recipe
* The *Estimating a probability distribution nonparametrically with a kernel density estimation* recipe

This chapter only gives you an idea of the wide range of possibilities that Python offers for statistical data analysis. You can find many books and online courses that cover statistical methods in much greater detail, such as:

* Statistics resources on Awesome Math, available at https://github.com/rossant/awesome-math#statistics
* Statistics on WikiBooks at http://en.wikibooks.org/wiki/Statistics
* Free statistical textbooks available at http://stats.stackexchange.com/questions/170/free-statistical-textbooks
