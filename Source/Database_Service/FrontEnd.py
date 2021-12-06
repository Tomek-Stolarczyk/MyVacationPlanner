from flask import Flask, render_template, request, redirect
from VacationPlannerFacade import VacationPlannerFacade

app = Flask(__name__)
vp = VacationPlannerFacade()

@app.route('/', methods=['GET'])
def HomePage():
    return vp.HomePage()

@app.route('/ListAirports')
def ListAirports():
    return vp.ListAirports()

@app.route('/ListFlights')
def ListFlights():
    return vp.ListFlights()

@app.route('/Results', methods=['POST'])
def SearchResults():
    return vp.SearchResults()

@app.route('/Checkout', methods=['POST'])
def Checkout():
    return vp.Checkout()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
