---
title: "Large language model ensembles turn echocardiography reports into structured data"
layout: post
date: 2025-05-01
author: alison-pouch
---

Intraoperative transesophageal echocardiography (TEE) is routine in cardiac surgery, and each exam produces a free-text report. These reports hold valuable measurements of heart function before and after surgery, but because they are unstructured, using them for research or quality improvement has meant reading and coding each one by hand.

In a study published in the *British Journal of Anaesthesia*, Emily MacKay, [Alison Pouch](/members/alison-pouch.html) and colleagues tested whether open-source large language models (LLMs) could do this extraction automatically. The team sampled 600 intraoperative TEE reports from 7,106 adult cardiac surgery patients at two Penn hospitals. They asked five open-source LLMs to extract three key parameters from the presurgical and postsurgical sections of each report: left ventricular ejection fraction, right ventricular systolic function, and tricuspid regurgitation.

Instead of trusting any single model, the study combined the five models into an ensemble and compared four voting rules, from requiring all five models to agree (unanimous) to accepting the answer given by at least two (plurality):

- The **unanimous** ensemble was the most trustworthy when it returned an answer, with 99.4% presurgical and 97.9% postsurgical consensus accuracy. It returned an answer for only about 81% of reports.
- The **plurality** ensemble extracted data from almost every report (99.4% presurgical, 98.9% postsurgical) with the highest raw accuracy (96.1% and 93.7%), at the cost of a higher error rate.

The voting rule therefore lets researchers choose between completeness and certainty, depending on how the data will be used. The study shows that consensus-based ensembles of open-source LLMs can reliably turn unstructured clinical text into structured data.

{%
  include figure.html
  image="images/research/llm-echo-ensemble.svg"
  width="600px"
  caption="Five open-source LLMs read each TEE report independently, and a voting rule combines their answers into structured data."
%}

**Reference:** MacKay EJ, Goldfinger S, Chan TJ, Grasfield RH, Eswar VJ, Li K, Cao Q, Pouch AM. Automated structured data extraction from intraoperative echocardiography reports using large language models. *British Journal of Anaesthesia*. 2025. [doi:10.1016/j.bja.2025.01.028](https://doi.org/10.1016/j.bja.2025.01.028)
