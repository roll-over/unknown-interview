// Интерфейс для последнего сообщения в чате
export interface LastMessage {
  custom_id: string;           // Уникальный идентификатор сообщения
  author_id: string;           // Идентификатор автора сообщения
  created_at: string;          // Временная метка, когда было отправлено сообщение
  text: string;                // Текст сообщения
  own: boolean | null;         // Флаг указывающий, является ли сообщение собственным (от пользователя)
}

// Интерфейс для чата
export interface Chats {
  chat_id: string;             // Уникальный идентификатор чата
  chat_name: string;           // Название чата
  last_message: LastMessage[]; // Массив последних сообщений в чате
}

// Интерфейс для заметки
export interface Note {
  custom_id: string;           // Уникальный идентификатор заметки
  related_id: string;          // Связанный идентификатор
  created_at: string;          // Временная метка, когда была создана заметка
  note_text: string;           // Текст заметки
}

// Интерфейс для ответа от сервера с данными чата
export interface ChatResponseSchema {
  chat_name: string;           // Название чата
  messages: LastMessage[];     // Массив сообщений в чате
  notes: Note[];               // Массив заметок в чате
}

// Интерфейс для сообщения в чате
export interface Message {
  chat_name: string;           // Название чата
  text: string;                // Текст сообщения
  own: boolean | null;         // Флаг указывающий, является ли сообщение собственным (от пользователя)
  created_at: string;          // Временная метка, когда было отправлено сообщение
}

// Интерфейс для чата с массивом сообщений
export interface Chat {
  chat_name: string;           // Название чата
  messages: Message[];         // Массив сообщений в чате
}

// Функция форматирования даты
export const dateFormatter = (dateString: string | null): string => {
  return dateString ? new Date(dateString).toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' }) : '';
};

// Функция форматирования временной метки
export const formatTimestamp = (timestamp: number | null | string): string => {
  const timestampAsNumber = typeof timestamp === 'string' ? Date.parse(timestamp) / 1000 : timestamp;

  if (timestampAsNumber === null || isNaN(timestampAsNumber)) {
    return '';
  }

  return new Date(timestampAsNumber * 1000).toLocaleDateString(undefined, { hour: 'numeric', minute: 'numeric' });
};
