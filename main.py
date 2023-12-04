from datetime import datetime
import tracker

# Current members on the health and fitness tracker
members = {
    "Shouvik Guha": "password123",
    # other members...
}

def yes_or_no(question):
    while True:
        answer = input(question+" ").strip().lower()
        if answer in ['y', 'n']:
            return "Yes" if answer == 'y' else "No"
        else:
            print("Please enter 'Y' for Yes or 'N' for No.")

def mcq_and_rating_scale(question, min_val, max_val):
    while True:
        try:
            value = int(input(question+" "))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a number.")

gym_exercises = ["Chest", "Shoulders", "Legs", "Back", "Arms", "Core"]
range_calories= ["<800", "800-1000", "1000-1500", "1500-2000", "2000-2500", ">2500"]
diet_choices = ["Standard", "Carnivore", "Vegetarian", "Vegan", "Keto", "Paleo", "Gluten-free", "Other"]
litres = ["<1", "1-2", "2-3", "3-4", ">4"]
weight_goal_list = ["Weight Loss", "Weight Gain", "Maintaining Current Weight", "Improving Muscle Tone", "No Specific Goal"]
exercise_questions = ["""Q1) What type of exercise did you predominantly perform today?\n[Choices: Gym, Walking, Running, Cycling, Yoga, Other]""", f"""Q2) On a scale of 1 to 10, how intense was your workout today?\n[Rating Scale: 1 (Low Intensity) to 10 (High Intensity)""", """Q3) Did you engage in at least 60 minutes of physical activity today?\n[Y: Yes/N: No]"""]
diet_questions = [f"""Q1) What type of diet do you currently follow?\n[Choices: {diet_choices[:]}]""","Q2) How many meals did you eat today? [Enter number]","""Q3) How satisfied are you with your current diet?\n[Rating Scale: 1 (Not Satisfied) to 5 (Very Satisfied)]"""]
weight_height_questions = ["Q1) How much do you weigh right now in kilograms?", "Q2) How tall are you in meters?", """Q3) What is your current goal regarding your weight?\n[Enter the corresponding number to mark your choice -\n1: Weight Loss\n2: Weight Gain\n3: Maintaining Current Weight\n4: Improving Muscle Tone\n5: No Specific Goal]""", """Q4) How do you feel about your current weight in relation to your health and fitness goals?\n[Rating Scale: 1 (Very Dissatisfied) to 5 (Very Satisfied)]"""]
caloric_intake_questions=["""Q1) Select the range that best estimates your total calorie intake for today.\n[Enter the corresponding number to mark your choice -\n1: <800 calories\n2: 800-1000 calories\n3: 1000-1500 calories\n4: 1500-2000 calories\n5: 2000-2500\n6: 2500+]""", """Q2) Select the range that best estimates your total for calories burned.\n[Enter the corresponding number to mark your choice -\n1: <800 calories\n2: 800-1000 calories\n3: 1000-1500 calories\n4: 1500-2000 calories\n5: 2000-2500\n6: 2500+]""", """Q3) Select the category that best describes your food intake today.\n [Choice - \n1: Insufficient\n2: Adequate\n3: Sufficient or Good\n4: Excessive]"""]
water_intake_questions = ["""Q1) Approximately how much water did you drink today?\n[Enter the corresponding number to mark your choice - \n1: <1L\n2: 1-2L\n3: 2-3L\n4: 3-4L\n5: >4L]""", """Q2) On a scale of 1 to 5, how well-hydrated did you feel today?\n[Rating Scale: 1 (Very Dehydrated) to 5 (Very Hydrated)]""", """Q3) On average what colour was your pee today?\n[Rating Scale: 1 (Yellow) to 5 (Clear)]"""]
sleep_quality_questions = ["""Q1) How many hours of sleep did you get last night?\n[Round to the nearest half hour — for ex: 6 hours 42 minutes = 6.5, 4 hours 12 = 4]""", """Q2) Rate the quality of your sleep last night.\n[Rating Scale: 1 (Poor) to 5 (Excellent)]""", "Q3) How many times did you wake up in your sleep?","Q4) Did you feel tired in general today? [Y: Yes/N: No]"]
mood_energy_questions = ["""Q1) Rate your overall mood today.\n[Rating Scale: 1 (Very Poor) to 5 (Excellent)]""", "Q2) Was your mood and energy level better today than yesterday? [Y: Yes/N: No]", """Q3) Choose three words that best describe your mood today.\n[Formatted Example: "Happy, Anxious, Energetic"]"""]
stress_level_questions = ["""Q1) Rate your stress level today.\n[Rating Scale: 1 (Very Low) to 5 (Very High)]""", """Q2) Did you use any stress management techniques today (e.g., meditation, deep breathing)?\n[Y: Yes/N: No]""", """Q3) Identify the main factors that contributed to your stress today (minimum 2).\n[Example Choices: Work, Personal Life, Health, Finances, Other]"""]

