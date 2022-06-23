import React, {ChangeEvent, FormEvent, useEffect, useState} from "react";
import styles from './InterviewPage.module.css';
import {withLayout} from "../../layout";
import {Badge, H, Helper, Input, Listener, P, WordTranslation} from "../../components";


function InterviewPage(): JSX.Element {


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
                    {/*<P>What do you think about global warmness?</P>*/}
                    {/*<P color='cyan' size='normal'>Have you ever heard about something new, than can be cause of new*/}
                    {/*    global*/}
                    {/*    warmness?</P>*/}
                </div>
            </section>
            <section className={styles.listener_block}>
                <Listener person='duck'/>
                <WordTranslation/>
            </section>
        </div>
    </>;
}

export default withLayout(InterviewPage);

