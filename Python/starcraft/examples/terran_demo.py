from starcraft.races.terran import Terran

terran = Terran()

# === 기본 유닛 생성 ===
marine1 = terran.train("marine")
dropship1 = terran.train("dropship")

# === 커스터마이즈 유닛 생성 (테스트 유닛) ===
marine2 = terran.train("marine", name="EliteMarine", hp=150, speed=6, atk=7)
marine3 = terran.train("marine", name="BossMarine", hp=500, speed=3, atk=20)

# === 각 유닛 확인 ===
print("\n--- 생성된 유닛 ---")
for u in terran.units:
    print(f"{u.name} | HP: {u.hp} | Speed: {u.speed} | ATK: {u.atk}")

# === 테스트 시뮬레이션 ===
print("\n--- 테스트 전투 시나리오 ---")
marine1.attack("적 저글링")
marine2.attack("적 히드라리스크")
marine3.attack("적 울트라리스크")
dropship1.move("전방")