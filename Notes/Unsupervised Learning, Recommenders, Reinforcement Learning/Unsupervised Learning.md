 
- Cluster a group of data which are similar to each other 

## K-Means Algorithm

### Steps :
	1. Randomly assign K number of Cluster Centroids
	2. Calculate the distances of each datapoints from the centroid
	3. Move the Centroid to get less total distance
	4. At the end it find a patch of data points which are together
	5. If the centroid it not assigned to any things the reinicialise it

![[Pasted image 20260228112333.png]]

## Optimization Objective

![[Pasted image 20260228115302.png]]
- Also called as Distortion Function
## Initializing K-means 

### Random Initialization
- Choose K < m
	- K is the number of centroids and m is the no of training examples
- Randomly pick some training examples
- Do this multiple time and pick the one which gave lowest J (cost function)

## Choosing the the no of Clusters (K)

- Elbow method
	- Run K-means with a variety of values of K and compare the cost function(Distortion function) of it


## Anomaly Detection 

### Finding Unusual Events
- Method - Density Estimation 
- Used in Fraud Detection, Financial Fraud

### Gaussian Distribution / Normal Distribution

 ![[Pasted image 20260304183547.png]]
![[Pasted image 20260304184224.png]]
- The area under the curve is always equal to one
![[Pasted image 20260304184540.png]]
![[Pasted image 20260304185211.png]]


### Real Number Evaluation

- Include a few anomalous examples with labels 
- 

| Anamoly Detection                                                                           | Supervised Learning                                  |
| ------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Very small number of positive examples                                                      | Larger number of positive examples                   |
| Many different types of anomalies (Future Anomalies may not look like the trained examples) | Future examples are similar to the data trained from |
| Ex : Fraud Detection                                                                        | Ex : Email Spam Classification                       |


### Choosing features to use 

- Use Gaussian features 
	- ![[Pasted image 20260310191602.png]]

