<script lang="ts">
	import { page } from '$app/stores';
	import RandomMatchView from '../../RandomMatchView.svelte';

	$: id = $page.params.id;
</script>

{#if id}
	<RandomMatchView profileMeta={{ id, type: 'offer' }} />
{:else}
	Something went wrong
{/if}
