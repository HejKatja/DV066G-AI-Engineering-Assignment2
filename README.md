# Local LLM Testing: Unit Tests and LLM-as-a-Judge

## Introduction

The purpose of this project is to evaluate consistency and reliablility a local LLM using Ollama. Unit tests and LLM-as-a-judge approach are used to test answer accuracy, error handling and the detectio of hallucinations.<br>

Sex unit tests were implemented to test the LLM answer and validate the LLM-as-a-judge evaluation:<br>

### Test 1. Wrong model (*test_unknown_model_returns_failure*)
Checks whether the *ask_capital()* function returns **"Failure."** when an unknown model is provided as argument.

### Test 2. LLM consistency: Sweden (*test_knows_capital_of_sweden*)
Asks the LLM the question "What is the capital of Sweden?". The test passes if at leats two of the three answers contain "Stockholm".

### Test 3. LLM consistency: Australia (*test_knows_capital_of_australia*)
Asks the LLM the question "What is the capital of Australia?". The test passes if at leats two of the three answers contain "Canberra".

### Test 4. LLM-as-a-judge: Sweden (*test_judge_accepts_right_capital_sweden*)
Checks whether the LLM judge accepts the correct answer that Stockholm is the capital of Sweden.

### Test 5. LLM-as-a-judge: Australia (*test_judge_accepts_right_capital_australia*)
Checks whether the LLM judge accepts the correct answer that Canberra is the capital of Australia.

### Test 6. LLM-as-a-judge: Bealandia (*test_judge_rejects_invented_capital*)
Checks whether the LLM judge rejects the incorrect answer that Bea City is the capital of the fictional country Bealandia

## Setup and Requirements 

### Requirements

* Python 3.12 or later 
* Ollama 
* Ollama Python library

### 1. Install Ollama 

#### **macOS**

Download and install Ollama via [ollama.com/download](https://ollama.com/download).<br>
Alternatively, install it using the terminal:<br>

````
curl -fsSL https://ollama.com/install.sh | sh
````
#### **Windows**

Download and install Ollama via [ollama.com/download/windows](https://ollama.com/download/windows).<br>
Alternatively, install it using the terminal:<br>

````
irm https://ollama.com/install.ps1 | iex
````

### 2. Clone the repository

````
git clone https://github.com/HejKatja/DV066G-AI-Engineering-Assignment2.git
````

### 3. Install Python package

````
pip install ollama
````

### 4. Download the models

````
ollama pull gemma4
````

## How to Run 

Run the unit tests: 

````
python -m unittest tests.ollama_test -v
````


## Results 

#### Run 1<br>


|     Test      |   Result           |  
| ------------- | ------------------ | 
|     Test 1    |       pass         | 
|     Test 2    |       pass         |    
|     Test 3    |       pass         | 
|     Test 4    |       pass         |
|     Test 5    |       pass         | 
|     Test 6    |       pass         |

<br>


#### Run 2<br>


|     Test      |   Result           |  
| ------------- | ------------------ | 
|     Test 1    |       pass         |     
|     Test 2    |       pass         | 
|     Test 3    |       pass         | 
|     Test 4    |       pass         |   
|     Test 5    |       pass         |   
|     Test 6    |       pass         |    

<br>


#### Run 3<br>


|     Test      |    Result          |   
| ------------- | ------------------ | 
|     Test 1    |       pass         | 
|     Test 2    |       pass         |  
|     Test 3    |       pass         | 
|     Test 4    |       pass         |      
|     Test 5    |       pass         |     
|     Test 6    |       pass         |    

<br>


#### Run 4<br>


|     Test      |   Result           |  
| ------------- | ------------------ | 
|     Test 1    |      pass          | 
|     Test 2    |      pass          |  
|     Test 3    |      pass          |
|     Test 4    |      pass          |
|     Test 5    |      pass          |
|     Test 6    |      pass          | 

<br>


#### Run 5<br>


|     Test      |   Result           | 
| ------------- | ------------------ | 
|     Test 1    |      pass          | 
|     Test 2    |      pass          |
|     Test 3    |      pass          |
|     Test 4    |      pass          |
|     Test 5    |      pass          | 
|     Test 6    |      pass          | 

<br>


## Reflections

All of the aforementioned tests were run 5 times and passed in every run. Does this result allow us to conclude that local LLMs are trustworthy? Not necessarily, since our experiment's result is not representative of local LLMs in genereal: we tested only one local model, on quite easy questions, with a small number of runs and with exactly the same model (gemma4) as the judge.<br>

### Do the tests always give the same result?

If by this question we mean the same pass/fail result, then yes, the tests gave the same result (pass) in all 5 runs. We believe this is because the model's training data is not corrupted with incorrect information about the facts that Stockholm and Canberra are the capitals of Sweden and Australia respectively. So the correct answer is by far the most probable one. The question itself is also very simple and unambiguous, which leaves little chance for the model to answer incorrectly. <br>

However, the stable result we've got should not be considered as proof that the model does not hallucinate or that it is completely free from bias and mistakes. Since hallucinations often stem from poor/biased training data, factual mistakes or vague prompts (to name a few), we could mitigate them by using well-designed tests. First of all, the tests are built around a clear and straightforward prompt that contains no false premises and asks for a well-documented fact that is unlikely to confuse the model. Moreover, the LLM-as-a-judge is used in a way that also helps to reduce its own risk of hallucinating: the judge is given the expected answer, the prompt is clear and constraint (yes or no). Since we use the same model for testing and judging, this also helps to mitigate models' blind spots (shared training data with the same mistakes). In addition, the consistency tests use a threshold of 2 correct answers out of 3, which protects against a single random mistake but at the same time means that one incorrect answer can pass unnoticed. 


If the question instead addresses the determinism of the model ,meaning whether it gaves identical answers every time, then we cannot answer it, since tests are not designed to evaluate it. The tests do not compare the model's answers with each other across different runs, they only check whether each answer contains the expected word ("Stockholm" or "Canberra"), so different variations of a correct answer will still pass. Because the model's ouput is generated with some inherent randomness, it is likely that the wording varied between runs, but our tests would not have shown it.

### Can we tell whether a failure comes from the model or the judge? 

Yes, the design of the tests makes it possible to differintiate the source of failure. 

### Comclusion 

In conclusion, in this particular situation, with these particular tests, these particular prompts, this particular model version, this particluar threshold and this particular numbers of runs, the local LLM behave as reliable. The result may not hold for other models or even the same model versions, vague or ambiguous prompts, larger number of runs or higher threshold. Testing an AI component (the local LLM in our case) therevore should be seen as continuous activity. 