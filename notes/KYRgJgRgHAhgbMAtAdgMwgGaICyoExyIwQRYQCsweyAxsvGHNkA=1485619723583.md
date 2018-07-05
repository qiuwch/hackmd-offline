# Review rebuttal

[Rebuttal draft in Overleaf.com](https://www.overleaf.com/7894358qwmthfjkbntx#/27785847/)

[Release preparation for UnrealStereo](https://hackmd.io/CwIwrAnMDGCmDMBaEA2AJgBkcMHbLWgA5swAmeWYCItMgMzKA===)

Domain adaptation is always a problem. The conclusion from one camera can not generalize to another and the lab setting can not generalize to the real world setting.

Yes, it is dangerous to make conclusion purely based on synthetic images.

https://www.unrealengine.com/marketplace/cinema-camera
Rain drop effects.


Questions

## Reviewer 1.

- immature and requires polishing
yes

- theoretical and technical contributions limited
subjective and hard to say

- domain transfer
use 1. related work and 2. our training to show domain transfer

- limited number of algorithms
how many is enough? Is our selection representative?

- doubtable whether this is fully achiveable with a purely synthetic. 

No only synthetic is not enough, real data as a verification. No verification is more dangerous.

- whether reasonable to evaluate.

Of course, not reasonable to challenge the importance of vision here. The importance of semantic info. Encourage this direction, show the difference. Elaborate from here. 

- Real world effect.

lens effect, doable with plugin and other modifcation. technical challenge.

## Reviewer 2

- motion blur

yes, technical issue


- Remark

Answer the occlusion remark

## Reviewer 3

- domain transfer

Show one example is sufficient

- contain only 4 scenes

Not really, measure by number of images. We have more images, show more.

- What conclusion for take away

This is also what I want to know. One good example is the no texture case which CNN works better.

Strong conclusion is useful for the future algorithms

## Comments from Alan

Reviewer 1 --  this person is not intelligent or has no immagination.

Doesn't appreciate the novelty -- first paper to do this -- new method
for evaluating algorithms.

Very worried about "safety" and "danger". We are not concerned with
"real-world safety" or even "real world applications" we are trying to
evaluate how stereo algorithms perform when we vary nuisance factors.
We certainly don't claim that our system is yet capable of deciding
which algorithms would work in really dangerous conditions -- but our
work develops a new approach which could eventually do this (as the
virtual world get more realistic).


The stereo algorithms selected are not arbitrary -- we selected some
of the top ranked algorithms. '

We don't evaluate "lens effects" -- but we could.

Not fair to evaluate stereo algorithms on textureless regions? No, we
show that some do better than others. Some have priors that can deal
with these situations.

Reviewer 3 -- this person is intelligent

Yes, correct that there are "half occlusions" and "fence occlusions"

Yes, we can edit and polish the paper.

Yes, motion blur, lens blur -- we plan to consider all types of nuisance error

Reviewer 4 --  this reviewer is intelligent.

We don't verify that performance on virtual datset would generalize to
real scenes -- we might be able to check this, e.g., train algorithms
on this dataset and test them on others -- but that is not the goal of
the current paper.


Only 4 scenes -- yes, more would be better.

Insights -- yes, we could train on these types of datsets to
strengthen performance -- good future work. But surely, determining
which algorithms are robust to varying these nuisance factors is
worthwhile. This helps people develop algorithms which can deal with
these nuisances -- suggests a new set of vision challenges.