# Function that gets responses for a chosen health item after posing relevant questions
def get_responses_for(item):
    #global ans2_2
    curr_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    responses = [curr_date_time] # Log response date and time
    print(f"Answer questions for {item}:")
    if item == "Exercise":
        # gymm = ["Chest", "Shoulders", "Legs", "Back", "Arms", "Core"]
        # exquestions = ["""Q1) What type of exercise did you predominantly perform today?\n[Choices: Gym, Walking, Running, Cycling, Yoga, Other]""", """Q2) On a scale of 1 to 10, how intense was your workout today?\n[Rating Scale: 1 (Low Intensity) to 10 (High Intensity)""", """Q3) Did you engage in at least 60 minutes of physical activity today?\n[Y: Yes/N: No]"""]
        for i in range(len(exercise_questions)):
            ##ans = input(exercise_questions[i] + " ").lower().strip()
            if i == 0:
                ans = input(exercise_questions[i] + " ").lower().strip()
                if "gym" in ans:
                    workout_gym_type = mcq_and_rating_scale("""Q1.1) Enter the corresponding number to mark your choice for type of gym exercise -\n1: Chest\n2: Shoulders\n3: Legs\n4: Back\n5: Arms\n6: Core\n>""", 1, 6)
                        #exercise_num = int(workout_gym_type)
                    ans += f": {gym_exercises[workout_gym_type - 1]}"
                    #responses.append(ans.title().strip())

                elif ans == "other":
                    specify_other = input("Please specify: ")
                    specify_other.strip().title()
                    ans += f": {specify_other}"

                responses.append(ans.title().strip())
            elif i == 1:
                responses.append(str(mcq_and_rating_scale(exercise_questions[i], 1, 10)))
            elif i == 2:
                responses.append(yes_or_no(exercise_questions[i]))

    elif item == "Diet":
        # diet_questions = [
        #     """Q1) What type of diet do you currently follow?\n[Choices: Standard, Vegetarian, Vegan, Keto, Paleo, Gluten-free, Other]""",
        #     "Q2) How many meals did you eat today? [Enter number]",
        #     """Q3) How satisfied are you with your current diet?\n[Rating Scale: 1 (Not Satisfied) to 5 (Very Satisfied)]"""]
        for q in diet_questions:
            if q.startswith("Q1)"):
                choice_chosen = False
                while not choice_chosen:
                    ans = input(q + " ").lower().strip()
                    choice = ans.title()
                    if choice in diet_choices:
                        choice_chosen = True
                        if choice == "Other":
                            specify_other = input("Please specify: ")
                            choice += f": {specify_other}"
                    else:
                        print("Invalid choice! Please choose from the list.")
                responses.append(choice)
            else:
                ans = input(q + " ").lower().strip()
                if q.startswith("Q2)"):
                    meals_num = int(ans)
                    if (meals_num == 1):
                        ans_2_1 = yes_or_no("Q2.1) Was your meal today home-cooked? [Y: Yes/N: No]")
                        ans_2_2 = mcq_and_rating_scale("""Q2.2) Rate the healthiness of the meal.\n[Rating Scale: 1 (Much Less Healthy) to 5 (Much Healthier)])""", 1, 5)
                        ans = f"{meals_num}, {ans_2_1}, {ans_2_2}"
                    if (meals_num > 1):
                        #ans2_2 = ""
                        ans_2_1 = mcq_and_rating_scale(f"Q2.1) How many of your {meals_num} meals today were home-cooked? [Enter number] ", 0, meals_num)
                        # if (int(ans_2_1) > 0 and int(ans_2_1)<=meals_num):
                        #     ans_2_2 = ""
                        if(int(ans_2_1)!=meals_num):
                            ans_2_2 = mcq_and_rating_scale("""Q2.2) Rate the healthiness of meals eaten outside versus home-cooked.\n[Rating Scale: 1 (Much Less Healthy) to 5 (Much Healthier)])""", 1, 5)
                        else:
                            ans_2_2 = mcq_and_rating_scale("""Q2.2) Rate the healthiness of the meal.\n[Rating Scale: 1 (Much Less Healthy) to 5 (Much Healthier)])""", 1, 5)

                        ans = f"{meals_num}, {ans_2_1}, {ans_2_2}"

            # else:
                responses.append(ans.title())

    elif item == "Weight & Height":
        for q in weight_height_questions:
            #ans = input(q + " ").lower().strip()
            #ans.strip()
            if q.startswith("Q3)"):
                ans = mcq_and_rating_scale(q, 1, 5)
                ans = weight_goal_list[ans - 1]
            elif q.startswith("Q4)"):
                ans = mcq_and_rating_scale(q, 1, 5)
                str(ans)
            else:
                ans = input(q + " ").lower().strip()

            responses.append(ans)

    elif item == "Caloric Intake":
        for q in caloric_intake_questions:
            #range_calories_q1 = ["<1500", "1500-2000", "2000-2500", ">2500"]
            #range_calories= ["<800", "800-1000", "1000-1500", "1500-2000", "2000-2500", ">2500"]
            if q.startswith("Q1)"):
                ans = mcq_and_rating_scale(q,1,6)
                ans = range_calories[ans - 1]
                responses.append(ans.title())
            elif q.startswith("Q2)"):
                ans = mcq_and_rating_scale(q, 1, 6)
                ans = range_calories[ans - 1]
                responses.append(ans.title())
            elif q.startswith("Q3)"):
                ans = mcq_and_rating_scale(q, 1, 4)
                ans = range_calories[ans - 1]
                responses.append(ans.title())


    elif item == "Water Intake":
        for q in water_intake_questions:
            ans = mcq_and_rating_scale(q, 1, 5)
            if q.startswith("Q1)"):
                ans = litres[ans - 1]
            str(ans)
            responses.append(ans)

    elif item == "Sleep Quality":
        for q in sleep_quality_questions:
            if(q.startswith("Q2)")):
                ans = mcq_and_rating_scale(q,1, 5)
                str(ans)
            elif(q.startswith("Q4)")):
                ans = yes_or_no(q)
            else:
                ans = input(q + " ").lower().strip()

            responses.append(ans)

    elif item == "Mood & Energy":
        for q in mood_energy_questions:
            if(q.startswith("Q1)")):
                ans = mcq_and_rating_scale(q, 1, 5)
                str(ans)
            elif(q.startswith("Q2)")):
                ans = yes_or_no(q)
            else:
                ans = input(q + " ").lower().strip()

            responses.append(ans)

    elif item == "Stress Levels":
        for q in stress_level_questions:
            if q.startswith("Q1)"):
                ans = mcq_and_rating_scale(q,1,5)
                str(ans)
            if q.startswith("Q2)"):
                ans = yes_or_no(q)
                if(ans == "Yes"):
                    ans = ans+": "+input(""""Q2.1) What was your stress management technique? """).strip()
            elif q.startswith("Q3)"):
                ans = input(q + " ").lower().strip()
            responses.append(ans)

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
    if members[user_name] == password:
        print(f"Welcome back, {user_name}! Pulling up your report.")
    else:
        print("Incorrect password! Please try again.")

