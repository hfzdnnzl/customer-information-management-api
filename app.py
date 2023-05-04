from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a list to store customer data
customers = []

# Endpoint to register a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()

    customer_id = customers[-1]['id'] + 1 if len(customers) else 1
    customer = {
        'id': customer_id,
        'name': data['name'],
        'email': data['email'],
        'phone': data['phone']
    }
    customers.append(customer)

    response = {
        "msg": "Registered successfully",
        "customer": customer
    }
    return jsonify(response), 201

# Endpoint to view all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

# Endpoint to view a specific customer by ID
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if customer:
        return jsonify(customer)
    else:
        return '', 404

# Endpoint to update a specific customer by ID
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if not customer:
        return '', 404
    data = request.get_json()
    customer.update({
        'name': data['name'],
        'email': data['email'],
        'phone': data['phone']
    })

    response = {
        "msg": "Updated successfully",
        "customer": customer
    }
    return jsonify(response)

# Endpoint to delete a specific customer by ID
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if not customer:
        return '', 404
    customers.remove(customer)

    response = {
        "msg": "Deleted successfully",
        "customer": customer
    }
    return jsonify(response), 204

if __name__ == '__main__':
    app.run(debug=True)
