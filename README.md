# Image-to-Speech

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

This project enables users to upload an image, generate a descriptive caption using an AI model, transform the caption into a short story, and then convert the story into speech using another AI model. It leverages Streamlit for the user interface, Hugging Face Transformers for image captioning, Google's Gemini for story generation, and Kokoro via Hugging Face InferenceClient for text-to-speech conversion.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Important Links](#important-links)
- [Footer](#footer)

## Features

- 🖼️ **Image Upload:** Allows users to upload images in JPG, JPEG, or PNG formats.
- 🤖 **AI-Powered Caption Generation:** Generates captions for uploaded images using the Salesforce/blip-image-captioning-large model.
- 📖 **Short Story Creation:** Transforms image captions into creative short stories using Google's Gemini-2.5-flash model.
- 🔊 **Text-to-Speech Conversion:** Converts generated stories into speech using the Kokoro model via Hugging Face InferenceClient.
- 🎧 **Audio Playback:** Provides an audio player to listen to the generated speech directly in the browser.
- 💾 **Audio Download:** Offers a download button to save the generated speech as a WAV file.

## Tech Stack

- 🐍 **Python:** Primary programming language.
- 🧰 **Streamlit:** For building the interactive web application.
- 🧠 **Transformers:** Hugging Face library for using pre-trained models.
- 🔥 **PyTorch:** Open source machine learning framework.
- 📜 **Langchain:** Framework for developing applications powered by language models.
- ☁️ **Google Generative AI:** Utilized for story generation.

## Installation

1.  **Clone the repository:**
   ```bash
   git clone https://github.com/paritosh142/image-to-Speech.git
   cd image-to-Speech
   ```

2.  **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/macOS
   # venv\Scripts\activate  # On Windows
   ```

3.  **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4.  **Set up environment variables:**
   - Create a `.env` file in the project root.
   - Add your Google API key and Hugging Face token (if you have one) to the `.env` file:
	```
	GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
	HF_TOKEN=YOUR_HUGGING_FACE_API_TOKEN
	```
   - **Note:** You need a Google API key to use the Gemini model and a Hugging Face token to use the Kokoro text-to-speech model.  If you do not provide the Hugging Face token the program will raise an error.

## Usage

1.  **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

2.  **Access the application in your browser:**
    - Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your web browser.

3.  **Upload an image:**
    - Use the file uploader to select an image from your local machine.

4.  **Generate the story and speech:**
    - The application will automatically generate a caption, create a short story based on the caption, and convert the story into speech.

5.  **Listen to the generated speech:**
    - An audio player will appear, allowing you to listen to the generated speech.

6.  **Download the audio (optional):**
    - Click the "Download WAV" button to save the generated speech as a WAV file.

## Project Structure

```
image-to-Speech/
├── app.py                  # Main Streamlit application file
├── requirements.txt        # List of Python dependencies
├── README.md               # Project documentation
├── .env                    # Environment variables (API keys)
├── img/                    # Directory to store uploaded images
├── kokoro_ee2f9faa70ea46fc895420098ed5cbe6.wav #An example audio file that could be generated
├── test.py                 # Simple script to test image captioning
├── test_speech.py          # Script to test text-to-speech functionality
└── test_story.py           # Script to test story generation
```

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.

## Important Links

-   **Repository:** [https://github.com/paritosh142/image-to-Speech](https://github.com/paritosh142/image-to-Speech)

## Footer

[Image-to-Speech](https://github.com/paritosh142/image-to-Speech) - Made with ❤️ by [paritosh142](https://github.com/paritosh142). Feel free to fork, star, and open issues!


---
**<p align="center">Generated by [ReadmeCodeGen](https://www.readmecodegen.com/)</p>**