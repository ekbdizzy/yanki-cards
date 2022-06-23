import styles from './WordTranslation.module.css';
import {Input, P, Helper} from '../../components';
import React, {ChangeEvent, FormEvent, useState} from "react";

export const WordTranslation = () => {
    const [translation, setTranslation] = useState<string>('');
    const [word, setWord] = useState<string>('');
    const [addNewCardButton, setAddNewCardButton] = useState<boolean>(false);
    const [addTranslateButton, setAddTranslateButton] = useState<boolean>(false);
    const [isLoading, setIsLoading] = useState<boolean>(false);

    const changeWord = (e: ChangeEvent<HTMLInputElement>) => {
        setWord(e.target.value);
        if (e.target.value == '') {
            setAddNewCardButton(false);
            setAddTranslateButton(false);
            setTranslation('');
        } else {
            e.target.value && setAddNewCardButton(false);
            setTranslation('');
            setAddTranslateButton(true);
        }
    };

    const fetchTranslate = async (phrase: string): Promise<void> => {

        if (phrase === '') {
            return;
        }
        const url = `${process.env.REACT_APP_BASE_URL}/api/words/translate/`;
        setIsLoading(true);
        const response = await fetch(url,
            {
                method: 'post',
                headers: {'Content-type': 'application/json'},
                body: JSON.stringify({
                    phrase: phrase
                })
            });
        if (response.ok) {
            const data = await response.json();
            setTranslation(data[0].text);
        } else {
            setTranslation('Error with loading. Try once more...');
        }
        setAddNewCardButton(true);
        setIsLoading(false);
    };

    const submitWordToTranslate = (e: FormEvent): void => {
        e.preventDefault();
        setAddTranslateButton(false);
        fetchTranslate(word);
        return;
    };


    return <>
        <form method='POST' onSubmit={submitWordToTranslate}>
            <Input value={'Need new word?'}
                   onChange={changeWord}
            />
        </form>
        {
            (translation || isLoading) &&
            <P color='purple' size='big' center>
                {isLoading ? 'translating...' : translation}
            </P>
        }

        {addTranslateButton && <Helper size='medium' icon='update'
                                       onClick={submitWordToTranslate}>Translate</Helper>}

        {addNewCardButton && <Helper size='medium' icon='save'>Add new card</Helper>}
    </>;
};
