 
## Iterative Loop of ML Development

- Choose architecture(model, data, etc)
- Train Model
- Diagnostics (Bias, Variance, Error Analysis)
## Error Analysis

- Do the Bias and Variance Analysis ![[Pasted image 20260222193341.png]]

## Adding Data

- Add more data where the error analysis is indicated
	- which is the larger problem
	- where the model is doing its worse
- Data Augmentation
	- Modifying existing training examples to create more and new training examples ![[Pasted image 20260222193431.png]]
- Data Synthesis
	- Creating our own new training examples 
- AI = Code + Data
	- Model Centered Approach : Focusing on code more
	- Data Centered Approach : Focusing on data more 

## Transfer Learning 

- machine learning technique where you **reuse a model trained on one task as the starting point for a different but related task**.
- Used when you have less training examples to train a model.
- Steps :
	- Supervised Pre-training (Training the first model)
		- You can you model from somewhere else but the input type should be same(images, audio, text)
	- Fine tuning (Training the other model)
- Options : 
	- Option 1 : Train only the last layer
	- Option 2 : Train all the parameters initialized with the other model

## Full Cycle of Machine Learning Project 

- Define Project
- Collect Data
- Train Model 
- Deploy in Production ![[Pasted image 20260222214327.png]]
	- MLOps
		- Practice of how to build and deploy a machine learning system.


## Fairness, Bias, and Ethics

- Biased bank loan approvals
- Deepfake Videos
- Brainstorm things that might go wrong before starting a project 
- Audit the system against possible harm prior to deployment
- Develop a mitigation plan

## Error metrics for skewed datasets

- The error analysis doesn't work on these kinda datasets where the odds are far away from 50-50. (Ex : Rare Diseases)![[Pasted image 20260222221107.png]]

## Trading off Precision and Recall

- If y thrush-hold is increased it increase precision and decreases recall and wise-versa. 
  ![[Pasted image 20260222222024.png]] 
- F1 Score
	-  2 * ( Precision * Recall ) / ( Precision + Recall )