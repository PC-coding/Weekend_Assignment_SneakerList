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

if __name__ == "__main__":
    app.run()