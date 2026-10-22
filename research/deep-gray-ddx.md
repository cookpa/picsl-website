---
title: Explainable AI for deep gray matter diagnosis on clinical brain MRI
layout: post
date: '2020-09-01'
author: jim-gee
---

Diseases involving the deep gray matter of the brain are numerous and often rare, which makes them hard for non-specialists to diagnose on MRI.

In *Radiology: Artificial Intelligence*, Jeffrey Rudie, Andreas Rauschecker, [Long Xie](/members/long-xie.html), [Jiancong Wang](/members/jiancong-wang.html), [Tessa Cook](/members/tessa-cook.html), [Jim Gee](/members/jim-gee.html) and colleagues developed and validated a hybrid AI system for 35 neurologic diseases of the deep gray matter. Three-dimensional convolutional neural networks and atlas-based image processing extract 11 imaging features, and expert-derived Bayesian networks combine them with clinical information to generate differential diagnoses.

- On the held-out test set of 102 patients, the imaging pipeline detected the 11 features with 89% accuracy relative to academic neuroradiologists.
- The system's top three diagnoses were correct 85% of the time, better than radiology residents (56%), general radiologists (53%) and neuroradiology fellows (72%), and not different from academic neuroradiologists (84%).

Because it reports disease burden, interpretable intermediate features and a probabilistic diagnosis together, this kind of system could support clinical decisions for common and rare diseases.

{%
  include figure.html
  image="images/research/deep-gray-ddx.svg"
  width="600px"
  caption="Accuracy of the top three differential diagnoses, as reported in the paper."
%}

**Reference:** Rudie JD, Rauschecker AM, Xie L, et al., Mohan S, Gee JC. Subspecialty-level deep gray matter differential diagnoses with deep learning and Bayesian networks on clinical brain MRI: a pilot study. *Radiology: Artificial Intelligence*. 2020. [doi:10.1148/ryai.2020190146](https://doi.org/10.1148/ryai.2020190146)
