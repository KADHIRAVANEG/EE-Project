# OAuth Token Replay Attack Simulation

This project simulates an OAuth token replay vulnerability in a university login system using Python Flask.

## Features
- Simulated Google login
- Token generation on login
- Token-based access control
- Replay attack demo

## Setup Instructions
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Usage
1. Go to `/login` and login using a simulated email.
2. Copy the generated token.
3. Visit `/access?token=your_token` to view protected content.
4. Simulate a replay attack by submitting the same token at `/replay`.

## Security Recommendations
- Validate tokens against OAuth provider (e.g., Google)
- Bind tokens to device/IP
- Rotate tokens after use

## Author
Kadhiravan E.G
