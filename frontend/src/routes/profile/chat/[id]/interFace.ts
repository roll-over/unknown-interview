export interface LastMessage {
	custom_id: string;
	author_id: string;
	created_at: string;
	text: string;
	own: boolean | null;
}

export interface Chats {
	chat_id: string;
	chat_name: string;
	last_message: LastMessage[];
}

export interface Note {
	custom_id: string;
	related_id: string;
	created_at: string;
	note_text: string;
}

export interface ChatResponseSchema {
	chat_name: string;
	messages: LastMessage[];
	notes: Note[];
}

export interface ChatResponse {
	chat_name: string;
	messages: Message[];
}

export interface Message {
	custom_id: string;
	author_id: string;
	created_at: string;
	text: string;
	own: boolean | null;
	notes: Note[];
}

export interface Chat {
	chat_name: string;
	messages: Message[];
}

export const dateFormatter = (dateString: string | null): string => {
	return dateString
		? new Date(dateString).toLocaleDateString(undefined, {
				year: 'numeric',
				month: 'long',
				day: 'numeric'
		  })
		: '';
};

export function formatTime(timestamp: string | null): string {
	if (!timestamp) return '';

	const date = new Date(timestamp);
	return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

export function formatDate(dateString: string | null): string {
	return dateFormatter(dateString);
}

export const formatTimestamp = (timestamp: number | null | string): string => {
	const timestampAsNumber =
		typeof timestamp === 'string' ? Date.parse(timestamp) / 1000 : timestamp;

	if (timestampAsNumber === null || isNaN(timestampAsNumber)) {
		return '';
	}

	return new Date(timestampAsNumber * 1000).toLocaleDateString(undefined, {
		hour: 'numeric',
		minute: 'numeric'
	});
};
