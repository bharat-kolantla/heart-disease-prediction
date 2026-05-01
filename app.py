from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("models/model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form values
        features = [float(x) for x in request.form.values()]
        final_features = np.array([features])

        # Prediction
        prediction = model.predict(final_features)[0]

        if prediction == 1:
            result = "High Risk of Heart Disease"
        else:
            result = "Low Risk of Heart Disease"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)