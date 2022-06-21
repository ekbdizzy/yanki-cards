import React, {ChangeEvent, FormEvent, useEffect, useState} from "react";
import styles from './InterviewPage.module.css';
import {withLayout} from "../../layout";
import {Badge, H, Helper, Input, Listener, P} from "../../components";


function InterviewPage(): JSX.Element {

    const [translation, setTranslation] = useState<string>('');
    const [word, setWord] = useState<string>('');
    const [themes, setThemes] = useState<string[]>([]);

    const changeWord = (e: ChangeEvent<HTMLInputElement>) => {
        setWord(e.target.value);
    };

    const fetchThemes = async (): Promise<void> => {
        const url = `${process.env.REACT_APP_BASE_URL}/api/themes`;
        const response = await fetch(url);
        const result = await response.json();
        setThemes(result);
    };

    const anotherFetchThemes = async (): Promise<void> => {
        const url = `/api/themes`;
        const response = await fetch(url);
        const result = await response.json();
        console.log('another fetching');
        setThemes(result);
    };


    const fetchTranslate = async (phrase: string): Promise<void> => {
        const url = `${process.env.REACT_APP_BASE_URL}/api/words/translate/`;
        const response = await fetch(url,
            {
                method: 'post',
                headers: {'Content-type': 'application/json'},
                body: JSON.stringify({
                    phrase: phrase
                })
            });
        const text = await response.json();
        setTranslation(text[0].text);
    };

    const submitWordToTranslate = (e: FormEvent<HTMLFormElement>): void => {
        e.preventDefault();
        fetchTranslate(word);
    };

    useEffect(() => {
        const a = 2;
    }, [translation]);
    useEffect(() => {
        console.log(themes);
    }, [themes]);

    return <>
        <div className={styles.main}>
            <section>
                <H tag={'h1'}>{themes.toString()}</H>
                <div>
                    <Badge onClick={fetchThemes}>Career</Badge>
                    <Badge onClick={anotherFetchThemes}>Another Badge</Badge>
                    <Helper size='small' icon='update'>Change question</Helper>
                </div>
                <H tag={'h1'}>What do you know about the capital of Great Britain?</H>
                <div className={styles.extension}/>
                <div>
                    <Helper size='medium' icon='update'>New hint</Helper>
                </div>
                <div className={styles.extension}/>
                <div>
                    <P>What do you think about global warmness?</P>
                    <P color='cyan' size='normal'>Have you ever heard about something new, than can be cause of new
                        global
                        warmness?</P>
                </div>
            </section>
            <section className={styles.listener_block}>
                <Listener person='duck'/>
                <form method='POST' onSubmit={submitWordToTranslate}>
                    <Input value={'Need new word?'}
                           onChange={changeWord}/>
                </form>
                <P color='purple' size='big'>{translation}</P>
                <Helper size='medium' icon='save'>Add new card</Helper>
            </section>
        </div>
    </>;
}

export default withLayout(InterviewPage);

