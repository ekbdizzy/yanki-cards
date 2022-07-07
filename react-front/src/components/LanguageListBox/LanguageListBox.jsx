import React, { Fragment, useEffect, useState, useContext } from 'react';
import { Listbox, Transition } from '@headlessui/react';
import { CheckIcon, SelectorIcon } from '@heroicons/react/solid';
import { CurrentTranslationContext } from '../../context';

const languages = [
  { language: 'Translate to english', code: 'en' },
  { language: 'Перевести на русский', code: 'ru' },
  { language: 'Türkçeye çevir', code: 'tr' },
  { language: 'Spain', code: 'sp' },
];

export const LanguageListBox = () => {
  const [selected, setSelected] = useState(languages[0]);
  const [translation, setTranslation] = useContext(CurrentTranslationContext);

  useEffect(() => {
    console.log('select');
    if (!translation) { return; };
    setTranslation(null);
    console.log(translation);
  }, [selected]);

  return (
    <div className="w-60">
      <Listbox
        value={selected}
        onChange={setSelected}
        name="language"
      >
        <div className="relative mt-1">
          <Listbox.Button
            className="relative w-full cursor-pointer rounded-lg bg-white py-2 pl-3 pr-10 text-left shadow-md focus:outline-none focus-visible:border-indigo-500 focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75 focus-visible:ring-offset-2 focus-visible:ring-offset-orange-300 sm:text-sm">
            <span className="block truncate text-indigo-700 font-medium">{selected.language}</span>
            <span className="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2">
              <SelectorIcon
                className="h-5 w-5 text-indigo-700"
                aria-hidden="true"
              />
            </span>
          </Listbox.Button>
          <Transition
            as={Fragment}
            leave="transition ease-in duration-100"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <Listbox.Options
              className="absolute mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm">
              {languages.map((language, Idx) => (
                <Listbox.Option
                  key={Idx}
                  className={({ active }) =>
                    `relative cursor-default select-none py-2 pl-10 pr-4 font-medium
                    ${active ? 'bg-amber-300 text-amber-900 transition' : 'text-grey-700'}`
                  }
                  value={language}
                >
                  {({ selected }) => (
                    <>
                      <span
                        className={`block truncate ${
                          selected ? 'font-medium' : 'font-normal'
                        }`}
                      >
                        {language.language}
                      </span>
                      {selected && (
                        <span className="absolute inset-y-0 left-0 flex items-center pl-3 text-amber-600">
                          <CheckIcon className="h-5 w-5" aria-hidden="true"/>
                        </span>
                      )}
                    </>
                  )}
                </Listbox.Option>
              ))}
            </Listbox.Options>
          </Transition>
        </div>
      </Listbox>
    </div>
  );
};
