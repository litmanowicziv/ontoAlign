from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union
from ..model.ontology import Ontology


class IOntologyParser(ABC):

    @abstractmethod
    def parse_from_file(self, input_file: Union[str, Path]) -> Ontology:
        pass
