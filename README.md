# LiveChat

## About the project:
This is a Live chating/messaging application created with in Flask and FlaskWebSockeIO can create room wchich can be accessed by multiple people at the same time and provide seamless communication
<br>
<hr>

## setup:
Make sure you have python installed after that we make a virtual enviorment and install the requirements
```
python -m venv env && python -r requirements.txt
```

To intialize the server you can run (with gunicorn):

```
gunicorn run:app
```
note - if you having trouble with guincorn you can use teh other method to run the app or directly run the Run.py file with python

To intialize the server you can run (without gunicorn):
```
export FLASK_APP=Run.py && flask run
```
<br>
<hr>

## Our Contributors

<a href="https://github.com/volt-l18/Live-Chat-room-with-Flask/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=volt-l18/Live-Chat-room-with-Flask" />
</a>
<br>
<hr>
