import tracker

# Current members on the health and fitness tracker
members = {
    "Shouvik Guha": "password123",
    # other members...
}


# Function that gets responses for a chosen health item after posing relevant questions
def get_responses_for(item):
    print(f"Answer questions for {item}:")
    responses = []

    if item == "Exercise":
        gymm = ["Chest", "Shoulders", "Legs", "Back", "Arms", "Core"]
        exquestions = ["""Q1) What type of exercise did you predominantly perform today?\n[Choices: Gym, Walking, Running, Cycling, Yoga, Other]""", """Q2) On a scale of 1 to 10, how intense was your workout today?\n[Rating Scale: 1 (Low Intensity) to 10 (High Intensity)""", """Q3) Did you engage in at least 60 minutes of physical activity today?\n[Y: Yes/N: No]"""]
        for i in range(len(exquestions)):
            ans = input(exquestions[i] + " ")
            ans.lower()
            ans.strip()
            if i == 0:
                if ans == "gym":
                    workout_gym_type = input("""Enter the corresponding number to mark your choice for type of gym exercise -\n1: Chest\n2: Shoulders\n3: Legs\n4: Back\n5: Arms\n6: Core\n> """)
                    exercise_num = int(workout_gym_type)
                    ans += f": {gymm[exercise_num - 1]}"
                elif ans == "other":
                    specify_other = input("Please specify: ")
                    ans += f": {specify_other}"
                responses.append(ans.title().strip())
            elif i == 2:
                if ans == "y":
                    responses.append("Yes")
                else:
                    responses.append("No")
            else:
                responses.append(ans)

    elif item == "Diet":
        questions = ["""Q1) What type of diet do you currently follow?\n[Choices: Standard, Vegetarian, Vegan, Keto, Paleo, Gluten-free, Other]""",
                     "Q2) How many meals did you eat today? [Enter number]", """Q3) How satisfied are you with your current diet? 
[Rating Scale: 1 (Not Satisfied) to 5 (Very Satisfied)]"""]
        for q in questions:
            ans = input(q + " ")
            ans.strip()
            checker = ans.lower()
            if checker == "other":
                specify_other = input("Please specify: ")
                ans += f": {specify_other}"
            if q.startswith("Q2)"):
                meals_num = int(ans)
                if (meals_num == 1):
                    ans_2_1 = input(f"Q2.1) Was your meal today home-cooked? [Y: Yes/N: No] ")
                    ans2_2 = input("""Q2.2) Rate the healthiness of the meal. 
 [Rating Scale: 1 (Much Less Healthy) to 5 (Much Healthier)]) """)
                if (meals_num > 1):
                    ans_2_1 = input(f"Q2.1) How many of your {meals_num} meals today were home-cooked? [Enter number] ")
                    if (int(ans_2_1) > 0):
                        ans_2_2 = input("""Q2.2) Rate the healthiness of meals eaten outside versus home-cooked. 
                     [Rating Scale: 1 (Much Less Healthy) to 5 (Much Healthier)]) """)
                    else:
                        ans_2_2 = input("""Q2.2) Rate the healthiness of the meal. 
 [Rating Scale: 1 (Much Less Healthy) to 5 (Much Healthier)]) """)
                    ans = ans + ": " + ans_2_1 + ": " + ans2_2
            # else:
            responses.append(ans.strip().title())

    elif item == "Weight and Height":
        goal_list = ["Weight Loss", "Weight Gain", "Maintaining Current Weight", "Improving Muscle Tone",
                     "No Specific Goal"]
        questions = ["Q1) How much do you weigh right now in kilograms?", "Q2) How tall are you in meters?", """Q3) What is your current goal regarding your weight?
        [Enter the corresponding number to mark your choice - 
        1: Weight Loss
        2: Weight Gain
        3: Maintaining Current Weight
        4: Improving Muscle Tone
        5: No Specific Goal]""", """Q4) How do you feel about your current weight in relation to your health and fitness goals?
        [Rating Scale: 1 (Very Dissatisfied) to 5 (Very Satisfied)]"""]
        for q in questions:
            ans = input(q + " ")
            ans.strip()
            if q.startswith("Q3)"):
                ans = goal_list[int(ans) - 1]
            responses.append(ans.strip().title())

    elif item == "Caloric Intake":
        questions=["""Q1) Select the range that best estimates your total calorie intake for today. 
[Enter the corresponding number to mark your choice - 
1: <1500 calories 
2: 1500-2000 calories 
3: 2000-2500 calories 
4: >2500 calories]""", """Q2) Select the range that best estimates your total for calories burned. 
[Enter the corresponding number to mark your choice - 
1: <800 calories 
2: 800-1000 calories 
3: 1000-1500 calories 
4: 1500-2000 calories 
5: 2000-2500 
6: 2500+]""", """Q3) Select the category that best describes your food intake today. 
[Multiple Choice: Insufficient, Adequate, Excessive]"""]
        for q in questions:
            ans = input(q + " ")
            range_calories_q1 = ["<1500", "1500-2000", "2000-2500", ">2500"]
            range_calories_q2 = ["<800", "800-1000", "1000-1500", "1500-2000", "2000-2500", "2500+"]
            if q.startswith("Q1)"):
                ans = range_calories_q1[int(ans) - 1]
            if q.startswith("Q2)"):
                ans = range_calories_q2[int(ans) - 1]

            responses.append(ans.strip().title())

    elif item == "Water Intake":
        litres = ["<1", "1-2", "2-3", "3-4", ">4"]
        questions = ["""Q1) Approximately how much water did you drink today?
[Enter the corresponding number to mark your choice - 
1: <1L
2: 1-2L
3: 2-3L
4: 3-4L
5: >4L]""", """Q2) On a scale of 1 to 5, how well-hydrated did you feel today?
[Rating Scale: 1 (Very Dehydrated) to 5 (Very Hydrated)]""", """Q3) On average what colour was your pee today? 
[Rating Scale: 1 (Yellow) to 5 (Clear)]"""]
        for q in questions:
            ans = input(q + " ")
            if q.startswith("Q1)"):
                ans = litres[int(ans) - 1]
                responses.append(ans.strip().title())

    elif item == "Sleep Quality":
        questions = ["""Q1) How many hours of sleep did you get last night? 
        [Round to the nearest half hour — for ex: 6 hours 42 minutes = 6.5, 4 hours 12 = 4]""", """Q2) Rate the quality of your sleep last night.
        [Rating Scale: 1 (Poor) to 5 (Excellent)]""", "Q3) How many times did you wake up in your sleep?",
                     "Q4) Did you feel tired in general today? [Y: Yes/N: No]"]
        for q in questions:
            ans = input(q + " ")
            responses.append(ans.strip().title())

    elif item == "Mood and Energy":
        questions = ["""Q1) Rate your overall mood today. 
        [Rating Scale: 1 (Very Poor) to 5 (Excellent)]""", "Q2) Was your mood and energy level better today than yesterday? [Y: Yes/N: No]", """Q3) Choose three words that best describe your mood today. 
        [Formatted Example: "Happy, Anxious, Energetic"]"""]

        for q in questions:
            ans = input(q + " ")
            responses.append(ans.strip().title())

    elif item == "Stress Levels":
        questions = ["""Q1) Rate your stress level today. 
        [Rating Scale: 1 (Very Low) to 5 (Very High)]""", """Q2) Did you use any stress management techniques today (e.g., meditation, deep breathing)? 
        [Y: Yes/N: No]""", """Q3) Identify the main factors that contributed to your stress today (minimum 2).
        [Choices: Work, Personal Life, Health, Finances, Other]"""]

        for q in questions:
            ans = input(q + " ")
            if q.startswith("Q2)"):
                ans = ans+": "+input(""""Q2.1) What was your stress management technique? """)
            responses.append(ans.strip().title())

    return responses


user_name = input("Please enter your full name (ex: John Doe): ")
password = input(f"Please enter your password {user_name}: ")
user_name.lower()

filename = f"{user_name}_health_fitness_tracker.xlsx"

if user_name not in members:
    members[user_name] = password
    tracker.create_workbook(filename)
    print(f"Welcome, {user_name}! Your report is being prepared.")
else:
    print(f"Welcome back, {user_name}! Pulling up your report.")

health_items = ["Exercise", "Diet", "Weight and Height", "Caloric Intake", "Water Intake", "Sleep Quality", "Mood and Energy", "Stress Levels"]
while health_items:
    print("\nWhat would you like to report on?")
    for item in health_items:
        print(f"- {item}")
    choice = input("> ")
    choice.title().strip()
    if choice in health_items:
        responses = get_responses_for(choice)
        tracker.add_data(filename, choice, responses)
        health_items.remove(choice)
    else:
        print("Invalid choice! Please choose from the list.")

print(f"""You have finished reporting on all health items.
 
      We have finished tracking your progess for today. 
      Remember to come check-in again tomorrow {user_name.title()}! """)
