<script lang="ts">
	import { onMount } from 'svelte';
	import {
		modeCurrent,
		setModeUserPrefers,
		setModeCurrent,
		getModeOsPrefers
	} from './index.js';
	import MaterialSymbolsSunnyOutlineRounded from '~icons/material-symbols/sunny-outline-rounded';
	import MaterialSymbolsDarkModeOutlineRounded from '~icons/material-symbols/dark-mode-outline-rounded';

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
	export let height: CssClasses = 'h-15';
	/** Provide classes to set border radius styles. */
	export let rounded: CssClasses = 'rounded-token';
	/** Provide classes to set the light SVG fill color. */
	export let fillLight: CssClasses = 'text-black';
	/** Provide classes to set the dark SVG fill color. */
	export let fillDark: CssClasses = 'text-white';

	// Classes
	const cTransition = `transition-all duration-[300ms]`;
	const cTrack = 'cursor-pointer';
	const cThumb = 'aspect-square scale-[0.8] flex justify-center items-center';
	const cIcon = 'w-7 h-7';

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
		{#if $modeCurrent}
			<MaterialSymbolsDarkModeOutlineRounded class={classesIcon} />
			<span class="sr-only">Dark</span>
		{:else}
			<MaterialSymbolsSunnyOutlineRounded class={classesIcon} />
			<span class="sr-only">Light</span>
		{/if}
	</div>
</div>
