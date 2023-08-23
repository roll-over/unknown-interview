FROM node:20-slim AS base


COPY ./ /frontend
WORKDIR /frontend


COPY ./package.json /package.json
RUN npm install -g pnpm     
RUN pnpm install