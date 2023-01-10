import streamlit as st
import pandas as pd
import numpy as np

st.title('ADHD Self-Report Scale (ASRS)')
st.text('''
Adult 
The Adult ADHD Self-Report Scale (ASRS v1.1) is an 18-item self-report questionnaire designed to assess Attention Deficit Hyperactivity Disorder (ADHD) symptoms in adults (18+). This scale is based on the World Health Organization Composite International Diagnostic Interview (2001), and the questions are consistent with DSM criteria, but reworded to better reflect symptom manifestation in adults. This scale is useful for screening and diagnosis of ADHD among adults 18+ and should be used in conjunction with a clinical interview to provide additional clinical information.

Part A contains 6 items and it has been found that these questions are the most predictive of ADHD and are best for use as a screening instrument. Part-B contains 12 additional questions based on DSM criteria that provide additional cues and can serve as further probes into the patient’s symptoms. For a client’s symptoms to be considered consistent with an ADHD diagnosis, they require 4 or more responses at specific severity levels in Part A of the ASRS.

Psychometric Properties
The ASRS has high internal consistency (Cronbach’s alpha = 0.88) and concurrent validity (r = 0.84) (Adler et al., 2006).

For a client’s symptoms to be considered consistent with an ADHD diagnosis, they require 4 or more responses in the criterion boxes of Part A (the first 6 questions) of the ASRS. Using this scoring convention, previous studies (e.g., Hines, King & Curry, 2012) report high sensitivity (1.0) and moderate positive predictive power (0.52), suggesting that the ASRS would rarely miss ADHD in an adult who has ADHD. Moreover, the ASRS has moderate specificity (.71) and high negative predictive power (1.0), indicating that this tool is quite successful in not identifying someone with ADHD when they do not have the disorder (Hines, King & Curry, 2012).

Adler et al. (2018) found that in a sample of 22,397 randomly selected adults in the USA that the mean total score was 2.0 (SD = 3.2). Of note, ASRS total scores where significantly related to age:

– Age 18-29: mean = 2.99, stdev = 4.1
– Age 30-39: mean = 2.59, stdev = 3.1
– Age 40-49: mean = 2.26, stdev = 3.1
– Age 50-64: mean = 1.82, stdev = 3.1
– Age > 65: mean = 1.23, stdev = 2.1

This age specific normative data is used to compute percentiles.

Stanton, Forbes and Zimmerman (2018) determined, by using CFA with over 1,000 adult subjects, that the ASRS had three factors:

Inattentive subscale
Motor Hyperactive/Impulsive subscale
Verbal Hyperactive/Impulsive subscale
These factors are used to compute subscale scores. It is noted that the DSM specifies two subtypes (Inattentive and Hyperactive/Impulsive) however analysis of this scale indicates three distinct symptom clusters. 
Scoring and Interpretation
Three seperate metrics are computed:

–Part A (items 1-6. Scores range from 0 to 6)
If the respondent scores 4 or more in Part-A, then the symptom profile of the individual is considered to be highly consistent with an ADHD diagnosis in adults (Adler et al., 2006; Kessler et al., 2007).

–Part B (items 7-18. Scores range from 0 to 12)
The frequency scores on Part B provide additional cues and can serve as further probes into the patient’s symptom severity and the impact that inattention or hyperactivity has on their life.

– Total Score (and percentile) (scores range from 0 to 18)
Over and above the key interpretation metrics from Part A and Part B, the total score (sum of part A and B) is converted into a percentile to contextualise responses in comparison to normative data (22,397 adults; Adler et al., 2018). For example, a percentile of 90 represents that the respondent scored higher than 90 percent of other typical adults in their age range in the community.

These percentiles compare total scores to age related peers, so it is imperative to ensure the correct client date of birth is entered for the client.

While Part A contains the items that have been found to be most predictive of ADHD, looking at the total score (and percentile) can also be informative about diagnosis in cases where the Part A score was only 3. This scale should always be used in conjunction with a clinical interview to provide additional clinical information important for diagnosis.

Three ADHD subscales are presented according to factors identified by Stanton et al. (2018). Raw scores as well as the percentage of items endorsed are presented, providing more specific information about difficulties:

Inattentive subscale (Items 1, 2, 3, 4, 7, 8, 9, 10, 11, range 0 to 9)): measuring an adult’s difficulty in focussing on details, being organised, remembering appointments, making careless mistakes, and concentrating.
Hyperactive/Impulsive subscale (Motor) (Items 5, 6, 12, 13, 14, range 0 to 5): measuring an adult’s difficulty in sitting still, staying seated, and ability to relax.
Hyperactive/Impulsive subscale (Verbal) (Items 15, 16, 17, 18, range 0 to 4): measuring an adult’s difficulty in controlling how much they are talking, interrupting others, and waiting their turn.
Considering the percentage of items endorsed for each of the subscales can be helpful in determining the ADHD subtype defined in DSM-V: Combined, Hyperactivity-Impulsivity or Inattentive. Note that the DSM-V does not make a distinction between verbal and motor hyperactive subtypes.

Depending on the question, responses are either scored as 0 or 1. On items 1-3, 9, 12, 16, and 18 ratings of sometimes, often, or very often are assigned one point (ratings of never or rarely are assigned zero points). For the remaining 11 items, ratings of often or very often are assigned one point (ratings of never, rarely, or sometimes are assigned zero points).

Developer
Kessler, R. C., Adler, L., Ames, M., Demler, O., Faraone, S., Hiripi, E., Howes, M. J., Jin, R., Secnik, K., Spencer, T., Ustun, T. B., & Walters, E. E. (2005). The World Health Organization Adult ADHD Self-Report Scale (ASRS): a short screening scale for use in the general population. Psychological Medicine, 35(2), 245–256. https://doi.org/10.1017/s0033291704002892

References
Adler, L. A., Faraone, S. V., Sarocco, P., Atkins, N., & Khachatryan, A. (2019). Establishing US norms for the Adult ADHD Self-Report Scale (ASRS-v1.1) and characterising symptom burden among adults with self-reported ADHD. International Journal of Clinical Practice, 73(1), e13260. https://doi.org/10.1111/ijcp.13260

Adler, L. A., Spencer, T., Faraone, S. V., Kessler, R. C., Howes, M. J., Biederman, J., & Secnik, K. (2006). Validity of pilot Adult ADHD Self- Report Scale (ASRS) to Rate Adult ADHD symptoms. Annals of Clinical Psychiatry: Official Journal of the American Academy of Clinical Psychiatrists, 18(3), 145–148. https://doi.org/10.1080/10401230600801077

Hines, J. L., King, T. S., & Curry, W. J. (2012). The adult ADHD self-report scale for screening for adult attention deficit-hyperactivity disorder (ADHD). Journal of the American Board of Family Medicine: JABFM, 25(6), 847–853. https://doi.org/10.3122/jabfm.2012.06.120065

Stanton, K., Forbes, M. K., & Zimmerman, M. (2018). Distinct dimensions defining the Adult ADHD Self-Report Scale: Implications for assessing inattentive and hyperactive/impulsive symptoms. Psychological Assessment, 30(12), 1549–1559. https://doi.org/10.1037/pas0000604 
''')