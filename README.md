# Market Intelligence Dashboard 📊

A simple Streamlit dashboard built to connect with a market intelligence API and display search results.

## Project Overview

This project is the frontend/dashboard part of a larger market intelligence system.

The dashboard allows a user to enter a keyword and send a search request to a local FastAPI backend. The returned results are then displayed in the Streamlit application.

## Features

* Keyword search
* API request to backend
* HTTP status display
* JSON result display
* Basic error handling

## Tech Stack

* Python
* Streamlit
* Requests
* FastAPI backend

## How It Works

```text
User enters keyword
        ↓
Streamlit dashboard
        ↓
FastAPI /search endpoint
        ↓
Backend processes request
        ↓
Search results returned
        ↓
Dashboard displays results
```

## Project Structure

```text
market-intelligence-dashboard/
│
├── app.py
├── requirements.txt
└── README.md
```

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the dashboard:

```bash
streamlit run app.py
```

The dashboard expects the backend API to be available at:

```text
http://127.0.0.1:8000
```

## Backend Repository

The related backend project is:

```text
market-intelligence-backend
```

## Current Status

This is a work-in-progress project focused on connecting a Streamlit frontend with a FastAPI backend.

## Future Improvements

* Add a better dashboard layout
* Add charts and analytics
* Add API configuration through environment variables
* Improve result formatting
* Add loading states
* Deploy frontend and backend

## Author

**Mujtaba Shokat**

Aspiring Data Scientist | Data Analytics & AI
