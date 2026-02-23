
## Decision Tree Model

![[Pasted image 20260223065421.png]]
- Root Node, Decision Nodes, Leaf Nodes

## Learning Process

- What Decisions to use?
	- Decisions which maximizes the purity 
- When to stop splitting?
	- When the nodes reach a certain depth
	- When a node gets 100% result
	- When a node has less training example of desired result as compared to the other

## Measuring Purity

- **Entropy** as a measure of Impurity
  ![[Pasted image 20260223071110.png]]![[Pasted image 20260223072059.png]]
	- p_x is the probability of positives in any node in a decision tree.

## Choose a Split : Information Gain

- What set of features **reduces entropy** the most.
	- Reduction of entropy is called **Information Gain.**
- Information Gain
	- Taking a **Weighted Average** and subtracting it with the entropy of the previous node 
	  ![[Pasted image 20260223074526.png]]
	  ![[Pasted image 20260223074034.png]]
	- The reduction in the entropy resulted in a split is called **information gain**
	- The increase in information gain result in better model

## Using one-hot encoding of Categorical Features

- Convert each category into new feature

## Continuous Valued Features

- Change the threshold according to the value of information gain 

## Using Multiple Decision Trees

- Tree Ensemble
	- From the multiple decision tree we get multiple outputs. we consider the output which is repeated more times.

## Sampling with Replacement

- Here we take a small sample not from the training example and create a new sample.
- Doesn't matter if the samples are repeated.
- With individual samples you can create a decision tree and get the output value from multiple of those and from that you can get the predicted value.

## Random Forest Algorithm
![[Pasted image 20260223164642.png]]
- Where does a Machine Learning Engineer go camping?
	- To a Random Forest 

## XGBoost

- Extreme Gradient Boosting
- Same like creating a Tree Ensemble but instead of picking from all examples with equal probability, make it more likely to pick misclassified examples from previously trained tree.
- Its one of the highly competitive algorithms in competitions. ![[Pasted image 20260223165735.png]]

## When to use Decision Trees

- Works well in structured data and not preferred for unstructured data.
- Faster to train

### When to use Neural Networks
- work on all types of data
- works with transfer learning
- slower to build
