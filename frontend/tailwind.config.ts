import { Config } from 'tailwindcss';
import plugin from 'tailwindcss/plugin';

export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		fontFamily: {
      title: ['Comfortaa'],
			body: ['Montserrat'],
    },
		extend: {
			colors: {
				'pattens-blue': '#CBE6F7',
				'dodger-blue': '#2B93E1',
				'alice-blue': '#EAF4FD',
				'summer-sky': '#4DA9E9',
				'focus-blue': '#1985E2',
				},
		}
	},
	plugins: [
		plugin(({ addVariant }) => {
			addVariant('current', ['&:focus-within', '&:hover']);
		})
	]
} satisfies Config;
