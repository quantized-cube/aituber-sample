from play_sound import PlaySound
from voicevox_adapter import VoicevoxAdapter

input_str = "いらっしゃいませ"
# input_str = input("話す内容を入力してください。")
voicevox_adapter = VoicevoxAdapter()
play_sound = PlaySound("スピーカー")
data, rate = voicevox_adapter.get_voice(input_str)
play_sound.play_sound(data, rate)
