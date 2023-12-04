<script lang="ts">
	import { onMount } from 'svelte';
	import {
		modeCurrent,
		setModeUserPrefers,
		setModeCurrent,
		setInitialClassState,
		getModeOsPrefers
	} from './index.js';

	// Types
	type CssClasses = string;
	type SvelteEvent<E extends Event = Event, T extends EventTarget = Element> = E & {
		currentTarget: EventTarget & T;
	};

	// Props
	/** Customize the `title` attribute for the component.  */
	export let title = 'Toggle light or dark mode.';
	// Props (styles)
	/** Provide classes to set the dark hover color. */
	export let hoverDark: CssClasses = 'hover:bg-blue-100';
	/** Provide classes to set the light hover color. */
	export let hoverLight: CssClasses = 'hover:bg-gray-300';
	/** Provide classes to set height styles. Should be half of width. */
	export let height: CssClasses = 'h-8';
	/** Provide classes to set border radius styles. */
	export let rounded: CssClasses = 'rounded-token';
	/** Provide classes to set the light SVG fill color. */
	export let fillLight: CssClasses = 'fill-black';
	/** Provide classes to set the dark SVG fill color. */
	export let fillDark: CssClasses = 'fill-white';

	// Classes
	const cTransition = `transition-all duration-[300ms]`;
	const cTrack = 'cursor-pointer';
	const cThumb = 'aspect-square scale-[0.8] flex justify-center items-center';
	const cIcon = 'w-7 h-7';

	// Local
	const svgPath = {
		sun: 'M12 5q-.425 0-.713-.288T11 4V2q0-.425.288-.713T12 1q.425 0 .713.288T13 2v2q0 .425-.288.713T12 5Zm4.95 2.05q-.275-.275-.275-.687t.275-.713l1.4-1.425q.3-.3.712-.3t.713.3q.275.275.275.7t-.275.7L18.35 7.05q-.275.275-.7.275t-.7-.275ZM20 13q-.425 0-.713-.288T19 12q0-.425.288-.713T20 11h2q.425 0 .713.288T23 12q0 .425-.288.713T22 13h-2Zm-8 10q-.425 0-.713-.288T11 22v-2q0-.425.288-.713T12 19q.425 0 .713.288T13 20v2q0 .425-.288.713T12 23ZM5.65 7.05l-1.425-1.4q-.3-.3-.3-.725t.3-.7q.275-.275.7-.275t.7.275L7.05 5.65q.275.275.275.7t-.275.7q-.3.275-.7.275t-.7-.275Zm12.7 12.725l-1.4-1.425q-.275-.3-.275-.713t.275-.687q.275-.275.688-.275t.712.275l1.425 1.4q.3.275.288.7t-.288.725q-.3.3-.725.3t-.7-.3ZM2 13q-.425 0-.713-.288T1 12q0-.425.288-.713T2 11h2q.425 0 .713.288T5 12q0 .425-.288.713T4 13H2Zm2.225 6.775q-.275-.275-.275-.7t.275-.7L5.65 16.95q.275-.275.687-.275t.713.275q.3.3.3.713t-.3.712l-1.4 1.4q-.3.3-.725.3t-.7-.3ZM12 18q-2.5 0-4.25-1.75T6 12q0-2.5 1.75-4.25T12 6q2.5 0 4.25 1.75T18 12q0 2.5-1.75 4.25T12 18Zm0-2q1.65 0 2.825-1.175T16 12q0-1.65-1.175-2.825T12 8q-1.65 0-2.825 1.175T8 12q0 1.65 1.175 2.825T12 16Zm0-4Z',
		moon: 'M12 21q-3.775 0-6.388-2.613T3 12q0-3.45 2.25-5.988T11 3.05q.325-.05.575.088t.4.362q.15.225.163.525t-.188.575q-.425.65-.638 1.375T11.1 7.5q0 2.25 1.575 3.825T16.5 12.9q.775 0 1.538-.225t1.362-.625q.275-.175.563-.162t.512.137q.25.125.388.375t.087.6q-.35 3.45-2.938 5.725T12 21Zm0-2q2.2 0 3.95-1.213t2.55-3.162q-.5.125-1 .2t-1 .075q-3.075 0-5.238-2.163T9.1 7.5q0-.5.075-1t.2-1q-1.95.8-3.163 2.55T5 12q0 2.9 2.05 4.95T12 19Zm-.25-6.75Z'
	};

	function onToggleHandler(): void {
		$modeCurrent = !$modeCurrent;
		setModeUserPrefers($modeCurrent);
		setModeCurrent($modeCurrent);
	}

	// A11y Input Handlers
	function onKeyDown(event: SvelteEvent<KeyboardEvent, HTMLDivElement>): void {
		// Enter/Space triggers selection event
		if (['Enter', 'Space'].includes(event.code)) {
			event.preventDefault();
			event.currentTarget.click();
		}
	}

	// Lifecycle
	onMount(() => {
		// Sync lightswitch with the theme
		if (!('modeCurrent' in localStorage)) {
			setModeCurrent(getModeOsPrefers());
		}
	});

	// State
	$: hoverBg = $modeCurrent === true ? hoverDark : hoverLight;
	$: iconFill = $modeCurrent === true ? fillLight : fillDark;
	// Reactive
	$: classesTrack = `${cTrack} ${cTransition} ${height} ${hoverBg} ${rounded} ${
		$$props.class ?? ''
	}`;
	$: classesThumb = `${cThumb} ${cTransition} ${height} ${rounded}`;
	$: classesIcon = `${cIcon} ${iconFill}`;
</script>

<!-- eslint-disable -->
<svelte:head>
	<!-- Workaround for a svelte parsing error: https://github.com/sveltejs/eslint-plugin-svelte/issues/492 -->
	{@html `<\u{73}cript nonce="%sveltekit.nonce%">(${setInitialClassState.toString()})();</script>`}
</svelte:head>

<div
	class="lightswitch-track {classesTrack}"
	on:click={onToggleHandler}
	on:click
	on:keydown={onKeyDown}
	on:keydown
	on:keyup
	on:keypress
	role="switch"
	aria-label="Light Switch"
	aria-checked={$modeCurrent}
	{title}
	tabindex="0"
>
	<!-- Thumb -->
	<div class="lightswitch-thumb {classesThumb}">
		<!-- SVG -->
		<svg
			class="lightswitch-icon {classesIcon}"
			xmlns="http://www.w3.org/2000/svg"
			viewBox="0 0 24 24"
		>
			<path d={$modeCurrent ? svgPath.moon : svgPath.sun} />
		</svg>
	</div>
</div>
