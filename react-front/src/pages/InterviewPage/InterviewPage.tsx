import React, {useEffect, useState} from "react";
import styles from './InterviewPage.module.css';
import {Body, Feedback, withLayout} from "../../layout";
import {Badge, H, Helper, Input, Listener, P} from "../../components";


function InterviewPage(): JSX.Element {

    const [translation, setTranslation] = useState<string>('');
    const [word, setWord] = useState<string>('');

    const changeWord = (e: any) => {
        setWord(e.target.value);
    };

    const fetchTranslate = async (phrase: string) => {
        const url = 'http://localhost:8000/api/words/translate/';
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


    const submitWordToTranslate = (e: any) => {
        e.preventDefault();
        fetchTranslate(word);
    };

    useEffect(() => {
        const a = 2;
    }, [translation]);


    return <>
        <div className={styles.main}>
            <section>
                <div>
                    <Badge>Career</Badge>
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


        {/*<Body>*/}
        {/*    <Feedback/>*/}
        {/*</Body>*/}
    </>;
}

export default withLayout(InterviewPage);

