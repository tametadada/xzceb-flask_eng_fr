"""
Module translates from English to French using IBM language_translator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv
load_dotenv()

apikey="apikey"
url="url" 

# Preparing the Authenticator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
version='2018-05-01',
authenticator=authenticator
)
language_translator.set_service_url(url)


def englishToFrench(englishText: str):
    """Function takes the string in englsh and return translated string in french"""
    try:
        translation = language_translator.translate(
            text=englishText,
            model_id='en-fr').get_result()
        #To get the pure translation string
        frenchText = translation['translations'][0]['translation']
        return frenchText
    except Exception as error:
        print(error)
        return None


def frenchToEnglish(frenchText: str):
    """Function takes the string in french and return translated string in english"""
    try:
        translation = language_translator.translate(
            text=frenchText,
            model_id='fr-en').get_result()
        #To get pure translation string
        englishText = translation['translations'][0]['translation']
        return englishText
    except Exception as error:
        print(error)
        return None