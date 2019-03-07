# Data Download and Pre Processing
1. Download the "Adult Data Set" from this link:http://archive.ics.uci.edu/ml/datasets/Adult
2. Download the "Credit Card Defualt" data set from this link: http://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients
3. Convert the data files to csv
4. In the Credit Card Default Data Set:
-Filter Eductaion to 0, 5, and 6. Delete these rows. 
-Filter Marriage to 0. Delete these rows. 
-Delte blank rows by going to Find & Select > Go To Special > Blanks
-Unfilter and save as csv
5. In the Adult data set:
-Add column names by referring to this link:http://archive.ics.uci.edu/ml/datasets/Adult
-Filter workclass column to ?. Delete these rows. 
-Delte blank rows by going to Find & Select > Go To Special > Blanks
-name the last class column as incomeLabel and change >$50k as 1 and <=$50k as 0
-Unfilter and save as csv
6. Open Weka
-Go to Tools and ArffViewer
-Open both the csv data sets and save it as arff files
-open the arff files and make sure to change the class labels. See example below:
@attribute income_label {0,1}

# Create Train and Test Data set
1.Open Weka and click explorer
2. Click Open file..
3. Slect Credit Defualt arff file you created in the previous step
4. Select Under Filter > unsupervised > instance > resample
5. Left click on resample and change the noReplacement to True
6. Set the sampleSizePercent as 70 and click ok and apply
7. Select Under Filter > unsupervised > instance > randomize
9. Save the file and call it trainCreditDefualt.arff (this file should be larger than test file)
10. Select Under Filter > unsupervised > instance > resample
11. Left click on resample and change invertSelection to True and click ok and apply
12. Select Under Filter > unsupervised > instance > randomize
13. Save the file and call it testCreditDefualt.arff (this file should be smaller than train file)
14. Repeat these steps to create train and test files for the Adult data set

# Weka Instructions
1. Download the latest version of Weka from this link:https://www.cs.waikato.ac.nz/ml/weka/downloading.html
2. Download and install latest version of Java from this link: https://www.java.com/en/download/
3. Upon download, click on Weka and go to tools and package manager
4. Install SMOTE and GridSearch. Please note that if you don't have a package, you can revisit package explorer to download it. 

# Instructions for running the algorithms in Weka
1. Decesion Tree: 
-Click on classify tab
-Click on Choose and under Meta select CostSensitiveClassfier
-Left click on it and a tab pops up. Under costMatrix > Classes enter 2 and resize 
-In the Cost 2 by 2 matrix, chnage 1 to 5 under first column second row and close that window
-Now in classifier Choose trees > J48 and click ok
-Under Test options select either Training, Supplied Test Set , or Cross-validation
-If you use Supplied Test Set, ensure you supply the test arff file that you created in the previous step

2. Boosting:
-Click on classify tab
-Click on Choose and under Meta select CostSensitiveClassfier
-Left click on it and a tab pops up. Under costMatrix > Classes enter 2 and resize 
-In the Cost 2 by 2 matrix, chnage 1 to 5 under first column second row and close that window
-Now in classifier Choose meta > AdaBoostM1 and click ok
-Left clik on AdaBoostM1 and window pops up. 
-In the boosting window, choose classifier treees >J48 and click ok. In J48 you can manipulate the confidence factor and minimum instace. Click ok. 
-Under Test options select either Training, Supplied Test Set , or Cross-validation
-If you use Supplied Test Set, ensure you supply the test arff file that you created in the previous step

3. KNN:
-Click on classify tab
-Click on Choose and under Meta select CostSensitiveClassfier
-Left click on it and a tab pops up. Under costMatrix > Classes enter 2 and resize 
-In the Cost 2 by 2 matrix, chnage 1 to 5 under first column second row and close that window
-Now in classifier Choose lazy> ibk and click ok
-Left click on ibk to manipulate k

4. Neural Network:
-Click on classify tab
-Click on Choose and under Meta select CostSensitiveClassfier
-Left click on it and a tab pops up. Under costMatrix > Classes enter 2 and resize 
-In the Cost 2 by 2 matrix, chnage 1 to 5 under first column second row and close that window
-Now in classifier Choose functions> multilayePerception and click ok
-Left click on multilayePerception to manipulate hiddenlayers, momentum, and learning rate. click ok. 

5. Support Vector Machine:
-Click on classify tab
-Click on Choose and under Meta select CostSensitiveClassfier
-Left click on it and a tab pops up. Under costMatrix > Classes enter 2 and resize 
-In the Cost 2 by 2 matrix, chnage 1 to 5 under first column second row and close that window
-Now in classifier Choose functions> SMO and click ok
-Left click on SMO to manipulate with the kernal type, C, and gamma. click ok. 

Learning Curve:
To create a learning curve:
-Click on classify tab
-Click on Choose FilteredClassifier
-Left click on FilteredClassifier and select your desired classifier
-Under filter in the FilterdClassifier tab, select unsupervised > instace > resample
-Left click on resample and change the noReplacement to True
-Set the sampleSizePercent from 10 to 90 and click ok and apply
-Generate your accuracy scores by clicking on Use training set and test set. 
-Note these scores in an excel spreadsheet along with the sample sizes.
-Create a line graph in excel with your results where the x axis is size of dataset and y is accuracy score
 
