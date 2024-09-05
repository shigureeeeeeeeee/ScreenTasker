# Screenshot to Google Tasks

## Overview
This tool captures screenshots, analyzes the image content using AI (Gemini), and automatically adds the results as tasks to Google Tasks.

## Features
- Screenshot capture via key input
- AI (Gemini) image analysis and text generation
- Automatic addition of generated text to Google Tasks

## Requirements
- Python 3.7 or higher
- Google Cloud Project account
- Gemini API key
- Google Tasks API enabled

## Installation
1. Clone the repository:
   ```
   git clone [repository URL]
   cd [repository name]
   ```

2. Install required libraries:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file and set your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. Obtain OAuth 2.0 client ID from Google Cloud Console and save it as `credentials.json` in the project's root directory.

## Usage
1. Run `main.py`:
   ```
   python main.py
   ```

2. Press the 'q' key to capture a screenshot.

3. AI will analyze the image and generate a task name and details.

4. The generated task will be automatically added to Google Tasks.

## File Structure
- `main.py`: Main script
- `text_generator.py`: AI image analysis and text generation functionality
- `task_manager.py`: Google Tasks API integration
- `requirements.txt`: List of required Python libraries
- `.env`: Environment variable configuration file (for API keys, etc.)
- `credentials.json`: Google OAuth authentication information (to be added by user)

## Notes
- Google authentication is required on first run. A browser will open, and you'll need to grant access.
- A `token.pickle` file will be generated and used for subsequent authentications. Keep this file secure.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
