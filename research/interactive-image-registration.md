---
title: Interactive Medical Image Registration
layout: post
date: '2014-04-11'
redirect_from:
- /interactive-image-registration/
---

Interactive image registration is required by some medical applications since automatic image registration is often slow and sometimes error-prone. We consider interactive registration methods that incorporate user-specified local transforms around control handles. The deformation between handles is interpolated by some smooth functions, usually minimizing some variational energies. Besides smoothness, we expect the impact of a control handle to be local. Therefore we choose bounded biharmonic weight functions to blend local transforms, a cutting-edge technique in computer graphics.

|  |  |
| --- | --- |
| Thin-Plate Spline | Bounded Biharmonic Function |
| thinplate | bbf |
