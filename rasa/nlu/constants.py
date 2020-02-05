TEXT_ATTRIBUTE = "text"

RESPONSE_KEY_ATTRIBUTE = "response_key"

INTENT_ATTRIBUTE = "intent"

RESPONSE_ATTRIBUTE = "response"

ENTITIES_ATTRIBUTE = "entities"
BILOU_ENTITIES_ATTRIBUTE = "bilou_entities"

EXTRACTOR_ATTRIBUTE = "extractor"

PRETRAINED_EXTRACTORS = {"DucklingHTTPExtractor", "SpacyEntityExtractor"}

CLS_TOKEN = "__CLS__"

MESSAGE_ATTRIBUTES = [TEXT_ATTRIBUTE, INTENT_ATTRIBUTE, RESPONSE_ATTRIBUTE]

TOKENS_NAMES = {
    TEXT_ATTRIBUTE: "tokens",
    INTENT_ATTRIBUTE: "intent_tokens",
    RESPONSE_ATTRIBUTE: "response_tokens",
}

SPARSE_FEATURE_NAMES = {
    TEXT_ATTRIBUTE: "text_sparse_features",
    INTENT_ATTRIBUTE: "intent_sparse_features",
    RESPONSE_ATTRIBUTE: "response_sparse_features",
}

DENSE_FEATURE_NAMES = {
    TEXT_ATTRIBUTE: "text_dense_features",
    INTENT_ATTRIBUTE: "intent_dense_features",
    RESPONSE_ATTRIBUTE: "response_dense_features",
}

SPACY_DOCS = {
    TEXT_ATTRIBUTE: "text_spacy_doc",
    RESPONSE_ATTRIBUTE: "response_spacy_doc",
}
LANGUAGE_MODEL_DOCS = {
    TEXT_ATTRIBUTE: "text_language_model_doc",
    RESPONSE_ATTRIBUTE: "response_language_model_doc",
}

DENSE_FEATURIZABLE_ATTRIBUTES = [TEXT_ATTRIBUTE, RESPONSE_ATTRIBUTE]

RESPONSE_SELECTOR_PROPERTY_NAME = "response_selector"
DEFAULT_OPEN_UTTERANCE_TYPE = "default"
OPEN_UTTERANCE_PREDICTION_KEY = "response"
OPEN_UTTERANCE_RANKING_KEY = "ranking"
RESPONSE_IDENTIFIER_DELIMITER = "/"