health_items = ["Exercise", "Diet", "Weight & Height", "Caloric Intake", "Water Intake", "Sleep Quality", "Mood & Energy", "Stress Levels"]

# health_items_questions = {
#     "1": exercise_questions,
#     "Exercise": exercise_questions,
#     "2": diet_questions,
#     "Diet": diet_questions,
#     "3": weight_height_questions,
#     "Weight & Height": weight_height_questions,
#     "4": caloric_intake_questions,
#     "Caloric Intake": caloric_intake_questions,
#     "5": water_intake_questions,
#     "Water Intake": water_intake_questions,
#     "6": sleep_quality_questions,
#     "Sleep Quality": sleep_quality_questions,
#     "7": mood_energy_questions,
#     "Mood & Energy": mood_energy_questions,
#     "8": stress_level_questions,
#     "Stress Levels": stress_level_questions,
# }

health_item_choice_map = {
    "1" : "Exercise",
    "2" : "Diet",
    "3" : "Weight & Height",
    "4" : "Caloric Intake",
    "5" : "Water Intake",
    "6" : "Sleep Quality",
    "7" : "Mood & Energy",
    "8" : "Stress Levels"
}

# health_q_list = list(health_items_questions.keys())
health_q_dict = {
    "Exercise" : exercise_questions,
    "Diet" : diet_questions,
    "Weight & Height" : weight_height_questions,
    "Caloric Intake" : caloric_intake_questions,
    "Water Intake" : water_intake_questions,
    "Sleep Quality" : sleep_quality_questions,
    "Mood & Energy" : mood_energy_questions,
    "Stress Levels" : stress_level_questions
}
#questions_all = [exercise_questions, weight_height_questions, caloric_intake_questions, water_intake_questions, sleep_quality_questions, mood_energy_questions, stress_level_questions]
while health_items:
    print("\nWhat would you like to report on?")
    for number, item in health_item_choice_map.items():
        if item in health_items:
            print(f"- {number}: {item}")
    choice = input("> ").strip()
    if choice.isdigit():
        if choice in health_item_choice_map:
            choice = health_item_choice_map[choice]
    choice = choice.title()
    if choice in health_items:
        responses = get_responses_for(choice)
        tracker.add_data(filename, choice, health_q_dict[choice], responses)
        health_items.remove(choice)
    else:
        print("Invalid choice! Please choose from the list.")

print(f"""You have finished reporting on all health items.
 
      We have finished tracking your progress for today. 
      Remember to come check-in again tomorrow {user_name.title()}! """)
