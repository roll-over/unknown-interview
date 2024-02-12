import { skeleton } from '@skeletonlabs/tw-plugin';
import { join } from 'path';
import type { Config } from 'tailwindcss';
import plugin from 'tailwindcss/plugin';
import defaultTheme from 'tailwindcss/defaultTheme';
import { hideHireTheme } from './src/theme';

export default {
	darkMode: 'class',
	content: [
		'./src/**/*.{html,js,svelte,ts}',
		join(require.resolve('@skeletonlabs/skeleton'), '../**/*.{html,js,svelte,ts}')
	],
	theme: {
		extend: {
			fontFamily: {
				title: ['Inter Variable', ...defaultTheme.fontFamily.sans],
				body: ['Montserrat Variable', ...defaultTheme.fontFamily.sans]
			},
			fontSize: {
				m32: '2rem'
			},
			colors: {
				app: {
					blue: {
						50: '#EAF4FD',
						100: '#CBE6F7',
						400: '#4DA9E9',
						500: '#2B93E1',
						600: '#1985E2'
					},
					dark: {
						gray: '#353535',
						blue: '#3B4751',
						light: '#757575',
						amber: "#0b0b0b"
					}
				}
			},
			backgroundImage: {
				'light-background': 'linear-gradient(90deg, #B8E4FF 0%, #EDF5FA 52.6%, #B8E4FF 100%)',
				'dark-background': 'linear-gradient(90deg, #151618 0%, #909498 49.32%, #151618 100%)'
			},
			transitionDuration: { DEFAULT: '300ms' }
		}
	},
	plugins: [
		plugin(({ addVariant, matchVariant }) => {
			addVariant('current', ['&:focus-within', '&:hover']);
			addVariant('group-current', [':merge(.group):focus-within &', ':merge(.group):hover &']);
			addVariant('peer-current', [':merge(.peer):focus-within ~ &', ':merge(.peer):hover ~ &']);
			matchVariant('not', (value) => `&:not(${value})`);
		}),
		skeleton({
			themes: {
				custom: [hideHireTheme]
			}
		})
	]
} satisfies Config;
