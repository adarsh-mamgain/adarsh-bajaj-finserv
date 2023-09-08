from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Helper function to find the highest alphabet in an array of alphabets
def find_highest_alphabet(alphabets):
    if not alphabets:
        return []
    return [max(alphabets, key=lambda x: ord(x.lower()))]

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])
        
        # Extract numbers and alphabets from the input data
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        
        response = {
            "is_success": True,
            "user_id": "Adarsh_Mamgain_31072002",
            "email": "am7722@srmist.edu.in",
            "roll_number": "RA2011003010381",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": find_highest_alphabet(alphabets)
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
