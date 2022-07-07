import React, { useEffect, useState, useContext } from 'react';
import { LanguageListBox } from '../LanguageListBox/LanguageListBox';
import { Button } from '../Button/Button';
import axios from 'axios';
import { API, withBaseUrl } from '../../api';
import { CurrentTranslationContext } from '../../context';

export const TranslationForm = () => {
  const [translation, setTranslation] = useContext(CurrentTranslationContext);
  const [isTranslating, setIsTranslating] = useState(false);
  const [phrase, setPhrase] = useState(null);
  const [languageCode, setLanguageCode] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const body = {};
    formData.forEach((value, key) => {
      // convert 'language[code]' --> 'language_code'
      key = key.replace('[', '_').replace(']', '');
      body[key] = value;
    });
    setLanguageCode(body.language_code);
    setTranslation(null);
    setIsTranslating(true);
  };

  const translatePhrase = (phrase, languageCode) => {
    axios.post(
      withBaseUrl(API.translate),
      { phrase, language_code: languageCode },
    ).then((response) => {
      const translation = response.data[0];
      setTranslation(translation.text);
      setIsTranslating(false);
    }).catch((error) => {
      console.log(error.response.data);
      setIsTranslating(false);
      setError('Server error');
    });
  };

  useEffect(() => {
    setTranslation(null);
    setError(null);
  }, [phrase]);

  useEffect(() => {
    if (!isTranslating) { return; }
    translatePhrase(phrase, languageCode);
  }, [isTranslating]);

  return (
    <div className="flex flex-col items-center mb-10">
      <form className="w-full flex flex-row gap-3 justify-center items-center"
            onSubmit={handleSubmit}
      >
        <div className="w-full flex flex-col items-center">
          <input placeholder="Need new phrase?"
                 className="text-2xl text-center p-3  border-b-2 border-b-amber-500 outline-none text-fuchsia-600 w-full
                 focus:drop-shadow-xl transition-all"
                 name="phrase"
                 value={phrase}
                 required
                 onChange={(e) => setPhrase(e.target.value)}
          />
          <div className="flex items-baseline">
            <p className="text-2xl text-center text-fuchsia-600 mt-3">
              {(error || translation) || (isTranslating ? 'Translating...' : <p className="text-white">.</p>)} </p>
          </div>
        </div>
        <div className="flex flex-col items-center gap-y-5">
          <LanguageListBox/>
          {translation
            ? <Button icon="add" size="large" color="fuchsia">Add new card</Button>
            : <Button icon="translate" size="large" type="submit">Translate</Button>
          }
        </div>
      </form>
    </div>
  );
};
