<script lang="ts">
	import { route } from '$lib/utils/route';
</script>

<div>YOUR JOB OFFERS</div>
<a href={route((p) => `/profile/offer/${p(1)}`)}>YOUR FIRST OFFER</a>
