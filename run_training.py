from dp.preprocess import preprocess
from dp.train import train
from dict_reader import DictReader

if __name__ == '__main__':
    # Data Format: List of tuples ('en_us', 'word', 'PHONEMES')

    # Read Dicts
    dict_train = DictReader('dicts_prod/data_training.dict').dict
    dict_valid = DictReader('dicts_prod/data_validation.dict').dict

    # Convert to tuples
    train_data = list(zip(['en_us'], dict_train.keys(), dict_train.values()))
    val_data = list(zip(['en_us'], dict_valid.keys(), dict_valid.values()))

    config_file = 'dp/configs/autoreg_config.yaml'

    preprocess(config_file=config_file,
               train_data=train_data,
               val_data=val_data,
               deduplicate_train_data=False)

    train(config_file=config_file)
