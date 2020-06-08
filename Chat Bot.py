from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)


@app.route("/")
def hello():
    return "AI Chat Bot"

@app.route("/sms",methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')
    phone_number = request.form.get('From')
    import utilities
    resp = MessagingResponse()
    resp.message(taking_data())
    return str(resp)
def taking_data():
        response = "Hi There! Please " \
                   "Enter Your Name,Age, Gender,Email"
        return response
if __name__ == "__main__":
    app.run(debug=True)


