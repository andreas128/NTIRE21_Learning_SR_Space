# Learning the Super-Resolution Space Challenge<br><sub>NTIRE 2021 at CVPR</sub>

Learning the Super-Resolution Space challenge is held as a part of the [6th edition of NTIRE: New Trends in Image Restoration and Enhancement workshop](https://data.vision.ee.ethz.ch/cvl/ntire21/) in conjunction with CVPR 2021. The goal of this challenge is to develop a super-resolution method that can actively sample from the space of plausible super-resolutions. 

## How to participate?

To participate in this challenge, please sign up using the following link and clone this repo to benchmark your results. **Challenge participants can submit their paper to this CVPR 2021 Workshop.**

<p align="center">
  <a href="http://bit.ly/3qTbsyd">
  <img width="140px" alt="CVPR 2021 Challenge Signup" src="https://user-images.githubusercontent.com/11280511/105862009-9d8cb980-5fef-11eb-8952-3e29b628afb7.png">
  </a>
</p>

## Tackling the ill-posed nature of Super-Resolution

<a href="http://bit.ly/3qTbsyd">
<img alt="CVPR 2021 Challenge" src="https://user-images.githubusercontent.com/11280511/105862172-c7de7700-5fef-11eb-8f96-319e30b6846b.gif">
</a>


Usually, super-resolution (SR) is trained using pairs of high- and low-resolution images. **Infinitely many high-resolution images can be downsampled to the same low-resolution image.** That means that the problem is ill-posed and cannot be inverted with a deterministic mapping. Instead, one can frame the SR problem as learning a stochastic mapping, capable of **sampling from the space of plausible high-resolution images given a low-resolution image**. This problem has been addressed in recent works [1, 2, 3]. The one-to-many stochastic formulation of the SR problem allows for a few potential advantages:
* The development of more robust learning formulations that better accounts for the ill-posed nature of the SR problem.
* Multiple predictions can be sampled and compared.  
* It opens the potential for controllable exploration and editing in the space of SR predictions.   

| <img width="1000" alt="Super-Resolution with Normalizing Flow" src="https://user-images.githubusercontent.com/11280511/104035941-152aae00-51d3-11eb-9294-6fc71489c562.png"> | <img width="1000" alt="Explorable SR" src="https://user-images.githubusercontent.com/11280511/104035744-c7ae4100-51d2-11eb-9e1c-e501020c9216.png">  | <img width="1000" alt="Screenshot 2021-01-12 at 16 05 43" src="https://user-images.githubusercontent.com/11280511/104332087-1a983900-54f0-11eb-8b69-0656eaaa6c84.png"> |
| :--: | :--: | :--: |
| [[Paper]](http://de.arxiv.org/pdf/2006.14200) [[Project]](https://github.com/andreas128/SRFlow) | [[Paper]](https://arxiv.org/pdf/1912.01839.pdf) [[Project]](https://github.com/YuvalBahat/Explorable-Super-Resolution) | [[Paper]](https://arxiv.org/pdf/2004.04433.pdf) [[Project]](https://mcbuehler.github.io/DeepSEE/) |
| [1]  SRFlow: Learning the Super-Resolution Space with Normalizing Flow. Lugmayr et al., ECCV 2020.  | [2]  Explorable Super-Resolution. Bahat & Michaeli, CVPR 2020.  | [3] DeepSEE: Deep Disentangled Semantic Explorative Extreme Super-Resolution. Bühler et al., ACCV 2020.  |



## CVPR 2021 Challenge on Learning the Super-Resolution Space

We organize this challenge to stimulate research in the emerging area of learning one-to-many SR mappings that are capable of sampling from the space of plausible solutions. Therefore the task is to develop a super-resolution method that: 
1. Each individual SR prediction should achieve highest possible **photo-realism**, as perceived by humans.
2. Is capable of sampling an arbitrary number of SR images capturing **meaningful diversity**, corresponding to the *uncertainty* induced by the ill-posed nature of the SR problem together with image priors.
3. Each individual SR prediction should be consistent with the input low-resolution image.

The challenge contains two tracks, targeting 4X and 8X super-resolution respectively. You can download the training and validation data in the table below. At a later stage, the low-resolution of the test set will be released.

<table>
<thead>
<tr>
<th>&nbsp;</th>
<th colspan="2">Training</th>
<th colspan="2">Validation</th>
</tr>
</thead>
<tbody>
<tr>
<td>&nbsp;</td>
<td>Low-Resolution</td>
<td>High-Resolution</td>
<td>Low-Resolution</td>
<td>High-Resolution</td>
</tr>
<tr>
<td>Track 4X</td>
<td><a href="https://data.vision.ee.ethz.ch/alugmayr/NTIRE2021/DIV2K-tr_4X.zip" rel="nofollow">4X LR Train</a></td>
<td><a href="https://data.vision.ee.ethz.ch/alugmayr/NTIRE2021/DIV2K-tr_1X.zip" rel="nofollow">4X HR Train</a></td>
<td><a href="https://data.vision.ee.ethz.ch/alugmayr/NTIRE2021/DIV2K-va_4X.zip" rel="nofollow">4X LR Valid</a></td>
<td><a href="https://data.vision.ee.ethz.ch/alugmayr/NTIRE2021/DIV2K-va_1X.zip" rel="nofollow">4X HR Valid</a></td>
</tr>
<tr>
<td>Track 8X</td>
<td><a href="https://data.vision.ee.ethz.ch/alugmayr/NTIRE2021/DIV2K-tr_8X.zip" rel="nofollow">8X LR Train</a></td>
<td><a href="https://data.vision.ee.ethz.ch/alugmayr/NTIRE2021/DIV2K-tr_1X.zip" rel="nofollow">8X HR Train</a></td>
<td><a href="https://data.vision.ee.ethz.ch/alugmayr/NTIRE2021/DIV2K-va_8X.zip" rel="nofollow">8X LR Valid</a></td>
<td><a href="https://data.vision.ee.ethz.ch/alugmayr/NTIRE2021/DIV2K-va_1X.zip" rel="nofollow">8X HR Valid</a></td>
</tr>
</tbody>
</table>



### Challenge Rules

To guide the research towards useful and generalizable techniques, submissions need to adhere to the following rules. All participants must submit code of their solution along with the final results.

* The method must be able to generate an **arbitrary number** of diverse samples. That is, your method cannot be limited to a maximum number of different SR samples (corresponding to e.g. a certain number of different output network heads).
* All SR samples must be generated by a **single model**. That is, **no ensembles** are allowed.
* **No self-ensembles** during inference (e.g. flipping and rotation).
* All SR samples must be generated using the **same hyper-parameters**. That is, the generated SR samples shall not be the result of different choices of hyper-parameters during inference.
* We accept submissions of **deterministic methods**. However, they will naturally score zero in the diversity measure and therefore **not** be able to win the challenge.
* Other than the validation and test split of the DIV2k dataset, **any training data** or pre-training is allowed. You are not allowed to use DIV2K validation or test sets (low- and high-resolution images) for training.


## Evaluation Protocol

A method is evaluated by first predicting a **set of 10** randomly sampled SR images for each low-resolution image in the dataset. From this set of images, evaluation metrics corresponding to the three criteria above will be considered. The participating methods will be ranked according to each metric. These ranks will then be combined into a final score. The three evaluation metrics are described next.


```bash
git clone --recursive https://github.com/andreas128/NTIRE21_Learning_SR_Space.git
python3 measure.py OutName path/to/Ground-Truch path/to/Super-Resolution n_samples scale_factor

# n_samples = 10
# scale_factor = 4 for 4X and 8 for 8X
```

### How we measure Photo-realism?
To assess the photo-realism, a **human study** will be performed on the test set for the final submission.

Automatically assessing the photo-realism and image quality is an extremely difficult task. All existing methods have severe shortcomings. As a very rough guide, you can use the LPIPS distance. **Note:** LPIPS will not be used to score photo-realism of you final submission. So beware of overfitting to LPIPS, as that can lead to worse results. LPIPS is integrated in our provided [toolkit](#evaluation-protocol) in `measure.py`.

### How we measure the spanning of the SR Space?
The samples of the developed method should provide a meaningful diversity. To measure that, we define the following score. We sample 10 images, densely calculate a metric between the samples and the ground truth. To obtain the *local best* we pixel-wise select the best score out of the 10 samples and take the full image's average. The *global best* is obtained by averaging the whole image's score and selecting the best. Finally, we calculate the score using the following formula:

score = (global best - local best)/(global best) * 100


|  | [ESRGAN](https://github.com/xinntao/ESRGAN) | [SRFlow](https://github.com/andreas128/SRFlow) |
| :--: | :--: | :--: |
| Track 4X | 0 | 25.36 |
| Track 8X | 0 | 10.62 |


### How we measure the Low Resolution Consistency
To measure how much information is preserved in the super-resloved image from the low-resolution image, we measure the LR-PSNR. The goal in this challenge is to obtain a LR-PSNR of 45dB. All approaches that have an average PSNR above this value will be ranked equally in terms of this criteria.


|  | [ESRGAN](https://github.com/xinntao/ESRGAN) | [SRFlow](https://github.com/andreas128/SRFlow) |
| :--: | :--: | :--: |
| Track 4X | 39.01 | 49.91 |
| Track 8X | 31.28 | 50.0  |



## Important Dates

| Date       | Event |
| ---------- | ----  |
| 2021.03.15 | Final test data release (inputs only) |
| 2021.03.20 | test result submission deadline |
| 2021.03.20 | fact sheet / code / model submission deadline |
| 2021.03.22 | test preliminary score release to the participants |
| 2021.04.02 | challenge paper submission deadline |
| 2021.04.15 | camera-ready deadline |
| 2021.06.15 | workshop day |


## Submission of Final Test Results

After the final testing phase, participants will be asked to submit:
* SR predictions on the test set.
* Code.
* A fact sheet describing their method.

**Details will follow when the test phase starts ...**


## Issues and questions
In case of any questions about the challenge or the toolkit, feel free to open an issue on Github.

## Organizers
* [Andreas Lugmayr](https://twitter.com/AndreasLugmayr) (andreas.lugmayr@vision.ee.ethz.ch)
* [Martin Danelljan](https://martin-danelljan.github.io/) (martin.danelljan@vision.ee.ethz.ch)
* [Radu Timofte](http://people.ee.ethz.ch/~timofter/) (radu.timofte@vision.ee.ethz.ch)

## CVPR 2021 NTIRE Terms and conditions
The terms and conditions for participating in the challenge are provided [here](TERMSandCONDITIONS.md)


## How to participate?

To participate in this challenge, please sign up using following link and clone this repo to benchmark your results. **Challenge participants can submit their paper to this CVPR 2021 Workshop.**

<p align="center">
  <a href="http://bit.ly/3qTbsyd">
  <img width="140px" alt="CVPR 2021 Challenge Signup" src="https://user-images.githubusercontent.com/11280511/105862009-9d8cb980-5fef-11eb-8952-3e29b628afb7.png">
  </a>
</p>

<meta name="google-site-verification" content="Q-FqD2hd4f7FvP9bO8xUgYHt6vp3TctGik9IkNBwMZ4" />
