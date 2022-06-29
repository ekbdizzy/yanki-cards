import {withLayout} from "../../layout";
import {H} from '../../components';
import styles from './Auth.module.css';
import React, {FormEvent, useEffect, useState} from "react";
import {useFetch} from "../../hooks/useFetch";
import {useNavigate} from "react-router-dom";
import {API, withBaseUrl} from '../../api';
import {fetchUserData} from "../../api/services";


interface Token extends Response {
    access: string
    refresh: string
}

function LoginPage(): JSX.Element {

    const [token, setToken] = useState<string | null>(null);
    const [{isLoading, response, error}, doFetch] = useFetch<Token>(withBaseUrl(API.auth.create_jwt));
    const [user, setUser] = useState({});

    const [isLoadingUser, setIsLoadingUser] = useState<boolean>(false);

    const navigate = useNavigate();

    const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const body: Record<string, unknown> = {};
        const formData = new FormData(e.target as HTMLFormElement);
        formData.forEach((value, key) => body[key] = value);
        doFetch({
            method: 'post',
            headers: {'Content-type': 'application/json'},
            body: JSON.stringify({...body})
        });
    };

    useEffect(() => {
        if (!response) {
            return;
        }

    }, [response]);


    useEffect(() => {
        if (!token) {
            return;
        }
        localStorage.setItem('token', token);
        const user = fetchUserData(token);
        setUser(user);
    }, [token]);


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

