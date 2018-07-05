# Done: Alan comment for experiment section
###### tags: `cvpr17`

@qiuwch, need to put harzadours factors in the beginning of paper

@qiuwch, change reflectance to specularity? I need to change many places.

@qiuwch, from Peng, polish figure caption.

@yizhang, change caption Tab.2 performance on extreme cases.

@yizhang, relation between thin object and disparity jump. Disparity jump contains 1. thin object 2. occlusion.

## Experiment analysis
@yizhang

A trick from Alan, 如果我们有些东西现在不能解释，但Rebuttal的时候能解释，那就把Reviewer朝这个方向引导，到时候拿来讨论。

Do not directly copy and paste my words, need to have a big picture.

1. Why EPE and 3px are different and what they can tell us.

EPE measures the average error, 3px measures the number of incorrect pixels. In some cases (which), the estimation is very wrong for a small region, this causes the difference between these two. The difference between EPE and 3px also shows the characteristics of some method.

2. The ratio of performance decrease is important, for some methods the error is double, for some error just increase a bit. 

3. CoR and SPS are similar results, which is as expected.

4. MC-CNN are generally good in the scenes we show, these scenes are less extreme than Fig.7. Overall good  but less robust.

5. DispNet performance various a lot, conjecture it is because of training data.

6. The textureless performance of dispnet is different for different scenes. We think it is because the level of texturelessness is different. That is a good reason why we need to control harzadous factor.

7. For SumTemple, the overall performance is worse than mean of individuals, because we don't fully cover all potential harzardous regions. Need further investigation.

8. DispNet depends on training data. Finetune is an issue, whether training data contains harzadous cases is also important.