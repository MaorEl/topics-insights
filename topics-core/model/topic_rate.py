import datetime
from dataclasses import dataclass


@dataclass
class TopicRate:
    time: datetime
    rate: int
