from flask import Flask, request, render_template
from src.utils import start_process, predict as model_predict

app = Flask(__name__)

# --------------------------------------------------
# Initialize model ONCE
# --------------------------------------------------
try:
    start_process()
except Exception as e:
    raise RuntimeError(f"Model initialization failed: {e}")


@app.route("/", methods=["GET", "POST"])
def home():

    # -----------------------------
    # GET → show form
    # -----------------------------
    if request.method == "GET":
        return render_template("index.html",prediction='')

   
    try:
        hours_studied = request.form.get("hours_studied")
        previous_scores = request.form.get("previous_scores")
        extracurricular = request.form.get("extracurricular")
        sleep_hours = request.form.get("sleep_hours")
        sample_papers = request.form.get("sample_papers")

        if not all([hours_studied, previous_scores, extracurricular, sleep_hours, sample_papers]):
            return render_template("index.html", error="All fields are required")

        # Type casting
        hours_studied = int(hours_studied)
        previous_scores = int(previous_scores)
        sleep_hours = int(sleep_hours)
        sample_papers = int(sample_papers)

        # Range validation
        if not (0 <= hours_studied <= 24):
            raise ValueError("Hours studied must be between 0 and 24")

        if not (0 <= previous_scores <= 100):
            raise ValueError("Previous scores must be between 0 and 100")

        if not (0 <= sleep_hours <= 24):
            raise ValueError("Sleep hours must be between 0 and 24")

        if sample_papers < 0:
            raise ValueError("Sample papers cannot be negative")

      

        # Model input
        input_data = {
            "Hours Studied": [hours_studied],
            "Previous Scores": [previous_scores],
            "Extracurricular Activities": [extracurricular],
            "Sleep Hours": [sleep_hours],
            "Sample Question Papers Practiced": [sample_papers]}

          

        # print(input_data)
        # Prediction
        prediction = float(model_predict(input_data))
        print("Prediction value is")
        print(prediction)
        return render_template("index.html", prediction=prediction)

    except Exception as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)
