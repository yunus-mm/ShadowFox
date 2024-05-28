total_jumping_jacks = 100
jumping_jacks_per_set = 10

for i in range(0, total_jumping_jacks, jumping_jacks_per_set):
    print(f"Do {jumping_jacks_per_set} jumping jacks!")
    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()
    if tired in ['yes', 'y']:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ['yes', 'y']:
            print(f"You completed a total of {i + jumping_jacks_per_set} jumping jacks.")
            break
    else:
        remaining = total_jumping_jacks - (i + jumping_jacks_per_set)
        print(f"{remaining} jumping jacks remaining.")
else:
    print("Congratulations! You completed the workout.")

