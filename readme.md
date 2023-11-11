# Health Pet

This repository contains the code for our submission to Junction 2023 Huawei "Sense the motion" -challenge.

### Contributors:
* @Vsimpro (https://www.github.com/Vsimpro)
* @laivii (https://www.github.com/laivii)

## Why and What does it do?

This is project was written to visualize our idea of a Health Pet for the Huawei Health -application. Basicly the idea of the pet is to visualise the data that the watch collects (of you), and by doing so make you more motivated to take care of yourself. The feature kind of gamificates the process of being healthy. We decided on making the pet visualize the data of your <i>sleep, steps and stress</i>.

The website should have:
* Instructions on how to use it
* The actual visual representation in the middle
* Four buttons to change the dataset
  * By pressing a button the visuals should change :)

## How to run:

frontend:
```
cd frontend/
npm install
npm start
```

backend:
```
cd backend/
python3 main.py
```
You may need to install packages like Flask, flask-cors, pymysql, and dotenv.
