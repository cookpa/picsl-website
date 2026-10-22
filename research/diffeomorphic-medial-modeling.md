---
title: Diffeomorphic medial modeling
layout: post
date: '2019-06-01'
author: alison-pouch
---

Shape models that describe objects by their medial axis, or skeleton, provide rich geometric features for analyzing sheet-like biological structures such as the myocardium.

At Information Processing in Medical Imaging (IPMI 2019), [Paul Yushkevich](/members/paul-yushkevich.html), [Ahmed Aly](/members/ahmed-aly.html), [Jiancong Wang](/members/jiancong-wang.html), [Long Xie](/members/long-xie.html), Robert Gorman, Laurent Younes and [Alison Pouch](/members/alison-pouch.html) presented a shape analysis approach that combines the benefits of medial shape modeling and diffeomorphometry.

The algorithm matches shapes using diffeomorphic flows, under constraints that approximately preserve the geometry of the medial axis during the deformation. As a result, the medial axes of similar shapes stay in correspondence. The approach was evaluated by modeling the shape of the left ventricular wall from 3D echocardiography.

{%
  include figure.html
  image="images/research/diffeomorphic-medial.svg"
  width="600px"
  caption="Main ideas of diffeomorphic medial modeling (illustration)."
%}

**Reference:** Yushkevich PA, Aly A, Wang J, Xie L, Gorman RC, Younes L, Pouch AM. Diffeomorphic medial modeling. *Information Processing in Medical Imaging (IPMI)*. 2019. [doi:10.1007/978-3-030-20351-1_16](https://doi.org/10.1007/978-3-030-20351-1_16)
