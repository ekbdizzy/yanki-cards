import React from 'react';
import { LanguageListBox } from '../LanguageListBox/LanguageListBox';
import { Button } from '../Button/Button';

export const TranslationForm = () => {
  return (
    <div className="flex flex-col items-center mb-10">
      <form className="w-full flex flex-row justify-center items-center">
        <div className="w-full flex flex-col items-center">
          <input placeholder="Need new phrase?"
                 className="text-2xl text-center p-3 mr-4 border-b-2 border-b-amber-500 outline-none text-fuchsia-600 w-full
                 focus:drop-shadow-xl transition-all"
          />
          <div className="flex items-baseline">
            <p className="text-2xl text-center text-fuchsia-600 mt-3">Translating...</p>
          </div>
        </div>
        <div className="flex flex-col items-center gap-y-5">
          <LanguageListBox/>
          {/*<Button icon="translate" size="large">Translate</Button>*/}
          <Button icon="add" size="large" color="fuchsia">Add new card</Button>
        </div>
      </form>
    </div>
  );
};
