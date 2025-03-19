from flask import Flask, request, jsonify
import hashlib
from facial_recognition import recognize_face
from voice_recognition import recognize_voice
from dental_recognition import recognize_dental

app = Flask(__name__)

@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.json
    facial_hash = recognize_face(data['facial'])
    voice_hash = recognize_voice(data['voice'])
    dental_hash = recognize_dental(data['dental'])
    combined_data = facial_hash + voice_hash + dental_hash
    user_hash = hashlib.sha256(combined_data.encode()).hexdigest()
    # Here, you would interact with the blockchain to create the user account
    return jsonify({"wallet_address": user_hash})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
