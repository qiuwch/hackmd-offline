# Ethan project

Ethan (Gao Yuan) a Ph.D student from Hong Kong.

[A demo](https://hackmd.io/EYBgpgxgTAnAhmAtMaJEBY4DMKPsYRANmCIgGYisBWARgBNzyg==#)

Given 2D point, reconstruct 3D point location.

Input: $x$
Output: $X$

Status: a CVPR submission, use PASCAL 3D+ data. Want to extend to a journal version. Need more experiments and more data.

Idea: Use CG to generate $x$ and $X$ and camera pose $P$

Discussion:

How to sample keypoint from models. Do we need to manually do this or some annotations already exsit. Check what [shapenet annotation](https://www.shapenet.org/annotations) already provides.