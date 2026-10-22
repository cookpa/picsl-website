---
title: Relating Cerebral Blood Flow to Structural & Functional Metrics in Typically Developing Children
layout: post
date: '2013-02-01'
redirect_from:
- /relating-cerebral-blood-flow-to-structural-functional-metrics-in-typically-developing-children/
---

![pediatric_atlas](/images/wp/2013/02/pediatric_atlas-300x245.png)

Sample slices from the multivariate atlas used as a basis for neuro-anatomical comparison

[Could not find the bibliography file(s)
**Purpose**: To evaluate the relationships between cerebral blood flow and other magnetic resonance (MR) imaging based measures such as fractional anisotropy, magnetic transfer ratio, cortical thickness and mean resting state BOLD signal in typically developing children.
**Methods:** Eighty-eight children aged 7-17 underwent pseudo-continuous arterial spin-labeled perfusion MRI (pCASL) [?] examinations along with anatomical (T1), diffusion tensor (DTI), magnetic transfer (MT) and BOLD resting state functional MRI (rs-fMRI) examinations. For each imaging modality, the ANTs [?] toolkit was used to create a modality-specific template from a subset (n=30) of the subjects. For non-scalar modalities, derived scalar images were used for template building. For pCASL the mean CBF image was used; for DTI the average diffusion weighted image was used; for rs-fMRI the mean BOLD image was used; and for MT the M0 image was used. Each modality-specific template was then registered to the T1 template to obtain a single multi-modality template (MMT). The T1 component of the MMT was then brain-masked, labeled, and three-tissue segmented using the Atropos segmentation tool [?]. For each subject, each modality was aligned to the corresponding component of the MMT for brain-masking and labeling. Intra-subject registrations were then performed to align all modalities to each subject’s T1 image. To provide a basis for comparison, a scalar metric was derived for each image modality. For pCASL the mean CBF was calculated; for T1 images, the cortical thickness was measured using the DiRECT method; fractional anisotropy was calculated from the DTI; the magnetization transfer ratio (MTR) was calculated from the MT images; and mean BOLD signal was calculated from the resting state fMRI data.
**Results:** Regularized canonical correlation analysis, as implemented in the sscan tool [?], was used to identify the relationship between CBF and each of the additional modalities. The analysis of each modality type is restricted to the most informative tissue type for that modality. For CBF, rs-fMRI and cortical thickness, only values in gray matter are examined, while only values in white matter are examined for FA and MTR.
**Discussion:** To the best of our knowledge, this is the first study to simultaneously compare CBF to cortical thickness, fractional anisotropy, magnetization transfer ratio and mean resting BOLD signal in a single population. In doing so, we hope to gain insight regarding the degree to which CBF provides statistically unique information in relation to these additional MR imaging modalities. Additionally, the development of the framework for analyzing these modalities provides a basis for future studies to explore the relationship between CBF and network based measures of both structural and functional connectivity.
**Conclusion:** The relationship between cortical thickness and Mean CBF (R2=0.4777) was the strongest of the metrics examined. In white matter, the MTR (R2=0.3126)  was stronger than FA (R2=0.1462). The mean BOLD (R2=0.1414) metric was the weakest.
