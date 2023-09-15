[На главную](../README.md) > [Для разработчиков](../README/for-developers.md) > [Фронтенд](./README.md)

# Документация по фронтенду

## Scripts

Scripts are stored in ./frontend/scripts in .ts files - just specify the filename w/o extension.
Scripts are used for some menial tasks like codegen or starting a bulk of commands

```bash
# run script
pnpm script scriptname
```

### Checks

```bash
# run typechecking
pnpm check

# run typechecking in watch mode
pnpm check --watch

# run formatter
pnpm format

# run linting and check formatting
pnpm lint
```

### Testing

#### Unit

```bash
# run tests in watch mode
pnpm test:unit

# run tests once
pnpm test:unit run

# run tests with ui
pnpm test:unit --ui
```

#### Component/Integration

```bash
# todo
```

#### E2E

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
