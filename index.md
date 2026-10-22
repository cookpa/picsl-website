---
---

# Penn Image Computing and Science Laboratory

PICSL develops computational methods for extracting, analyzing and integrating
clinically and scientifically meaningful information from biomedical images.
Our work covers segmentation, registration, morphometry and shape analysis,
with collaborations spanning many organ systems and imaging modalities.
We also make these methods freely available as open-source software.

{%
  include button.html
  link="about"
  text="About the lab"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% include section.html %}

## Highlights

{% capture text %}

Imaging of neurodegenerative disease from in vivo MRI to postmortem MRI and
histology, image registration, cardiac shape modeling, and AI for clinical imaging.

{%
  include button.html
  link="research"
  text="Browse our research"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

<small>Image: tau tangle burden mapped into a 3D atlas of the medial temporal lobe,
from [Ravikumar et al., *Nature Communications* (2024)](research/mtl-tau-atlas.html),
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).</small>

{% endcapture %}

{%
  include feature.html
  image="images/home/research.jpg"
  link="research"
  title="Research"
  text=text
%}

{% capture text %}

ITK-SNAP, ANTs, FireANTs, Greedy, ASHS and other open-source tools for medical
image analysis.

{%
  include button.html
  link="software"
  text="Get our software"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

<small>Image: mouse brain templates built with ANTs (left) and FireANTs (right), from
[Jena, Chaudhari & Gee, *Nature Communications* (2026)](research/fireants.html),
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).</small>

{% endcapture %}

{%
  include feature.html
  image="images/home/software.jpg"
  link="software"
  title="Software"
  flip=true
  text=text
%}

{% capture text %}

Faculty, staff, students and alumni of PICSL.

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/home/team.jpg"
  link="team"
  title="Team"
  text=text
%}
