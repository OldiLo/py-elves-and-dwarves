from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(
    players: list[DwarfBlacksmith | DwarfWarrior | Druid | ElfRanger],
) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(players: list[Druid | ElfRanger]) -> None:
    [player.play_elf_song() for player in players]


def feast_of_the_dwarves(
    players: list[DwarfBlacksmith | DwarfWarrior],
) -> None:
    [player.eat_favourite_dish() for player in players]
