from flask import Flask, render_template, request
import pandas as pd # pyright: ignore[reportMissingModuleSource]
import joblib

app = Flask(__name__)

# Correct path
MODEL_PATH = r"C:\Users\hp\Downloads\Final Year Project\Heart_Desease_Project\models\xgb_boost.joblib"

model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        data = {
            "age": float(request.form["age"]),
            "sex": float(request.form["sex"]),
            "cp": float(request.form["cp"]),
            "trestbps": float(request.form["trestbps"]),
            "chol": float(request.form["chol"]),
            "fbs": float(request.form["fbs"]),
            "restecg": float(request.form["restecg"]),
            "thalach": float(request.form["thalach"]),
            "exang": float(request.form["exang"]),
            "oldpeak": float(request.form["oldpeak"]),
            "slope": float(request.form["slope"]),
            "ca": float(request.form["ca"]),
            "thal": float(request.form["thal"])
        }

        df = pd.DataFrame([data])
        prediction = int(model.predict(df)[0])

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
