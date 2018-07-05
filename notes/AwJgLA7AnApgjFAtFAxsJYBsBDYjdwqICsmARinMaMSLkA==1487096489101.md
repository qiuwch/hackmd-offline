# 2/14 Google research

Algorithmic bias in artificial intelligence

Microsoft research -> Google research

Larry Zitnick
Ross Girshick
Josh Lovejoy.
Margaret Mitchell
Ishan Misra, student of CMU

general AI

bias: a **systematic** deviation from **full** ground truth

overgeneralization bias
dataset bias
reporting bias
What the meaning...

Why bias?

**goals set by human**, **data collected by human**.

Active vision is related to dataset bias.

> Information technology can amplify misinformation
> Legal software can propagate discrimination

If we want to make our technology **universally accessible and useful**, what we develop - apps, infrastructure, models - need to **work for everyone** (avoid bias).

Human data perpetuates human biases 

Training data are collected and clasified -> algorithms are programmed

How does bias get created the picture.
![](https://i.imgur.com/JqHbZsG.jpg)

Image search of professor

The the top professor returned. No picture of female. The bias in the sofa data.

**Fairness**: no one subcategory is disproportionately affected by prediction accuracy.

Preprocessing, add more data
Adjust loss function
Postprocessing, correction.

World learning: ensure frequency in data reflects real world frequencies.


The distribution of the real world, is this really important??

**Bias in AI** -> **Fairness in AI**

## Reporting bias in vision and language

annotated data is limited.

exhaustively annotated data is expensive

What is the relationship with bias??

WILD labeled images

**The annotation missed a lot of things, these things can be helpful for understanding the world**

**Human reporting bias** is the data annotation procedure.

Humans subjectively decide **what to report** and **what not to report** in an image. Can be used as a **signal**.

Signal??

So much information that human can not throughly annotate.

## Problem setup

Input: Image, human-biased labels
Goal: learn visually correct classifiers
Challenge: Do not have some label, have what humans report.

A lot of things going on, so that annotator won't report everything.

**Human biased labels**

**Use synthetic data to systematically study the human bias**

Check what is reported by humans.

visual presence *v*
Relevance *r*
$h=f(r,v)$

Predict what is there and predict what human will say. **Noise estimator** predict the human bias.

**How to get the visual ground truth, is it what synthetic data can do?**

The linguistic data?

The yellow sky, which is very unfrequent.

Evaluate using $y$ (human-biased) and $z$ (annotated)
