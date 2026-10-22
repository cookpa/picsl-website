---
title: "FireANTs: fast, training-free image registration on the GPU"
layout: post
date: 2026-06-09
author: jim-gee
---

Image registration, the problem of finding a smooth deformation that brings one image into alignment with another, sits underneath almost every quantitative imaging study: building atlases, comparing subjects, tracking change over time, and fusing modalities. For more than a decade, [ANTs](/software/ants.html), developed at PICSL, has been a community standard for accurate diffeomorphic registration. Its main drawback is speed. Deep learning registration methods are fast at inference, but they need long training, use a lot of memory, and often fail when the data look different from what they were trained on.

In a paper published in *Nature Communications*, [Rohit Jena](/members/rohit-jena.html), Pratik Chaudhari and [Jim Gee](/members/jim-gee.html) introduce **FireANTs**, a training-free, GPU-accelerated algorithm for multi-scale diffeomorphic image matching. FireANTs treats registration as an optimization on the space of diffeomorphisms and uses adaptive Riemannian optimization to deal with the poor conditioning that slows down classical methods.

Key results:

- More than twice as fast as ANTs on a CPU, and two orders of magnitude faster on a GPU.
- Inference speed competitive with deep learning methods, while using up to 10× less memory.
- Robust across modalities, species and organs with no domain-specific training or tuning, including first place in the mouse brain task of the RnR-ExM challenge.
- Fast enough that large hyperparameter searches, and population templates at very high resolution, become practical.

{%
  include figure.html
  image="images/research/fireants-templates.jpg"
  caption="Brain templates built with ANTs (left in each panel) and FireANTs (right), including a 25 μm fMOST mouse brain template. Figure 6 from Jena, Chaudhari & Gee, *Nature Communications* (2026), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)."
%}

**Reference:** Jena R, Chaudhari P, Gee JC. Adaptive Riemannian optimization for multi-scale diffeomorphic matching. *Nature Communications*. 2026. [doi:10.1038/s41467-026-72508-3](https://doi.org/10.1038/s41467-026-72508-3)
