---
title: Segmenting the left ventricle and mitral valve together in 3D echo
layout: post
date: '2019-01-01'
author: alison-pouch
---

Ischemic mitral regurgitation (IMR) is mainly a disease of the left ventricle: after a heart attack, the ventricle remodels and the mitral valve stops closing properly. Automated methods had analyzed the mitral valve and the left ventricle separately, so they could not capture how the two interact in this disease.

At the Statistical Atlases and Computational Models of the Heart (STACOM) workshop, [Ahmed Aly](/members/ahmed-aly.html), [Abdullah Aly](/members/abdullah-aly.html), [Paul Yushkevich](/members/paul-yushkevich.html), [Alison Pouch](/members/alison-pouch.html) and colleagues used multi-atlas label fusion to segment the left ventricular mitral valve complex together in pre-operative 3D transesophageal echocardiography.

The preliminary pipeline achieved an average Dice coefficient of 0.78. Patient-specific segmentations like these could enable statistical shape analysis for predicting clinical outcomes and stratifying surgical risk. The work was later extended to a [fully automated deep learning and medial modeling pipeline](/research/lv-mv-modeling.html).

{%
  include figure.html
  image="images/research/lv-mv-segmentation-stacom.svg"
  width="600px"
  caption="The segmentation approach (illustration)."
%}

**Reference:** Aly AH, Aly AH, Elrakhawy M, et al., Yushkevich PA, Pouch AM. Semi-automated image segmentation of the midsystolic left ventricular mitral valve complex in ischemic mitral regurgitation. *Statistical Atlases and Computational Models of the Heart (STACOM)*. 2019. [doi:10.1007/978-3-030-12029-0_16](https://doi.org/10.1007/978-3-030-12029-0_16)
