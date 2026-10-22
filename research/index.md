---
title: Research
nav:
  order: 2
  tooltip: Research projects
---

# {% include icon.html icon="fa-solid fa-microscope" %}Research

PICSL develops computational methods for biomedical image analysis, including
segmentation, registration, morphometry and shape analysis, and applies them
across organ systems and imaging modalities.

{% include search-box.html %}

{% include search-info.html %}

{% include section.html %}

## Projects

{% include list.html component="card" data="projects" filter="(tags || []).include?('research') and group != 'area'" style="small" %}

{% include section.html %}

## Research areas

{% include list.html component="card" data="projects" filter="group == 'area'" %}
