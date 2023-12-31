[На главную](../README.md) > [Для разработчиков](../README/for-developers.md) > [Фронтенд](./README.md)

# Документация по фронтенду

## Scripts

Scripts are stored in ./frontend/scripts in .ts files - just specify the filename w/o extension.
Scripts are used for some menial tasks like codegen or starting a bulk of commands.
A script needs to a export a default function which will be executed when a command is ran.

```bash
# run script
pnpm rscript scriptname
```

### Checks

```bash
# run typechecker
pnpm check

# run typechecker in watch mode
pnpm check --watch

# run formatter
pnpm format

# run format checker
pnpm format-check

# run linter
pnpm lint

# run linter, typechecker and formatter
pnpm check-all
```

### Testing

#### Unit

Files must be somewhere in the `./src` directory and named `*.{spec,test}.ts`.

```bash
# run tests in watch mode
pnpm test:unit

# run tests once
pnpm test:unit run

# run tests with ui
pnpm test:unit --ui

# run tests with code coverage (you can combine it with ui flag)
pnpm test:unit --coverage
```

#### Component/Integration

Files must be somewhere in the `./src` directory and named `*.{cspec,ctest}.ts`.

```bash
# run tests once
pnpm test:comp

# run tests with ui in watch mode - watches only changes in test files
pnpm test:comp --ui
```

### Stack

- Web Framework - [Svelte](https://svelte.dev/docs/introduction)
  - [SvelteKit](https://kit.svelte.dev/docs/introduction)
- Async State - [Tanstack-Query Svelte](https://tanstack.com/query/v5/docs/svelte/overview)
- UI - [Skeleton](https://www.skeleton.dev/)
- CSS - [TailwindCSS](https://tailwindcss.com/docs/utility-first)
  - [cheatsheet](https://tailwindcomponents.com/cheatsheet/)
- Icons - [Unplugin Icons](https://github.com/unplugin/unplugin-icons)
  - [Icones](https://icones.js.org/)
