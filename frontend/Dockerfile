FROM node:20-slim AS base

COPY ./package.json /package.json
RUN npm install -g pnpm     
RUN pnpm install

ENV PATH /node_modules/.bin:$PATH

COPY ./ /frontend
WORKDIR /frontend

