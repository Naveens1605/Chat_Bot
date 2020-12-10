from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
# import mysql.connector
# mydb = mysql.connector.connect(host="localhost", user="root", database="user")
# cursor = mydb.cursor()
app = Flask(__name__)

@app.route("/")
def hello():
    return "AI Chat Bot"

@app.route('/sms',methods=['POST'])
def bot():
    # def database(str):
    #     sqlform = " Insert into `list`(`Product List`) values (%s)"
    #     details = [(str.capitalize())]
    #     cursor.execute(sqlform,details)
    #     mydb.commit()

    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    # return a quote
    if 'chips' not in incoming_msg  and 'something' not in incoming_msg and 'lichi' not in incoming_msg and 'hi' in incoming_msg or 'hello' in incoming_msg or 'hii' in incoming_msg or 'hy' in incoming_msg:
        reply = "{} ! I am Chat Bot How Can i help you ?".format(incoming_msg.capitalize())
        msg.body(reply)
        responded = True
        return str(resp)
    if 'order' in incoming_msg or 'buy something' in incoming_msg:
        reply = 'Select the Category of order \n 1.Fruits and Vegetables \n 2.Foodgrains, Oils and Masalas \n '\
                '3.Dairy Bakers Cakes\n 4.Beverages\n 5.Others'
        msg.body(reply)
        responded = True
        return str(resp)
    if 'fruit' in incoming_msg or 'vegetable' in incoming_msg or 'food' in incoming_msg or 'grain' in incoming_msg or 'oil' in incoming_msg or 'masala' in incoming_msg or 'dairy' in incoming_msg or 'baker' in incoming_msg or 'cake' in incoming_msg or 'beverage' in incoming_msg:
        reply = "Which {} you want to purchase".format(incoming_msg)
        msg.body(reply)
        responded = True
        return str(resp)
    if 'other' in incoming_msg:
        reply = " Other Categories \n 1.Snacks\n 2.Clothing\n 3.Cleaning Household"
        msg.body(reply)
        responded = True
        return str(resp)
    if 'snack'in incoming_msg or 'clothing' in incoming_msg or 'cleaning' in incoming_msg or 'household' in incoming_msg:
        reply = "Which {} you want to buy".format(incoming_msg)
        msg.body(reply)
        responded = True
        return str(resp)
    if 'yes' in incoming_msg:
        reply = "Please Enter"
        msg.body(reply)
        responded = True
        return str(resp)
    if 'no' in incoming_msg:
        reply = "Please Write *Confirm* to Confirm Your Order"
        msg.body(reply)
        responded = True
        return str(resp)
    if 'confirm' in incoming_msg:
        reply = "Thanks for Shopping with us"
        msg.body(reply)
        responded = True
        return str(resp)
    if not responded:
            # database(incoming_msg)
            msg.body("Do You Want to Enter More ?")
    return str(resp)
if __name__ == "__main__":
        app.run(debug=True)




