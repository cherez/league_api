from league_api.api import ApiType
from typing import List, Mapping



class InventoryDataStats(ApiType):
    PercentCritDamageMod: float = None
    PercentSpellBlockMod: float = None
    PercentHPRegenMod: float = None
    PercentMovementSpeedMod: float = None
    FlatSpellBlockMod: float = None
    FlatCritDamageMod: float = None
    FlatEnergyPoolMod: float = None
    PercentLifeStealMod: float = None
    FlatMPPoolMod: float = None
    FlatMovementSpeedMod: float = None
    PercentAttackSpeedMod: float = None
    FlatBlockMod: float = None
    PercentBlockMod: float = None
    FlatEnergyRegenMod: float = None
    PercentSpellVampMod: float = None
    FlatMPRegenMod: float = None
    PercentDodgeMod: float = None
    FlatAttackSpeedMod: float = None
    FlatArmorMod: float = None
    FlatHPRegenMod: float = None
    PercentMagicDamageMod: float = None
    PercentMPPoolMod: float = None
    FlatMagicDamageMod: float = None
    PercentMPRegenMod: float = None
    PercentPhysicalDamageMod: float = None
    FlatPhysicalDamageMod: float = None
    PercentHPPoolMod: float = None
    PercentArmorMod: float = None
    PercentCritChanceMod: float = None
    PercentEXPBonus: float = None
    FlatHPPoolMod: float = None
    FlatCritChanceMod: float = None
    FlatEXPBonus: float = None

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
    def flat_crit_damage_mod(self):
        return self.FlatCritDamageMod

    @flat_crit_damage_mod.setter
    def flat_crit_damage_mod(self, value):
        self.FlatCritDamageMod = value

    @property
    def flat_energy_pool_mod(self):
        return self.FlatEnergyPoolMod

    @flat_energy_pool_mod.setter
    def flat_energy_pool_mod(self, value):
        self.FlatEnergyPoolMod = value

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
    def flat_movement_speed_mod(self):
        return self.FlatMovementSpeedMod

    @flat_movement_speed_mod.setter
    def flat_movement_speed_mod(self, value):
        self.FlatMovementSpeedMod = value

    @property
    def percent_attack_speed_mod(self):
        return self.PercentAttackSpeedMod

    @percent_attack_speed_mod.setter
    def percent_attack_speed_mod(self, value):
        self.PercentAttackSpeedMod = value

    @property
    def flat_block_mod(self):
        return self.FlatBlockMod

    @flat_block_mod.setter
    def flat_block_mod(self, value):
        self.FlatBlockMod = value

    @property
    def percent_block_mod(self):
        return self.PercentBlockMod

    @percent_block_mod.setter
    def percent_block_mod(self, value):
        self.PercentBlockMod = value

    @property
    def flat_energy_regen_mod(self):
        return self.FlatEnergyRegenMod

    @flat_energy_regen_mod.setter
    def flat_energy_regen_mod(self, value):
        self.FlatEnergyRegenMod = value

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
    def flat_hp_regen_mod(self):
        return self.FlatHPRegenMod

    @flat_hp_regen_mod.setter
    def flat_hp_regen_mod(self, value):
        self.FlatHPRegenMod = value

    @property
    def percent_magic_damage_mod(self):
        return self.PercentMagicDamageMod

    @percent_magic_damage_mod.setter
    def percent_magic_damage_mod(self, value):
        self.PercentMagicDamageMod = value

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
    def percent_physical_damage_mod(self):
        return self.PercentPhysicalDamageMod

    @percent_physical_damage_mod.setter
    def percent_physical_damage_mod(self, value):
        self.PercentPhysicalDamageMod = value

    @property
    def flat_physical_damage_mod(self):
        return self.FlatPhysicalDamageMod

    @flat_physical_damage_mod.setter
    def flat_physical_damage_mod(self, value):
        self.FlatPhysicalDamageMod = value

    @property
    def percent_hp_pool_mod(self):
        return self.PercentHPPoolMod

    @percent_hp_pool_mod.setter
    def percent_hp_pool_mod(self, value):
        self.PercentHPPoolMod = value

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
    def percent_exp_bonus(self):
        return self.PercentEXPBonus

    @percent_exp_bonus.setter
    def percent_exp_bonus(self, value):
        self.PercentEXPBonus = value

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

