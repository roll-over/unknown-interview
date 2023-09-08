import { Config } from 'tailwindcss';
import plugin from 'tailwindcss/plugin';

export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		// colors: {
    //   'blue': '#CBE6F7',
    // },
		fontFamily: {
      title: ['Comfortaa'],
			body: ['Montserrat'],
    },
		extend: {}
	},
	plugins: [
		plugin(({ addVariant }) => {
			addVariant('current', ['&:focus-within', '&:hover']);
		})
	]
} satisfies Config;
