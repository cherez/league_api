from .api import api_function
from .types import *
from typing import List, Mapping

get_all_champion_masteries = api_function('/lol/champion-mastery/v3/champion-masteries/by-summoner/{}', List[ChampionMastery], int)
get_all_league_positions_for_summoner = api_function('/lol/league/v3/positions/by-summoner/{}', List[LeaguePosition], int)
get_all_leagues_for_summoner = api_function('/lol/league/v3/leagues/by-summoner/{}', List[LeagueList], int)
get_by_account_id = api_function('/lol/summoner/v3/summoners/by-account/{}', Summoner, str)
get_by_summoner_id = api_function('/lol/summoner/v3/summoners/{}', Summoner, str)
get_by_summoner_name = api_function('/lol/summoner/v3/summoners/by-name/{}', Summoner, str)
get_challenger_league = api_function('/lol/league/v3/challengerleagues/by-queue/{}', LeagueList, str)
get_champion_by_id = api_function('/lol/static-data/v3/champions/{}', Champion, int, version=str, locale=str, champData=str)
get_champion_list = api_function('/lol/static-data/v3/champions', ChampionList, version=str, champListData=str, dataById=bool, locale=str)
get_champion_mastery = api_function('/lol/champion-mastery/v3/champion-masteries/by-summoner/{}/by-champion/{}', ChampionMastery, int, int)
get_champion_mastery_score = api_function('/lol/champion-mastery/v3/scores/by-summoner/{}', int, int)
get_champions = api_function('/lol/platform/v3/champions', ChampionList, freeToPlay=bool)
get_champions_by_id = api_function('/lol/platform/v3/champions/{}', Champion, int)
get_current_game_info_by_summoner = api_function('/lol/spectator/v3/active-games/by-summoner/{}', CurrentGameInfo, int)
get_featured_games = api_function('/lol/spectator/v3/featured-games', FeaturedGames)
get_item_by_id = api_function('/lol/static-data/v3/items/{}', Item, int, version=str, itemData=str, locale=str)
get_item_list = api_function('/lol/static-data/v3/items', ItemList, version=str, itemListData=str, locale=str)
get_language_strings = api_function('/lol/static-data/v3/language-strings', LanguageStrings, version=str, locale=str)
get_languages = api_function('/lol/static-data/v3/languages', List[str])
get_map_data = api_function('/lol/static-data/v3/maps', MapData, version=str, locale=str)
get_master_league = api_function('/lol/league/v3/masterleagues/by-queue/{}', LeagueList, str)
get_mastery_by_id = api_function('/lol/static-data/v3/masteries/{}', Mastery, int, masteryData=str, version=str, locale=str)
get_mastery_list = api_function('/lol/static-data/v3/masteries', MasteryList, version=str, masteryListData=str, locale=str)
get_mastery_pages_by_summoner_id = api_function('/lol/platform/v3/masteries/by-summoner/{}', MasteryPages, str)
get_match = api_function('/lol/match/v3/matches/{}', Match, int)
get_match_by_tournament_code = api_function('/lol/match/v3/matches/{}/by-tournament-code/{}', Match, int, str)
get_match_ids_by_tournament_code = api_function('/lol/match/v3/matches/by-tournament-code/{}/ids', List[int], str)
get_match_timeline = api_function('/lol/match/v3/timelines/by-match/{}', MatchTimeline, int)
get_matchlist = api_function('/lol/match/v3/matchlists/by-account/{}', Matchlist, int, beginTime=int, endIndex=int, season=List[int], champion=List[int], beginIndex=int, queue=List[int], endTime=int)
get_profile_icons = api_function('/lol/static-data/v3/profile-icons', ProfileIconData, version=str, locale=str)
get_realm = api_function('/lol/static-data/v3/realms', Realm)
get_recent_matchlist = api_function('/lol/match/v3/matchlists/by-account/{}/recent', Matchlist, int)
get_rune_by_id = api_function('/lol/static-data/v3/runes/{}', Rune, int, version=str, runeData=str, locale=str)
get_rune_list = api_function('/lol/static-data/v3/runes', RuneList, version=str, runeListData=str, locale=str)
get_rune_pages_by_summoner_id = api_function('/lol/platform/v3/runes/by-summoner/{}', RunePages, str)
get_shard_data = api_function('/lol/status/v3/shard-data', ShardStatus)
get_summoner_spell_by_id = api_function('/lol/static-data/v3/summoner-spells/{}', SummonerSpell, int, version=str, spellData=str, locale=str)
get_summoner_spell_list = api_function('/lol/static-data/v3/summoner-spells', SummonerSpellList, version=str, spellListData=str, dataById=bool, locale=str)
get_versions = api_function('/lol/static-data/v3/versions', List[str])