# CrowdControl AI
### Machine Learning-Driven Crowd Optimization and Virtual Queueing for Pilgrimage Sites

A modular, scalable, and secure AI-powered crowd management system designed to mitigate extreme overcrowding and prevent stampedes at high-footfall temples. By leveraging Machine Learning predictive analytics and dual QR-code verification, the system replaces chaotic physical bottlenecks with a streamlined, predictive virtual queue. Built with Streamlit, Python, and Supabase.

## 🚀 Features

- **ML-Driven Entry & Wait Time Prediction**: Utilizes time-series forecasting to predict the exact window a devotee can physically enter the temple queue. Predictions automatically adapt to live throughput, historical festival peaks, and time-of-day surges.
- **Dual QR-Code Flow Tracking**: 
  - **Entry Scan**: Devotees scan a QR code at designated outer perimeters to activate their virtual slot and enter the physical holding area.
  - **Exit Scan**: Devotees scan an exit QR code upon leaving, providing the ML model with real-time temple clearance rates to continuously train and update wait-time accuracy.
- **Dynamic Batching Admin Dashboard**: Allows temple administrators to monitor live inner-sanctum capacity, track parallel service points, and adjust maximum thresholds on the fly.
- **Smart Virtual Pass**: Users register securely to claim a spot in the virtual line, viewing a live, dynamic countdown timer instead of standing in hazardous physical lines for hours.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) (Mobile-responsive prototype)
- **Machine Learning**: Python (Scikit-learn / Time-Series Forecasting)
- **Database & Backend**: [Supabase](https://supabase.com/) (PostgreSQL + Real-time listening)

## 📦 Setup Instructions

### 1. Database Setup (Supabase)

Create two core tables in your Supabase SQL editor:
* `configurations`: Tracks temple metadata (entrances, exits, max inner capacity, and average interaction times).
* `queue_entries`: Tracks live user tokens, positions, and critical data points for the ML engine (`predicted_entry_time`, `entered_at` via Entry QR, and `exited_at` via Exit QR).

> 💡 *Note: For full database table schemas and Row Level Security (RLS) policies to allow anonymous prototype testing, see the `/database/schema.sql` file.*

### 2. Environment Variables

Create a `.env` file in the project root:

```env
SUPABASE_URL="your-project-url"
SUPABASE_KEY="your-anon-key"

```

### 3. Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

### 4. Running the Application

```bash
streamlit run main.py

```

## ⚖️ Governance & Principles

This project follows the **Queue Management System Constitution (v1.0.0)**:

* **Predictive Optimization**: Always prioritize ML data health to ensure safe, accurate crowd pacing.
* **Modular Architecture**: Independent predictive models, front-end views, and QR validation endpoints.
* **Security & Privacy First**: Tokenized check-ins to protect pilgrim user identity.
* **Fail-Safe Operation**: If the ML prediction layer experiences downtime, the system gracefully reverts to standard linear FIFO (First-In, First-Out) queuing based on queue position.

```

```
