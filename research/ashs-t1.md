---
title: 'ASHS-T1: segmenting medial temporal lobe subregions on routine T1 MRI'
layout: post
date: '2019-08-15'
author: paul-yushkevich
---

The subregions of the medial temporal lobe (MTL) are the first to be affected by tau tangles in Alzheimer's disease (AD), which makes them promising biomarkers. Segmenting them automatically on standard T1-weighted MRI is hard: the MTL cortex varies a lot between people, and the dura mater looks similar to gray matter on T1 MRI, so standard tools often mistake one for the other.

In *Human Brain Mapping*, [Long Xie](/members/long-xie.html), [Paul Yushkevich](/members/paul-yushkevich.html) and colleagues built a new atlas set from 15 cognitively normal older adults and 14 people with mild cognitive impairment, with the dura given its own label. Used with the multi-atlas pipeline [ASHS](/software/ashs.html) (ASHS-T1), it segments the anterior and posterior hippocampus, entorhinal cortex, Brodmann areas 35 and 36, and parahippocampal cortex.

- Cross-validation showed good accuracy, with only 6.5% of the dura mislabeled as gray matter, compared with 62.4% for FreeSurfer.
- Applied to 663 ADNI participants, ASHS-T1 detected volume and thickness loss in BA35, entorhinal cortex and posterior hippocampus in early prodromal AD, and in all subregions at later stages.

The atlas and ASHS-T1 are publicly available for early diagnosis, disease monitoring and brain-behavior studies.

{%
  include figure.html
  image="images/research/ashs-t1.svg"
  width="600px"
  caption="The ASHS-T1 approach (illustration)."
%}

Other PICSL contributors include [Laura Wisse](/members/laura-wisse.html), [Robin de Flores](/members/robin-deflores.html) and [Sandhitsu Das](/members/sandhitsu-sandy-das.html).

**Reference:** Xie L, Wisse LEM, Pluta J, et al., Yushkevich PA. Automated segmentation of medial temporal lobe subregions on in vivo T1-weighted MRI in early stages of Alzheimer's disease. *Human Brain Mapping*. 2019. [doi:10.1002/hbm.24607](https://doi.org/10.1002/hbm.24607)
