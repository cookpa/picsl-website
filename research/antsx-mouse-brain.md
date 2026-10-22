---
title: ANTsX pipelines for mapping the mouse brain
layout: post
date: '2025-11-22'
author: jim-gee
---

The BRAIN Initiative Cell Census Network (BICCN) is building a comprehensive reference atlas of cell types in the mouse brain. A central challenge is bringing very different datasets, acquired with different imaging, tissue processing and profiling methods, into shared coordinate frameworks.

In a paper in *Nature Communications*, Nicholas Tustison, [Min Chen](/members/min-chen.html), [Jeffrey Duda](/members/jeffrey-duda.html), [Jim Gee](/members/jim-gee.html) and colleagues present mouse brain mapping pipelines built on the [Advanced Normalization Tools Ecosystem (ANTsX)](/software/ants.html). The pipelines align:

- MERFISH spatial transcriptomics and high-resolution fMOST morphology data to the Allen Common Coordinate Framework (CCFv3).
- Developmental MRI and light-sheet fluorescence microscopy data to the Developmental CCF (DevCCF).

The paper also introduces two new methods: a velocity field approach for continuous interpolation between developmental time points, and a deep learning framework for automatic brain parcellation trained on minimally annotated, publicly available data. All workflows are open-source and reproducible, and the paper gives practical guidance for choosing a strategy for new types of data.

{%
  include figure.html
  image="images/research/antsx-mouse.jpg"
  caption="Developmental mouse brain templates warped across time points with the DevCCF velocity flow model. Figure 5 from Tustison et al., *Nature Communications* (2025), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)."
%}

**Reference:** Tustison NJ, Chen M, Kronman FN, Duda JT, et al., Gee JC. The ANTsX ecosystem for mapping the mouse brain. *Nature Communications*. 2025. [doi:10.1038/s41467-025-66741-5](https://doi.org/10.1038/s41467-025-66741-5)
