FROM node:20-slim AS base

COPY ./ /frontend
WORKDIR /frontend

RUN corepack enable    
RUN pnpm install
