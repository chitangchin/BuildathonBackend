# Backend API for [Buildathon](https://github.com/craftingweb/Buildathon)

[![CI Build and Test Validation](https://github.com/chitangchin/BuildathonBackend/actions/workflows/buildandvalidationtest.yml/badge.svg)](https://github.com/chitangchin/BuildathonBackend/actions/workflows/buildandvalidationtest.yml)

## Overview
This backend service provides location-based descriptions using Claude AI and converts them into speech using ElevenLabs' text-to-speech API. Users can request information about a place, and the service will generate an audio file that describes the location.

## Features
- Fetch brief descriptions of locations using Claude AI
- Convert descriptions into speech using ElevenLabs
- Serve the generated audio files via API
- Logging and environment-based configuration support

## Technologies Used
- Python (Flask)
- Claude AI API (Anthropic)
- ElevenLabs Text-to-Speech API
- dotenv for environment variable management
- Logging for debugging and monitoring

---

## Installation
### Prerequisites
- Python 3.8+
- `pip` installed
- API keys for Claude AI and ElevenLabs
- `.env` file with the required API credentials

### Steps
1. [Fork the repository](https://github.com/chitangchin/BuildathonBackend/fork)

2. Clone the repository:
   ```sh
   git clone https://github.com/{yourusername}/BuildathonBackend.git
   cd BuildathonBackend
   ```

3. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate
   # On Windows use `source venv/Scripts/activate` for bash or venv\Scripts\activate in cmd
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add the following:
   ```sh
     #API Key
     CLAUDE_API_KEY = "skxxx"
     ELEVENLABS_API_KEY = "skxxx"
     
     
     #DEFAULT
     CLAUDE_MODEL = "claude-3-opus-20240229"
     ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1/text-to-speech"
     CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"
     ELEVENLABS_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"
   ```

5. Start the server:
   ```sh
   python main.py
   ```
   The server should now be running on `http://127.0.0.1:5000/`.

---

## API Endpoints
### Health Check
- **Endpoint:** `/health`
- **Method:** `GET`
- **Response:**
  ```json
  {"status": "healthy"}
  ```

### Get Location Description & Audio
- **Endpoint:** `/get-location-audio`
- **Method:** `GET`
- **Query Parameters:**
  - `place`: The name of the location (e.g., `?place=Paris`)
- **Response:**
  - Returns an MP3 audio file with the location description.
  - If an error occurs, returns a JSON error response.

### Get Location Description (Text Only)
- **Endpoint:** `/get-location-info`
- **Method:** `GET`
- **Query Parameters:**
  - `place`: The name of the location (e.g., `?place=Paris`)
- **Response:**
  ```json
  {
    "place": "Paris",
    "description": "Now approaching the Eiffel Tower, a symbol of France..."
  }
  ```
  
---

## Logging
Logging is handled via `logging_util.py`, configured through the `config.py` file. The log level can be adjusted based on the `FLASK_ENV` variable.

---

## Deployment
### Running in Production
- Ensure `FLASK_ENV=production` in the `.env` file.
- Use a production-ready server like Gunicorn:
  ```sh
  gunicorn -w 4 -b 0.0.0.0:5000 app:app
  ```

### Docker Deployment
1. Create a `Dockerfile` (not included yet).
2. Build and run the Docker container:
   ```sh
   docker build -t location-audio .
   docker run -p 5000:5000 location-audio
   ```

---

## Contributing
1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## License
This project is licensed under the MIT License.

