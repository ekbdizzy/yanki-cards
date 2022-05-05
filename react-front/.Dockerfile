FROM node:16-alpine
WORKDIR ./react-front
COPY . .
RUN npm -ci --silent
RUN npm run build
