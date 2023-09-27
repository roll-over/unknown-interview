<script lang="ts">
	import { route } from '$lib/utils/route';
</script>

<div>YOUR CVs</div>
<a href={route((p) => `/profile/cv/${p(1)}`)}>YOUR FIRST CV</a>
