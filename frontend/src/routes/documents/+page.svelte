<script lang="ts">
	import { route } from '$lib/utils/route';
</script>

<h1 class="pb-2 text-6xl text-gray-900 dark:text-white">Documents</h1>
<nav class="dark:text-white">
	<ul>
		<li>
			<a href={route('/documents/cookie-policy')}>Cookie Policy</a>
		</li>
		<li><a href={route('/documents/privacy-policy')}>Privacy Policy</a></li>
		<li>
			<a href={route('/documents/terms-of-service')}>Terms of Service</a>
		</li>
	</ul>
</nav>
