---
title: Accounting for the Confound of Meninges in Segmenting Entorhinal and Perirhinal Cortices in T1-weighted MRI
layout: post
date: '2016-10-13'
redirect_from:
- /accounting-for-the-confound-of-meninges-in-segmenting-entorhinal-and-perirhinal-cortices-in-t1-weighted-mri/
---

Quantification of medial temporal lobe (MTL) cortices, including entorhinal cortex (ERC) and perirhinal cortex (PRC), from *in vivo* MRI is desirable for studying the human memory system as well as in early diagnosis and monitoring of Alzheimer’s disease. However, ERC and PRC are commonly over-segmented in T1-weighted MRI (T1w MRI) because of the adjacent meninges, which consist of three layers of membranes, including dura mater, arachnoid mater and pia mater, and envelop the brain and spinal cord.

![](/images/wp/2016/10/Presentation1-1-1024x602.jpg)

Figure 1. Meningeal Layers.

The dura mater has similar intensity to gray matter (GM) in T1 contrast (Figure 2a). By contrast, in T2w MRI, meninges are easy to separate from GM due to their dark appearance in T2 contrast (Figure 2b). The likely mislabeling of meninges as GM by intensity-based methods using T1w MRI would introduce errors to the quantification of ERC and PRC, potentially confounding the findings of research studies by generating incorrect measurements.

![](/images/wp/2016/10/Presentation1-1024x394.jpg)

Figure 2. The appearance of meninges in T1-weighted and T2-weighted MRI.

To the best of our knowledge, none of the analysis pipelines for MTL cortices using T1w MRI have addressed this confound, and the dura mater are often segmented as part of the GM by the state-of-the-art image processing algorithms (ANTS [1], FreeSurfer [2], Figure 3)

![](/images/wp/2016/10/Presentation1-2-1024x394.jpg)

Figure 3. The meninges is often segmented as gray matter by the state-of-the-art image processing algorithms, including (a) ANTS and (b) FreeSurfer.

Recent work by Xie *et al*. presented at the [19th international conference on Medical Image Computing and Computer Assisted Intervention (MICCAI 2016](http://miccai2016.org/en/)) [3] proposed to segment MTL cortices along with the adjacent dura mater in T1w MRI using an established multi-atlas segmentation framework ([ASHS](/software/ashs.html) [4]) together with [super-resolution technique](http://personales.upv.es/jmanjon/reconstruction/super.html) [5]. Experimental results comparing the proposed pipeline with existing pipelines support the notion that a large portion of meninges is segmented as gray matter by existing algorithms but not by our algorithm. Cross-validation experiments demonstrate promising segmentation accuracy. Further, agreement between the volume and thickness measures from the proposed pipeline and those from the manual segmentations increase dramatically as a result of accounting for the confound of meninges. Evaluated in the context of group discrimination between patients with amnestic mild cognitive impairment and normal controls, the proposed pipeline generates more biologically plausible results and improves the statistical power in discriminating groups in absolute terms comparing to other techniques using T1w MRI.

![](/images/wp/2016/10/Presentation1-3-1024x394.jpg)

Figure 4. An example of manual and automatic segmentation.

Our evaluation also showed that the proposed pipeline using T1w MRI is not as reliable or accurate as T2-based segmentation of ERC and PRC, which could due to the poorer ability to resolve GM boundaries limited by low resolution and the confound of meninges in T1w MRI. This suggests that the T2-weighted MRI should be preferred for studies focused on these structures. However, T1w MRI is much more common in today’s neuroimaging studies, and the proposed approach makes it possible to generate ERC and PRC measures that are strongly consistent with T2-measures. Thus we expect it to have significant application in the analysis of retrospective and prospective brain imaging data, particularly in studies involving AD, aging, and memory.
 
**References:**

- [1] Das, S.R., Avants, B.B., Grossman, M., Gee, J.C. Registration based cortical thickness measurement. Neuroimage 2009. 45, 867–79.
- [2] Fischl B. FreeSurfer. Neuroimage 2012; 62: 774–81.
- [3] Xie, L., Wisse, E. M. L., Manjon, V. J. Wang, H., Das, S. R., Wolk, A. D., Yushkevich, A. P. Accounting for the Confound of Meninges in Segmenting Entorhinal and Perirhinal Cortices in T1-weighted MRI. *In Medical Image Computing and Computer-Assisted Intervention–MICCAI 2016.* Springer International Publishing.
- [4] Yushkevich PA, Pluta JB, Wang H, Xie L, Ding S, Gertje EC, et al. Automated volumetry and regional thickness analysis of hippocampal subfields and medial temporal cortical structures in mild cognitive impairment. Hum. Brain Mapp. 2015; 36: 258–287.
- [5] Manjón J V, Coupé P, Buades A, Collins LD, Robles M. MRI superresolution using self- similarity and image priors. Int. J. Biomed. Imaging 2010a; 2010: 425891.
