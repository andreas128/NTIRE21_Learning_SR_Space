# Learning the Super-Resolution Space Challenge
These are the official rules (terms and conditions) that govern how the 
NTIRE 2021 challenge on Learning the Super-Resolution Space will operate. This challenge will 
be simply referred to as the "challenge" or the "contest" throughout the remaining part 
of these rules and may be named as "NTIRE" benchmark, challenge, or 
contest, elsewhere (our webpage, our documentation, other publications).

In these rules, "we", "our", and "us" refer to the organizers 
(Andreas Lugmayr (andreas.lugmayr [at] vision.ee.ethz.ch), Martin Danelljan (martin.danelljan [at] vision.ee.ethz.ch) 
and Radu Timofte (Radu.Timofte [at] vision.ee.ethz.ch)) of NTIRE challenge and "you" and "yourself" 
refer to an eligible contest participant.

Note that these official rules can change during the contest until the start of the 
final phase. If at any point during the contest the registered participant considers 
that can not anymore meet the eligibility criteria or does not agree with the changes 
in the official terms and conditions then it is the responsibility of the participant 
to send an email to the organizers such that to be removed from all the records. 
Once the contest is over no change is possible in the status of the registered 
participants and their entries.

## 1. Contest description
This is a skill-based contest and chance plays no part in the determination of the 
winner (s).

The goal of this challenge is to develop a super-resolution method that can actively sample from the space of plausible super-resolutions. The challenge is called Learning the Super-Resolution Space.

Focus of the contest: it will be made available a dataset adapted for the specific 
needs of the challenge. The images have a large diversity of contents. 
We will refer to this dataset, its partition, and related materials as the Dataset. 
The dataset is divided into training, validation and testing data. We focus on the 
quality of the results, the aim is to achieve output images with the best fidelity, as 
computed via PSNR or a user study. 
and similar to the reference clean ground truth. The participants will not have 
access to the ground truth images from the test data. 
The ranking of the participants is according to the performance of their methods on 
the test data. The participants will provide descriptions of their methods, 
details on (run)time complexity, platform and (extra) data used for modeling. 
The winners will be determined according to their entries, the reproducibility of 
the results and uploaded codes or executables, and the above mentioned criteria as 
judged by the organizers.

## 2. Tentative contest schedule
The registered participants will be notified by email if any changes are made to the 
schedule. The schedule is available on the [NTIRE workshop web page](https://data.vision.ee.ethz.ch/cvl/ntire21/) 
and on the 
official GitHub [repository]().

## 3. Eligibility
You are eligible to register and compete in this contest only if you meet all the 
following requirements:

* You are an individual or a team of people willing to contribute to the open tasks, who accepts to follow the rules of this contest
* You are not an NTIRE challenge organizer or an employee of NTIRE challenge organizers
* You are not involved in any part of the administration and execution of this contest
* You are not a first-degree relative, partner, household member of an employee or of an organizer of NTIRE challenge or of a person involved in any part of the administration and execution of this contest
This contest is void wherever it is prohibited by law.

Entries submitted but not qualified to enter the contest, it is considered voluntary 
and for any entry you submit NTIRE reserves the right to evaluate it for scientific 
purposes, however under no circumstances will such entries qualify for sponsored 
prizes. If you are an employee, affiliated with or representant of any of the 
NTIRE challenge sponsors then you are allowed to enter in the contest and get ranked, 
however, if you will rank among the winners with eligible entries you will receive 
only a diploma award and none of the sponsored money, products or travel grants.

NOTE: industry and research labs are allowed to submit entries and to compete in both 
validation phase and final test phase. However, in order to get officially ranked on 
the final test leaderboard and to be eligible for awards the reproducibility of the 
results is a must and, therefore, the participants need to make available and submit 
their codes or executables. All the top entries will be checked for reproducibility 
and marked accordingly.

We will have 3 categories of entries in the final test ranking:
1) checked with publicly released codes 
2) checked with publicly released executable
3) unchecked (with or without released codes or executables)

 

