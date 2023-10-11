import type { components } from '$lib/openapi';
export const cvContent = `Carrying  out testing of customized / developed software, analysis of the results, formalization of comments and their discussion with the project team.
	
Requirements:
-Strong knowledge of C++, STL libraries (basic algorithms and containers). 
-Understanding of simple data structures, knowledge of object-oriented programming principles, and good problem-solving skills.
- Familiarity with version control systems such as Git.
- Experience with software development tools, including integrated development environments (IDEs), compilers, and debuggers.
- A solid foundation in computer science concepts such as algorithms, data structures, and computer architecture.
- Effective communication skills, both written and verbal, as you'll be collaborating with team members and possibly communicating with non-technical stakeholders.
- The ability to work both independently and as part of a team, as software development often involves both individual tasks and collaborative efforts.
- Attention to detail and a commitment to writing clean, maintainable, and well-documented code.
- Knowledge of software development best practices, including unit testing, code reviews, and continuous integration.
- Experience with software design patterns and the ability to apply them appropriately to solve complex problems.
`;
export const vacancyContent = `We are looking for C++ developers to join our team, both talented Juniors and experienced Middle and Senior`;
export const randomCv: components['schemas']['CVResponseSchema'] = {
	profession: { name: 'C++ programmer' },
	title: 'manager',
	grade: 'principal',
	skillset: [{ name: 'CSS' }, { name: 'HTML5' }, { name: 'JS/TS' }],
	salary: { currency: 'USD', max_level: 3500, min_level: 3000 },
	extra_info: `Professional skills:
- Experience with HTML5, CSS3, JS;
- knowledge of JavaScript/JQuery;
- experience of adaptive layout;
- experience in creating HTML website pages based on design layouts;
- experience in website layout and templates for CMS;
- skills in linking scripts to the user interface that provide visualization and animation of site pages;
- skills to provide the required level of user interface (UI 
- User Interface) and interaction experience (UX 
- User Experience);
- knowledge of CSS frameworks;
- knowledge of cross
-browser layout;
- knowledge of Photoshop;
- knowledge of other programming languages.

Additional information:The ability to work in multitasking mode and high analytical skills allow me to work effectively with large amounts of information, quickly find high-quality solutions to complex problems.`,
	owner_id: '',
	custom_id: ''
};

export const randomVacancy: components['schemas']['VacancyResponseSchema'] = {
	profession: { name: 'С++ programmer' },
	title: 'lead',
	grade: 'junior',
	skillset: [{ name: 'C++' }, { name: 'SQL' }, { name: 'Rust' }],
	salary: { currency: 'EUR', min_level: 300, max_level: 700 },
	extra_info: `C++ programmers are required for the design and development of highly loaded information systems.
		
We are looking for C++ developers to join our team, both talented Juniors and experienced Middle and Senior.

Requirements:

- Strong knowledge of C++, including a deep understanding of the C++ Standard Template Library (STL), encompassing proficiency in basic algorithms and various containers such as vectors, lists, and maps.
- An understanding of simple data structures, combined with the ability to code in C at a fundamental level, enabling you to appreciate the core principles of programming.
- A strong curiosity and desire to delve into the inner workings of the technology you work with, allowing you to comprehend how software and hardware components interact and how systems are architected.
- Proficiency in working with memory, including memory management and allocation, an essential skill for optimizing resource utilization and preventing memory leaks in your code.
- Hands-on experience in software development under the Linux operating system, particularly in an environment following Object-Centric (OC) practices, which is crucial for developing robust and efficient software solutions on the Linux platform.
- A solid foundation in Structured Query Language (SQL), with the ability to design and interact with databases effectively. This skill is valuable for data-driven applications and database management, ensuring your software can store, retrieve, and manipulate data efficiently.
`,
	custom_id: '',
	owner_id: ''
};
