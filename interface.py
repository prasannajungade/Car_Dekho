from flask import Flask,request,render_template,jsonify
from utils import CarDekho
import Config


app = Flask(__name__)



@app.route("/home1")
def home1():
    
    return "Hello"


@app.route("/home")
def home():
    
    return render_template("new_one.html")

@app.route("/Car_dekho/price_prediction",methods=["POST"])

def pred_charges():
    
    data=request.form.get
    print("DATA",data)

    Year = int(data("Year"))
    Present_Price = eval(data("Present_Price"))
    Kms_Driven = float(data("Kms_Driven"))
    Fuel_Type = data("Fuel_Type")
    Seller_Type =data("Seller_Type")
    Transmission = data("Transmission")
    Owner = int(data("Owner"))


    obj = CarDekho(Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner) 
    pred_price = obj.get_predicted_price()

    # return jsonify({"RESULT" : f"Predicted Car Price is == {pred_price}"})

    return render_template("new_one.html",prediction =pred_price)
    
if __name__ =="__main__":
    app.run(host="0.0.0.0",port=Config.PORT_NUMBER)

