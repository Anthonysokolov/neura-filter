from flask import Flask

app = Flask(__name__)

@app.route('/')
def landing_page():
    return 'pls upload a photo/video file'

app.run()