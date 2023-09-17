import { test, expect } from '@playwright/experimental-ct-svelte';
import Input from '$lib/components/Input.svelte';

test.use({ viewport: { width: 500, height: 500 } });

test('Input', async ({ mount }) => {
	const component = await mount(Input, {});
	await expect(component).toBeVisible();
	await component.fill('123');
	await expect(await component.inputValue()).toEqual('123');
});
