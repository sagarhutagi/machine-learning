
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

- Entropy as a measure of Impurity
  ![[Pasted image 20260223071110.png]]![[Pasted image 20260223072059.png]]
	- p_x is the probability of positives in any node in a decision tree.

## Choose a Split : Information Gain

- What set of features reduces entropy the most.
	- Reduction of entropy is called **Information Gain.**
- Information Gain
	- Taking a **Weighted Average** and subtracting it with the entropy of the previous node 
	  ![[Pasted image 20260223074526.png]]
	  ![[Pasted image 20260223074034.png]]
	- The reduction in the entropy resulted in a split is called **information gain** 