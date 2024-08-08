class User:
    def __init__(self) -> None:
        self.rank = -8
        self._progress: int = 0

    @property
    def MIN_RANK(self) -> int:
        return -8

    @property
    def MAX_RANK(self) -> int:
        return 8

    @property
    def rank(self) -> int:
        return min(self._rank, self.MAX_RANK)

    @rank.setter
    def rank(self, value: int) -> None:
        if value < self.MIN_RANK:
            raise ValueError
        if value > self.MAX_RANK:
            raise ValueError
        if value == 0:
            self._rank: int = 1
        else:
            self._rank: int = value

    @property
    def progress(self) -> int:
        return self._progress

    @property
    def MAX_PROGRESS(self) -> int:
        return 100

    def _relative_rank(self, kata_rank: int) -> int:
        ranks: list[int] = [
            rank
            for rank in range(self.MIN_RANK, self.MAX_RANK + 1) if rank != 0
        ]
        return ranks.index(kata_rank) - ranks.index(self.rank)

    def inc_progress(self, rank: int) -> None:
        relative_rank: int = self._relative_rank(rank)
        if relative_rank <= -2:
            return
        if relative_rank == -1:
            increase: int = 1
        if relative_rank == 0:
            increase: int = 3
        if relative_rank > 0:
            increase: int = 10 * relative_rank * relative_rank
        new_total: int = self.progress + increase
        while new_total > self.MAX_PROGRESS:
            self.rank += 1
            new_total -= self.MAX_PROGRESS
        self._progress: int = new_total


if __name__ == "__main__":
    user: User = User()
    user.inc_progress(1)
    user.inc_progress(1)
    user.inc_progress(1)
    user.inc_progress(1)
    user.inc_progress(1)
    user.inc_progress(2)
    user.inc_progress(2)
    user.inc_progress(-1)
    print(user.rank, user.progress)
