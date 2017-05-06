from league_api.api import ApiType
from typing import List, Mapping



class ParticipantStats(ApiType):
    physicalDamageDealt: int = None
    neutralMinionsKilledTeamJungle: int = None
    magicDamageDealt: int = None
    totalPlayerScore: int = None
    deaths: int = None
    win: bool = None
    neutralMinionsKilledEnemyJungle: int = None
    altarsCaptured: int = None
    largestCriticalStrike: int = None
    totalDamageDealt: int = None
    magicDamageDealtToChampions: int = None
    visionWardsBoughtInGame: int = None
    damageDealtToObjectives: int = None
    largestKillingSpree: int = None
    item1: int = None
    quadraKills: int = None
    teamObjective: int = None
    totalTimeCrowdControlDealt: int = None
    longestTimeSpentLiving: int = None
    wardsKilled: int = None
    firstTowerAssist: bool = None
    firstTowerKill: bool = None
    item2: int = None
    item3: int = None
    item0: int = None
    firstBloodAssist: bool = None
    visionScore: int = None
    wardsPlaced: int = None
    item4: int = None
    item5: int = None
    item6: int = None
    turretKills: int = None
    tripleKills: int = None
    damageSelfMitigated: int = None
    champLevel: int = None
    nodeNeutralizeAssist: int = None
    firstInhibitorKill: bool = None
    goldEarned: int = None
    magicalDamageTaken: int = None
    kills: int = None
    doubleKills: int = None
    nodeCaptureAssist: int = None
    trueDamageTaken: int = None
    nodeNeutralize: int = None
    firstInhibitorAssist: bool = None
    assists: int = None
    unrealKills: int = None
    neutralMinionsKilled: int = None
    objectivePlayerScore: int = None
    combatPlayerScore: int = None
    damageDealtToTurrets: int = None
    altarsNeutralized: int = None
    physicalDamageDealtToChampions: int = None
    goldSpent: int = None
    trueDamageDealt: int = None
    trueDamageDealtToChampions: int = None
    participantId: int = None
    pentaKills: int = None
    totalHeal: int = None
    totalMinionsKilled: int = None
    firstBloodKill: bool = None
    nodeCapture: int = None
    largestMultiKill: int = None
    sightWardsBoughtInGame: int = None
    totalDamageDealtToChampions: int = None
    totalUnitsHealed: int = None
    inhibitorKills: int = None
    totalScoreRank: int = None
    totalDamageTaken: int = None
    killingSprees: int = None
    timeCCingOthers: int = None
    physicalDamageTaken: int = None

    @property
    def physical_damage_dealt(self):
        return self.physicalDamageDealt

    @physical_damage_dealt.setter
    def physical_damage_dealt(self, value):
        self.physicalDamageDealt = value

    @property
    def neutral_minions_killed_team_jungle(self):
        return self.neutralMinionsKilledTeamJungle

    @neutral_minions_killed_team_jungle.setter
    def neutral_minions_killed_team_jungle(self, value):
        self.neutralMinionsKilledTeamJungle = value

    @property
    def magic_damage_dealt(self):
        return self.magicDamageDealt

    @magic_damage_dealt.setter
    def magic_damage_dealt(self, value):
        self.magicDamageDealt = value

    @property
    def total_player_score(self):
        return self.totalPlayerScore

    @total_player_score.setter
    def total_player_score(self, value):
        self.totalPlayerScore = value

    @property
    def neutral_minions_killed_enemy_jungle(self):
        return self.neutralMinionsKilledEnemyJungle

    @neutral_minions_killed_enemy_jungle.setter
    def neutral_minions_killed_enemy_jungle(self, value):
        self.neutralMinionsKilledEnemyJungle = value

    @property
    def altars_captured(self):
        return self.altarsCaptured

    @altars_captured.setter
    def altars_captured(self, value):
        self.altarsCaptured = value

    @property
    def largest_critical_strike(self):
        return self.largestCriticalStrike

    @largest_critical_strike.setter
    def largest_critical_strike(self, value):
        self.largestCriticalStrike = value

    @property
    def total_damage_dealt(self):
        return self.totalDamageDealt

    @total_damage_dealt.setter
    def total_damage_dealt(self, value):
        self.totalDamageDealt = value

    @property
    def magic_damage_dealt_to_champions(self):
        return self.magicDamageDealtToChampions

    @magic_damage_dealt_to_champions.setter
    def magic_damage_dealt_to_champions(self, value):
        self.magicDamageDealtToChampions = value

    @property
    def vision_wards_bought_in_game(self):
        return self.visionWardsBoughtInGame

    @vision_wards_bought_in_game.setter
    def vision_wards_bought_in_game(self, value):
        self.visionWardsBoughtInGame = value

    @property
    def damage_dealt_to_objectives(self):
        return self.damageDealtToObjectives

    @damage_dealt_to_objectives.setter
    def damage_dealt_to_objectives(self, value):
        self.damageDealtToObjectives = value

    @property
    def largest_killing_spree(self):
        return self.largestKillingSpree

    @largest_killing_spree.setter
    def largest_killing_spree(self, value):
        self.largestKillingSpree = value

    @property
    def quadra_kills(self):
        return self.quadraKills

    @quadra_kills.setter
    def quadra_kills(self, value):
        self.quadraKills = value

    @property
    def team_objective(self):
        return self.teamObjective

    @team_objective.setter
    def team_objective(self, value):
        self.teamObjective = value

    @property
    def total_time_crowd_control_dealt(self):
        return self.totalTimeCrowdControlDealt

    @total_time_crowd_control_dealt.setter
    def total_time_crowd_control_dealt(self, value):
        self.totalTimeCrowdControlDealt = value

    @property
    def longest_time_spent_living(self):
        return self.longestTimeSpentLiving

    @longest_time_spent_living.setter
    def longest_time_spent_living(self, value):
        self.longestTimeSpentLiving = value

    @property
    def wards_killed(self):
        return self.wardsKilled

    @wards_killed.setter
    def wards_killed(self, value):
        self.wardsKilled = value

    @property
    def first_tower_assist(self):
        return self.firstTowerAssist

    @first_tower_assist.setter
    def first_tower_assist(self, value):
        self.firstTowerAssist = value

    @property
    def first_tower_kill(self):
        return self.firstTowerKill

    @first_tower_kill.setter
    def first_tower_kill(self, value):
        self.firstTowerKill = value

    @property
    def first_blood_assist(self):
        return self.firstBloodAssist

    @first_blood_assist.setter
    def first_blood_assist(self, value):
        self.firstBloodAssist = value

    @property
    def vision_score(self):
        return self.visionScore

    @vision_score.setter
    def vision_score(self, value):
        self.visionScore = value

    @property
    def wards_placed(self):
        return self.wardsPlaced

    @wards_placed.setter
    def wards_placed(self, value):
        self.wardsPlaced = value

    @property
    def turret_kills(self):
        return self.turretKills

    @turret_kills.setter
    def turret_kills(self, value):
        self.turretKills = value

    @property
    def triple_kills(self):
        return self.tripleKills

    @triple_kills.setter
    def triple_kills(self, value):
        self.tripleKills = value

    @property
    def damage_self_mitigated(self):
        return self.damageSelfMitigated

    @damage_self_mitigated.setter
    def damage_self_mitigated(self, value):
        self.damageSelfMitigated = value

    @property
    def champ_level(self):
        return self.champLevel

    @champ_level.setter
    def champ_level(self, value):
        self.champLevel = value

    @property
    def node_neutralize_assist(self):
        return self.nodeNeutralizeAssist

    @node_neutralize_assist.setter
    def node_neutralize_assist(self, value):
        self.nodeNeutralizeAssist = value

    @property
    def first_inhibitor_kill(self):
        return self.firstInhibitorKill

    @first_inhibitor_kill.setter
    def first_inhibitor_kill(self, value):
        self.firstInhibitorKill = value

    @property
    def gold_earned(self):
        return self.goldEarned

    @gold_earned.setter
    def gold_earned(self, value):
        self.goldEarned = value

    @property
    def magical_damage_taken(self):
        return self.magicalDamageTaken

    @magical_damage_taken.setter
    def magical_damage_taken(self, value):
        self.magicalDamageTaken = value

    @property
    def double_kills(self):
        return self.doubleKills

    @double_kills.setter
    def double_kills(self, value):
        self.doubleKills = value

    @property
    def node_capture_assist(self):
        return self.nodeCaptureAssist

    @node_capture_assist.setter
    def node_capture_assist(self, value):
        self.nodeCaptureAssist = value

    @property
    def true_damage_taken(self):
        return self.trueDamageTaken

    @true_damage_taken.setter
    def true_damage_taken(self, value):
        self.trueDamageTaken = value

    @property
    def node_neutralize(self):
        return self.nodeNeutralize

    @node_neutralize.setter
    def node_neutralize(self, value):
        self.nodeNeutralize = value

    @property
    def first_inhibitor_assist(self):
        return self.firstInhibitorAssist

    @first_inhibitor_assist.setter
    def first_inhibitor_assist(self, value):
        self.firstInhibitorAssist = value

    @property
    def unreal_kills(self):
        return self.unrealKills

    @unreal_kills.setter
    def unreal_kills(self, value):
        self.unrealKills = value

    @property
    def neutral_minions_killed(self):
        return self.neutralMinionsKilled

    @neutral_minions_killed.setter
    def neutral_minions_killed(self, value):
        self.neutralMinionsKilled = value

    @property
    def objective_player_score(self):
        return self.objectivePlayerScore

    @objective_player_score.setter
    def objective_player_score(self, value):
        self.objectivePlayerScore = value

    @property
    def combat_player_score(self):
        return self.combatPlayerScore

    @combat_player_score.setter
    def combat_player_score(self, value):
        self.combatPlayerScore = value

    @property
    def damage_dealt_to_turrets(self):
        return self.damageDealtToTurrets

    @damage_dealt_to_turrets.setter
    def damage_dealt_to_turrets(self, value):
        self.damageDealtToTurrets = value

    @property
    def altars_neutralized(self):
        return self.altarsNeutralized

    @altars_neutralized.setter
    def altars_neutralized(self, value):
        self.altarsNeutralized = value

    @property
    def physical_damage_dealt_to_champions(self):
        return self.physicalDamageDealtToChampions

    @physical_damage_dealt_to_champions.setter
    def physical_damage_dealt_to_champions(self, value):
        self.physicalDamageDealtToChampions = value

    @property
    def gold_spent(self):
        return self.goldSpent

    @gold_spent.setter
    def gold_spent(self, value):
        self.goldSpent = value

    @property
    def true_damage_dealt(self):
        return self.trueDamageDealt

    @true_damage_dealt.setter
    def true_damage_dealt(self, value):
        self.trueDamageDealt = value

    @property
    def true_damage_dealt_to_champions(self):
        return self.trueDamageDealtToChampions

    @true_damage_dealt_to_champions.setter
    def true_damage_dealt_to_champions(self, value):
        self.trueDamageDealtToChampions = value

    @property
    def participant_id(self):
        return self.participantId

    @participant_id.setter
    def participant_id(self, value):
        self.participantId = value

    @property
    def penta_kills(self):
        return self.pentaKills

    @penta_kills.setter
    def penta_kills(self, value):
        self.pentaKills = value

    @property
    def total_heal(self):
        return self.totalHeal

    @total_heal.setter
    def total_heal(self, value):
        self.totalHeal = value

    @property
    def total_minions_killed(self):
        return self.totalMinionsKilled

    @total_minions_killed.setter
    def total_minions_killed(self, value):
        self.totalMinionsKilled = value

    @property
    def first_blood_kill(self):
        return self.firstBloodKill

    @first_blood_kill.setter
    def first_blood_kill(self, value):
        self.firstBloodKill = value

    @property
    def node_capture(self):
        return self.nodeCapture

    @node_capture.setter
    def node_capture(self, value):
        self.nodeCapture = value

    @property
    def largest_multi_kill(self):
        return self.largestMultiKill

    @largest_multi_kill.setter
    def largest_multi_kill(self, value):
        self.largestMultiKill = value

    @property
    def sight_wards_bought_in_game(self):
        return self.sightWardsBoughtInGame

    @sight_wards_bought_in_game.setter
    def sight_wards_bought_in_game(self, value):
        self.sightWardsBoughtInGame = value

    @property
    def total_damage_dealt_to_champions(self):
        return self.totalDamageDealtToChampions

    @total_damage_dealt_to_champions.setter
    def total_damage_dealt_to_champions(self, value):
        self.totalDamageDealtToChampions = value

    @property
    def total_units_healed(self):
        return self.totalUnitsHealed

    @total_units_healed.setter
    def total_units_healed(self, value):
        self.totalUnitsHealed = value

    @property
    def inhibitor_kills(self):
        return self.inhibitorKills

    @inhibitor_kills.setter
    def inhibitor_kills(self, value):
        self.inhibitorKills = value

    @property
    def total_score_rank(self):
        return self.totalScoreRank

    @total_score_rank.setter
    def total_score_rank(self, value):
        self.totalScoreRank = value

    @property
    def total_damage_taken(self):
        return self.totalDamageTaken

    @total_damage_taken.setter
    def total_damage_taken(self, value):
        self.totalDamageTaken = value

    @property
    def killing_sprees(self):
        return self.killingSprees

    @killing_sprees.setter
    def killing_sprees(self, value):
        self.killingSprees = value

    @property
    def time_c_cing_others(self):
        return self.timeCCingOthers

    @time_c_cing_others.setter
    def time_c_cing_others(self, value):
        self.timeCCingOthers = value

    @property
    def physical_damage_taken(self):
        return self.physicalDamageTaken

    @physical_damage_taken.setter
    def physical_damage_taken(self, value):
        self.physicalDamageTaken = value

