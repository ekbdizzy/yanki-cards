import {useEffect, useState} from "react";
import {To} from "react-router-dom";

export interface requestBody extends Record<string, File | string | number | boolean> {
}

interface useFetchOptions {
    isLoading: boolean
    response: requestBody | null
    error: requestBody | string | null
}

interface Token {
    access: string,
    refresh: string
}

export const useFetch = (url: string): [useFetchOptions, ((options: requestBody) => void)] => {
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [response, setResponse] = useState<requestBody | null>(null);
    const [error, setError] = useState<requestBody | string | null>(null);
    const [options, setOptions] = useState<requestBody>({});

    const doFetch = (options: requestBody = {}): void => {
        setOptions(options);
        setIsLoading(true);
    };

    useEffect(() => {
        if (!isLoading) {
            return;
        }

        const fetchData = async <T>(options: requestBody = {}): Promise<T> => {
            const baseUrl = `${process.env.REACT_APP_BASE_URL}/api/`;
            const response = await fetch(`${baseUrl}${url}`,
                {
                    method: 'post',
                    headers: {'Content-type': 'application/json'},
                    body: JSON.stringify({...options})
                });
            const data = await response.json();
            setResponse(data);
            setIsLoading(false);
            return data;
        };
        const result = fetchData<Token>(options);
    }, [isLoading, options, url]);

    return [{isLoading, response, error}, doFetch];
};

