# recommendation_model.py
class Recommendations:
    def __init__(self, gender, part_time_job, absence_days, extracurricular_activities,
                 weekly_self_study_hours, math_score, history_score,
                 physics_score, chemistry_score, biology_score,
                 english_score, geography_score, total_score, average_score):
        self.gender = gender
        self.part_time_job = part_time_job
        self.absence_days = absence_days
        self.extracurricular_activities = extracurricular_activities
        self.weekly_self_study_hours = weekly_self_study_hours
        self.math_score = math_score
        self.history_score = history_score
        self.physics_score = physics_score
        self.chemistry_score = chemistry_score
        self.biology_score = biology_score
        self.english_score = english_score
        self.geography_score = geography_score
        self.total_score = total_score
        self.average_score = average_score

    def __iter__(self):
        # Dummy logic — replace with your actual prediction logic
        recommendations = [
            ("Engineering", 0.85),
            ("Medical", 0.65),
            ("Law", 0.40)
        ]
        for r in recommendations:
            yield r
