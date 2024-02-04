sample_text = open('new_article.txt','r',encoding='utf-8')
text=sample_text.read()

def count_word_frequency(text):
    # Convert the text to lowercase to treat words in a case-insensitive manner
    text = text.lower()
    
    # Split the text into words
    words = text.split()

    # Initialize an empty dictionary to store word frequencies
    word_frequency = {}

    # Count the frequency of each word
    for word in words:
        # Remove punctuation if necessary
        word = word.strip('.,!?()[]{}":;')

        # Update the word frequency in the dictionary
        word_frequency[word] = word_frequency.get(word, 0) + 1

    
    Frequency=open('Word_Frequency.txt','w',encoding='utf-8') 
    for word, frequency in word_frequency.items():  
        Frequency.write(f"{word}: {frequency}\n")
    return word_frequency
# Example usage

result = count_word_frequency(text)

# Display the word frequencies
for word, frequency in result.items():
    print(f"{word}: {frequency}")


