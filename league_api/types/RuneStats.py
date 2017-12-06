from league_api.api import ApiType
from typing import List, Mapping



class RuneStats(ApiType):
    PercentTimeDeadModPerLevel: float = None
    PercentArmorPenetrationModPerLevel: float = None
    PercentCritDamageMod: float = None
    PercentSpellBlockMod: float = None
    PercentHPRegenMod: float = None
    PercentMovementSpeedMod: float = None
    FlatSpellBlockMod: float = None
    FlatEnergyRegenModPerLevel: float = None
    FlatEnergyPoolMod: float = None
    FlatMagicPenetrationModPerLevel: float = None
    PercentLifeStealMod: float = None
    FlatMPPoolMod: float = None
    PercentCooldownMod: float = None
    PercentMagicPenetrationMod: float = None
    FlatArmorPenetrationModPerLevel: float = None
    FlatMovementSpeedMod: float = None
    FlatTimeDeadModPerLevel: float = None
    FlatArmorModPerLevel: float = None
    PercentAttackSpeedMod: float = None
    FlatDodgeModPerLevel: float = None
    PercentMagicDamageMod: float = None
    PercentBlockMod: float = None
    FlatDodgeMod: float = None
    FlatEnergyRegenMod: float = None
    FlatHPModPerLevel: float = None
    PercentAttackSpeedModPerLevel: float = None
    PercentSpellVampMod: float = None
    FlatMPRegenMod: float = None
    PercentHPPoolMod: float = None
    PercentDodgeMod: float = None
    FlatAttackSpeedMod: float = None
    FlatArmorMod: float = None
    FlatMagicDamageModPerLevel: float = None
    FlatHPRegenMod: float = None
    PercentPhysicalDamageMod: float = None
    FlatCritChanceModPerLevel: float = None
    FlatSpellBlockModPerLevel: float = None
    PercentTimeDeadMod: float = None
    FlatBlockMod: float = None
    PercentMPPoolMod: float = None
    FlatMagicDamageMod: float = None
    PercentMPRegenMod: float = None
    PercentMovementSpeedModPerLevel: float = None
    PercentCooldownModPerLevel: float = None
    FlatMPModPerLevel: float = None
    FlatEnergyModPerLevel: float = None
    FlatPhysicalDamageMod: float = None
    FlatHPRegenModPerLevel: float = None
    FlatCritDamageMod: float = None
    PercentArmorMod: float = None
    FlatMagicPenetrationMod: float = None
    PercentCritChanceMod: float = None
    FlatPhysicalDamageModPerLevel: float = None
    PercentArmorPenetrationMod: float = None
    PercentEXPBonus: float = None
    FlatMPRegenModPerLevel: float = None
    PercentMagicPenetrationModPerLevel: float = None
    FlatTimeDeadMod: float = None
    FlatMovementSpeedModPerLevel: float = None
    FlatGoldPer10Mod: float = None
    FlatArmorPenetrationMod: float = None
    FlatCritDamageModPerLevel: float = None
    FlatHPPoolMod: float = None
    FlatCritChanceMod: float = None
    FlatEXPBonus: float = None

    @property
    def percent_time_dead_mod_per_level(self):
        return self.PercentTimeDeadModPerLevel

    @percent_time_dead_mod_per_level.setter
    def percent_time_dead_mod_per_level(self, value):
        self.PercentTimeDeadModPerLevel = value

    @property
    def percent_armor_penetration_mod_per_level(self):
        return self.PercentArmorPenetrationModPerLevel

    @percent_armor_penetration_mod_per_level.setter
    def percent_armor_penetration_mod_per_level(self, value):
        self.PercentArmorPenetrationModPerLevel = value

    @property
    def percent_crit_damage_mod(self):
        return self.PercentCritDamageMod

    @percent_crit_damage_mod.setter
    def percent_crit_damage_mod(self, value):
        self.PercentCritDamageMod = value

    @property
    def percent_spell_block_mod(self):
        return self.PercentSpellBlockMod

    @percent_spell_block_mod.setter
    def percent_spell_block_mod(self, value):
        self.PercentSpellBlockMod = value

    @property
    def percent_hp_regen_mod(self):
        return self.PercentHPRegenMod

    @percent_hp_regen_mod.setter
    def percent_hp_regen_mod(self, value):
        self.PercentHPRegenMod = value

    @property
    def percent_movement_speed_mod(self):
        return self.PercentMovementSpeedMod

    @percent_movement_speed_mod.setter
    def percent_movement_speed_mod(self, value):
        self.PercentMovementSpeedMod = value

    @property
    def flat_spell_block_mod(self):
        return self.FlatSpellBlockMod

    @flat_spell_block_mod.setter
    def flat_spell_block_mod(self, value):
        self.FlatSpellBlockMod = value

    @property
    def flat_energy_regen_mod_per_level(self):
        return self.FlatEnergyRegenModPerLevel

    @flat_energy_regen_mod_per_level.setter
    def flat_energy_regen_mod_per_level(self, value):
        self.FlatEnergyRegenModPerLevel = value

    @property
    def flat_energy_pool_mod(self):
        return self.FlatEnergyPoolMod

    @flat_energy_pool_mod.setter
    def flat_energy_pool_mod(self, value):
        self.FlatEnergyPoolMod = value

    @property
    def flat_magic_penetration_mod_per_level(self):
        return self.FlatMagicPenetrationModPerLevel

    @flat_magic_penetration_mod_per_level.setter
    def flat_magic_penetration_mod_per_level(self, value):
        self.FlatMagicPenetrationModPerLevel = value

    @property
    def percent_life_steal_mod(self):
        return self.PercentLifeStealMod

    @percent_life_steal_mod.setter
    def percent_life_steal_mod(self, value):
        self.PercentLifeStealMod = value

    @property
    def flat_mp_pool_mod(self):
        return self.FlatMPPoolMod

    @flat_mp_pool_mod.setter
    def flat_mp_pool_mod(self, value):
        self.FlatMPPoolMod = value

    @property
    def percent_cooldown_mod(self):
        return self.PercentCooldownMod

    @percent_cooldown_mod.setter
    def percent_cooldown_mod(self, value):
        self.PercentCooldownMod = value

    @property
    def percent_magic_penetration_mod(self):
        return self.PercentMagicPenetrationMod

    @percent_magic_penetration_mod.setter
    def percent_magic_penetration_mod(self, value):
        self.PercentMagicPenetrationMod = value

    @property
    def flat_armor_penetration_mod_per_level(self):
        return self.FlatArmorPenetrationModPerLevel

    @flat_armor_penetration_mod_per_level.setter
    def flat_armor_penetration_mod_per_level(self, value):
        self.FlatArmorPenetrationModPerLevel = value

    @property
    def flat_movement_speed_mod(self):
        return self.FlatMovementSpeedMod

    @flat_movement_speed_mod.setter
    def flat_movement_speed_mod(self, value):
        self.FlatMovementSpeedMod = value

    @property
    def flat_time_dead_mod_per_level(self):
        return self.FlatTimeDeadModPerLevel

    @flat_time_dead_mod_per_level.setter
    def flat_time_dead_mod_per_level(self, value):
        self.FlatTimeDeadModPerLevel = value

    @property
    def flat_armor_mod_per_level(self):
        return self.FlatArmorModPerLevel

    @flat_armor_mod_per_level.setter
    def flat_armor_mod_per_level(self, value):
        self.FlatArmorModPerLevel = value

    @property
    def percent_attack_speed_mod(self):
        return self.PercentAttackSpeedMod

    @percent_attack_speed_mod.setter
    def percent_attack_speed_mod(self, value):
        self.PercentAttackSpeedMod = value

    @property
    def flat_dodge_mod_per_level(self):
        return self.FlatDodgeModPerLevel

    @flat_dodge_mod_per_level.setter
    def flat_dodge_mod_per_level(self, value):
        self.FlatDodgeModPerLevel = value

    @property
    def percent_magic_damage_mod(self):
        return self.PercentMagicDamageMod

    @percent_magic_damage_mod.setter
    def percent_magic_damage_mod(self, value):
        self.PercentMagicDamageMod = value

    @property
    def percent_block_mod(self):
        return self.PercentBlockMod

    @percent_block_mod.setter
    def percent_block_mod(self, value):
        self.PercentBlockMod = value

    @property
    def flat_dodge_mod(self):
        return self.FlatDodgeMod

    @flat_dodge_mod.setter
    def flat_dodge_mod(self, value):
        self.FlatDodgeMod = value

    @property
    def flat_energy_regen_mod(self):
        return self.FlatEnergyRegenMod

    @flat_energy_regen_mod.setter
    def flat_energy_regen_mod(self, value):
        self.FlatEnergyRegenMod = value

    @property
    def flat_hp_mod_per_level(self):
        return self.FlatHPModPerLevel

    @flat_hp_mod_per_level.setter
    def flat_hp_mod_per_level(self, value):
        self.FlatHPModPerLevel = value

    @property
    def percent_attack_speed_mod_per_level(self):
        return self.PercentAttackSpeedModPerLevel

    @percent_attack_speed_mod_per_level.setter
    def percent_attack_speed_mod_per_level(self, value):
        self.PercentAttackSpeedModPerLevel = value

    @property
    def percent_spell_vamp_mod(self):
        return self.PercentSpellVampMod

    @percent_spell_vamp_mod.setter
    def percent_spell_vamp_mod(self, value):
        self.PercentSpellVampMod = value

    @property
    def flat_mp_regen_mod(self):
        return self.FlatMPRegenMod

    @flat_mp_regen_mod.setter
    def flat_mp_regen_mod(self, value):
        self.FlatMPRegenMod = value

    @property
    def percent_hp_pool_mod(self):
        return self.PercentHPPoolMod

    @percent_hp_pool_mod.setter
    def percent_hp_pool_mod(self, value):
        self.PercentHPPoolMod = value

    @property
    def percent_dodge_mod(self):
        return self.PercentDodgeMod

    @percent_dodge_mod.setter
    def percent_dodge_mod(self, value):
        self.PercentDodgeMod = value

    @property
    def flat_attack_speed_mod(self):
        return self.FlatAttackSpeedMod

    @flat_attack_speed_mod.setter
    def flat_attack_speed_mod(self, value):
        self.FlatAttackSpeedMod = value

    @property
    def flat_armor_mod(self):
        return self.FlatArmorMod

    @flat_armor_mod.setter
    def flat_armor_mod(self, value):
        self.FlatArmorMod = value

    @property
    def flat_magic_damage_mod_per_level(self):
        return self.FlatMagicDamageModPerLevel

    @flat_magic_damage_mod_per_level.setter
    def flat_magic_damage_mod_per_level(self, value):
        self.FlatMagicDamageModPerLevel = value

    @property
    def flat_hp_regen_mod(self):
        return self.FlatHPRegenMod

    @flat_hp_regen_mod.setter
    def flat_hp_regen_mod(self, value):
        self.FlatHPRegenMod = value

    @property
    def percent_physical_damage_mod(self):
        return self.PercentPhysicalDamageMod

    @percent_physical_damage_mod.setter
    def percent_physical_damage_mod(self, value):
        self.PercentPhysicalDamageMod = value

    @property
    def flat_crit_chance_mod_per_level(self):
        return self.FlatCritChanceModPerLevel

    @flat_crit_chance_mod_per_level.setter
    def flat_crit_chance_mod_per_level(self, value):
        self.FlatCritChanceModPerLevel = value

    @property
    def flat_spell_block_mod_per_level(self):
        return self.FlatSpellBlockModPerLevel

    @flat_spell_block_mod_per_level.setter
    def flat_spell_block_mod_per_level(self, value):
        self.FlatSpellBlockModPerLevel = value

    @property
    def percent_time_dead_mod(self):
        return self.PercentTimeDeadMod

    @percent_time_dead_mod.setter
    def percent_time_dead_mod(self, value):
        self.PercentTimeDeadMod = value

    @property
    def flat_block_mod(self):
        return self.FlatBlockMod

    @flat_block_mod.setter
    def flat_block_mod(self, value):
        self.FlatBlockMod = value

    @property
    def percent_mp_pool_mod(self):
        return self.PercentMPPoolMod

    @percent_mp_pool_mod.setter
    def percent_mp_pool_mod(self, value):
        self.PercentMPPoolMod = value

    @property
    def flat_magic_damage_mod(self):
        return self.FlatMagicDamageMod

    @flat_magic_damage_mod.setter
    def flat_magic_damage_mod(self, value):
        self.FlatMagicDamageMod = value

    @property
    def percent_mp_regen_mod(self):
        return self.PercentMPRegenMod

    @percent_mp_regen_mod.setter
    def percent_mp_regen_mod(self, value):
        self.PercentMPRegenMod = value

    @property
    def percent_movement_speed_mod_per_level(self):
        return self.PercentMovementSpeedModPerLevel

    @percent_movement_speed_mod_per_level.setter
    def percent_movement_speed_mod_per_level(self, value):
        self.PercentMovementSpeedModPerLevel = value

    @property
    def percent_cooldown_mod_per_level(self):
        return self.PercentCooldownModPerLevel

    @percent_cooldown_mod_per_level.setter
    def percent_cooldown_mod_per_level(self, value):
        self.PercentCooldownModPerLevel = value

    @property
    def flat_mp_mod_per_level(self):
        return self.FlatMPModPerLevel

    @flat_mp_mod_per_level.setter
    def flat_mp_mod_per_level(self, value):
        self.FlatMPModPerLevel = value

    @property
    def flat_energy_mod_per_level(self):
        return self.FlatEnergyModPerLevel

    @flat_energy_mod_per_level.setter
    def flat_energy_mod_per_level(self, value):
        self.FlatEnergyModPerLevel = value

    @property
    def flat_physical_damage_mod(self):
        return self.FlatPhysicalDamageMod

    @flat_physical_damage_mod.setter
    def flat_physical_damage_mod(self, value):
        self.FlatPhysicalDamageMod = value

    @property
    def flat_hp_regen_mod_per_level(self):
        return self.FlatHPRegenModPerLevel

    @flat_hp_regen_mod_per_level.setter
    def flat_hp_regen_mod_per_level(self, value):
        self.FlatHPRegenModPerLevel = value

    @property
    def flat_crit_damage_mod(self):
        return self.FlatCritDamageMod

    @flat_crit_damage_mod.setter
    def flat_crit_damage_mod(self, value):
        self.FlatCritDamageMod = value

    @property
    def percent_armor_mod(self):
        return self.PercentArmorMod

    @percent_armor_mod.setter
    def percent_armor_mod(self, value):
        self.PercentArmorMod = value

    @property
    def flat_magic_penetration_mod(self):
        return self.FlatMagicPenetrationMod

    @flat_magic_penetration_mod.setter
    def flat_magic_penetration_mod(self, value):
        self.FlatMagicPenetrationMod = value

    @property
    def percent_crit_chance_mod(self):
        return self.PercentCritChanceMod

    @percent_crit_chance_mod.setter
    def percent_crit_chance_mod(self, value):
        self.PercentCritChanceMod = value

    @property
    def flat_physical_damage_mod_per_level(self):
        return self.FlatPhysicalDamageModPerLevel

    @flat_physical_damage_mod_per_level.setter
    def flat_physical_damage_mod_per_level(self, value):
        self.FlatPhysicalDamageModPerLevel = value

    @property
    def percent_armor_penetration_mod(self):
        return self.PercentArmorPenetrationMod

    @percent_armor_penetration_mod.setter
    def percent_armor_penetration_mod(self, value):
        self.PercentArmorPenetrationMod = value

    @property
    def percent_exp_bonus(self):
        return self.PercentEXPBonus

    @percent_exp_bonus.setter
    def percent_exp_bonus(self, value):
        self.PercentEXPBonus = value

    @property
    def flat_mp_regen_mod_per_level(self):
        return self.FlatMPRegenModPerLevel

    @flat_mp_regen_mod_per_level.setter
    def flat_mp_regen_mod_per_level(self, value):
        self.FlatMPRegenModPerLevel = value

    @property
    def percent_magic_penetration_mod_per_level(self):
        return self.PercentMagicPenetrationModPerLevel

    @percent_magic_penetration_mod_per_level.setter
    def percent_magic_penetration_mod_per_level(self, value):
        self.PercentMagicPenetrationModPerLevel = value

    @property
    def flat_time_dead_mod(self):
        return self.FlatTimeDeadMod

    @flat_time_dead_mod.setter
    def flat_time_dead_mod(self, value):
        self.FlatTimeDeadMod = value

    @property
    def flat_movement_speed_mod_per_level(self):
        return self.FlatMovementSpeedModPerLevel

    @flat_movement_speed_mod_per_level.setter
    def flat_movement_speed_mod_per_level(self, value):
        self.FlatMovementSpeedModPerLevel = value

    @property
    def flat_gold_per10_mod(self):
        return self.FlatGoldPer10Mod

    @flat_gold_per10_mod.setter
    def flat_gold_per10_mod(self, value):
        self.FlatGoldPer10Mod = value

    @property
    def flat_armor_penetration_mod(self):
        return self.FlatArmorPenetrationMod

    @flat_armor_penetration_mod.setter
    def flat_armor_penetration_mod(self, value):
        self.FlatArmorPenetrationMod = value

    @property
    def flat_crit_damage_mod_per_level(self):
        return self.FlatCritDamageModPerLevel

    @flat_crit_damage_mod_per_level.setter
    def flat_crit_damage_mod_per_level(self, value):
        self.FlatCritDamageModPerLevel = value

    @property
    def flat_hp_pool_mod(self):
        return self.FlatHPPoolMod

    @flat_hp_pool_mod.setter
    def flat_hp_pool_mod(self, value):
        self.FlatHPPoolMod = value

    @property
    def flat_crit_chance_mod(self):
        return self.FlatCritChanceMod

    @flat_crit_chance_mod.setter
    def flat_crit_chance_mod(self, value):
        self.FlatCritChanceMod = value

    @property
    def flat_exp_bonus(self):
        return self.FlatEXPBonus

    @flat_exp_bonus.setter
    def flat_exp_bonus(self, value):
        self.FlatEXPBonus = value

