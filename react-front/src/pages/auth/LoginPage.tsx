import {withLayout} from "../../layout";
import {H, Helper, Input} from '../../components';
import styles from './Auth.module.css';
import React, {FormEvent, useEffect, useState} from "react";
import {useFetch, requestBody} from "../../hooks/useFetch";


function LoginPage(): JSX.Element {

    const [token, setToken] = useState<object>({});
    const [{isLoading, response, error}, doFetch] = useFetch('auth/jwt/create/');

    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const body: requestBody = {};
        const formData = new FormData(e.target as HTMLFormElement);
        formData.forEach((value, key) => body[key] = value);
        doFetch(body);
    };

    useEffect(() => {
        if (!response) {
            return;
        }
        localStorage.setItem('token', response.access.toString());
    }, [response]);


    return <>
        <H tag='h1'>Login Page</H>
        <form method='POST' className={styles.form} onSubmit={(e) => handleSubmit(e)}>
            <input placeholder='email' name='email' type='email'/>
            <input placeholder='password' name='password' type='password'/>
            <button type='submit'>Login</button>
        </form>
    </>;
}

export default withLayout(LoginPage);

