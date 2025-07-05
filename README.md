📊 Career Recommendation System Based on Student Scores
This project is a machine learning-based Career Recommendation System that predicts suitable career paths for students based on their academic performance and personal attributes such as part-time jobs, extracurricular activities, and more.

🔍 Overview
The system uses a classification model trained on a student dataset to predict the most appropriate career path. It covers the complete ML pipeline:

Data preprocessing & encoding

Balancing classes with SMOTE

Feature scaling

Model training using various classifiers

Model evaluation and comparison

Single input career prediction

Web integration for recommendation

🧠 Machine Learning Algorithms Used
Random Forest Classifier 🌲

Decision Tree Classifier 🌳

Logistic Regression 📈

Support Vector Classifier (SVC) 💠

Gradient Boosting Classifier 🚀

K-Nearest Neighbors (KNN) 👥

Naive Bayes Classifier 🧮

📁 Dataset Features
The dataset includes the following features:

gender

part_time_job (True/False)

absence_days

extracurricular_activities (True/False)

weekly_self_study_hours

Academic Scores: math_score, history_score, physics_score,biology_score,english_score,geographic_score,history_score

🎯 Target Variable
career_aspiration: Encoded into 17 career labels including Doctor, Lawyer, Software Engineer, Artist, etc.

🧪 Evaluation Metrics
Accuracy

Confusion Matrix

Classification Report

⚙️ Key Technologies
Python 🐍

Pandas & NumPy

scikit-learn

imbalanced-learn (SMOTE)

Jupyter Notebook

Web integration (Flask-ready)
