import os

from dotenv import load_dotenv

from .obs_adapter import OBSAdapter
from .voicevox_adapter import VoicevoxAdapter
from .openai_adapter import OpenAIAdapter
from .youtube_comment_adapter import YoutubeCommentAdapter
from .play_sound import PlaySound

load_dotenv()


class AITuberSystem:
    def __init__(self) -> None:
        speaker_id = os.getenv("VOICEVOX_SPEAKER_ID")
        if speaker_id is None:
            raise Exception("VOICEVOX_SPEAKER_IDが設定されていません。")
        video_id = os.getenv("YOUTUBE_VIDEO_ID")
        if video_id is None:
            raise Exception("YOUTUBE_VIDEO_IDが設定されていません。")
        self.youtube_comment_adapter = YoutubeCommentAdapter(video_id)
        self.openai_adapter = OpenAIAdapter()
        self.voice_adapter = VoicevoxAdapter(speaker_id)
        self.obs_adapter = OBSAdapter()
        self.play_sound = PlaySound(output_device_name="CABLE Input")

    def talk_with_comment(self) -> bool:
        print("コメントを読み込みます…")
        comment = self.youtube_comment_adapter.get_comment()
        if comment is None:
            print("コメントがありませんでした。")
            return False
        response_text = self.openai_adapter.create_chat(comment)
        data, rate = self.voice_adapter.get_voice(response_text)
        self.obs_adapter.set_question(comment)
        self.obs_adapter.set_answer(response_text)
        self.play_sound.play_sound(data, rate)
        return True
