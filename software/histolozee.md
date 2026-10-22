---
title: HistoloZee
redirect_from:
- /software/histolozee/
---

# HistoloZee

{%
  include figure.html
  image="images/wp/2014/04/HZee01-1024x577.jpg"
  width="80%"
  caption="Loading an MRI reference image with a reconstructed histology stack of the human hippocampal formation."
%}

*HistoloZee* is a tool that integrates histology reconstruction, MRI co-registration, and manual segmentation tools in an easy-to-use and intuitive interface. HistoloZee permits real-time interaction with complex and large (multi-GB) histology datasets during the co-registration steps of histology reconstruction.

HistoloZee was developed by [Daniel Adler](/members/daniel-adler.html "Daniel Adler") under the supervision of [Paul Yushkevich](/members/paul-yushkevich.html "Paul Yushkevich"). Please [contact us](mailto:histolozee@gmail.com) to request a pre-distribution copy of the software. HistoloZee is under active development and the release (v.03) currently run under Mac OS X (>10.6), with Linux and Windows versions forthcoming.

## Reconstruction procedure

Basic reconstruction procedure for a stack of histology slides with accompanying reference imaging data (e.g. MRI):

1. Slides from the tissue block are loaded and co-registered to each other to form an initial volumetric reconstruction. Sorting of slides and the setting of pixel size, slice thickness, and slice spacing are done during this stage.
2. Reference MRI is loaded and aligned to the histology slide stack.
3. Each slide is transformed to better match its corresponding cut-plane in the MRI.

… subsequent iteration of steps 2 & 3. Histology and MRI image transformations are combined harmoniously by a mapping all data into global, physical coordinates.

## Main features

- Formats: Loading of stacks of very large (>1GB) microscopy slides, including support for most common life-sciences imaging formats (implemented using [OpenSlide](http://www.openslide.org)) and loading of 3D reference image data (e.g. MRI) in NIfTI format
- Organization: Facility for sorting of slides and saving of reconstruction projects in XML format
- Visualization: Multi-scale viewing of slides and ability to load image overlays with transparency, thresholding, and live edge detection (OpenGL and GLSL shaders)
- 3D views: Linked cursors between orthogonal views of imaging data
- Manual affine slide registration: Tools for fine-scaled manual 2D-2D alignment of slides at any resolution
- Manual affine MRI registration: Tools for interactive 3D affine transformation of  reference MRI to match histology slides
- Automated affine slide registration: GPU-accelerated metric computation (MSE, NCC, NMI) and transformations for alignment of slides to each other (2D-2D) and with reference MRI data (2D-3D)
- Manual segmentation: Tools for delineation of regions using vector-graphics (“lossless”) label masks stored in SVG format
- Exporting: Reconstructed histology slide stacks can be exported to NIfTI format (or as an image series) at any resolution, while preserving the global coordinate mapping with MRI

## Video tutorials

Please visit our YouTube Playlist: **[HistoloZee Tutorials](https://www.youtube.com/playlist?list=PL68v8FP_IVlg2tCgJXrsO3UHve1q9wLjI)**
Feel free to give us any feedback or suggestions on the tutorials and software!

## Screenshots

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 0 20px; align-items: start;">
{%
  include figure.html
  image="images/wp/2014/04/HZee03-1024x577.jpg"
  link="images/wp/2014/04/HZee03-1024x577.jpg"
  caption="Viewing a histology slide with an edge overlay atop the MRI reference image."
%}
{%
  include figure.html
  image="images/wp/2014/04/HZee06-1024x577.jpg"
  link="images/wp/2014/04/HZee06-1024x577.jpg"
  caption="High-resolution detail of cells."
%}
{%
  include figure.html
  image="images/wp/2014/04/HZee02-1024x577.jpg"
  link="images/wp/2014/04/HZee02-1024x577.jpg"
%}
{%
  include figure.html
  image="images/wp/2014/04/HZee04-1024x577.jpg"
  link="images/wp/2014/04/HZee04-1024x577.jpg"
%}
{%
  include figure.html
  image="images/wp/2014/04/HZee05-1024x577.jpg"
  link="images/wp/2014/04/HZee05-1024x577.jpg"
%}
{%
  include figure.html
  image="images/wp/2014/04/HZee07-1024x577.jpg"
  link="images/wp/2014/04/HZee07-1024x577.jpg"
%}
{%
  include figure.html
  image="images/wp/2014/04/HZee08-1024x577.jpg"
  link="images/wp/2014/04/HZee08-1024x577.jpg"
%}
{%
  include figure.html
  image="images/wp/2014/04/HZee09-1024x577.jpg"
  link="images/wp/2014/04/HZee09-1024x577.jpg"
%}
{%
  include figure.html
  image="images/wp/2014/04/HZee10-1024x577.jpg"
  link="images/wp/2014/04/HZee10-1024x577.jpg"
%}
</div>
