---
title: Open-source tools for 4D cardiac image analysis
layout: post
date: '2025-06-01'
author: alison-pouch
---

4D cardiac imaging, a 3D image of the heart at every point of the cardiac cycle, gives rich insight into how heart structures move. Analyzing it with conventional 3D software is laborious, since each time point has to be handled separately.

In a paper at Functional Imaging and Modeling of the Heart (FIMH 2025), [Jilei Hao](/members/jilei-hao.html), [Paul Yushkevich](/members/paul-yushkevich.html), [Alison Pouch](/members/alison-pouch.html) and colleagues introduce three open-source applications designed natively for 4D data:

- **[ITK-SNAP](https://www.itksnap.org) 4** for 4D image input and output, visualization and segmentation.
- **Greedy Propagation** for registration within an image series, turning a few sparse 3D segmentations into a full 4D segmentation.
- **Scherzo** for fast, web-based generation and visualization of 4D models.

The tools support common 4D cardiac image formats and offer a streamlined user experience. Experiments on their core features demonstrate feasibility and consistency.

{%
  include figure.html
  image="images/research/4d-cardiac-tools.svg"
  width="600px"
  caption="Three tools that handle every stage of a 4D cardiac analysis."
%}

**Reference:** Hao J, Yushkevich PA, Dong NJ, Amin S, Guo Z, Yushkevich N, Aggarwal A, Pouch AM. Streamlining 4D cardiac image workflows: open-source tools for segmentation, registration, and visualization. *Functional Imaging and Modeling of the Heart (FIMH)*. 2025. [doi:10.1007/978-3-031-94562-5_15](https://doi.org/10.1007/978-3-031-94562-5_15)
