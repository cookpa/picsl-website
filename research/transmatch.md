---
title: 'TransMatch: transformer-based feature matching for deformable registration'
layout: post
date: '2024-01-01'
author: jim-gee
---

Deformable image registration depends on establishing correspondences between regions of two images. Traditional feature-based methods match features explicitly but iteratively, which can take minutes per registration. Learning-based methods such as VoxelMorph and TransMorph are fast and competitive, but they are typically single-stream: the two images are stacked into one input, and the correspondence between them is only learned implicitly.

In *IEEE Transactions on Medical Imaging*, Zeyuan Chen, [Yuanjie Zheng](/members/yuanjie-zheng.html) and [Jim Gee](/members/jim-gee.html) introduce **TransMatch**, an end-to-end, unsupervised, dual-stream registration framework:

- Each image is processed by its own branch, which extracts features independently.
- Features are then matched explicitly between the two images at multiple levels, using the query-key matching idea from the Transformer's self-attention mechanism.

On three 3D brain MRI datasets (LPBA40, IXI and OASIS), TransMatch achieved state-of-the-art performance on several metrics compared with widely used methods including SyN, NiftyReg, VoxelMorph, CycleMorph, ViT-V-Net and TransMorph.

{%
  include figure.html
  image="images/research/transmatch.svg"
  width="600px"
  caption="TransMatch processes each image in its own stream and matches features explicitly at multiple levels."
%}

**Reference:** Chen Z, Zheng Y, Gee JC. TransMatch: a transformer-based multilevel dual-stream feature matching network for unsupervised deformable image registration. *IEEE Transactions on Medical Imaging*. 2024. [doi:10.1109/TMI.2023.3288136](https://doi.org/10.1109/TMI.2023.3288136)
