# SAVE PATIENTS

n = int(input())
strength = list(map(int, input().split()))
patient = list(map(int, input().split()))
strength.sort()
patient.sort()

for i in range(n):
    if strength[i]<patient[i]:
        print("No")
        break
else:
    print("Yes")
