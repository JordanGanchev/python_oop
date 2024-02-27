from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        added_player = []
        for player in players:
            if player in self.players:
                continue
            self.players.append(player)
            added_player.append(player.name)
        return f'Successfully added: {", ".join(added_player)}'

    def add_supply(self, *supply: Supply):
        self.supplies.extend(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)
        if player is None:
            return
        if sustenance_type != 'Food' and sustenance_type != 'Drink':
            return
        index, supply = self.__find_supply_by_type(sustenance_type)
        if supply in None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."
        player.stamina = min(player.stamina + supply.energy, 100)
        self.supplies.pop(index)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        error_message = ''
        if first_player.stamina == 0:
            error_message += f"Player {first_player.name} does not have enough stamina."
        if second_player.stamina == 0:
            error_message += '\n' + f"Player {second_player.name} does not have enough stamina."
        if error_message:
            return error_message.strip()
        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player
        first_player_damage = first_player.stamina / 2
        second_player.stamina = max(second_player.stamina - first_player_damage, 0)

        if second_player.stamina == 0:
            return f"Winner: {first_player.name}"

        second_player_damage = second_player.stamina / 2
        first_player.stamina = max(first_player.stamina - second_player_damage, 0)
        if second_player.stamina == 0:
            return f"Winner: {second_player.name}"

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        pass

    def __str__(self):
        pass

    def __find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __find_supply_by_type(self, sustenance_type):
        for index in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[index]
            if supply.__class__.__name__ == sustenance_type:
                return (index, supply)
        return (-1, None)
