---
title: LESYMAP
redirect_from:
- /software/lesymap/
---

# LESYMAP

![](/images/wp/2017/07/LESYMAP-300x150.png)
[Lesymap](https://dorianps.github.io/LESYMAP/) uses univariate and multivariate methods to map functional regions of the brain that, when lesioned, cause specific cognitive deficits. All is required is a set of Nifti images with the lesion of each subject and the vector of behavioral scores. Lesions must be already registered in template space, use `antsRegistration` or other ANTs tools to achieve this. Lesymap will check that lesions are in the same space before running. By default, voxels with identical lesion patterns are grouped together in unique patches, and analysis are run on patches. Patch-based mapping decreases the number of multiple comparisons and speeds up the analyses. Multivariate mapping is performed using an optimized version of sparse canonical correlations (SCCAN).
