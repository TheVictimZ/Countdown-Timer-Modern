from PySide6.QtCore import QObject, Signal

class Team(QObject):
    """
    Represents a single team with a name and score.
    """
    score_changed = Signal(int)
    name_changed = Signal(str)

    def __init__(self, name, start_score=0):
        super().__init__()
        self._name = name
        self._score = start_score

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        self._score = value
        self.score_changed.emit(self._score)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self._name != value:
            self._name = value
            self.name_changed.emit(self._name)

class TeamManager(QObject):
    """
    Manages the list of teams and global settings for adding/subtracting scores.
    """
    team_added = Signal(Team)
    team_removed = Signal(Team)
    default_increment_changed = Signal(int)

    def __init__(self):
        super().__init__()
        self.teams = []
        self._next_team_id = 1
        self._default_score_increment = 100
        self._default_initial_score = 0

    @property
    def default_score_increment(self):
        return self._default_score_increment

    @default_score_increment.setter
    def default_score_increment(self, value):
        self._default_score_increment = value
        self.default_increment_changed.emit(value)

    def add_team(self):
        name = f"Team {self._next_team_id}"
        self._next_team_id += 1
        new_team = Team(name, self._default_initial_score)
        self.teams.append(new_team)
        self.team_added.emit(new_team)
        return new_team

    def remove_team(self, team):
        if team in self.teams:
            self.teams.remove(team)
            self.team_removed.emit(team)

    def clear_teams(self):
        for team in list(self.teams):
            self.remove_team(team)
        self._next_team_id = 1
