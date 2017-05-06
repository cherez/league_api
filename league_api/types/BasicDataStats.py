from league_api.api import ApiType
from typing import List, Mapping



class BasicDataStats(ApiType):
    rPercentMagicPenetrationModPerLevel: float = None
    rFlatEnergyModPerLevel: float = None
    PercentMagicDamageMod: float = None
    PercentCritDamageMod: float = None
    PercentSpellBlockMod: float = None
    PercentHPRegenMod: float = None
    PercentMovementSpeedMod: float = None
    FlatSpellBlockMod: float = None
    PercentHPPoolMod: float = None
    FlatEnergyPoolMod: float = None
    rFlatDodgeMod: float = None
    PercentLifeStealMod: float = None
    rFlatMPRegenModPerLevel: float = None
    FlatMPPoolMod: float = None
    rFlatGoldPer10Mod: float = None
    FlatMovementSpeedMod: float = None
    rPercentCooldownMod: float = None
    rFlatMPModPerLevel: float = None
    rPercentCooldownModPerLevel: float = None
    PercentAttackSpeedMod: float = None
    rPercentMagicPenetrationMod: float = None
    PercentBlockMod: float = None
    rFlatTimeDeadModPerLevel: float = None
    FlatEnergyRegenMod: float = None
    rPercentAttackSpeedModPerLevel: float = None
    PercentSpellVampMod: float = None
    FlatMPRegenMod: float = None
    rFlatTimeDeadMod: float = None
    rFlatMagicDamageModPerLevel: float = None
    FlatAttackSpeedMod: float = None
    rFlatMagicPenetrationMod: float = None
    rFlatCritChanceModPerLevel: float = None
    PercentMPRegenMod: float = None
    PercentDodgeMod: float = None
    rFlatHPModPerLevel: float = None
    PercentPhysicalDamageMod: float = None
    rFlatDodgeModPerLevel: float = None
    rPercentMovementSpeedModPerLevel: float = None
    rFlatSpellBlockModPerLevel: float = None
    FlatBlockMod: float = None
    PercentMPPoolMod: float = None
    FlatMagicDamageMod: float = None
    rFlatMagicPenetrationModPerLevel: float = None
    FlatHPRegenMod: float = None
    rFlatPhysicalDamageModPerLevel: float = None
    rFlatEnergyRegenModPerLevel: float = None
    FlatPhysicalDamageMod: float = None
    rPercentTimeDeadMod: float = None
    FlatCritDamageMod: float = None
    rFlatArmorPenetrationMod: float = None
    PercentArmorMod: float = None
    PercentCritChanceMod: float = None
    rFlatArmorPenetrationModPerLevel: float = None
    rFlatArmorModPerLevel: float = None
    rFlatHPRegenModPerLevel: float = None
    rPercentTimeDeadModPerLevel: float = None
    PercentEXPBonus: float = None
    rFlatCritDamageModPerLevel: float = None
    rFlatMovementSpeedModPerLevel: float = None
    rPercentArmorPenetrationMod: float = None
    rPercentArmorPenetrationModPerLevel: float = None
    FlatEXPBonus: float = None
    FlatHPPoolMod: float = None
    FlatCritChanceMod: float = None
    FlatArmorMod: float = None

    @property
    def r_percent_magic_penetration_mod_per_level(self):
        return self.rPercentMagicPenetrationModPerLevel

    @r_percent_magic_penetration_mod_per_level.setter
    def r_percent_magic_penetration_mod_per_level(self, value):
        self.rPercentMagicPenetrationModPerLevel = value

    @property
    def r_flat_energy_mod_per_level(self):
        return self.rFlatEnergyModPerLevel

    @r_flat_energy_mod_per_level.setter
    def r_flat_energy_mod_per_level(self, value):
        self.rFlatEnergyModPerLevel = value

    @property
    def percent_magic_damage_mod(self):
        return self.PercentMagicDamageMod

    @percent_magic_damage_mod.setter
    def percent_magic_damage_mod(self, value):
        self.PercentMagicDamageMod = value

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
    def percent_hp_pool_mod(self):
        return self.PercentHPPoolMod

    @percent_hp_pool_mod.setter
    def percent_hp_pool_mod(self, value):
        self.PercentHPPoolMod = value

    @property
    def flat_energy_pool_mod(self):
        return self.FlatEnergyPoolMod

    @flat_energy_pool_mod.setter
    def flat_energy_pool_mod(self, value):
        self.FlatEnergyPoolMod = value

    @property
    def r_flat_dodge_mod(self):
        return self.rFlatDodgeMod

    @r_flat_dodge_mod.setter
    def r_flat_dodge_mod(self, value):
        self.rFlatDodgeMod = value

    @property
    def percent_life_steal_mod(self):
        return self.PercentLifeStealMod

    @percent_life_steal_mod.setter
    def percent_life_steal_mod(self, value):
        self.PercentLifeStealMod = value

    @property
    def r_flat_mp_regen_mod_per_level(self):
        return self.rFlatMPRegenModPerLevel

    @r_flat_mp_regen_mod_per_level.setter
    def r_flat_mp_regen_mod_per_level(self, value):
        self.rFlatMPRegenModPerLevel = value

    @property
    def flat_mp_pool_mod(self):
        return self.FlatMPPoolMod

    @flat_mp_pool_mod.setter
    def flat_mp_pool_mod(self, value):
        self.FlatMPPoolMod = value

    @property
    def r_flat_gold_per10_mod(self):
        return self.rFlatGoldPer10Mod

    @r_flat_gold_per10_mod.setter
    def r_flat_gold_per10_mod(self, value):
        self.rFlatGoldPer10Mod = value

    @property
    def flat_movement_speed_mod(self):
        return self.FlatMovementSpeedMod

    @flat_movement_speed_mod.setter
    def flat_movement_speed_mod(self, value):
        self.FlatMovementSpeedMod = value

    @property
    def r_percent_cooldown_mod(self):
        return self.rPercentCooldownMod

    @r_percent_cooldown_mod.setter
    def r_percent_cooldown_mod(self, value):
        self.rPercentCooldownMod = value

    @property
    def r_flat_mp_mod_per_level(self):
        return self.rFlatMPModPerLevel

    @r_flat_mp_mod_per_level.setter
    def r_flat_mp_mod_per_level(self, value):
        self.rFlatMPModPerLevel = value

    @property
    def r_percent_cooldown_mod_per_level(self):
        return self.rPercentCooldownModPerLevel

    @r_percent_cooldown_mod_per_level.setter
    def r_percent_cooldown_mod_per_level(self, value):
        self.rPercentCooldownModPerLevel = value

    @property
    def percent_attack_speed_mod(self):
        return self.PercentAttackSpeedMod

    @percent_attack_speed_mod.setter
    def percent_attack_speed_mod(self, value):
        self.PercentAttackSpeedMod = value

    @property
    def r_percent_magic_penetration_mod(self):
        return self.rPercentMagicPenetrationMod

    @r_percent_magic_penetration_mod.setter
    def r_percent_magic_penetration_mod(self, value):
        self.rPercentMagicPenetrationMod = value

    @property
    def percent_block_mod(self):
        return self.PercentBlockMod

    @percent_block_mod.setter
    def percent_block_mod(self, value):
        self.PercentBlockMod = value

    @property
    def r_flat_time_dead_mod_per_level(self):
        return self.rFlatTimeDeadModPerLevel

    @r_flat_time_dead_mod_per_level.setter
    def r_flat_time_dead_mod_per_level(self, value):
        self.rFlatTimeDeadModPerLevel = value

    @property
    def flat_energy_regen_mod(self):
        return self.FlatEnergyRegenMod

    @flat_energy_regen_mod.setter
    def flat_energy_regen_mod(self, value):
        self.FlatEnergyRegenMod = value

    @property
    def r_percent_attack_speed_mod_per_level(self):
        return self.rPercentAttackSpeedModPerLevel

    @r_percent_attack_speed_mod_per_level.setter
    def r_percent_attack_speed_mod_per_level(self, value):
        self.rPercentAttackSpeedModPerLevel = value

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
    def r_flat_time_dead_mod(self):
        return self.rFlatTimeDeadMod

    @r_flat_time_dead_mod.setter
    def r_flat_time_dead_mod(self, value):
        self.rFlatTimeDeadMod = value

    @property
    def r_flat_magic_damage_mod_per_level(self):
        return self.rFlatMagicDamageModPerLevel

    @r_flat_magic_damage_mod_per_level.setter
    def r_flat_magic_damage_mod_per_level(self, value):
        self.rFlatMagicDamageModPerLevel = value

    @property
    def flat_attack_speed_mod(self):
        return self.FlatAttackSpeedMod

    @flat_attack_speed_mod.setter
    def flat_attack_speed_mod(self, value):
        self.FlatAttackSpeedMod = value

    @property
    def r_flat_magic_penetration_mod(self):
        return self.rFlatMagicPenetrationMod

    @r_flat_magic_penetration_mod.setter
    def r_flat_magic_penetration_mod(self, value):
        self.rFlatMagicPenetrationMod = value

    @property
    def r_flat_crit_chance_mod_per_level(self):
        return self.rFlatCritChanceModPerLevel

    @r_flat_crit_chance_mod_per_level.setter
    def r_flat_crit_chance_mod_per_level(self, value):
        self.rFlatCritChanceModPerLevel = value

    @property
    def percent_mp_regen_mod(self):
        return self.PercentMPRegenMod

    @percent_mp_regen_mod.setter
    def percent_mp_regen_mod(self, value):
        self.PercentMPRegenMod = value

    @property
    def percent_dodge_mod(self):
        return self.PercentDodgeMod

    @percent_dodge_mod.setter
    def percent_dodge_mod(self, value):
        self.PercentDodgeMod = value

    @property
    def r_flat_hp_mod_per_level(self):
        return self.rFlatHPModPerLevel

    @r_flat_hp_mod_per_level.setter
    def r_flat_hp_mod_per_level(self, value):
        self.rFlatHPModPerLevel = value

    @property
    def percent_physical_damage_mod(self):
        return self.PercentPhysicalDamageMod

    @percent_physical_damage_mod.setter
    def percent_physical_damage_mod(self, value):
        self.PercentPhysicalDamageMod = value

    @property
    def r_flat_dodge_mod_per_level(self):
        return self.rFlatDodgeModPerLevel

    @r_flat_dodge_mod_per_level.setter
    def r_flat_dodge_mod_per_level(self, value):
        self.rFlatDodgeModPerLevel = value

    @property
    def r_percent_movement_speed_mod_per_level(self):
        return self.rPercentMovementSpeedModPerLevel

    @r_percent_movement_speed_mod_per_level.setter
    def r_percent_movement_speed_mod_per_level(self, value):
        self.rPercentMovementSpeedModPerLevel = value

    @property
    def r_flat_spell_block_mod_per_level(self):
        return self.rFlatSpellBlockModPerLevel

    @r_flat_spell_block_mod_per_level.setter
    def r_flat_spell_block_mod_per_level(self, value):
        self.rFlatSpellBlockModPerLevel = value

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
    def r_flat_magic_penetration_mod_per_level(self):
        return self.rFlatMagicPenetrationModPerLevel

    @r_flat_magic_penetration_mod_per_level.setter
    def r_flat_magic_penetration_mod_per_level(self, value):
        self.rFlatMagicPenetrationModPerLevel = value

    @property
    def flat_hp_regen_mod(self):
        return self.FlatHPRegenMod

    @flat_hp_regen_mod.setter
    def flat_hp_regen_mod(self, value):
        self.FlatHPRegenMod = value

    @property
    def r_flat_physical_damage_mod_per_level(self):
        return self.rFlatPhysicalDamageModPerLevel

    @r_flat_physical_damage_mod_per_level.setter
    def r_flat_physical_damage_mod_per_level(self, value):
        self.rFlatPhysicalDamageModPerLevel = value

    @property
    def r_flat_energy_regen_mod_per_level(self):
        return self.rFlatEnergyRegenModPerLevel

    @r_flat_energy_regen_mod_per_level.setter
    def r_flat_energy_regen_mod_per_level(self, value):
        self.rFlatEnergyRegenModPerLevel = value

    @property
    def flat_physical_damage_mod(self):
        return self.FlatPhysicalDamageMod

    @flat_physical_damage_mod.setter
    def flat_physical_damage_mod(self, value):
        self.FlatPhysicalDamageMod = value

    @property
    def r_percent_time_dead_mod(self):
        return self.rPercentTimeDeadMod

    @r_percent_time_dead_mod.setter
    def r_percent_time_dead_mod(self, value):
        self.rPercentTimeDeadMod = value

    @property
    def flat_crit_damage_mod(self):
        return self.FlatCritDamageMod

    @flat_crit_damage_mod.setter
    def flat_crit_damage_mod(self, value):
        self.FlatCritDamageMod = value

    @property
    def r_flat_armor_penetration_mod(self):
        return self.rFlatArmorPenetrationMod

    @r_flat_armor_penetration_mod.setter
    def r_flat_armor_penetration_mod(self, value):
        self.rFlatArmorPenetrationMod = value

    @property
    def percent_armor_mod(self):
        return self.PercentArmorMod

    @percent_armor_mod.setter
    def percent_armor_mod(self, value):
        self.PercentArmorMod = value

    @property
    def percent_crit_chance_mod(self):
        return self.PercentCritChanceMod

    @percent_crit_chance_mod.setter
    def percent_crit_chance_mod(self, value):
        self.PercentCritChanceMod = value

    @property
    def r_flat_armor_penetration_mod_per_level(self):
        return self.rFlatArmorPenetrationModPerLevel

    @r_flat_armor_penetration_mod_per_level.setter
    def r_flat_armor_penetration_mod_per_level(self, value):
        self.rFlatArmorPenetrationModPerLevel = value

    @property
    def r_flat_armor_mod_per_level(self):
        return self.rFlatArmorModPerLevel

    @r_flat_armor_mod_per_level.setter
    def r_flat_armor_mod_per_level(self, value):
        self.rFlatArmorModPerLevel = value

    @property
    def r_flat_hp_regen_mod_per_level(self):
        return self.rFlatHPRegenModPerLevel

    @r_flat_hp_regen_mod_per_level.setter
    def r_flat_hp_regen_mod_per_level(self, value):
        self.rFlatHPRegenModPerLevel = value

    @property
    def r_percent_time_dead_mod_per_level(self):
        return self.rPercentTimeDeadModPerLevel

    @r_percent_time_dead_mod_per_level.setter
    def r_percent_time_dead_mod_per_level(self, value):
        self.rPercentTimeDeadModPerLevel = value

    @property
    def percent_exp_bonus(self):
        return self.PercentEXPBonus

    @percent_exp_bonus.setter
    def percent_exp_bonus(self, value):
        self.PercentEXPBonus = value

    @property
    def r_flat_crit_damage_mod_per_level(self):
        return self.rFlatCritDamageModPerLevel

    @r_flat_crit_damage_mod_per_level.setter
    def r_flat_crit_damage_mod_per_level(self, value):
        self.rFlatCritDamageModPerLevel = value

    @property
    def r_flat_movement_speed_mod_per_level(self):
        return self.rFlatMovementSpeedModPerLevel

    @r_flat_movement_speed_mod_per_level.setter
    def r_flat_movement_speed_mod_per_level(self, value):
        self.rFlatMovementSpeedModPerLevel = value

    @property
    def r_percent_armor_penetration_mod(self):
        return self.rPercentArmorPenetrationMod

    @r_percent_armor_penetration_mod.setter
    def r_percent_armor_penetration_mod(self, value):
        self.rPercentArmorPenetrationMod = value

    @property
    def r_percent_armor_penetration_mod_per_level(self):
        return self.rPercentArmorPenetrationModPerLevel

    @r_percent_armor_penetration_mod_per_level.setter
    def r_percent_armor_penetration_mod_per_level(self, value):
        self.rPercentArmorPenetrationModPerLevel = value

    @property
    def flat_exp_bonus(self):
        return self.FlatEXPBonus

    @flat_exp_bonus.setter
    def flat_exp_bonus(self, value):
        self.FlatEXPBonus = value

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
    def flat_armor_mod(self):
        return self.FlatArmorMod

    @flat_armor_mod.setter
    def flat_armor_mod(self, value):
        self.FlatArmorMod = value

