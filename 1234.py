import rasa

rasa.train(config="config.yml",training_files="Utterances.yml",output="saved_model",domain="domain.yml")