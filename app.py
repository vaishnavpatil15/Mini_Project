from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Load ML Models (optional, adjust paths based on folder structure)
models_path = './models/'  # Adjust path if your models are in a different directory
DecisionTree = pickle.load(open(models_path + 'DecisionTree.pkl', 'rb'))
# Load other models here (e.g., NaiveBayes, SVM, etc.)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict_crop():
    try:
        # Get user input from request data
        data = request.get_json()

        nitrogen = data['nitrogen']
        phosphorus = data['phosphorus']
        potassium = data['potassium']
        temperature = data['temperature']
        humidity = data['humidity']
        ph = data['ph']
        rainfall = data['rainfall']

        # Prepare input data as a NumPy array for model prediction
        X_new = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])

        # Make prediction using the chosen model (e.g., DecisionTree)
        prediction = DecisionTree.predict(X_new)

        # Debugging: Print prediction to console
        print("Prediction raw output:", prediction)

        # Assuming the model returns a single label as a string
        predicted_label = prediction[0]  # Directly use the prediction
        print("Predicted label:", predicted_label)  # Log the predicted label

        crop_mapping = {
    'rice': 'rice',
    'maize': 'maize',
    'wheat': 'wheat',
    'cotton': 'cotton',
    'jute': 'jute',
    'sugarcane': 'sugarcane',
    'mung bean': 'mung bean',
    'lentil': 'lentil',
    'kidney beans': 'kidney beans',
    'pigeon peas': 'pigeon peas',
    'blackgram': 'blackgram',
    'chickpea': 'chickpea',
    'coconut': 'coconut',
    'coffee': 'coffee',
    'tea': 'tea',
    'rubber': 'rubber',
    'tobacco': 'tobacco',
    'apple': 'apple',
    'mango': 'mango',
    'banana': 'banana',
    'orange': 'orange',
    # Add more crops as necessary...
}


        # Check if the predicted label exists in the crop mapping
        if predicted_label not in crop_mapping:
            print(f"Error: Unknown prediction label '{predicted_label}'")
            return jsonify({'error': f'Unknown prediction label: {predicted_label}'}), 400

        recommended_crop = crop_mapping[predicted_label]

        # Return the prediction as JSON
        return jsonify({'recommended_crop': recommended_crop})

    except Exception as e:
        # Handle any unexpected errors and return a clear message
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)