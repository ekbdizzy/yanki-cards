FROM node:16-alpine
WORKDIR ./react-front
COPY . .
RUN npm install
RUN npm run build
