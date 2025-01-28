from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample crop data
crop_data = {
    "wheat": {"name": "Wheat", "season": "Winter", "soil": "Loamy Soil", "water": "Moderate", "pests": "Rust, Aphids"},
    "rice": {"name": "Rice", "season": "Monsoon", "soil": "Clayey Soil", "water": "High", "pests": "Stem Borer, Leaf Folder"},
    "maize": {"name": "Maize", "season": "Summer", "soil": "Well-drained", "water": "Low", "pests": "Armyworms, Rootworm"},
}

@app.route('/')
def index():
    # Serve the index.html file from the templates folder
    return render_template('index.html')

@app.route('/crop-info', methods=['GET'])
def get_crop_info():
    crop_name = request.args.get('crop-name', '').strip().lower()

    if not crop_name:
        return jsonify({"error": "Please provide a crop name."})

    crop_info = crop_data.get(crop_name)
    
    if crop_info:
        return jsonify(crop_info)
    else:
        return jsonify({"error": "Crop information not found."})
@app.route('/man')
def man():
    return render_template('man.html')
@app.route('/vet')
def vet():
    return render_template('vet.html')
@app.route('/script')
def script():
    return render_template('../static/script.js')

if __name__ == '__main__':
    app.run(debug=True)
