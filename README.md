# READ ME - 'ResearchMethods' Repository
Marieke Schelhaas, S4132734

Research Methods, 28 mrt. 2023

## General Information
Due to the popularity of social networking websites, scientists have access to huge quantities of user-generated data. These social networking sites are accessible, easy to use for many and thus create an insight into everyday life. Since hardware is allowing us to process more and more data, this has drawn the attention of researchers from all kinds of fields. However, one could argue that in their enthusiasm, a lot of conditions for conducting this research in an accurate way are still unknown or ignored. 
 
The aim of this research paper is to find if utterances of happiness are used less often in winter. By researching this phenomenon, researchers could take precautions in the collection and analysis of the Twitter data they use. This is of course in the pursue of establishing facts and reaching new conclusions.
This repository was made for the course "Research Methods" from the Information Science track.

## Background information
Due to the short and easily available messages generated, Twitter data is often used to predict trends in politics or in the economy. As an example, in the research of Cowlessur et al. (2019) it is already proven that public mood has an effect the stock market. It was concluded that “sadness” and “anger” were the most influential moods, when it comes to these predictions. Twitter is also often used predict outcomes regarding the elections, although this topic is quite controversial (Gayo-Avello, 2012). 
Just as Gayo-Avello (2012) already states, making predictions using Twitter data comes with certain conditions that are often overlooked in the enthusiasm of researchers. Seasonal Affective Disorder is a rather common phenomenon that is reported to affect 9% of the population (Booker, J. M., & Hellekson, C. J., 1992). Dam et al. (1998) concluded that about 12.4% of their respondents fulfilled the criteria of Seasonal Affective Disorder. More widely known as “winter depression”, SAD is a recurrent depression during winter-times which usually shows in increased appetite, increased sleeping and carbohydrates (Molin et al., 1996). 

SAD affects a large part of the population on a regular and yearly basis. When such a large part of a population is found in a depressive state, it is not a large stretch to make that this has an influence on public mood. This could mean that dependent on which month you use to make your predictions, your predictions might end up skewed. This could then in turn lead to falsely rejecting or accepting hypotheses, because one did not account for the time of year data was collected. If this effect is indeed true, this indeed needs to be avoided.


## Research Question
On basis of the aforementioned background literature & reasoning, we want to find out:
Does winter/seasonal depression affect the use of linguistic indicators of happiness?

On basis of this research question, we propose the following hypotheses:

H(0):'Utterances of happiness are used just as often in summer as in winter.'

H(a):‘Utterances of happiness are less often used in the winter’


## Method
The tweets from the selected time periods, were stripped of all metadata and the textual content of the tweets were put into a file. These files were then downloaded.
Since counting these words by hand would be prone to error and would also not feasible with the amount of data selected, a python program was created to count these words automatically. The code for this program can be found by going to the next url: https://github.com/maurebi/ResearchMethods. The tweets used for this small research will not be made public for privacy reasons.

The conscious choice was made to keep the retweets found in the extracted Twitter data. The reason being, that when someone retweets a certain message, on can assume that this person is resonating with the sentiment or mood in the tweet. Since tweets can only be retweeted once per person, it is quite save to assume that this approach will not lead to unnecessary duplicates.

This small research study is using qualitative methods (numbers and statistics) to answer the research question.
From the paper 29 words could be extracted, that according to Mihalcea, R. and H. Liu (2006) were indications of everyday happiness (shopping, birthday, cut etc.). Since a lot of English tweets seem to have slipped through the Karora filtering system, we have chosen to incorporate the English word as well as the Dutch translation of our small happiness corpus. In an attempt to filter out the opposite use of adjectives (not interesting vs. interesting), the program also counts these instances and subtracts this number from the detected amount of happy words.




## References
* Booker, J. M., & Hellekson, C. J. (1992). Prevalence of seasonal affective disorder in Alaska. The American journal of psychiatry, 149(9), 1176–1182. https://doi.org/10.1176/ajp.149.9.1176
* Cowlessur, S. K., Annappa, B., Sree, B. K., Gupta, S., & Velaga, C. (2019). Measuring the Influence of Moods on Stock Market Using Twitter Analysis. Advances in Intelligent Systems and Computing. https://doi.org/10.1007/978-981-13-3338-5_29
* Dam, H., Jakobsen, K., & Mellerup, E. T. (1998). Prevalence of winter depression in Denmark. Acta Psychiatrica Scandinavica, 97(1), 1–4. https://doi.org/10.1111/j.1600-0447.1998.tb09954.x
* Gayo-Avello, D. (2012). “I Wanted to Predict Elections with Twitter and all I got was this Lousy   Paper” -- A Balanced Survey on Election Prediction using Twitter Data. ArXiv (Cornell University). https://doi.org/10.48550/arxiv.1204.6441
* Mihalcea, R. and H. Liu (2006, 01). A corpus-based approach to finding happiness. pp. 139–144.
* Molin, J., Mellerup, E. T., Bolwig, T. G., Scheike, T. H., & Dam, H. (1996). The influence of climate on development of winter depression. Journal of Affective Disorders, 37(2–3), 151–155. https://doi.org/10.1016/0165-0327(95)00090-9

