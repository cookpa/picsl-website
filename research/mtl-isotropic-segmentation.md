---
title: Sharper medial temporal lobe segmentation from isotropic training
layout: post
date: '2026-10-15'
author: paul-yushkevich
---

The medial temporal lobe (MTL) is affected early in Alzheimer's disease, and its subregions are valuable imaging biomarkers. But the T2-weighted MRI scans used to see them are highly anisotropic, with thick slices that limit how well features such as thickness can be measured.

In a study in *NeuroImage*, [Yue Li](/members/yue-li.html), [Pulkit Khandelwal](/members/pulkit-khandelwal.html), [Rohit Jena](/members/rohit-jena.html), [Paul Yushkevich](/members/paul-yushkevich.html) and colleagues propose a segmentation framework that works in isotropic space. An implicit neural representation builds an isotropic training atlas from the low-resolution T2-weighted data, with T1-weighted MRI as an auxiliary input.

In an independent test set:

- Morphological measures from the isotropic model had stronger effect sizes than those from anisotropic models in separating people with mild cognitive impairment from cognitively unimpaired individuals.
- The isotropic measures were more stable in test-retest analysis.

The approach improves the reliability of MTL subregion biomarkers without additional manual atlas annotation.

{%
  include figure.html
  image="images/research/mtl-isotropic-inr.svg"
  width="600px"
  caption="An implicit neural representation turns anisotropic T2-weighted data into an isotropic training atlas (illustration)."
%}

Other PICSL contributors include [Long Xie](/members/long-xie.html), [Amanda Denning](/members/amanda-denning.html), [Laura Wisse](/members/laura-wisse.html) and [Sandhitsu Das](/members/sandhitsu-sandy-das.html).

**Reference:** Li Y, Khandelwal P, Jena R, et al., Wisse LEM, Das SR, Wolk DA, Yushkevich PA. Achieving detailed medial temporal lobe segmentation with upsampled isotropic training from implicit neural representation. *NeuroImage*. 2026;342:122294. [doi:10.1016/j.neuroimage.2026.122294](https://doi.org/10.1016/j.neuroimage.2026.122294)
