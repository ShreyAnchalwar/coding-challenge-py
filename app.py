from flask import Flask

app = Flask(__name__)

def correct_words(dictionary, mistypes):
    corrections = []
    for word in mistypes:
        for correct_word in dictionary:
            if len(word) == len(correct_word):
                diff_count = sum([1 for i in range(len(word)) if word[i] != correct_word[i]])
                if diff_count == 1:
                    corrections.append(correct_word)
                    break
    return corrections

@app.route('/the-clumsy-programmer', methods=['POST'])
def correct_words_api():
    data = request.get_json()[:4]  # Limit to the first 4 objects
    results = []
    for obj in data:
        dictionary = obj["dictionary"]
        mistypes = obj["mistypes"]
        corrections = correct_words(dictionary, mistypes)
        results.append({"corrections": corrections})
    return jsonify(results)

if __name__ == '__main__':
    app.run()
