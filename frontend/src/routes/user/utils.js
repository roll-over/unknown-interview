export const getMaxCharacters = (
    maxCharacters,
    isOpen,
    children,
    text
) => {
        if (maxCharacters) {
            if (isOpen) {
                text = children
            } else {
                text = children.substring(0, maxCharacters)
            }
            return text
        } else{
            return children
        }
};


export const isFullText = (truncatedText, text) => {
    return (
        truncatedText &&
        truncatedText.split('').filter((c) => c !== ' ').length ===
            text.split('').filter((c) => c !== ' ').length
    );
};

export const getMaxWords = (
    maxWords,
    isOpen,
    children,
    text
) => {
        if (maxWords) {
            if (isOpen) {
                text = children
            } else {
                const words = children.split(' ').filter((c) => c !== '')
                text = words.slice(0, maxWords).join(' ')
            }
            return text
        } else {
            return children
        }
};