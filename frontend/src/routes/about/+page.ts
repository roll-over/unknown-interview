export const prerender = true;

type GithubApiContributorsResponse = {
	login: string;
	id: number;
	node_id: string;
	avatar_url: string;
	gravatar_id: string;
	url: string;
	html_url: string;
	followers_url: string;
	following_url: string;
	gists_url: string;
	starred_url: string;
	subscriptions_url: string;
	organizations_url: string;
	repos_url: string;
	events_url: string;
	received_events_url: string;
	type: string;
	site_admin: boolean;
	contributions: number;
};
export const load = async ({ fetch }) => {
	const fetchContributorsList = async () => {
		const response = await fetch(
			'https://api.github.com/repos/roll-over/unknown-interview/contributors?per_page=100'
		);
		const result = (await response.json()) as Array<GithubApiContributorsResponse>;
		return result;
	};

	return { contributorsList: fetchContributorsList() };
};
