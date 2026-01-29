# GitHub Activity Tracker (Webhook Service)

This repository implements a GitHub webhook listener and UI to track repository activity in real time, as per the Developer Assessment task.

---

## Overview

This solution consists of **two repositories**:

### 1. `action-repo`
- A standard GitHub repository used to **generate events**
- Pushes and Pull Requests made to this repository trigger GitHub webhooks
- No backend logic is required in this repo

### 2. `webhook-repo` (this repository)
- Receives webhook events from GitHub
- Stores events in MongoDB
- Displays recent activity via a web UI
- UI polls the backend **every 15 seconds** (as required)

---

## Supported GitHub Events

- **Push**
- **Pull Request**
- **Merge** (implemented as an extension / bonus)

---

## Event Display Format

The UI displays events in the following formats:

- **Push**  
  `{author} pushed to {to_branch} on {timestamp}`

- **Pull Request**  
  `{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}`

- **Merge**  
  `{author} merged branch {from_branch} to {to_branch} on {timestamp}`

---

## UI Behavior (As Per Assessment)

- The frontend fetches data from `/events`
- Polling interval: **every 15 seconds**
- Displays the **latest events first**

`js
setInterval(loadEvents, 15000);
Tech Stack

Backend: Python, Flask

Database: MongoDB Atlas

Webhooks: GitHub Webhooks

Frontend: HTML, CSS, Vanilla JavaScript

How It Works

A push or pull request is made to action-repo

GitHub sends a webhook payload to /webhook

Flask parses and stores the event in MongoDB

The UI polls /events every 15 seconds

Latest activity is rendered in the browser

Running Locally
pip install -r requirements.txt
python app.py


The application runs at:

http://127.0.0.1:5000
---
Notes

Webhooks were tested locally using ngrok

MongoDB Atlas is used for persistence

The implementation strictly follows the assessment requirements
---
