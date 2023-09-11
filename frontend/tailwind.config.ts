import { skeleton } from '@skeletonlabs/tw-plugin';
import { join } from 'path';
import type { Config } from 'tailwindcss';
import plugin from 'tailwindcss/plugin';
import defaultTheme from 'tailwindcss/defaultTheme';

export default {
	content: [
		'./src/**/*.{html,js,svelte,ts}',
		join(require.resolve('@skeletonlabs/skeleton'), '../**/*.{html,js,svelte,ts}')
	],
	theme: {
		extend: {
			fontFamily: {
				title: ['Comfortaa', ...defaultTheme.fontFamily.sans],
				body: ['Montserrat', ...defaultTheme.fontFamily.sans]
			},
			colors: {
				app: {
					blue: {
						100: '#EAF4FD',
						300: '#CBE6F7',
						500: '#4DA9E9',
						700: '#2B93E1',
						900: '#1985E2'
					}
				}
			}
		}
	},
	plugins: [
		plugin(({ addVariant }) => {
			addVariant('current', ['&:focus-within', '&:hover']);
		}),
		skeleton
	]
} satisfies Config;
