# ML LAB MID 

An interactive, full-stack Machine Learning web application built with FastAPI, scikit-learn, Pydantic v2, and a vanilla HTML/JS interface. 

This repository features modular data processing, candidate model evaluation (Lasso vs. Ridge, Random Forest vs. Gradient Boosting), warning-free DataFrame inference, and custom Pydantic schemas.

---

## 📁 Repository Structure

```text
ML-LAB--MID/
├── models/                  # Generated binary model pipelines (.joblib)
│   ├── regression.joblib
│   ├── classification.joblib
│   └── sentiment.joblib
├── index.html               # Interactive frontend web dashboard
├── main.py                  # FastAPI server with CORS and endpoint routing
├── schemas.py               # Pydantic v2 schemas for API data validation
├── train.py                 # Candidate benchmarking, training, & pipeline creation
├── requirements.txt         # Project Python dependencies
└── README.md                # Project documentation
