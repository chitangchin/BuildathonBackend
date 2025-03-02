import requests

def text_to_speech(text, config, logger):
  """
  Convert text to speech using ElevenLabs API
  """
  logger.info(f"Converting text to speech, text length: {len(text)}")
  
  headers = {
    "xi-api-key": config.ELEVENLABS_API_KEY,
    "Content-Type": "application/json"
  }
  
  payload = {
    "text": text,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
      "stability": 0.5,
      "similarity_boost": 0.8
    }
  }
  
  try:
    url = f"{config.ELEVENLABS_API_URL}/{config.ELEVENLABS_VOICE_ID}"
    response = requests.post(
      url,
      json=payload,
      headers=headers
    )
    
    if response.status_code != 200:
      logger.error(f"ElevenLabs API error: {response.status_code} - {response.text}")
      return None, f"Error generating speech: {response.status_code}"
    
    logger.info("Successfully generated audio")
    return response.content, None
  
  except Exception as e:
    logger.error(f"Error calling ElevenLabs API: {str(e)}")
    return None, f"Error calling ElevenLabs API: {str(e)}"