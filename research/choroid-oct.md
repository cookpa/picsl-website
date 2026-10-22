---
title: Deep learning segments the choroid in OCT despite retinal disease
layout: post
date: '2017-09-14'
author: jim-gee
---

The choroid supplies the parts of the eye responsible for vision, and changes in it are associated with age-related macular degeneration (AMD), central serous chorioretinopathy, retinitis pigmentosa and diabetes. Choroid thickness can predict treatment response and visual function. Most methods for segmenting the choroid in optical coherence tomography (OCT) first detect the retinal boundaries, and they fail when disease disrupts or reshapes those boundaries.

At the Ophthalmic Medical Image Analysis (OMIA) workshop at MICCAI 2017, [Min Chen](/members/min-chen.html), [Jiancong Wang](/members/jiancong-wang.html), Ipek Oguz, Brian VanderBeek and [Jim Gee](/members/jim-gee.html) showed that a convolutional neural network can detect and segment the choroid without first delineating the retinal layers, avoiding the need to model unpredictable pathological changes in the retina.

In 62 manually delineated choroid segmentations from enhanced depth imaging OCT of patients with AMD, the method's accuracy exceeded that reported by state-of-the-art approaches on healthy retinas, with high accuracy overall on images with pathology.

{%
  include figure.html
  image="images/research/choroid-oct.svg"
  width="600px"
  caption="The approach (illustration)."
%}

**Reference:** Chen M, Wang J, Oguz I, VanderBeek BL, Gee JC. Automated segmentation of the choroid in EDI-OCT images with retinal pathology using convolution neural networks. *Fetal, Infant and Ophthalmic Medical Image Analysis (OMIA, MICCAI workshop)*. 2017. [doi:10.1007/978-3-319-67561-9_20](https://doi.org/10.1007/978-3-319-67561-9_20)
