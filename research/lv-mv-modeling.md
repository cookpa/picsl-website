---
title: Fully automated modeling of the left ventricle and mitral valve
layout: post
date: '2022-08-01'
author: paul-yushkevich
---

In ischemic mitral regurgitation, the mitral valve leaks because the left ventricle has remodeled after a heart attack. Surgical decisions would benefit from a fully automated tool that analyzes the left ventricle and mitral valve together from the 3D transesophageal echocardiography (TEE) acquired just before surgery. Earlier methods were semi-automatic, left out the ventricle, and could produce valve models whose leaflets intersect themselves.

In *Medical Image Analysis*, [Ahmed Aly](/members/ahmed-aly.html), [Pulkit Khandelwal](/members/pulkit-khandelwal.html), [Abdullah Aly](/members/abdullah-aly.html), [Alison Pouch](/members/alison-pouch.html), [Paul Yushkevich](/members/paul-yushkevich.html) and colleagues developed and validated a fully automated algorithm for segmenting and modeling the left ventricular mitral valve complex:

- **Segmentation** with nnU-Net, evaluated against expert manual segmentation on two datasets from separate institutions, gave average Dice scores of 0.82 and 0.87.
- **Shape modeling** by fitting a deformable medial template to the segmentation. The models matched the segmentations with Dice scores of 0.93 to 0.94 for the left ventricle and 0.75 to 0.81 for the mitral valve.

This is a substantial step toward automatic analysis of the left ventricle and mitral valve in the operating room.

{%
  include figure.html
  image="images/research/lv-mv-modeling.svg"
  width="600px"
  caption="The automated segmentation and modeling pipeline (illustration)."
%}

**Reference:** Aly AH, Khandelwal P, Aly AH, et al., Pouch AM, Gorman RC, Yushkevich PA. Fully automated 3D segmentation and diffeomorphic medial modeling of the left ventricle mitral valve complex in ischemic mitral regurgitation. *Medical Image Analysis*. 2022. [doi:10.1016/j.media.2022.102513](https://doi.org/10.1016/j.media.2022.102513)
