FROM node:20-slim AS base


COPY ./ /frontend
WORKDIR /frontend

RUN corepack enable    
RUN npm install -g nodemon
RUN pnpm install
