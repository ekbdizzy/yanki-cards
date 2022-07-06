import React from 'react';
import { withLayout } from '../../layout';
import { Badge, Button, Htag, Question, TranslationForm } from '../../components';
import Duck from '../../assets/images/duck.png';

const InterviewPage = () => {
  return (
    <>
      <div className="flex h-full">
        <Question/>
        <section className="basis-1/2 p-10">
          <img src={Duck} className="max-h-96 mx-auto" alt="Duck"/>
        </section>
      </div>
      <TranslationForm/>
    </>
  );
};

export default withLayout(InterviewPage);
