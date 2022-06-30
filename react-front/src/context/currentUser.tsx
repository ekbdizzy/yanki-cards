import {createContext, ReactNode, useState} from "react";
import {stringify} from "querystring";

export interface IUser {
    firstName: string
    lastName: string
    email: string
}

export interface IUserContext {
    user?: IUser
    isLoggedIn?: boolean
    isLoading?: boolean
    setUser?: (newUser: IUser) => void
}


export const CurrentUserContext = createContext<IUserContext>({
    user: {
        firstName: '',
        lastName: '',
        email: ''
    },
    isLoading: false,
    isLoggedIn: false,
});

export const CurrentUserContextProvider = ({
                                               user,
                                               isLoggedIn,
                                               isLoading,
                                               children
                                           }: IUserContext & { children: ReactNode }): JSX.Element => {

    const [userState, setUserState] = useState<IUserContext>({
        user,
        isLoading,
        isLoggedIn,
    },);
    const setUser = (user: IUser) => {
        setUserState({...userState, user});
    };

    return (
        <CurrentUserContext.Provider value={{user, isLoading, isLoggedIn, setUser}}>
            {children}
        </CurrentUserContext.Provider>
    );
};
