"""IBM Watson Translator."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
# Set some variables
apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'
MODEL_EN_FR = 'en-fr'
MODEL_FR_EN = 'fr-en'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)


def translation(text, model_id):
    """Translate any text and any language model."""
    language_translator.set_service_url(url)
    return language_translator.translate(
        text=text,
        model_id=model_id) \
        .get_result()


def translate_en_to_fr(english_text):
    """Translate English text to French."""
    return translation(english_text, MODEL_EN_FR).get["translations"][0].get["translation"]


def translate_fr_to_en(french_text):
    """Translate French text to English."""
    return translation(french_text, MODEL_FR_EN).get["translations"][0].get["translation"]
