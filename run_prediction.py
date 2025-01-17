from dp.phonemizer import Phonemizer

if __name__ == '__main__':

    checkpoint_path = 'checkpoints/pre_en_us_cmudict_forward.pt'
    phonemizer = Phonemizer.from_checkpoint(checkpoint_path, device='cuda')

    # noinspection SpellCheckingInspection
    text = "Adam'll"

    result = phonemizer.phonemise_list([text], lang='en_us')

    print(result.phonemes)
    for text, pred in result.predictions.items():
        tokens, probs = pred.phoneme_tokens, pred.token_probs
        for o, p in zip(tokens, probs):
            print(f'{o} {p}')
        tokens = ''.join(tokens)
        print(f'{text} | {tokens} | {pred.confidence}')

