# sentiment analysis for customer care in product reviews

This project focuses on the development of a Sentiment Analysis System designed to classify product reviews into positive, negative, or neutral sentiments. The system utilizes Natural Language Processing (NLP) techniques to analyse textual data and provide insights into customer opinions. The project involves data collection, pre-processing, model training, and evaluation to ensure accurate sentiment classification. Additionally, it includes a visualization module that presents sentiment trends through interactive charts and graphs, making it easier for users to interpret data. The system also supports data integration from CSV files and allows users to export analysis reports for further use.
The goal of this project is to enhance decision-making by providing businesses and individuals with actionable insights into customer sentiment. Through rigorous testing, the system ensures reliability, usability, and efficiency in analysing sentiment trends.

## Getting started

You can be able to run the application on your local machine

### Prerequisites

Some of the thngs and extensions you will need to download so that your application can be able to run locally are

```
Python
Django
Django-bootstrap3
xhtml2pdf
urllib3
sqlparse
reportlab
PyYAML
pandas
pillow
nltk
numpy
```

### Installing

You should create an enviroment in your folder which will be able to hold all the extensions you are going to be adding
The commands for this are:

```shell script
python3 -m venv --without-pip virtual
sudo apt install python3-pip
source virtual/bin/activate
```

After installation the application should be able to render from the local host.On the terminal run command

```
python3.6 manage.py runserver
```

## Running Test

As this is a python application we have tests.To be able to run the tests run the following command in your terminal

```
python3.6 manage.py test
```
## HOW TO USE THE SYSTEM

First you will need to create an admin user or the system. The admin user has all the rights. Run the following command to create a super user.

```
python manage.py createsuperuser
```
After that then you can login with the credentials you created. This will give you access toall the functionalities of the system including :- yping a review, Uploading dataset, Generating reports, deleting reviews, generating sentiment and creating users.
