from league_api.api import ApiType
from typing import List, Mapping



class ParticipantTimeline(ApiType):
    lane: str = None  # Participant's calculated lane. MID and BOT are legacy values.	             (Legal values:  MID,  MIDDLE,  TOP,  JUNGLE,  BOT,  BOTTOM)
    participantId: int = None
    csDiffPerMinDeltas: Mapping[str, float] = None  # Creep score difference versus the calculated lane opponent(s) for a specified period.
    goldPerMinDeltas: Mapping[str, float] = None  # Gold for a specified period.
    xpDiffPerMinDeltas: Mapping[str, float] = None  # Experience difference versus the calculated lane opponent(s) for a specified period.
    creepsPerMinDeltas: Mapping[str, float] = None  # Creeps for a specified period.
    xpPerMinDeltas: Mapping[str, float] = None  # Experience change for a specified period.
    role: str = None  # Participant's calculated role.	             (Legal values:  DUO,  NONE,  SOLO,  DUO_CARRY,  DUO_SUPPORT)
    damageTakenDiffPerMinDeltas: Mapping[str, float] = None  # Damage taken difference versus the calculated lane opponent(s) for a specified period.
    damageTakenPerMinDeltas: Mapping[str, float] = None  # Damage taken for a specified period.

    @property
    def participant_id(self):
        return self.participantId

    @participant_id.setter
    def participant_id(self, value):
        self.participantId = value

    @property
    def cs_diff_per_min_deltas(self):
        return self.csDiffPerMinDeltas

    @cs_diff_per_min_deltas.setter
    def cs_diff_per_min_deltas(self, value):
        self.csDiffPerMinDeltas = value

    @property
    def gold_per_min_deltas(self):
        return self.goldPerMinDeltas

    @gold_per_min_deltas.setter
    def gold_per_min_deltas(self, value):
        self.goldPerMinDeltas = value

    @property
    def xp_diff_per_min_deltas(self):
        return self.xpDiffPerMinDeltas

    @xp_diff_per_min_deltas.setter
    def xp_diff_per_min_deltas(self, value):
        self.xpDiffPerMinDeltas = value

    @property
    def creeps_per_min_deltas(self):
        return self.creepsPerMinDeltas

    @creeps_per_min_deltas.setter
    def creeps_per_min_deltas(self, value):
        self.creepsPerMinDeltas = value

    @property
    def xp_per_min_deltas(self):
        return self.xpPerMinDeltas

    @xp_per_min_deltas.setter
    def xp_per_min_deltas(self, value):
        self.xpPerMinDeltas = value

    @property
    def damage_taken_diff_per_min_deltas(self):
        return self.damageTakenDiffPerMinDeltas

    @damage_taken_diff_per_min_deltas.setter
    def damage_taken_diff_per_min_deltas(self, value):
        self.damageTakenDiffPerMinDeltas = value

    @property
    def damage_taken_per_min_deltas(self):
        return self.damageTakenPerMinDeltas

    @damage_taken_per_min_deltas.setter
    def damage_taken_per_min_deltas(self, value):
        self.damageTakenPerMinDeltas = value

