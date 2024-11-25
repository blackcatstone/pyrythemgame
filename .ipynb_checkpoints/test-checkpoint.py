import librosa
import numpy as np

# 음악 파일 로드
filename = 'hip.mp3'
y, sr = librosa.load(filename, sr=None)

# 음악 파일에서 비트 분석
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# 비트 타임스탬프로 변환
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print("비트 타이밍:", beat_times)

# 비트 타이밍을 기반으로 노트 생성 로직
# 예시로, 각 비트 타이밍에 대한 노트 위치와 정보를 저장할 배열을 만듭니다.
notes = []
for beat_time in beat_times:
    # 노트 정보 생성. 여기서는 예시로 비트 타임을 직접 사용합니다.
    # 실제 게임에서는 노트의 x 위치, 노트 타입 등 추가 정보가 필요할 수 있습니다.
    note = {
        'time': beat_time,
        'x_position': np.random.randint(0, 4),  # 0부터 3 중 하나를 랜덤으로 선택
        'type': 'normal'  # 노트 타입 (예시)
    }
    notes.append(note)

print("생성된 노트 정보:", notes)