## 4. Entry
In order to be eligible for judging, an entry must meet all the following requirements:

**Entry contents**: the participants are required to submit image results and code or 
executables. To be eligible for prizes, the top ranking participants should publicly 
release their code or executables under a license of their choice, taken among popular
OSI-approved licenses (http://opensource.org/licenses) and make their code or 
executables online accessible for a period of not less than one year following the end 
of the challenge (applies only for top three ranked participants of the competition). 
To enter the final ranking the participants will need to fill out a survey 
(fact sheet) briefly describing their method. All the participants are also invited 
(not mandatory) to submit a paper for peer-reviewing and publication at the 
NTIRE Workshop and Challenges (to be held online on June, 2021). To be eligible for 
prizes, the participants score must improve the baseline performance provided by the
challenge organizers.

**Use of data provided:** all data provided by NTIRE are freely available to the 
participants from the website of the challenge under license terms provided with the 
data. The data are available only for open research and educational purposes, 
within the scope of the challenge. NTIRE and the organizers make no warranties 
regarding the database, including but not limited to warranties of non-infringement or 
fitness for a particular purpose. The copyright of the images remains in property of 
their respective owners. By downloading and making use of the data, you accept full 
responsibility for using the data. You shall defend and indemnify NTIRE and the 
organizers, including their employees, Trustees, officers and agents, against any and 
all claims arising from your use of the data. You agree not to redistribute the data 
without this notice.

* Test data: The organizers will use the test data for the final evaluation and 
  ranking of the entries. The ground truth test data will not be made available to 
  the participants during the contest.
* Training and validation data: The organizers will make available to the participants 
  a training dataset with ground truth images and a validation dataset without 
  ground truth images. At the start of the final phase the test data without ground 
  truth images will be made available to the registered participants.
* Post-challenge analyses: the organizers may also perform additional post-challenge 
  analyses using extra-data, but without effect on the challenge ranking.
* Submission: the entries will be online submitted via the CodaLab web platform. 
  During development phase, while the validation server is online, the participants 
  will receive immediate feedback on validation data. The final 
  evaluation will be computed on the test data submissions, the final scores 
  will be released after the challenge is over.
* Original work, permissions: In addition, by submitting your entry into this contest 
  you confirm that, to the best of your knowledge: - your entry is your own original 
  work; and - your entry only includes material that you own, or that you have 
  permission to use.

## 5. Potential use of entry
Other than what is set forth below, we are not claiming any ownership rights to your 
entry. However, by submitting your entry, you:

* Are granting us an irrevocable, worldwide right and license, in exchange for your opportunity to participate in the contest and potential prize awards, for the duration of the protection of the copyrights to:

    1. Use, review, assess, test and otherwise analyze results submitted or produced by your code or executable and other material submitted by you in connection with this contest and any future research or contests by the organizers; and
    2. Feature your entry and all its content in connection with the promotion of this contest in all media (now known or later developed);


* Agree to sign any necessary documentation that may be required for us and our designees to make use of the rights you granted above;

* Understand and acknowledge that us and other entrants may have developed or commissioned materials similar or identical to your submission and you waive any claims you may have resulting from any similarities to your entry;

* Understand that we cannot control the incoming information you will disclose to our representatives or our co-sponsor’s representatives in the course of entering, or what our representatives will remember about your entry. You also understand that we will not restrict work assignments of representatives or our co-sponsor’s representatives who have had access to your entry. By entering this contest, you agree that use of information in our representatives’ or our co-sponsor’s representatives unaided memories in the development or deployment of our products or services does not create liability for us under this agreement or copyright or trade secret law;

* Understand that you will not receive any compensation or credit for use of your entry, other than what is described in these official rules.

If you do not want to grant us these rights to your entry, please do not enter this contest.

## 6. Submission of entries
The participants will follow the instructions on the Github repository to submit entries

The participants will be registered as mutually exclusive teams. Each team is allowed to submit only one single final entry. We are not responsible for entries that we do not receive for any reason, or for entries that we receive but do not work properly.

The participants must follow the instructions and the rules. We will automatically disqualify incomplete or invalid entries.

## 7. Judging the entries
The board of NTIRE will select a panel of judges to judge the entries; all judges will be forbidden to enter the 
contest and will be experts in causality, statistics, machine learning, computer vision, or a related field, or 
experts in challenge organization. A list of the judges will be made available upon request. 
The judges will review all eligible entries received and select (three) winners for each or for both of the 
competition tracks based upon the prediction score on test data. The judges will verify that the winners complied 
with the rules, including that they documented their method by filling out a fact sheet.

The decisions of these judges are final and binding. The distribution of prizes according to the decisions made by 
the judges will be made within three (3) months after completion of the last round of the contest. If we do not 
receive a sufficient number of entries meeting the entry requirements, we may, at our discretion based on the above 
criteria, not award any or all of the contest prizes below. In the event of a tie between any eligible entries, 
the tie will be broken by giving preference to the earliest submission, using the time stamp of the submission 
platform.

## 8. Prizes and Awards
The financial sponsors of this contest are listed on NTIRE 2021 workshop web page . 
There will be economic incentive prizes and travel grants for the winners (based on availability) 
to boost contest participation; these prizes will not require participants to enter into an IP agreement with any 
of the sponsors, to disclose algorithms, or to deliver source code to them. 
The participants affiliated with the industry sponsors agree to not receive any sponsored money, 
product or travel grant in the case they will be among the winners.

Incentive Prizes for each track competitions (tentative, the prizes depend on attracted funds from the sponsors)

* 1st place: ?00$ + ?GPU + ?award certificate
* 2nd place: ?00$ + ?GPU + ?award certificate
* 3rd place: ?00$ + ?award certificate

## 9. Other Sponsored Events
Publishing papers is optional and will not be a condition to entering the challenge or winning prizes. The top ranking participants are invited to submit a paper following CVPR2021 author rules, for peer-reviewing to NTIRE workshop.

The results of the challenge will be published together with NTIRE 2021 workshop papers in the 2021 CVPR Workshops proceedings.

The top ranked participants and participants contributing interesting and novel methods to the challenge will be invited to be co-authors of the challenge report paper which will be published in the 2021 CVPR Workshops proceedings. A detailed description of the ranked solution as well as the reproducibility of the results are a must to be an eligible co-author.

## 10. Notifications
If there is any change to data, schedule, instructions of participation, or these rules, the registered participants will be notified on the competition page and/or at the email they provided with the registration.

Within seven days following the determination of winners we will send a notification to the potential winners. If the notification that we send is returned as undeliverable, or you are otherwise unreachable for any reason, we may award the prize to an alternate winner, unless forbidden by applicable law.

The prize such as money, product, or travel grant will be delivered to the registered team leader given that the team is not affiliated with any of the sponsors. It is up to the team to share the prize. If this person becomes unavailable for any reason, the prize will be delivered to be the authorized account holder of the e-mail address used to make the winning entry.

If you are a potential winner, we may require you to sign a declaration of eligibility, use, indemnity and liability/publicity release and applicable tax forms. If you are a potential winner and are a minor in your place of residence, and we require that your parent or legal guardian will be designated as the winner, and we may require that they sign a declaration of eligibility, use, indemnity and liability/publicity release on your behalf. If you, (or your parent/legal guardian if applicable), do not sign and return these required forms within the time period listed on the winner notification message, we may disqualify you (or the designated parent/legal guardian) and select an alternate selected winner.

 ***

The terms and conditions are inspired by and use verbatim text from the `Terms and conditions' of 
[ChaLearn Looking at People Challenges](http://gesture.chalearn.org/icpr2016_contest) 
and of the [NTIRE 2017, 2018, 2019 and 2020 challenges](https://data.vision.ee.ethz.ch/cvl/ntire20/) 
and of the [AIM 2019 and 2020 challenges](https://data.vision.ee.ethz.ch/cvl/aim20/).
