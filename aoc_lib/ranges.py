from dataclasses import dataclass


@dataclass
class Range:
    start: int
    end: int

    def __contains__(self, item) -> bool:
        return self.start <= item <= self.end

    def __len__(self) -> int:
        return self.end - self.start + 1

    def __lt__(self, other: Range) -> bool:
        return self.start < other.start or self.end < other.end

    def __gt__(self, other: Range) -> bool:
        return self.start > other.start or self.end > other.end

    def overlap(self, other: Range) -> bool:
        """Determine if there is overlap between 2 ranges"""
        return self.end >= other.start and self.start <= other.end

    @classmethod
    def consolidate(cls, r1: Range, r2: Range) -> Range | None:
        """
        Factory function to consolidate 2 overlapping Ranges

        :param r1: First range
        :param r2: Second range
        :return: Consolidate range if there is overlap else None
        """
        return Range(min(r1.start, r2.start), max(r1.end, r2.end)) if r1.overlap(r2) else None

    def __hash__(self):
        return hash((self.start, self.end))
