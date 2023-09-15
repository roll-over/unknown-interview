import { test, expect } from '@playwright/experimental-ct-svelte';
import RadioGroup from '$lib/components/RadioGroup.svelte';

test.use({ viewport: { width: 500, height: 500 } });

test('Radio group', async ({ mount }) => {
	const component = await mount(RadioGroup, {
		props: { options: ['one', 'two', 'three'], name: 'profession', value: 'three' }
	});
	await expect(component).toBeVisible();
	await component.getByLabel('one').click();
	await component.press('ArrowRight');
	expect(await component.getByLabel('two').isChecked()).toBeTruthy();
});
