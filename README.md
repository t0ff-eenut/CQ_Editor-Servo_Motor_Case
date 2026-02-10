C:\Windows\System32\cmd.exe /K "C:\Users\iSEN\miniforge3\Scripts\activate.bat cad && cq-editor"
C:\Windows\System32\cmd.exe /K "%UserProfile%\miniforge3\Scripts\activate.bat cad && cq-editor"
cmd.exe /K "%UserProfile%\miniforge3\Scripts\activate.bat cad && cq-editor”

C:\WINDOWS\system32\cmd.exe /K %UserProfile%\miniforge3\Scripts\activate.bat cq-editor


1. 시작점 만들기 (Workplane)
모든 작업은 '작업면'을 설정하는 것부터 시작합니다.

cq.Workplane("XY"): XY 평면에 그림을 그릴 준비를 합니다.

cq.Workplane().box(10, 10, 10): 중심에 10x10x10 정육면체를 만듭니다.

2. 스케치 및 생성 (Modeling)
2D 도형을 그려서 3D로 만드는 문법입니다.

.circle(radius) / .rect(width, height): 원이나 사각형 스케치

.extrude(distance): 돌출시켜서 3D 물체 만들기

.hole(diameter): 구멍 뚫기

3. 선택기 (Selectors) - 가장 중요
어떤 면이나 모서리를 깎을지 선택하는 CadQuery만의 강력한 문법입니다.

.faces(">Z"): Z축 방향으로 가장 위에 있는 면 선택

.faces("<X"): X축 방향으로 가장 뒤에 있는 면 선택

.edges("|Z"): Z축과 평행한 모든 모서리 선택

.vertices(): 꼭짓점 선택

4. 수정 및 가공 (Modification)
선택한 부분에 효과를 줍니다.

.fillet(radius): 모서리를 둥글게 깎기

.chamfer(length): 모서리를 모따기(사선)

.shell(thickness): 속을 비워 껍데기만 남기기

5. CQ-editor 전용 명령 (UI 연동)
스크립트의 결과를 화면에 띄우는 문법입니다.

show_object(shape, name="이름", options={"alpha":0.5}): 모델을 화면에 표시

debug(shape): 디버그 모드(빨간색 반투명)로 표시



양방향 돌출: 중심을 기준으로 위아래 15씩, 총 30을 돌출시키고 싶을 때

temp_ = (
    cq.Workplane("YZ")
    .circle(10)           # 2. 반지름 10인 원을 그린 뒤 (스케치)
    .extrude(30)          # 3. 그것을 30만큼 위로 뽑아냄 (돌출)
)


Python
.extrude(30, both=True)
테이퍼(기울기) 돌출: 위로 갈수록 좁아지는 원뿔형 기둥을 만들 때 (각도 입력)

Python
.extrude(30, taper=10)



# 삼각형 만들기 (0,0), (10,0), (5,10) 좌표 연결
points = [(0, 0), (10, 0), (5, 10)]

result = (
    cq.Workplane("XY")
    .polygon(points)
    .extrude(5)
)

# 지름 20인 원에 들어가는 정육각형 만들기
result = (
    cq.Workplane("XY")
    .polygon(6, 20)
    .extrude(10)
)
