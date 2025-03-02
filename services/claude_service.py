import requests
import json

def get_location_info(place_name, config, logger):
	"""
	Get information about a location from Claude API
	"""
	logger.info(f"Getting information about: {place_name}")
	
	headers = {
		"x-api-key": config.CLAUDE_API_KEY,
		"anthropic-version": "2023-06-01",
		"content-type": "application/json"
	}
	
	prompt = f"""
	Please give me a brief description (about 3-4 sentences) about {place_name}. 
	Include interesting facts, cultural significance, or historical details. Keep in
	mind that this description will be converted to speech. It will also be played
	as the user approaches this location, so start by saying things like "now appraocking"
	or "next to you".
	"""
	
	payload = {
		"model": config.CLAUDE_MODEL,
		"max_tokens": 300,
		"messages": [
			{
				"role": "user", 
				"content": prompt
			}
		]
	}
	
	try:
		response = requests.post(
			config.CLAUDE_API_URL,
			headers=headers,
			json=payload
		)
		
		if response.status_code != 200:
			logger.error(f"Claude API error: {response.status_code} - {response.text}")
			return None, f"Error getting information: {response.status_code}"
		
		result = response.json()
		location_info = result["content"][0]["text"]
		logger.info(f"Received location info: {location_info[:50]}...")
		return location_info, None
	
	except Exception as e:
		logger.error(f"Error calling Claude API: {str(e)}")
		return None, f"Error calling Claude API: {str(e)}"