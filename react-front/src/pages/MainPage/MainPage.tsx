import {withLayout} from "../../layout";
import {H} from '../../components';
import React, {useEffect, useState, useContext} from "react";
import {UserData} from "../../api/services.props";
import {API, withBaseUrl} from "../../api";
import {CurrentUserContext, IUser} from '../../context/currentUser';

function MainPage(): JSX.Element {

    const {user, isLoading, isLoggedIn, setUser} = useContext(CurrentUserContext);

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
            return;
        }

        const fetchUserData = async (token: string): Promise<UserData[]> => {
            const response = await fetch(withBaseUrl(API.auth.getUser),
                {
                    headers: new Headers({
                        'Content-type': 'application/json',
                        'Authorization': `Bearer ${token}`
                    }),
                });
            try {
                const result = await response.json();
                if (setUser) {
                    setUser(result);
                    console.log(user);
                }
                return result;
            } catch (error) {
                console.error(error);
                throw error;
            }
        };
        token && fetchUserData(token);
    }, []);


    useEffect(() => {
        console.log(user);
    }, [user]);


    return <>
        <H tag='h1'>Main Page</H>
    </>;
}

export default withLayout(MainPage);

