import os
from modelscope.hub.snapshot_download import snapshot_download
from modelscope import AutoTokenizer, AutoModel

# MODEL_NAME_DICT = {
#     'modelscope': 'ZhipuAI/chatglm3-6b',
#     'huggingface': 'THUDM/chatglm3-6b',
# }


def get_model(model_id):
    MODELSCOPE_CACHE_PATH = os.environ.get('MODELSCOPE_CACHE')
    print('MODELSCOPE_CACHE_PATH: ', MODELSCOPE_CACHE_PATH)
    MODEL_PATH = snapshot_download(model_id)
    print('MODEL_PATH: ', MODEL_PATH)
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModel.from_pretrained(model_id, trust_remote_code=True)
    return tokenizer, model


if __name__ == '__main__':
    tokenizer, model = get_model('ZhipuAI/chatglm3-6b')
