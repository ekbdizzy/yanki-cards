import { Badge, Button, Htag } from '../index';
import { Link } from 'react-router-dom';
import { URLS } from '../../api';
import React from 'react';

export const Question = () => {
  return (
    <section className="flex flex-col justify-center p-10 basis-1/2">
      <div className="flex self-baseline mb-10">
        <Badge>
          <Link to={URLS.themes}>Career</Link>
        </Badge>
        <Button icon="refresh">New question</Button>
      </div>
      <div className="mb-10">
        <Htag>Tell me about yourself and what do you think about global warmness?</Htag>
      </div>
      <Button color="fuchsia" icon="refresh">What do you think about global warmness?</Button>
    </section>
  );
};
