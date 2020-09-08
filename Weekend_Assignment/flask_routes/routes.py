from flask import request, jsonify, Flask
from models.listing import SneakerListing

app = Flask(__name__)

@app.route("/", methods=["GET"])
def test():
    return jsonify({'message': 'this worked'})

@app.route("/listings/add", methods=["POST"])
def add_sneaker():
    data = request.get_json()
    if data is None:
        return jsonify({'success': False})
    new_sneaker = SneakerListing(**data)
    success = new_sneaker.insert()
    return jsonify({'success': True})

@app.route("/listings/update", methods=["POST"])
def update_list():
    data = request.get_json()
    if data is None:
        return jsonify({'Success': False})
    update_sneakers = SneakerListing(**data)
    Success = update_sneakers.update()
    return jsonify({"Success": True})

@app.route("/listings/delete", methods=["POST"])
def delete_sneaker():
    data = request.get_json().get('pk')
    if data is None:
        return jsonify({"Deleted": False})
    Deleted = SneakerListing.delete(data)
    return jsonify({"Deleted": Deleted})

@app.route("/listings/person", methods=["POST"])
def search_by_person():
    data = request.get_json().get('Contact_number', 'Contact_email')
    if data is None:
        return jsonify({"Success": False})
    Success = SneakerListing.select_person(data)
    return jsonify({"Success": Success})

@app.route("/listings/price", methods=["POST"])
def search_by_price():
    data = request.get_json().get('CP')
    if data is None:
        return jsonify({"Success": False})
    Success = SneakerListing.select_price(data)
    return jsonify({"Success": Success})

@app.route ("/listings/company", methods=["POST"])
def search_by_company():
    data = request.get_json().get('Company')
    if data is None:
        return jsonify({"Success": False})
    Success = SneakerListing.select_company(data)
    return jsonify({"Success": Success})

"""
curl -X POST http://localhost:5000/listings/add -H "Content-Type: application/json" -d '{"Name": "HypeBeast1", "Yr_release": 12082015, "Version_number": 221020, "Creator": "Partap", "OP": 127.0, "CP": 257.0, "Company": "Vans", "Contact_number": 3217628088, "Contact_email": "partap1@gmail.com"}'
curl -X POST http://localhost:5000/listings/person -H "Content-Type: application/json" -d '{"Contact_number": 3217628088, "Contact_email": "partap1@gmail.com"}'
curl -X POST http://localhost:5000/listings/price -H "Content-Type: application/json" -d '{"CP": 777.0}'
"""
@app.route ("/listings/percentage/<percent>", methods=["GET"])
def search_by_sneakersale(percent):
    reduction = SneakerListing.select_sneaker_sale(float(percent))
    return jsonify({"Sale": reduction})

@app.route("/listings/all_items", methods=["GET"])
def show_all():
    total_list = SneakerListing.select_all()
    return jsonify({"Sneaker_list": total_list})



if __name__ == "__main__":
    app.run()