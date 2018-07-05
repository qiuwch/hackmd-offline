# DONE: CVPR17, Experiment explain outline
###### tags: `unrealcv` `cvpr17`

Analyze the result in the following aspects

1. significance of hazardous factors. 
    original a
    For overall performance in full and non-occluded regions, results on UrbanCity is consistent with the ranking on KITTI~\cite{geiger2012we} both in terms of end-point and 3 pixel error metric, which indicates the authenticity of our data rendered from virtual scenes. Moreover, for reflective regions, results on RealisticRendering and UrbanCity also agree with those on KITTI, except for the performance of DispNetC~\cite{mayer2016large}. For Middlebury like scene in UnrealMiddlebury, significant deterioration of performance is observed. Therefore, the frequent disparity jumps and the transformation of shape due to viewpoint change significantly influences the difficulty of stereo matching. In large indoor environment as SunTemple, the lack of hazards results in relatively low errors. The top ranking method on KITTI MC-CNN~\cite{zbontar2015computing} outperforms other method as expected.
    
    On the boundary, errors higher than non-occluded regions are observed for all algorithms, which indicates that boundary region is a hazardous factor. This suggest that current stereo methods have difficulty predicting edge-preserved disparity maps, probably due to unsuccessful matching or the failure of segmentation to align well with the boundaries. 
    
2. comparion with manually designed case or explain using manually designed case? (Alan's 6)
   original b, modified
    Although generated in much more complex environment, most of the results on hazardous regions still coincide with the manually designed cases, i.e. robustness of stereo algorithms varies under different levels of hazardous factors. For reflection, SPS-St~\cite{yamaguchi2014efficient} and CoR \cite{chakrabarti2015low} outperform other methods on RealisticRendering and UrbanCity, while MC-CNN~\cite{zbontar2015computing} performs best on SunTemple. From Fig.~\ref{fig:case_performance} we find that they coincide respectively with high and low reflection conditions. For textureless materials, results on UrbanCity match the weakest textured case, where end-to-end DCNN based models perform best, while the other three could be interpreted as cases with evident texture. 

3. what can we get for algorithms from results on hazardous regions? or Characteristics of algorithms
    Characteristic of stereo algorithms (Alan's 3,4,5,8)
    original d,e,f

- SPS-St~\cite{yamaguchi2014efficient} and CoR~\cite{chakrabarti2015low} have similar performance both in designed case and rendered natural scenes. The latter uses the former to compute an initial semi-dense estimation of disparity and a multi-scale aggregation mechanism to further refine the result. In scenes with rich hazardous factors, e.g. RealisticRendering, UnrealMiddlebury and UrbanCity, adopting this mechanism results in better accuracy, while in simple scenes, e.g. SunTemple, no such gain in performance is observed.

- The performance of DCNN based models~\cite{mayer2016large} drops significantly on these rendered video sequences except for SunTemple. Since DCNN models highly hinges on training data, whether training data includes hazardous cases could determine the respective performance. Therefore, for DCNN models, finetuning becomes important when transfer from one dataset to another. 

- The state-of-the-art pixel-level global method MC-CNN~\cite{zbontar2015computing} receives best overall performance. However, it easily suffer from ambiguities brought by reflection and transparency. The convolutional neural network (CNN) for patch matching provide better initial disparity estimation on unambiguous regions, meanwhile, make the whole algorithm more vulnerable to reflection and transparency.

4. metric for evaluating stereo. (Alan's 1,7)
    The relation of the two error metrics is worth noticing. End-point error (EPE) measures the error in average, while 3 pixel error measures the percentage of incorrect pixels. They are not in agreement in some cases, which could reveal characteristics of some algorithms. Specifically, for DCNN based method, significantly higher 3 pixel errors is observed. The L1 loss function used in the training process of DCNN models encourages lower EPE, which could account for the discrepency. 


My original paragraphs,
a. comparison with KITTI. consist in overall and reflective 

b. coinside with manually designed case. Different level -> different performance (Alan's 6)

c. Boundary (boundary worse than non-occluded in most cases)

d. DCNN - Alan's 5,8  (need modify)

e. MC-CNN - Alan's 4 (keep)

f. SPS-St and CoR - Alan's 3 (keep)

Alan's 1,2,7 not included

Findings:

- 1-8 from alan
- overall and reflective performance in UrbanCity agree with KITTI
- like Alan's 6, reflection also need control
- boundary worse than non-occluded in most cases


