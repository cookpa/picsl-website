---
title: Relating brain anatomy and cognitive ability using a multivariate multimodal framework
layout: post
date: '2014-06-26'
redirect_from:
- /relating-brain-anatomy-and-cognitive-ability-using-a-multivariate-multimodal-framework/
---

Linking structural neuroimaging data from multiple modalities to cognitive performance is an important challenge for cognitive neuroscience. In this study we examined the relationship between verbal fluency performance and neuroanatomy in 54 patients with frontotemporal degeneration (FTD) and 15 age-matched controls, all of whom had T1- and diffusion-weighted imaging.
Our goal was to incorporate measures of both gray matter (voxel-based cortical thickness) and white matter (fractional anisotropy) into a single statistical model that relates to behavioral performance. We first used eigenanatomy to define data-driven regions of interest (DD-ROIs) for both gray matter and white matter. Eigenanatomy is a multivariate dimensionality reduction approach that identifies spatially smooth, unsigned principal components that explain the maximal amount of variance across subjects. We then used a statistical model selection procedure to see which of these DD-ROIs best modeled performance on verbal fluency tasks hypothesized to rely on distinct components of a large-scale neural network that support language: category fluency requires a semantic-guided search and is hypothesized to rely primarily on temporal cortices that support lexical-semantic representations; letter-guided fluency requires a strategic mental search and is hypothesized to require executive resources to support a more demanding search process, which depends on prefrontal cortex in addition to temporal network components that support lexical representations.
We observed that both types of verbal fluency performance are best described by a network that includes a combination of gray matter and white matter. For category fluency, the identified regions included bilateral temporal cortex and a white matter region including left inferior longitudinal fasciculus and frontal–occipital fasciculus. For letter fluency, a left temporal lobe region was also selected, and also regions of frontal cortex. These results are consistent with our hypothesized neuroanatomical models of language processing and its breakdown in FTD. We conclude that clustering the data with eigenanatomy before performing linear regression is a promising tool for multimodal data analysis.

![eigenanatomy_ftd](/images/wp/2013/05/eigenanatomy_ftd.png)

Thresholded soft ROIs generated from the Eigenanatomy decomposition of the cortical thickness (top) and fractional anisotropy (bottom) data based on sparse PCA. A total of 32 regions were generated for each modality.

This work is currently in press atNeuroImage, and is a collaboration between PICSL, the [Penn FTD Center](http://ftd.med.upenn.edu) and the [Peelle Lab](http://peellelab.org) at Washington University in St Louis.
Eigenanatomy is available as part of [ANTs](http://stnava.github.io/ANTs/).
Update: the paper is now published and is available free until August 21 2014:
http://www.sciencedirect.com/science/article/pii/S1053811914003735
