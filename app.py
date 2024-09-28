from flask import Flask

app = Flask(__name__)

@app.route('/the-clumsy-programmer', methods=['POST'])
def correct_mistypes():
    all_data = request.get_json()
    results = []

    for data in all_data:
        dictionary = data['dictionary']
        mistypes = data['mistypes']
        corrections = []

        for mistyped_word in mistypes:
            for correct_word in dictionary:
                if is_one_letter_off(mistyped_word, correct_word):
                    corrections.append(correct_word)
                    break

        results.append({"corrections": corrections})

    return jsonify(results), 200

def is_one_letter_off(mistyped_word, correct_word):
    differences = sum(1 for m, c in zip(mistyped_word, correct_word) if m != c)
    return differences == 1

if __name__ == '__main__':
    app.run()
