from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QScrollArea, QSpinBox, QLineEdit
)
from PySide6.QtCore import Qt
from app.core.team_logic import TeamManager, Team

class TeamCard(QWidget):
    def __init__(self, team: Team, manager: TeamManager, parent=None):
        super().__init__(parent)
        self.team = team
        self.manager = manager
        self.setObjectName("teamCard")
        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Team Name (Editable)
        self.name_input = QLineEdit(self.team.name)
        self.name_input.setObjectName("teamNameInputs")
        self.name_input.textChanged.connect(self.update_name_logic)
        layout.addWidget(self.name_input, stretch=1)
        
        # Score
        self.score_label = QLabel(str(self.team.score))
        self.score_label.setObjectName("teamScore")
        layout.addWidget(self.score_label)
        
        # Controls
        self.add_btn = QPushButton("+")
        self.add_btn.setFixedWidth(40)
        self.add_btn.clicked.connect(self.add_point)
        
        self.sub_btn = QPushButton("-")
        self.sub_btn.setFixedWidth(40)
        self.sub_btn.clicked.connect(self.sub_point)
        
        self.remove_btn = QPushButton("✕")
        self.remove_btn.setObjectName("stopButton") # Use red style
        self.remove_btn.setFixedWidth(40)
        self.remove_btn.clicked.connect(self.remove_self)
        
        layout.addWidget(self.sub_btn)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.remove_btn)

    def connect_signals(self):
        self.team.score_changed.connect(self.update_score)
        # Verify if external name changes (unlikely) need to reflect here
        pass

    def update_score(self, new_score):
        self.score_label.setText(str(new_score))

    def update_name_logic(self, new_name):
        self.team.name = new_name

    def add_point(self):
        self.team.score += self.manager.default_score_increment

    def sub_point(self):
        self.team.score -= self.manager.default_score_increment

    def remove_self(self):
        self.manager.remove_team(self.team)

class TeamWidget(QWidget):
    def __init__(self, team_manager: TeamManager):
        super().__init__()
        self.manager = team_manager
        self.cards = {} # Map team -> widget
        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Header / Controls
        header_layout = QHBoxLayout()
        header_label = QLabel("Teams")
        header_label.setObjectName("heading")
        header_layout.addWidget(header_label)
        
        self.add_team_btn = QPushButton("Add Team")
        self.add_team_btn.setObjectName("actionButton")
        self.add_team_btn.clicked.connect(self.manager.add_team)
        header_layout.addWidget(self.add_team_btn)
        
        layout.addLayout(header_layout)
        
        # Global Settings
        settings_layout = QHBoxLayout()
        settings_layout.addWidget(QLabel("Default Increment:"))
        self.inc_spin = QSpinBox()
        self.inc_spin.setRange(1, 10000)
        self.inc_spin.setValue(self.manager.default_score_increment)
        self.inc_spin.valueChanged.connect(self.update_increment)
        settings_layout.addWidget(self.inc_spin)
        settings_layout.addStretch()
        layout.addLayout(settings_layout)
        
        # Scroll Area for Teams
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        
        self.scroll_area.setWidget(self.scroll_content)
        layout.addWidget(self.scroll_area)

    def connect_signals(self):
        self.manager.team_added.connect(self.add_team_card)
        self.manager.team_removed.connect(self.remove_team_card)

    def update_increment(self, val):
        self.manager.default_score_increment = val

    def add_team_card(self, team):
        card = TeamCard(team, self.manager)
        self.scroll_layout.addWidget(card)
        self.cards[team] = card

    def remove_team_card(self, team):
        if team in self.cards:
            widget = self.cards.pop(team)
            self.scroll_layout.removeWidget(widget)
            widget.deleteLater()
