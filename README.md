
<h1>Iron Bank of Bravos</h1>
</br>
<p>The investment market has been known to be vulnerable by ample of market makers, which is protected by FINRA as a regulatory body.
As the brokers are closely related to both, the markets and the investors, hold huge significance in keeping the markets clean and stable. 
Here, we are trying to use the data provided by FINRA about the brokers of different firms and their background to:
</br>
</br>

1. Performed clustering on the data to identify possible number of groups which may act as a label to a set of similar brokers.

2. Assess the credibility of the brokers by using their background information and creating a metric.

3. Delinquent loan classifier.
</p>
</br>

<h3>1. Investment Broker Clustering :</h3>
<p> 
We tackled a fairly large dataset on the characteristics of Investment brokers which had about 300,000 datapoints. Most of the data was highly categorical in nature and needed an unsuperivised approach to make sense of the data. 

</br>
We looked at all the categorical variable and tried to make one hot and ordinal representations of the data. On top of these sparse embedding, we tried clustering using K-Mode clustering and mapped them into 4 classes, plotting them onto 2d and 3d surfaces. We used Linear Discriminant Analysis(LDA) for the dimensionality reduction.
</br>
We also tried Deep Learning based methods like Self Organizing Maps and Autoencoders to get an unsupervised clustering of the data and a feature dense embedding.
</p>

</br>
<p>
<h3>2. Designed a metric to measure credibility of Investment advisers:</h3>
We tried to assess the credibility of the brokers by using their background information and our insights from working with data in high dimensional space and created a metric.
</br>

We did fetaure analysis on the categorical variables and analyzed their respective performance on Random Forests to estimate what described the data the most and built a metric based on a weighted combination of these parameters.
</br>

</p>
<h3>3. Delinquent loan classifier. :</h3>
<p>
	Loan Default is one of the major problems faced by the Financial Institutions. In a lot of cases simple statistical approaches fail to identify some patterns which can precisely be located by ensemble models.
</br>

</br>
	 We have shown a demonstration of the same in my analysis wherein firstly, we try to identify the most the relevant features for our dependant variable and then use them for prediction. Initially we tried using the Logistric Regression Approach, however, it failed to give us a desired accuracy. Then we shifted to ensembe methods like decision trees and we successful to generate a model which would predict the loan_default probability of a customer for the bank and equip the banks to avoid the losses. The Overall Accuracy of the Decision Tree was around 98%. 
</br>

</p>
