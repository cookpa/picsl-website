---
title: Co-registration and surgical planning in epilepsy
layout: post
date: '2014-02-14'
redirect_from:
- /co-registration-and-surgical-planning-in-epilepsy/
---

*![flowchart](/images/wp/2014/02/flowchart-245x300.png)*
*Objective:* Visualizing implanted subdural electrodes in 3D space can greatly aid planning, executing, and validating resection in epilepsy surgery.  Co-registration software is available, but cost, complexity, insufficient accuracy or validation limit adoption.  We present a fully automated open-source application, based upon a novel method using post-implant CT and post-implant MR images, for accurately visualizing intracranial electrodes in 3D space.
*Methods:* CT-MR rigid brain co-registration, MR non-rigid registration, and prior-based segmentation were carried out on 7 subjects. Post-implant CT, post-implant MR, and an external labeled atlas were then aligned in the same space. The co-registration algorithm was validated by manually marking identical anatomical landmarks on the post-implant CT and post-implant MR images.  Following co-registration, distances between the center of the landmark masks on the post-implant MR and the co-registered CT images were calculated for all subjects. Algorithms were implemented in open source software and translated into a “drag and drop” desktop application for Apple Mac OS X.
*Results:* Despite post-operative brain deformation, the method was able to automatically align intra-subject multi-modal images and segment cortical subregions so that all electrodes could be visualized on the parcellated brain.  Manual marking of anatomical landmarks validated the co-registration algorithm with a mean misalignment distance of 2.87 ± 0.58 mm between the landmarks.  Software was easily used by operators without prior image processing experience.
*Significance:* We demonstrate an easy to use, novel platform for accurately visualizing subdural electrodes in 3D space on a parcellated brain.  We rigorously validated this method using quantitative measures.  The method is unique because it involves no pre-processing, is fully automated, and freely available worldwide.  A desktop application and source code are available for download on the International Epilepsy Electrophysiology Portal (<https://www.ieeg.org/>) for use and interactive refinement.
