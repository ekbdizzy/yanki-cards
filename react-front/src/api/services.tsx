import {API, withBaseUrl} from "./routes";
import {useEffect} from "react";
import {Credentials, TokenResponse, UserData} from './services.props';

export const authenticate = async (token: string): Promise<boolean> => {
    const response = await fetch(withBaseUrl(API.auth.verify));
    return response.ok;
};

export const fetchUserData = async (token: string): Promise<UserData[]> => {
    const response = await fetch(withBaseUrl(API.auth.getUser),
        {
            headers: new Headers({
                'Content-type': 'application/json',
                'Authorization': `Bearer ${token}`
            }),
        });
    try {
        const result = await response.json();
        return result;
    } catch (error) {
        console.error(error);
        throw error;
    }
};

// export const login = ({email, password}: Credentials) => {
//
//     const fetchToken = async ({email, password}: credentials): Promise<jwtTokenResponse> => {
//         const response = await fetch(withBaseUrl(API.auth.create_jwt));
//
//     };


// };
