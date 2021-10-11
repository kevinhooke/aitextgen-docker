from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer
from aitextgen.utils import GPT2ConfigCPU
from aitextgen import aitextgen

# With your trained model, you can reload the model at any time by
# providing the folder containing the pytorch_model.bin model weights + the config, and providing the tokenizer.
ai2 = aitextgen(model_folder="/trained_model",
                tokenizer_file="trained_model/aitextgen.tokenizer.json")

ai2.generate(10, prompt="Once apon a time there was")