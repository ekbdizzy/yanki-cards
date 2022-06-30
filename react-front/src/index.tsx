import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import {BrowserRouter, Outlet, Route, Routes} from "react-router-dom";
import {CurrentUserContextProvider} from './context/currentUser';
import {
    MainPage,
    InterviewPage,
    AboutPage,
    WordsPage,
    ProfilePage,
    LoginPage,
    LogoutPage,
    RegisterPage,
    Page404,
} from "./pages";


const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
);
root.render(
    <React.StrictMode>
        <CurrentUserContextProvider>
            <BrowserRouter>
                <Routes>
                    <Route path='/'
                           element={<MainPage/>}/>
                    <Route path='/about'
                           element={<AboutPage/>}/>
                    <Route path='/profile'
                           element={<ProfilePage/>}/>
                    <Route path='/words'
                           element={<WordsPage/>}/>
                    <Route path='/interview'
                           element={<InterviewPage/>}/>
                    <Route path='auth'>
                        <Route index element={<Page404/>}/>
                        <Route path='login' element={<LoginPage/>}/>
                        <Route path='register' element={<RegisterPage/>}/>
                        <Route path='logout' element={<LogoutPage/>}/>
                    </Route>
                    <Route path="*"
                           element={<Page404/>}/>
                </Routes>
            </BrowserRouter>
        </CurrentUserContextProvider>
    </React.StrictMode>
);
