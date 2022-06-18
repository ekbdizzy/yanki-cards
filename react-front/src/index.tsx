import React from 'react';
import ReactDOM from 'react-dom/client';
// import 'normalize.css';
import './index.css';
import App from './App';
import {BrowserRouter, Route, Routes} from "react-router-dom";

import reportWebVitals from './reportWebVitals';
import InterviewPage from "./pages/InterviewPage/InterviewPage";
import MainPage from "./pages/MainPage/MainPage";

const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
);
root.render(
    <React.StrictMode>
        <BrowserRouter>
            <Routes>
                <Route path='/interview'
                       element={<InterviewPage/>}/>
                <Route path=''
                       element={<MainPage/>}/>
            </Routes>

        </BrowserRouter>
    </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
