---
title: Team
nav:
  order: 5
  tooltip: About our team
redirect_from:
  - /people/
  - /people/faculty-staff/
  - /people/post-docs/
  - /people/students/
  - /people/alumni/
  - /people/administrators/
---

# {% include icon.html icon="fa-solid fa-users" %}Team

{% include section.html %}

## Faculty

{% include list.html data="members" component="portrait" filter="role == 'principal-investigator'" %}
{% include list.html data="members" component="portrait" filter="role == 'faculty'" %}

{% include section.html %}

## Staff, Postdocs and Students

{% include list.html data="members" component="portrait" filter="role != 'principal-investigator' and role != 'faculty' and group != 'alum'" %}

{% include section.html %}

## Alumni

{% include list.html data="members" component="portrait" filter="group == 'alum'" style="small" %}
