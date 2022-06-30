import {useEffect, useState} from "react";

interface useFetchOptions {
    isLoading: boolean
    response: Response | null
    error: Response | null
}


interface Token extends Response {
    access: string
    refresh: string
}


export const useFetch = <T extends Response>(url: string): [useFetchOptions, ((options: RequestInit) => void)] => {
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [response, setResponse] = useState<Response | null>(null);
    const [error, setError] = useState<Response | null>(null);
    const [options, setOptions] = useState<RequestInit>({});

    const doFetch = (options: RequestInit = {}): void => {
        setOptions(options);
        setIsLoading(true);
    };

    useEffect(() => {
        if (!isLoading) {
            return;
        }

        const fetchData = async <T>(options: RequestInit = {}): Promise<T> => {
            const response = await fetch(url, options);
            const data = await response.json();
            setResponse(data);
            setIsLoading(false);
            return data;
        };
        fetchData<T>(options);
    }, [isLoading, options, url]);

    return [{isLoading, response, error}, doFetch];
};

