import pytest

from rasa.nlu.training_data import Message, TrainingData
from rasa.nlu.constants import TEXT_ATTRIBUTE, INTENT_ATTRIBUTE, TOKENS_NAMES
from rasa.nlu.tokenizers.lm_tokenizer import LanguageModelTokenizer
from rasa.nlu.utils.hugging_face.hf_transformers import HFTransformersNLP


@pytest.mark.parametrize(
    "model_name, texts, expected_tokens, expected_indices",
    [
        (
            "bert",
            [
                "Good evening.",
                "hello",
                "you're",
                "r. n. b.",
                "rock & roll",
                "ńöñàśçií",
                "leaving ",
            ],
            [
                ["good", "evening"],
                ["hello"],
                ["you", "re"],
                ["r", "n", "b"],
                ["rock", "&", "roll"],
                ["ń", "ö", "ñ", "à", "ś", "ç", "i", "í"],
            ],
            [
                [(0, 4), (5, 12)],
                [(0, 5)],
                [(0, 3), (4, 6)],
                [(0, 1), (3, 4), (6, 7)],
                [(0, 4), (5, 6), (7, 11)],
                [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)],
            ],
        ),
        #         (
        #             "openaigpt",
        #             ["Good evening.","hello", "you're", "r. n. b.", "rock & roll", "ńöñàśçií"],
        #             [["good", "evening"],["hello"],["you", "re"],["r", "n", "b"],["rock", "&", "roll"],["ń", "ö", "ñ", "à", "ś", "ç", "i", "í"]],
        #             [[(0, 8), (9, 12), (13, 18)],[(0, 5)],[(0, 3), (4, 6)],[(0, 1), (3, 4), (6, 7)],[(0, 4), (5, 6), (7, 11)],[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]],
        #         ),
        #         (
        #             "gpt2",
        #             ["Good evening.","hello", "you're", "r. n. b.", "rock & roll", "ńöñàśçií"],
        #             [["good", "evening"],["hello"],["you", "re"],["r", "n", "b"],["rock", "&", "roll"],["ń", "ö", "ñ", "à", "ś", "ç", "i", "í"]],
        #             [[(0, 8), (9, 12), (13, 18)],[(0, 5)],[(0, 3), (4, 6)],[(0, 1), (3, 4), (6, 7)],[(0, 4), (5, 6), (7, 11)],[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]],
        #         ),
        #         (
        #             "xlnet",
        #             ["Good evening.","hello", "you're", "r. n. b.", "rock & roll", "ńöñàśçií"],
        #             [["good", "evening"],["hello"],["you", "re"],["r", "n", "b"],["rock", "&", "roll"],["ń", "ö", "ñ", "à", "ś", "ç", "i", "í"]],
        #             [[(0, 8), (9, 12), (13, 18)],[(0, 5)],[(0, 3), (4, 6)],[(0, 1), (3, 4), (6, 7)],[(0, 4), (5, 6), (7, 11)],[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]],
        #         ),
        #         (
        #             "distilbert",
        #             ["Good evening.","hello", "you're", "r. n. b.", "rock & roll", "ńöñàśçií"],
        #             [["good", "evening"],["hello"],["you", "re"],["r", "n", "b"],["rock", "&", "roll"],["ń", "ö", "ñ", "à", "ś", "ç", "i", "í"]],
        #             [[(0, 8), (9, 12), (13, 18)],[(0, 5)],[(0, 3), (4, 6)],[(0, 1), (3, 4), (6, 7)],[(0, 4), (5, 6), (7, 11)],[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]],
        #         ),
        # (
        #             "roberta",
        #             ["Good evening.","hello", "you're", "r. n. b.", "rock & roll", "ńöñàśçií"],
        #             [["good", "evening"],["hello"],["you", "re"],["r", "n", "b"],["rock", "&", "roll"],["ń", "ö", "ñ", "à", "ś", "ç", "i", "í"]],
        #             [[(0, 8), (9, 12), (13, 18)],[(0, 5)],[(0, 3), (4, 6)],[(0, 1), (3, 4), (6, 7)],[(0, 4), (5, 6), (7, 11)],[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]],
        #         ),
    ],
)
def test_lm_tokenizer_edge_cases(model_name, texts, expected_tokens, expected_indices):

    print("model name", model_name)
    transformers_config = {"model_name": model_name}

    transformers_nlp = HFTransformersNLP(transformers_config)
    lm_tokenizer = LanguageModelTokenizer()

    for text, gt_tokens, gt_indices in zip(texts, expected_tokens, expected_indices):
        message = Message.build(text=text)
        transformers_nlp.process(message)
        tokens = lm_tokenizer.tokenize(message, TEXT_ATTRIBUTE)

        print(text)
        print([t.text for t in tokens])
        print([(t.start, t.end) for t in tokens])
        print("-----------------------------------")

        # assert [t.text for t in tokens] == expected_tokens
        # assert [t.start for t in tokens] == [i[0] for i in expected_indices]
        # assert [t.end for t in tokens] == [i[1] for i in expected_indices]

    print("=================================")
    assert True == False


# @pytest.mark.parametrize(
#     "text, expected_tokens",
#     [
#         ("Forecast_for_LUNCH", ["Forecast_for_LUNCH"]),
#         ("Forecast for LUNCH", ["Forecast for LUNCH"]),
#     ],
# )
# def test_custom_intent_symbol(text, expected_tokens):
#     component_config = {"intent_tokenization_flag": True, "intent_split_symbol": "+"}
#
#     tk = ConveRTTokenizer(component_config)
#
#     message = Message(text)
#     message.set(INTENT_ATTRIBUTE, text)
#
#     tk.train(TrainingData([message]))
#
#     assert [
#         t.text for t in message.get(TOKENS_NAMES[INTENT_ATTRIBUTE])
#     ] == expected_tokens
