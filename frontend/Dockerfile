FROM node:20-slim AS base


COPY ./ /frontend
WORKDIR /frontend

RUN npm install -g pnpm     
RUN pnpm install