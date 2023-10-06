import RadioGroup from '$lib/components/RadioGroup.svelte';
import { expect, test } from '@playwright/experimental-ct-svelte';

test.use({ viewport: { width: 500, height: 500 } });

test('Radio group', async ({ mount }) => {
	const component = await mount<RadioGroup<string>>(RadioGroup, {
		props: { name: 'test', options: ['one', 'two', 'three'], value: 'three' }
	});
	await expect(component).toBeVisible();
	await component.getByLabel('one').click();
	await component.press('ArrowRight');
	expect(await component.getByLabel('two').isChecked()).toBeTruthy();
});
