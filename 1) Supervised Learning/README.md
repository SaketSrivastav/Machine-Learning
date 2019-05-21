# Data Download and Pre Processing
1. Download the "Adult Data Set" from this link:http://archive.ics.uci.edu/ml/datasets/Adult <br />
2. Download the "Credit Card Defualt" data set from this link: http://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients <br />
3. Convert the data files to csv <br />
4. In the Credit Card Default Data Set: <br />
-Filter Eductaion to 0, 5, and 6. Delete these rows.  <br />
-Filter Marriage to 0. Delete these rows.  <br />
-Delte blank rows by going to Find & Select > Go To Special > Blanks <br />
-Unfilter and save as csv <br />
5. In the Adult data set: <br />
-Add column names by referring to this link:http://archive.ics.uci.edu/ml/datasets/Adult <br />
-Filter workclass column to ?. Delete these rows.  <br />
-Delte blank rows by going to Find & Select > Go To Special > Blanks <br />
-name the last class column as incomeLabel and change >$50k as 1 and <=$50k as 0 <br />
-Unfilter and save as csv <br />
6. Open Weka <br />
-Go to Tools and ArffViewer <br />
-Open both the csv data sets and save it as arff files <br />
-open the arff files and make sure to change the class labels. See example below: <br />
@attribute income_label {0,1} <br />

# Create Train and Test Data set
1.Open Weka and click explorer <br />
2. Click Open file.. <br />
3. Slect Credit Defualt arff file you created in the previous step <br />
4. Select Under Filter > unsupervised > instance > resample <br />
5. Left click on resample and change the noReplacement to True <br />
6. Set the sampleSizePercent as 70 and click ok and apply <br />
7. Select Under Filter > unsupervised > instance > randomize <br />
9. Save the file and call it trainCreditDefualt.arff (this file should be larger than test file) <br />
10. Select Under Filter > unsupervised > instance > resample <br />
11. Left click on resample and change invertSelection to True and click ok and apply <br />
12. Select Under Filter > unsupervised > instance > randomize <br />
13. Save the file and call it testCreditDefualt.arff (this file should be smaller than train file) <br />
14. Repeat these steps to create train and test files for the Adult data set <br />

# Weka Instructions
1. Download the latest version of Weka from this link:https://www.cs.waikato.ac.nz/ml/weka/downloading.html <br />
2. Download and install latest version of Java from this link: https://www.java.com/en/download/ <br />
3. Upon download, click on Weka and go to tools and package manager <br />
4. Install SMOTE and GridSearch. Please note that if you don't have a package, you can revisit package explorer to download it. <br />

# Instructions for running the algorithms in Weka
1. Decesion Tree: <br />
-Click on classify tab <br />
-Click on Choose and under Meta select CostSensitiveClassfier <br />
-Left click on it and a tab pops up. Under costMatrix > Classes enter 2 and resize <br />
-In the Cost 2 by 2 matrix, chnage 1 to 5 under first column second row and close that window <br />
-Now in classifier Choose trees > J48 and click ok <br />
-Under Test options select either Training, Supplied Test Set , or Cross-validation <br />
-If you use Supplied Test Set, ensure you supply the test arff file that you created in the previous step <br />

2. Boosting: <br />
-Click on classify tab <br />
-Click on Choose and under Meta select CostSensitiveClassfier <br />
-Left click on it and a tab pops up. Under costMatrix > Classes enter 2 and resize <br />
-In the Cost 2 by 2 matrix, chnage 1 to 5 under first column second row and close that window
-Now in classifier Choose meta > AdaBoostM1 and click ok
-Left clik on AdaBoostM1 and window pops up. <br />
-In the boosting window, choose classifier treees >J48 and click ok. In J48 you can manipulate the confidence factor and minimum instace. Click ok. <br />
-Under Test options select either Training, Supplied Test Set , or Cross-validation <br />
-If you use Supplied Test Set, ensure you supply the test arff file that you created in the previous step <br />

3. KNN: <br />
-Click on classify tab <br />
-Click on Choose and under Meta select CostSensitiveClassfier <br />
-Left click on it and a tab pops up. Under costMatrix > Classes enter 2 and resize  <br />
-In the Cost 2 by 2 matrix, chnage 1 to 5 under first column second row and close that window <br />
-Now in classifier Choose lazy> ibk and click ok <br />
-Left click on ibk to manipulate k <br />

4. Neural Network: <br />
-Click on classify tab <br />
-Click on Choose and under Meta select CostSensitiveClassfier <br />
-Left click on it and a tab pops up. Under costMatrix > Classes enter 2 and resize  <br />
-In the Cost 2 by 2 matrix, chnage 1 to 5 under first column second row and close that window <br />
-Now in classifier Choose functions> multilayePerception and click ok <br />
-Left click on multilayePerception to manipulate hiddenlayers, momentum, and learning rate. click ok. <br /> 

5. Support Vector Machine: <br />
-Click on classify tab <br />
-Click on Choose and under Meta select CostSensitiveClassfier <br />
-Left click on it and a tab pops up. Under costMatrix > Classes enter 2 and resize  <br />
-In the Cost 2 by 2 matrix, chnage 1 to 5 under first column second row and close that window <br />
-Now in classifier Choose functions> SMO and click ok <br />
-Left click on SMO to manipulate with the kernal type, C, and gamma. click ok.  <br />

7. Learning Curve: <br />
To create a learning curve: <br />
-Click on classify tab <br />
-Click on Choose FilteredClassifier <br />
-Left click on FilteredClassifier and select your desired classifier <br />
-Under filter in the FilterdClassifier tab, select unsupervised > instace > resample <br />
-Left click on resample and change the noReplacement to True <br />
-Set the sampleSizePercent from 10 to 90 and click ok and apply <br />
-Generate your accuracy scores by clicking on Use training set and test set. <br />
-Note these scores in an excel spreadsheet along with the sample sizes. <br />
-Create a line graph in excel with your results where the x axis is size of dataset and y is accuracy score <br />
 
