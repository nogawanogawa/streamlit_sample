from sudachipy import tokenizer, dictionary

def get_token(source) :

    tokenizer_obj = dictionary.Dictionary().create()
    mode = tokenizer.Tokenizer.SplitMode.C
    result = tokenizer_obj.tokenize(source, mode)

    word_list = []
    for mrph in result:
        if not (mrph == ""):
            norm_word = mrph.normalized_form()
            hinsi = mrph.part_of_speech()[0] 

            word = tokenizer_obj.tokenize(norm_word, mode)[0].dictionary_form()
            word_list.append(word)

    return word_list
