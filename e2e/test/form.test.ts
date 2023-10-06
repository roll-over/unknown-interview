import { expect, test } from '@playwright/test';

test('From homepage to CV form', async ({ page }) => {
	await page.goto('/');
	await page.getByText('go to survey!').click();
	await page.getByText('CV').locator('visible=true').click();
	await expect(page.getByText('your review')).toBeVisible();
	const title = page
		.locator('fieldset')
		.filter({ hasText: 'Necessary title' })
		.locator('label')
		.nth(3);
	await title.click();

	await page.keyboard.press('Tab');
	await page.keyboard.press('ArrowRight');
	await page.keyboard.press('ArrowRight');
	const selectedGrade = await page.locator(':focus').inputValue();

	await page.getByLabel('min').fill('32');

	const selectedTitle = await title.inputValue();

	console.log({ selectedGrade, selectedTitle });
});
