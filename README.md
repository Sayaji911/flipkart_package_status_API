# Flipkart Package Tracker Bot

Whatsapp Bot that gives Delivery status of Package from Flipkart
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
python3 -m venv <myenvname>
source env/bin/activate
pip install -r requirements.txt
```

## Running the app
```
uvicorn main:app --reload
```

## Deployment

I've deployed the app on Microsoft Azure and used Twilio Sandbox to run the bot
```
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```
## Built With

* [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
* [Beautifulsoup](https://pypi.org/project/beautifulsoup4/) - Powerful Web Scrapper
* [Twilio](https://www.twilio.com/) - Messaging API
* [Microsoft Azure](https://azure.microsoft.com/) - Cloud

## Screenshots
![image](https://user-images.githubusercontent.com/22417162/116059704-bcf2bb80-a69e-11eb-81ad-e558df6df68a.png)




## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* People of FastAPI discord server

