import pickle
from pathlib import Path
from typing import Dict, List, Any, Union

import torch
import yaml
import math


def read_config(path: str) -> Dict[str, Any]:
    with open(path, 'r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
    return config


def save_config(config: Dict[str, Any], path: str) -> None:
    with open(path, 'w+', encoding='utf-8') as stream:
        yaml.dump(config, stream, default_flow_style=False)


def get_files(path: str, extension='.wav') -> List[Path]:
    return list(Path(path).expanduser().resolve().rglob(f'*{extension}'))


def pickle_binary(data: object, file: Union[str, Path]) -> None:
    with open(str(file), 'wb') as f:
        pickle.dump(data, f)


def unpickle_binary(file: Union[str, Path]) -> Any:
    with open(str(file), 'rb') as f:
        return pickle.load(f)


def to_device(batch: Dict[str, torch.tensor], device: torch.device) -> Dict[str, torch.tensor]:
    return {key: val.to(device) for key, val in batch.items()}


def get_sequence_prob(tokens: List[int], logits: torch.tensor) -> float:
    if len(tokens) == 0:
        return 1.
    norm_logits = logits.softmax(dim=-1)
    probs = [norm_logits[i, p] for i, p in enumerate(tokens[1:])]
    prob = math.exp(sum([math.log(p) for p in probs]))
    return prob