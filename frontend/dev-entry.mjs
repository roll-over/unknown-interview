import { spawn } from 'child_process';

/*
 * Install dependencies every time package.json changes
 */
spawn('nodemon -w package.json --exec "pnpm install"', {
	stdio: 'inherit',
	shell: true
});

/*
 * Restart node when a source file changes, plus:
 * Restart when `npm install` ran based on `package-lock.json` changing.
 */
spawn(
	'nodemon --inspect -e js,json -i node_modules -i package.json --exec "pnpm run dev -- --open --host 0.0.0.0"',
	{
		stdio: 'inherit',
		shell: true
	}
);
