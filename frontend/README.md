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
