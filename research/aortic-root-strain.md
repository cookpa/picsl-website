---
title: Measuring strain in the aortic root from 4D echocardiography
layout: post
date: '2023-07-01'
author: alison-pouch
---

Mechanics play a central role in the cardiovascular system, but measuring how tissue deforms and strains inside a living patient remains a practical challenge.

In *Medical Image Analysis*, Ankush Aggarwal, [Jilei Hao](/members/jilei-hao.html), [Alison Pouch](/members/alison-pouch.html) and colleagues present a semi-automated framework for estimating strains from 4D echocardiographic images, combining medial modeling with deformable registration. They applied it to the aortic roots of patients with normal three-leaflet (trileaflet) aortic valves and with congenital bicuspid aortic valves (BAV).

The method uses fully nonlinear shell-based kinematics, splitting strain into in-plane components (shear and dilatation) and an out-of-plane component.

Even for size-matched aortic roots without aneurysm, patients with bicuspid valves experienced larger regional shear strains. These elevated strains may contribute to the higher risk of aneurysm in BAV patients. The framework is openly available and can be applied to any tubular structure.

{%
  include figure.html
  image="images/research/aortic-root-strain.svg"
  width="600px"
  caption="From 4D echocardiography to a medial model of the aortic root to regional strain maps (illustration)."
%}

**Reference:** Aggarwal A, Mortensen P, Hao J, et al., Pouch AM. Strain estimation in aortic roots from 4D echocardiographic images using medial modeling and deformable registration. *Medical Image Analysis*. 2023. [doi:10.1016/j.media.2023.102804](https://doi.org/10.1016/j.media.2023.102804)
