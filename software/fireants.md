---
title: FireANTs
---

# FireANTs

{%
  include figure.html
  image="images/software/fireants-overview.jpg"
  width="70%"
  caption="FireANTs registers images across modalities, organs and species. Image from the [FireANTs repository](https://github.com/rohitrango/FireANTs) (Apache 2.0)."
%}

FireANTs is a lightweight, general-purpose Python library for diffeomorphic image
registration on GPUs. It uses an adaptive Riemannian optimization algorithm to perform
gradient descent on the space of diffeomorphisms, which makes it fast, accurate and
memory-efficient without any training. It works across modalities, organs and species,
and can register batches of image pairs at once.

FireANTs was developed by [Rohit Jena](/members/rohit-jena.html), Pratik Chaudhari and
[Jim Gee](/members/jim-gee.html), and is described in
[*Nature Communications*](https://doi.org/10.1038/s41467-026-72508-3) (see also
[our research highlight](/research/fireants.html)).

{% include button.html link="https://github.com/rohitrango/FireANTs" text="Code" icon="fa-brands fa-github" %}
{% include button.html link="https://fireants.readthedocs.io/en/latest/" text="Documentation" icon="fa-solid fa-book" %}
