---
title: An open-source tool for designing synthetic skeletons
layout: post
date: '2024-05-01'
author: alison-pouch
---

Deformable medial modeling represents anatomy by its skeleton, an approach that supports statistical shape analysis and patient-specific measurements such as locally varying thickness. It works by deforming a predefined synthetic skeleton, or template, to fit each anatomical structure. Until now, the lack of software for creating these skeletons has limited the method's wider use.

In the *Journal of Medical Imaging*, Christian Herz, [Abdullah Aly](/members/abdullah-aly.html), [Paul Yushkevich](/members/paul-yushkevich.html), [Alison Pouch](/members/alison-pouch.html) and colleagues present an open-source user interface for designing synthetic skeletons, built into 3D Slicer. A user imports and skeletonizes a 3D segmentation, then interactively places points in 3D and triangulates the medial surface to get the desired branching structure.

Three users designed skeletons for anatomies with a range of topologies: the placenta, aortic root wall, mitral valve, cardiac ventricles and uterus. The skeletons worked with both skeleton-first and boundary-first medial modeling software, and the fitted models represented the original segmentations accurately.

{%
  include figure.html
  image="images/research/synthetic-skeletons.svg"
  width="600px"
  caption="The synthetic skeleton design workflow (illustration)."
%}

**Reference:** Herz C, Vergnet N, Tian S, et al., Yushkevich PA, Pouch AM. Open-source graphical user interface for the creation of synthetic skeletons for medical image analysis. *Journal of Medical Imaging*. 2024. [doi:10.1117/1.JMI.11.3.036001](https://doi.org/10.1117/1.JMI.11.3.036001)
