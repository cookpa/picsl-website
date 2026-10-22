---
title: A pipeline for MRI-guided histology in brain banking
layout: post
date: '2025-05-28'
author: paul-yushkevich
---

Neuropathological examination after death remains the gold standard for diagnosing neurodegenerative diseases, but it usually samples only a handful of standard brain regions and can miss areas affected by Alzheimer's disease and related disorders. Ultra-high-resolution postmortem MRI can point to additional regions worth sampling, yet there have been no standard guidelines for combining MRI and histology in a traditional brain bank.

In a paper in *Acta Neuropathologica Communications*, [Chinmayee Athalye](/members/chinmayee-athalye.html), [Paul Yushkevich](/members/paul-yushkevich.html) and colleagues describe a complete protocol for 7 tesla MRI-guided histopathological sampling of whole brain hemispheres, with whole-slide digital imaging and quantitative analysis. The pipeline is designed for high-volume brain banking:

- **Patient-specific 3D-printed molds**, built from each hemisphere's postmortem MRI, guide standardized cutting of the tissue and keep a permanent spatial reference between MRI and tissue.
- A **semi-automated MRI-to-histology registration** pipeline links each tissue sample back to its location in the MRI.
- A **quantitative pathology scoring system** based on weakly supervised deep learning measures pathology on the digitized slides.

Validated in 29 brains across the Alzheimer's disease spectrum, the protocol revealed correlations between cortical thickness and phosphorylated tau accumulation. It offers a scalable, reproducible way to run large studies that integrate histology with neuroimaging.

{%
  include figure.html
  image="images/research/mri-guided-histology.jpg"
  caption="Hemisphere slabbing guided by a custom 3D-printed mold built from the donor's postmortem MRI. Figure 4 from Athalye et al., *Acta Neuropathologica Communications* (2025), [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)."
%}

Other PICSL contributors include [Zahra Khodakarami](/members/zahra-khodakarami.html), [Pulkit Khandelwal](/members/pulkit-khandelwal.html), [Lisa Levorse](/members/lisa-levorse.html), [Sydney Lim](/members/sydney-lim.html), [Ranjit Ittyerah](/members/ranjit-ittyerah.html) and [Sandhitsu Das](/members/sandhitsu-sandy-das.html).

**Reference:** Athalye C, Bahena A, Khandelwal P, et al., Yushkevich PA. Operationalizing postmortem pathology-MRI association studies in Alzheimer's disease and related disorders with MRI-guided histology sampling. *Acta Neuropathologica Communications*. 2025. [doi:10.1186/s40478-025-02030-y](https://doi.org/10.1186/s40478-025-02030-y)
