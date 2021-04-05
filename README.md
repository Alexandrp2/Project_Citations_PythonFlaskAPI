# Fullstack citation application

*This documentation is similar if you read it from the API GitHub repository or from website GitHub repository*

## Objective 

This application implements CRUD operations for citations.

## Parts of the project

A No-SQL database.
A REST API [here](https://github.com/Alexandrp2/Project_Citations_PythonFlaskAPI).
A website (a client consuming the API) [here](https://github.com/Alexandrp2/Project_Citations_WebSite).

## Technologies

The database is based on **MongoDB**.
The REST API is based on Python **Flask**.
The website is based on **HTML/CSS/Javascript**.

## Pre-requisites

Having installed mongodb. A GUI for MongoDB can be useful (we used Robo 3T).
According the official documentation *Flask supports Python 3.5 and newer, Python 2.7* but it is recommended to use the latest Python version.
The website has been developed to be used with no other action than launching the `index.html` file.

## Installation steps

1. Download the GitHub repositories
 * REST API [here](https://github.com/Alexandrp2/Project_Citations_PythonFlaskAPI).
 * Website [here](https://github.com/Alexandrp2/Project_Citations_WebSite).
2. Open mongodb and create a database named `citations-app` and one collection named `citations`
3. In this collection insert a dataset: copy/paste [this content](https://github.com/Alexandrp2/Project_Citations_PythonFlaskAPI/blob/master/mongoInitCollection) in the `citations` collection
    * This should create 14 documents in the collection
    * Your database is now set up
4. To set up your Flask environment, run these commands (on Windows). You can also consult the installation doc [here](https://flask.palletsprojects.com/en/1.1.x/installation/#installation).
    * This should be sufficient to work (although we don't create a virtual environment as recommended):
       * Install Flask : ```pip install flask```
       * Install pymongo: ```pip install flask_pymongo```
       * To manage CORS policy: ```pip install -U flask-cors```
       * **Optional** : To connect to a cluster (unused but useful to connect to a mongoDB cloud) : ```pip install dnspython```
    * Your API is now ready for use
5. Run the 3 stacks :
    * Mongodb: start MongoDB
    * API (example with *Visual Studio Code*) : open the code editor, install a Python extension: `ms-python.python` and simply run it with the run command of the editor
    * Website : simply click on the `index.html` to open the project in a browser

Alternatively you can launch the Flask API by opening a Windows terminal where is located `flask_api_mongo_citations.py`, and then enter the 2 following commands.
More details in the Flask [Quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/). 
```PowerShell
set FLASK_APP=flask_api_mongo_citations.py
flask run
```