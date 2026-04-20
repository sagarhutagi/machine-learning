
- training a model by trail and error with giving the rewards for the expected output

## Return 

- multiply with some factor to the reward for every step 
- the factor is called discount factor(y)
- markov decision process (MDP) - for the formulation 
- the first term is not discounted

## State Action Value Function / Q Function 

- Q(s, a) = Return if you 
	- start in state s 
	- take action a (once)
	- then behave optimally after that


## Bellman Equation 

![[Pasted image 20260420220311.png]]
![[Pasted image 20260420220453.png]]

## Stochastic Environment

![[Pasted image 20260420221048.png]]

## E-Greedy Policy 

![[Pasted image 20260420224236.png]]

## Mini-Batch and Soft Update

**![[Pasted image 20260420225201.png]]**