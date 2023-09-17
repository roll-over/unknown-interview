import { spawn } from 'child_process';

spawn(`pnpm tsx --tsconfig scripts/tsconfig.json scripts/${process.argv[2]}.ts`, {
	shell: true,
	stdio: 'inherit'
});
