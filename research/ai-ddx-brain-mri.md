---
title: An AI system approaching neuroradiologist-level diagnosis on brain MRI
layout: post
date: '2020-06-01'
author: jim-gee
---

Artificial intelligence (AI) shows promise across radiology, but had not been shown to generate differential diagnoses for both common and rare diseases on brain MRI.

In *Radiology*, Andreas Rauschecker, Jeffrey Rudie, [Long Xie](/members/long-xie.html), [Jiancong Wang](/members/jiancong-wang.html), [Tessa Cook](/members/tessa-cook.html), [Jim Gee](/members/jim-gee.html) and colleagues tested an AI system that combines data-driven and expert-knowledge methods:

1. Deep learning detects lesions.
2. Atlas-based registration and segmentation extract 18 quantitative imaging features.
3. Bayesian inference combines the imaging features with five clinical features to produce a probability-ranked differential diagnosis.

In 92 independent test patients with 19 common and rare diagnoses, the AI system's top three diagnoses were correct 91% of the time. That was similar to academic neuroradiologists (86%) and better than radiology residents (56%), general radiologists (57%) and neuroradiology fellows (77%). Unlike the radiologists, who were much more accurate for common than for rare diseases, the AI system's accuracy did not depend on how common the disease was.

{%
  include figure.html
  image="images/research/ai-ddx-brain-mri.svg"
  width="600px"
  caption="Accuracy of the top three differential diagnoses, as reported in the paper."
%}

**Reference:** Rauschecker AM, Rudie JD, Xie L, et al., Mohan S, Gee JC. Artificial intelligence system approaching neuroradiologist-level differential diagnosis accuracy at brain MRI. *Radiology*. 2020. [doi:10.1148/radiol.2020190283](https://doi.org/10.1148/radiol.2020190283)
