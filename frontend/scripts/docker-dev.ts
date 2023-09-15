import { spawn } from 'child_process';

spawn('pnpm nodemon -w package.json -L --exec "pnpm install"', { shell: true, stdio: 'inherit' });
spawn('pnpm script openapi-gen', { shell: true, stdio: 'inherit' });
spawn('pnpm dev', { shell: true, stdio: 'inherit' });
