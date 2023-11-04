// THIS IS A TEMP FILE WITH CHAT FIXTURES.
// DELETE WHEN BACKEND WILL IMPLEMENT THIS FEATURE
import type { StrictOmit } from '$lib/utils/types';
import { faker } from '@faker-js/faker';

type User = {
	id: string;
	name: string;
};
type Message = {
	id: string;
	content: string;
	timestamp: number;
	author: User;
	chatId: Chat['id'];
};
type Chat = {
	id: string;
	label: string;
	messages: Message[];
};
export type ChatGist = StrictOmit<Chat, 'messages'> & { lastMessage?: Message };
export async function getChatList(): Promise<ChatGist[]> {
	await delay();
	return chats.map(({ id, label, messages }) => ({ id, label, lastMessage: messages.at(-1) }));
}

export async function getChat(id: string): Promise<Chat | undefined> {
	await delay();
	return chats.find((chat) => chat.id === id);
}

async function delay(min = 50, max = 700) {
	return new Promise((r) => setTimeout(r, randomInt(min, max)));
}

function randomInt(min: number, max: number) {
	return Math.random() * (max - min) + min;
}

export const YourID = 'YOU';
function generateChats(): Chat[] {
	const chats: Chat[] = Array.from({ length: 50 })
		.map(() => {
			const chatId = crypto.randomUUID();
			const receiver = faker.person.fullName();
			const messages: Message[] = Array.from({ length: randomInt(3, 50) })
				.map(() => {
					const isYours = Math.random() > 0.5;

					return {
						author: {
							id: !isYours ? crypto.randomUUID() : YourID,
							name: !isYours ? receiver : 'Svelte developer'
						},
						chatId,
						content: faker.lorem.sentence({ min: 1, max: 30 }),
						id: crypto.randomUUID(),
						timestamp: faker.date.recent({ days: 15 }).getTime()
					};
				})
				.sort((a, b) => a.timestamp - b.timestamp);
			return { messages, id: chatId, label: receiver };
		})
		.sort((a, b) => (b.messages.at(-1)?.timestamp ?? 0) - (a.messages.at(-1)?.timestamp ?? 0));
	return chats;
}

const chats: Chat[] = generateChats();
