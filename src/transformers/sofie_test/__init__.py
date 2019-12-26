import spacy

from transformers import XLMRobertaModel

if __name__ == "__main__":
    print("GO")
    # model = XLMRobertaModel.from_pretrained("xlm-roberta-base")
    # model.save_pretrained("xlm-roberta-base")


    nlp = spacy.load("C:\\Users\\Sofie\\Documents\\git\\spacy-transformers\\examples\\distilbert-base-german-cased")
    nlp = spacy.load("C:\\Users\\Sofie\\Documents\\git\\spacy-transformers\\examples\\xlm-mlm-100-1280")

    print("type nlp", type(nlp))
    parsed_sentence = nlp("now I wonder what this is")
    print(parsed_sentence)

    print("DONE")
