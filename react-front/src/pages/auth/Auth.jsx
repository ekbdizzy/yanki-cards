import React from 'react';
import { Button, Htag } from '../../components';
import { Link } from 'react-router-dom';
import { URLS } from '../../api';

export const Auth = ({ title }) => {
  return (
    <form className="flex flex-col gap-10 items-center justify-start mx-auto px-5 max-w-lg">
      <div className="flex flex-col items-center">
        <Htag>{title}</Htag>
        {title === 'Login'
          ? <Link to={URLS.auth.register} className="text-indigo-500">Create new account</Link>
          : <Link to={URLS.auth.login} className="text-indigo-500">Already have an account</Link>
        }
      </div>
      <input placeholder="email"
             className="text-2xl text-center p-3 border-b-2 border-b-amber-500 outline-none text-fuchsia-600 w-full
                 focus:drop-shadow-xl transition-all"
             name="email"
             required
      />
      <input placeholder="password"
             className="text-2xl text-center p-3 border-b-2 border-b-amber-500 outline-none text-fuchsia-600 w-full
                 focus:drop-shadow-xl transition-all"
             name="password"
             type="password"
             required
      />
      {title === 'Sign Up' && <input placeholder="confirm password"
                                      className="text-2xl text-center p-3 border-b-2 border-b-amber-500 outline-none text-fuchsia-600 w-full
                 focus:drop-shadow-xl transition-all"
                                      name="password"
                                      type="password"
                                      required
      />}
      <Button icon="add" size="large">{title}</Button>
    </form>
  );
};
