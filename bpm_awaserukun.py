fps = input("FPSを入力してください: ")

bpm = input("BPMを入力してください: ")

fps = int(fps)
bpm = int(bpm)

rhythm = fps * 60 / bpm
answer = fps / rhythm

text = "ポスタリゼーション時間のFPSは{}です！"
result = text.format(answer)
print(result)
