---
title: Matching in vivo and ex vivo MRI of the hippocampus in the same people
layout: post
date: '2017-11-01'
author: paul-yushkevich
---

Many techniques have been proposed for measuring hippocampal subfields on MRI of living people, but they are hard to validate without linking them to the underlying tissue. High-resolution ex vivo MRI can act as a bridge between in vivo MRI and histology.

In *Cerebral Cortex*, [Laura Wisse](/members/laura-wisse.html), [Daniel Adler](/members/daniel-adler.html), [Paul Yushkevich](/members/paul-yushkevich.html) and colleagues evaluated how well information can be matched between in vivo and ex vivo MRI of the same individuals. They registered 10 pairs of in vivo (3 T, 0.4 × 0.4 × 2.6 mm) and ex vivo (9.4 T, 0.2 mm isotropic) scans and described the differences in how the hippocampus appears in each.

To test whether the dataset could validate in vivo segmentation, they applied the automatic subfield segmentation tool [ASHS](/software/ashs.html) to the in vivo scans and compared one of its boundaries to manual tracings on the ex vivo scans, and in two cases on histology.

- Registration between in vivo and ex vivo scans was satisfactory, and ASHS located the boundary with subvoxel accuracy.
- Ex vivo scans showed regional increases in thickness next to the ventricles, which were not explained by scanner, resolution or artifacts.

The results show this kind of dataset can be used to validate, and potentially improve, in vivo segmentation methods.

{%
  include figure.html
  image="images/wp/2016/10/ASHSComp09182015.jpg"
  caption="ASHS segmentation of in vivo MRI alongside ex vivo MRI and annotated histology of the same hippocampus (image from PICSL's earlier website)."
%}

Other PICSL contributors include [Ranjit Ittyerah](/members/ranjit-ittyerah.html) and [Sandhitsu Das](/members/sandhitsu-sandy-das.html).

**Reference:** Wisse LEM, Adler DH, Ittyerah R, et al., Yushkevich PA. Comparison of in vivo and ex vivo MRI of the human hippocampal formation in the same subjects. *Cerebral Cortex*. 2017. [doi:10.1093/cercor/bhw299](https://doi.org/10.1093/cercor/bhw299)
