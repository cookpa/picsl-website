---
title: Feature Selection for Characterization of ILD and COPD
layout: post
date: '2014-02-21'
redirect_from:
- /feature-selection-for-characterization-of-ild-and-copd/
---

![pipeline](/images/wp/2014/02/pipeline-300x65.jpg)
To compare the performance of various image-based metrics computed from thoracic HRCT modality with data from pulmonary function testing (PFT) in characterizing interstitial lung disease (ILD) and chronic obstructive pulmonary disease (COPD).
14 patients with ILD and 11 with COPD had undergone both PFT and HRCT within 3 days. For each patient, 93 image-based metrics were computed and their relationship with the 21 clinically-used PFT parameters were analyzed using a minimal-redundancy-maximal-relevance (MRMR) statistical framework. The first 20 features were selected out of the total 114 mixed image metrics and PFT values in characterization ILD and COPD.
Among the best performing 20 features, 14 were image metrics, derived from attenuation histograms and texture descriptions. The highest relevance value computed from PFT parameters was 0.47 and the highest from image metrics was 0.52, given the theoretical bound as [0, 0.69]. The ILD/COPD classifier using the first 4 features achieved a 1.92% error rate.
![svm_linear_comp6](/images/wp/2014/02/svm_linear_comp6-300x140.png)
Conclusion Some image metrics are not only as good discriminators as PFT for characterization of ILD and COPD, but also not redundant when PFT values are provided. Image metrics of attenuation histogram statistics and texture descriptions may be valuable for further investigation in computer-assisted diagnosis.
