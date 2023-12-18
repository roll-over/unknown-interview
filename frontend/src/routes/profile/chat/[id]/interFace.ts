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

export interface Message {
  chat_name: string;
  text: string;
  own: boolean | null;
  created_at: string;
}

export interface Chat {
  chat_name: string;
  messages: Message[];
}

export const dateFormatter = (dateString: string | null) => {
  if (dateString === null) {
    return '';
  }

  const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'long', day: 'numeric' };
  const formattedDate = new Date(dateString).toLocaleDateString(undefined, options);
  return formattedDate;
};

export const formatTimestamp = (timestamp: number | null | string) => {
  if (timestamp === null) {
    return '';
  }

  const timestampAsNumber = typeof timestamp === 'string' ? Date.parse(timestamp) / 1000 : timestamp;

  if (isNaN(timestampAsNumber)) {
    return ''; 
  }

  const options: Intl.DateTimeFormatOptions = {
    // weekday: 'long',
    // year: 'numeric',
    // month: 'long',
    // day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
    // second: 'numeric',
    // timeZoneName: 'short'
  };

  return new Date(timestampAsNumber * 1000).toLocaleDateString(undefined, options);
};