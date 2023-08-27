const h1Class = `
mb-4
text-4xl
font-extrabold
leading-none

tracking-tight
text-gray-900
md:text-5xl
lg:text-6xlmb-4

dark:text-white
dark:text-whitemb-4
dark:text-white
`;

const blueButtonClass = `
mb-2
mr-2
rounded-lg
bg-blue-700
px-5
py-2.5
text-sm
font-medium
text-white

hover:bg-blue-800

focus:outline-none
focus:ring-4
focus:ring-blue-300

dark:bg-blue-600
dark:hover:bg-blue-700
dark:focus:ring-blue-800
`;

const blueLinkLikeButtonClass = blueButtonClass;

const defaultInputClass = `
block
w-full
rounded-lg
border
border-gray-300
bg-gray-50
p-2.5
text-sm
text-gray-900

focus:border-blue-500
focus:ring-blue-500

dark:border-gray-600
dark:bg-gray-700
dark:text-white
dark:placeholder-gray-400
dark:focus:border-blue-500
dark:focus:ring-blue-500
`;

export { h1Class, blueLinkLikeButtonClass, blueButtonClass, defaultInputClass };
