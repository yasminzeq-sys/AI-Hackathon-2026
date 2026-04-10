# AI Hesitation Detector: Smart E-Commerce Engine

**GitHub Repository:** https://github.com/yasminzeq-sys/AI-Hackathon-2026

An AI-powered real-time detection system designed to identify consumer hesitation during the online shopping journey. This project implements a predictive framework based on recent behavioral research to convert "invisible" revenue leaks into successful sales.

## 📖 Project Explanation

The **AI Hesitation Detector** helps to reduce the cart abandonment rate in e-commerce. This tool uses a **Random Forest Classifier** to detect hesitation while the user is still active on the site.

### Research Foundation
As identified by **Li et al. (2025)**, hesitation acts as a critical influence for the final purchase decision. Our system specifically targets two stressors identified in this research:
* **Price Waiting Behavior:** Addressed by offering targeted 10% discounts.
* **Perceived Risk:** Addressed by triggering popularity nudges to increase perceived value.

### Tech Stack
* **Frontend:** Streamlit
* **AI Model:** Random Forest Classifier (Scikit-Learn)
* **Logic:** Customer Psychology (Helping them decide)

### Key Features:
* **Live Probability Scoring:** Real-time calculation of abandonment risk.
* **Automated Nudges:** Immediate UI updates (Discounts, Social Proof, and Recommendations) when hesitation is detected.
* **Behavioral Intelligence:** Analyzes Time on Site, Page Views, and Bounce Rate to distinguish between normal browsing and hesitant looping.

---

## 🛠️ Setup Instructions

### Prerequisites:
* **Python 3.8+**
* **pip** (Python package manager)

### 1. Clone or Download the Project
Download the project files to your local machine and navigate to the project directory:
```bash
cd ai-hesitation-detector
```

### How to Run
1. Adjust the sliders on the left side (Time on Site / Pages Viewed/Bounce Rate).
2. Observe the AI Status and the dynamic nudge output.

**Streamlit:** https://ai-hackathon-2026-nnnczhdkh5cxum4ep6djwf.streamlit.app/#smart-e-commerce-real-time-hesitation-detector
