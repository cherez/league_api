from league_api.api import ApiType
from typing import List, Mapping



class ParticipantTimeline(ApiType):
    lane: str = None
    participantId: int = None
    csDiffPerMinDeltas: Mapping[str, float] = None
    goldPerMinDeltas: Mapping[str, float] = None
    xpDiffPerMinDeltas: Mapping[str, float] = None
    creepsPerMinDeltas: Mapping[str, float] = None
    xpPerMinDeltas: Mapping[str, float] = None
    role: str = None
    damageTakenDiffPerMinDeltas: Mapping[str, float] = None
    damageTakenPerMinDeltas: Mapping[str, float] = None

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

