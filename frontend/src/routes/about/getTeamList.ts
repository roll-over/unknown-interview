interface ISocial {
	title: string;
	link: string;
}

interface IMember {
	id: number;
	avatar_path: string;
	fullname: string;
	role: string;
	social_media: ISocial;
}

export const teamList: IMember[] = [
	{
		id: 1,
		fullname: 'Timur Bondarenko',
		avatar_path: 'Timur_Bondarenko.webp',
		role: 'CEO',
		social_media: {
			title: 'ORBY.TECH',
			link: 'https://orby-tech.space/'
		}
	},
	{
		id: 2,
		fullname: 'Dmitry Ibragimov',
		avatar_path: 'Dmitry_Ibragimov.webp',
		role: 'Backend Developer',
		social_media: {
			title: 'Linkedin',
			link: 'https://www.linkedin.com/in/ibragimov-dmitry/'
		}
	},
	{
		id: 3,
		fullname: 'Evgenii Perminov',
		avatar_path: 'Evgenii_Perminov.webp',
		role: 'Frontend Developer',
		social_media: {
			title: 'Linkedin',
			link: 'https://www.linkedin.com/in/ibragimov-dmitry/'
		}
	},
	{
		id: 4,
		fullname: 'Vladislav Lushnikov',
		avatar_path: 'Vladislav_Lushnikov.webp',
		role: 'Frontend Developer',
		social_media: {
			title: 'Github',
			link: 'https://github.com/VladStashevski?tab=repositories'
		}
	},
	{
		id: 5,
		fullname: 'Vladimir Ovcharuk',
		avatar_path: 'Vladimir_Ovcharuk.webp',
		role: 'Frontend Developer',
		social_media: {
			title: 'Linkedin',
			link: 'https://www.linkedin.com/in/vladimir-ovcharuk'
		}
	},
	{
		id: 6,
		fullname: 'Ocean50ul',
		avatar_path: 'Ocean50ul.webp',
		role: 'Backend Developer',
		social_media: {
			title: 'Github',
			link: 'https://github.com/Ocean50ul'
		}
	},
	{
		id: 7,
		fullname: 'Ekaterina Krasnoperova',
		avatar_path: 'Ekaterina_Krasnoperova.webp',
		role: 'Backend Developer',
		social_media: {
			title: 'Linkedin',
			link: 'https://www.linkedin.com/in/ekaterina-krasnoperova-070302268/'
		}
	},
	{
		id: 8,
		fullname: 'Olesia Geleverya',
		avatar_path: 'Olesia_Geleverya.webp',
		role: 'Designer',
		social_media: {
			title: 'Behance',
			link: 'https://www.behance.net/4e7ba437'
		}
	},
	{
		id: 9,
		fullname: 'Olga Markova',
		avatar_path: 'Olga_Markova.webp',
		role: 'HR Manager',
		social_media: {
			title: 'Linkedin',
			link: 'https://www.linkedin.com/in/olga-markova-bb254b284/'
		}
	}
];
