from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/bot', methods=['POST'])
def bot():
    resp = MessagingResponse()
    msg = resp.message()
    incoming_msg = requests.values.get('Body', ' ').lower()
    if 'palavra chave' in incoming_msg:
        msg.media('http da API ')
    else:
        msg.body('Digite: palavra chave')
    return str(resp)

if __name__ == '__main__':
    app.run()