> [!NOTE]  
> Para acessar o README em Português-BR acesse este [link](https://github.com/VictorJSSantos/Embrapa-API/blob/main/README.pt-br.md)

# Overview 

This project is an API under development to access data from Embrapa regarding the grape production process (and other information as well; see the link for detailed data) in the State of Rio Grande do Sul, available at this link.

This project is the result of the first module of the FIAP postgraduate course in Machine Learning Engineering, which covered, among other topics:

* Fundamentals of Python
* Creating modules and libraries
* Object-oriented programming
* Data structures
* APIs and ML frameworks

This project was created by a team of two data engineering students, Victor Santos and Tatiana Haddad. We also received support from two course instructors, Leonardo Pena and Ioannis Eleftheriou, who helped clarify the questions we had along the way.

Thank you very much for your help, professors!

# Objectives 

The objective of this project is to create an API with a scope that should include the following areas of interest:

* Production
* Processing
* Commercialization
* Importation
* Exportation

Within this context, the project consisted of ensuring that the following activities were carried out:

* Create a REST API in Python that queries the Embrapa website. - ✔
* The API should be documented. - ✔
* It is recommended (but not mandatory) to choose an authentication method (e.g., JWT). - ✔
* Create a plan for deploying the API. - ✔
* Develop an MVP, deploy it with a shareable link, and provide a repository on GitHub. - ✔

# Project directories

The project contains the main files related to its operation inside the "app" folder, which will hold important information. Below is a brief description of the files and their contents:

main.py - The main file of the application, responsible for starting the application.
models.py - The file containing all the classes (models) that represent the query parameters to ensure the query is executed correctly.
requisicao_http.py - The file containing the Requisition class, designed to simplify the maintenance and execution of HTTP actions.
transformar.py - The file containing the Transform class, used for further manipulation of the results after the HTTP request.
utils.py - The file containing general-purpose functions that can be accessed across other parts of the program, aiming to centralize usage and improve maintainability.

Finally, we also have the "routes" and "schemas" folders. Both folders are separated according to the application context. For this project, each route and schema is organized by contexts (Production, Processing, Commercialization, etc.). The goal is to improve code maintainability and make it more aligned with best practices for API development.

# 
Prerequisites

Python - Version >= 3.9 to <= 3.11



# Environment Setup

1. Clone repo:
  > git clone https://github.com/VictorJSSantos/Modulo-1.git

2. Create a virtual env: 
  > python -m venv venv

3. Activate virtual env: 
Windows:
  > venv\Scripts\activate
Linux:
  > source venv/bin/activate

4. Configure the Python interpreter in a virtual environment:
Ctrl + Shift + P to open the command palete.
  > Write Python: Select Interpreter - To choose the Python interpreter inside the venv folder.

5. Update pip to ensure proper installation of dependencies:
  > python -m pip install --upgrade pip

5. Install the dependencies:
  > pip install -r requirements.txt



# API's architeture

![Arquitetura da API Embrapa](https://github.com/VictorJSSantos/Modulo-1/blob/main/API%20-%20Arquitetura%20.jpg)


![Funcionamento da API](https://github.com/VictorJSSantos/Modulo-1/blob/main/API%20-%20Funcionamento%20Interno.jpg)


