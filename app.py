from flask import Flask, request
import twilio.twiml
import os
from random import choice
 
app = Flask(__name__)

# Add more callers to the list to personalize the experience
callers = {
    "+447446088827": "Haje",
    "+447411426427": "Ziah",
    "+15103842583": "Tim",
    "+14155312828": "Robin",
}

@app.route("/", methods=['GET', 'POST'])
def hire_ziah():
    """Respond to incoming calls/texts with a text message of why you should hire Ziah."""
    from_number = request.values.get('From', None)

    if from_number in callers:
        greeting = "Hi, " + callers[from_number] + ". You should hire Ziah because "
    else:
        greeting = "Hi, there! You should hire Ziah because "

    resp = twilio.twiml.Response()
    resp.sms(greeting + choice(reasons))
    return str(resp)

 
reasons = [
    'she mixes a mean cocktail.',
    'she speaks geek, management, and artist fluently.',
    'she\'s got loads of experience helping people acheive their best with new or unfamiliar tools.',
    'she\'s a great leader.',
    'she understands the high level stuff, and just \"gets it\".',
    'she shines in a fast-paced, high stress environment.',
    'she\'s passionate about working with clever people and helping them succeed.',
    'people love working with her.',
    'she works and plays well with everyone.',
    'she\'s super-organized.',
    'she can write - both English & code.']

 
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
 
    if port == 5000:
        app.debug = True
 
    app.run(host='0.0.0.0', port=port)
