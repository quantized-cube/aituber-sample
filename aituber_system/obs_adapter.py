import os

from dotenv import load_dotenv
import obsws_python as obs


class OBSAdapter:
    def __init__(self) -> None:
        load_dotenv()
        password = os.environ.get("OBS_WS_PASSWORD")
        host = os.environ.get("OBS_WS_HOST")
        port = os.environ.get("OBS_WS_PORT")
        # 設定されていない場合はエラー
        if password is None or host is None or port is None:
            raise Exception("OBSの設定がされていません")
        self.ws = obs.ReqClient(host=host, port=port, password=password)

    def set_question(self, text: str) -> None:
        self.ws.set_input_settings(
            name="Question",
            settings={"text": text},
            overlay=True,
        )

    def set_answer(self, text: str) -> None:
        self.ws.set_input_settings(
            name="Answer",
            settings={"text": text},
            overlay=True,
        )


# fileを直接指定したとき
if __name__ == "__main__":
    import random

    obsAdapter = OBSAdapter()
    question_text = "Questionの番号は" + str(random.randint(0, 100)) + "になりました"
    obsAdapter.set_question(question_text)
    answer_text = "Answerの番号は" + str(random.randint(0, 100)) + "になりました"
    obsAdapter.set_answer(answer_text)
