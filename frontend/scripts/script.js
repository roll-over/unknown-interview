// this file removed the need to write boilerplate when executing scripts with tsx
import { spawn } from 'child_process';

spawn(`pnpm tsx --tsconfig scripts/tsconfig.json scripts/index.ts ${process.argv[2] ?? ''}`, {
	shell: true,
	stdio: 'inherit'
});
