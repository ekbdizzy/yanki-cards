import {useEffect, useState} from "react";

interface useFetchOptions {
    isLoading: boolean
    response: string | null
    error: string | null
}


export default (url: string): [useFetchOptions, ((options: object) => Promise<void>)] => {

    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [response, setResponse] = useState<string | null>(null);
    const [error, setError] = useState<string | null>(null);

    const doFetch = async (options: Record<string, any>) => {
        setIsLoading(true);
        const baseUrl = `${process.env.REACT_APP_BASE_URL}/api/`;
        const response = await fetch(`${baseUrl}${url}`,
            {
                method: 'post',
                headers: {'Content-type': 'application/json'},
                body: JSON.stringify({...options})
            });
        if (response.ok) {
            const data = await response.json();
            setResponse(await data);
            setIsLoading(false);
            console.log(data);
        } else {
            setError(await response.json());
            setIsLoading(false);
            console.log(await response);
        }
    };

    useEffect(() => {
        return;
    }, [isLoading]);

    return [{isLoading, response, error}, doFetch];
};

