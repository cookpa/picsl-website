---
title: 'NODEO: image registration with neural ordinary differential equations'
layout: post
date: '2022-06-19'
author: jim-gee
---

Deformable image registration, finding the spatial correspondence between images, is one of the most important problems in medical image analysis.

At the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2022), [Yifan Wu](/members/yifan-wu.html), Tom Jiahao, [Jiancong Wang](/members/jiancong-wang.html), [Paul Yushkevich](/members/paul-yushkevich.html), M. Hsieh and [Jim Gee](/members/jim-gee.html) presented **NODEO**, a generic diffeomorphic registration framework built on neural ordinary differential equations (neural ODEs).

NODEO models each voxel as a moving particle, and treats all the voxels of a 3D image as a high-dimensional dynamical system whose trajectory defines the deformation. A deep neural network models the dynamics, and the method optimizes the dynamical system and the resulting transformation together for each image pair. The formulation makes it possible to impose constraints along the transformation to keep it regular.

NODEO outperformed benchmark methods on several metrics, and the authors showed that it can be extended to register multiple sets of images with a single form of transformation.

{%
  include figure.html
  image="images/research/nodeo.svg"
  width="600px"
  caption="The NODEO formulation (illustration)."
%}

**Reference:** Wu Y, Jiahao TZ, Wang J, Yushkevich PA, Hsieh M, Gee JC. NODEO: a neural ordinary differential equation based optimization framework for deformable image registration. *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. 2022. [doi:10.1109/CVPR52688.2022.02014](https://doi.org/10.1109/CVPR52688.2022.02014)
