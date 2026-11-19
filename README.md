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


## Conclusions