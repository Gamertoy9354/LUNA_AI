import subprocess

# List of dependencies
dependencies = [
    "requests",
    "speech_recognition",
    "googlesearch-python",
    "beautifulsoup4",
    "gtts",
    "google-api-python-client",
    "playsound",
    "cryptography",
    "spacy",
    "nltk"
]

# Install each dependency
for dependency in dependencies:
    subprocess.call(["pip", "install", dependency])

# Download spaCy model
subprocess.call(["python", "-m", "spacy", "download", "en_core_web_sm"])

# Download NLTK data
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')