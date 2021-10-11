# aitextgen-docker
This is using https://github.com/minimaxir/aitextgen to train a new model and generate text from the model
packaged as a Docker image with supporting Python scripts to train and generate.

Run the training with:
$ docker run --volume /data/trained_model:/trained_model:rw \
  -d aitextgen sh -c "cd / && python3 train.py && mv aitextgen.tokenizer.json /trained_model"

The last step in the run command copies the generate token file to the EBS mounted volume so
it can be loaded by the next container instance to use the model and the token file 
to generate text after training.


Run the text generation with:
$ docker run --volume /data/trained_model:/trained_model:rw \
  -d aitextgen sh -c "cd / && python3 generate.py"