[На главную](../README.md) > [Для разработчиков](../README/for-developers.md) > [e2e](./README.md)

# Документация по e2e

## Scripts

For now requires that the server is already running

```bash
# run tests once
pnpm test:e2e

# run tests with ui - has watch mode support (only watches test file changes)
pnpm test:e2e --ui

```

You can also generate user actions on a page using this command

```bash
pnpm playwright codegen URL
```
