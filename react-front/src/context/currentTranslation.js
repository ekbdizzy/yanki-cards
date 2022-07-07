import React, { createContext, useState } from 'react';

export const CurrentTranslationContext = createContext([{}, () => {}]);

export const CurrentTranslationProvider = ({ children }) => {
  const [state, setState] = useState(null);
  return <CurrentTranslationContext.Provider value={[state, setState]}>{children}</CurrentTranslationContext.Provider>;
};
