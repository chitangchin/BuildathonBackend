from flask import Blueprint, request, jsonify, Response
from services.claude_service import get_location_info
from services.elevenlabs_service import text_to_speech

location_bp = Blueprint('location', __name__)

@location_bp.route('/get-location-audio', methods=['GET'])
def get_location_audio():
    # Extract the place name from the request query parameters
    place_name = request.args.get('place')
    
    if not place_name:
        return jsonify({"error": "No place name provided. Use ?place=Paris"}), 400
    
    # Step 1: Get information about the place from Claude
    location_info, error = get_location_info(place_name, location_bp.config, location_bp.logger)
    if error:
        return jsonify({"error": error}), 500
    
    # Step 2: Convert the location information to speech using your text-to-speech service
    audio_data, error = text_to_speech(location_info, location_bp.config, location_bp.logger)
    if error:
        return jsonify({"error": error}), 500
    
    # Step 3: Return the audio file as a download
    response = Response(audio_data, mimetype='audio/mpeg')
    response.headers['Content-Disposition'] = f'attachment; filename={place_name.replace(" ", "_")}.mp3'
    
    return response

@location_bp.route('/get-location-info', methods=['GET'])
def get_location_info_only():
    """Optional endpoint to just get the text without converting to audio."""
    place_name = request.args.get('place')
    
    if not place_name:
        return jsonify({"error": "No place name provided. Use ?place=Paris"}), 400
    
    location_info, error = get_location_info(place_name, location_bp.config, location_bp.logger)
    if error:
        return jsonify({"error": error}), 500
    
    return jsonify({"place": place_name, "description": location_info})
