from flask import Flask, render_template, request
from recommendation_model import Recommendations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        # Get form data
        data = {k: request.form[k] for k in request.form}

        # Convert to appropriate types
        rec = Recommendations(
            gender=data["gender"],
            part_time_job=data.get("part_time_job") == "on",
            absence_days=int(data["absence_days"]),
            extracurricular_activities=data.get("extracurricular_activities") == "on",
            weekly_self_study_hours=int(data["weekly_self_study_hours"]),
            math_score=int(data["math_score"]),
            history_score=int(data["history_score"]),
            physics_score=int(data["physics_score"]),
            chemistry_score=int(data["chemistry_score"]),
            biology_score=int(data["biology_score"]),
            english_score=int(data["english_score"]),
            geography_score=int(data["geography_score"]),
            total_score=int(data["total_score"]),
            average_score=float(data["average_score"])
        )

        result = list(rec)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
