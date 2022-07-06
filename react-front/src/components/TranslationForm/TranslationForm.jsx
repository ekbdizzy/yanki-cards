import React, { useEffect, useState } from 'react';
import { LanguageListBox } from '../LanguageListBox/LanguageListBox';
import { Button } from '../Button/Button';
import axios from 'axios';
import { API, withBaseUrl } from '../../api';

export const TranslationForm = () => {
  const [isTranslating, setIsTranslating] = useState(false);
  const [translation, setTranslation] = useState(null);
  const [phrase, setPhrase] = useState(null);
  const [languageCode, setLanguageCode] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const body = {};
    formData.forEach((value, key) => {
      key = key.replace('[', '_').replace(']', '');
      body[key] = value;
    });
    console.log(body);
    setPhrase(body.phrase);
    setIsTranslating(true);
  };

  useEffect(() => {
    if (!isTranslating) { return; }

    const fetchTranslation = async (phrase, languageCode) => {
      const response = await axios.post(
        withBaseUrl(API.translate),
        { phrase },
      );
      const text = (response.data[0]);
      console.log(text.text);
    };
    fetchTranslation(phrase, languageCode);
    setIsTranslating(false);
  }, [isTranslating]);


  return (
    <div className="flex flex-col items-center mb-10">
      <form className="w-full flex flex-row justify-center items-center" onSubmit={handleSubmit}>
        <div className="w-full flex flex-col items-center">
          <input placeholder="Need new phrase?"
                 className="text-2xl text-center p-3 mr-4 border-b-2 border-b-amber-500 outline-none text-fuchsia-600 w-full
                 focus:drop-shadow-xl transition-all"
                 name="phrase"
          />
          <div className="flex items-baseline">
            <p className="text-2xl text-center text-fuchsia-600 mt-3">
              {translation || 'Translating...'} </p>
          </div>
        </div>
        <div className="flex flex-col items-center gap-y-5">
          <LanguageListBox/>
          {!isTranslating && <Button icon="translate" size="large" type="submit">Translate</Button>}
          {translation && <Button icon="add" size="large" color="fuchsia">Add new card</Button>}
        </div>
      </form>
    </div>
  );
};
