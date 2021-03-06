from flask import Flask, jsonify, request
import Similarity as sim
import SimilarityConfig as cfg

app = Flask(__name__)

@app.route('/DocSimilarity/', methods=['POST'])
def GetDocSim():
    data = request.get_json()
    return jsonify({
        'Cosine Similarity' : sim.GetCosineSimilarity(data['Text1'], data['Text2'])
        })

app.run(cfg.HOST)