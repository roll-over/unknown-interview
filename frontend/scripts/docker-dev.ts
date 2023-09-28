import { spawn } from 'child_process';

export default function runDockerProcess() {
	spawn('pnpm install', { shell: true, stdio: 'inherit' }).addListener('exit', async (e) => {
		if (e !== 0) throw Error('There was an error trying to install dependencies');

		const watcher = (await import('chokidar')).watch('package.json');
		watcher.on('change', () => {
			spawn('pnpm install', { shell: true, stdio: 'inherit' });
		});

		spawn('pnpm dev', { shell: true, stdio: 'inherit' });
	});
}
