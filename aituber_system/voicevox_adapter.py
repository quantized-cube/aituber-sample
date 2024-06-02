import io
import json

import requests
import soundfile


class VoicevoxAdapter:
    URL = "http://127.0.0.1:50021/"

    # 二回postする。一回目で変換、二回目で音声合成
    def __init__(self, speaker_id: int) -> None:
        self.speaker_id = speaker_id

    def __create_audio_query(self, text: str) -> json:
        item_data = {
            "text": text,
            "speaker": self.speaker_id,
        }
        response = requests.post(
            self.URL + "audio_query",
            params=item_data,
        )
        return response.json()

    def __create_request_audio(self, query_data) -> bytes:
        a_params = {
            "speaker": self.speaker_id,
        }
        headers = {
            "accept": "audio/wav",
            "Content-Type": "application/json",
        }
        res = requests.post(
            self.URL + "synthesis",
            params=a_params,
            data=json.dumps(query_data),
            headers=headers,
        )
        print(res.status_code)
        return res.content

    def get_voice(self, text: str):
        query_data: json = self.__create_audio_query(text)
        audio_bytes = self.__create_request_audio(query_data)
        audio_stream = io.BytesIO(audio_bytes)
        data, sample_rate = soundfile.read(audio_stream)
        return data, sample_rate


if __name__ == "__main__":
    voicevox = VoicevoxAdapter()
    data, sample_rate = voicevox.get_voice("こんにちは")
    print(sample_rate)
