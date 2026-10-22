---
title: 4D modeling of normal and leaking mitral valves
layout: post
date: '2021-01-01'
author: alison-pouch
---

Studying how the mitral valve moves in living patients depends on image analysis that accurately reconstructs the valve's shape and motion. Patient-specific models of both normal and leaking (regurgitant) valves can feed biomechanical analyses and shed light on diseases such as ischemic mitral regurgitation (IMR).

In *Experimental Mechanics*, [Ahmed Aly](/members/ahmed-aly.html), [Abdullah Aly](/members/abdullah-aly.html), [Paul Yushkevich](/members/paul-yushkevich.html), [Alison Pouch](/members/alison-pouch.html) and colleagues present a framework for 4D segmentation and geometric modeling of the mitral valve in real-time 3D echocardiography, which is used for pre-operative planning of mitral interventions. The framework combines groupwise multi-atlas label fusion and template-based medial modeling with Kalman filtering to produce descriptive, temporally consistent models of the valve over the cardiac cycle.

The method was evaluated on image series from 28 patients, 14 with normal valves and 14 with severe IMR, totaling 613 3D images. Each 3D segmentation was validated against manual tracing, and the segmentations were consistent over time. The approach enables reliable, non-invasive comparison of annular and leaflet dynamics, with future applications in strain estimation, fluid dynamics simulation and surgical risk stratification.

{%
  include figure.html
  image="images/research/4d-mitral-valve.svg"
  width="600px"
  caption="The 4D modeling framework (illustration)."
%}

**Reference:** Aly AH, Aly AH, Lai EK, et al., Yushkevich PA, Pouch AM. In vivo image-based 4D modeling of competent and regurgitant mitral valve dynamics. *Experimental Mechanics*. 2021. [doi:10.1007/s11340-020-00656-8](https://doi.org/10.1007/s11340-020-00656-8)
