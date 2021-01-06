from flask import Flask, jsonify, request
import TextSimilarityExecise.Similarity as sim

app = Flask(__name__)

@app.route('/DocSimilarity/', methods=['POST'])
def GetDocSim():
    data = request.get_json()
    return jsonify({
        'Cosine Similarity' : sim.GetCosineSimilarity(data['Text1'], data['Text2'])
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0')