<script lang="ts">
	import { route } from '$lib/utils/route';
</script>

<div>YOUR VACANCIES</div>
<a href={route((p) => `/profile/vacancy/${p(1)}`)}>YOUR FIRST VACANCY</a>
