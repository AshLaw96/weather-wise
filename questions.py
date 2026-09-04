import random
import tkinter as tk
from tkinter import ttk, messagebox

# --- Question Datasets ---
EASY_QUESTIONS = [
    {"question": "What do we wear on our feet when it's raining?", "choices": ["Rain boots", "Sneakers", "Sandals", "Slippers"], "answer": "Rain boots"},
    {"question": "What do we call white, fluffy ice crystals that fall from the sky?", "choices": ["Snow", "Rain", "Hail", "Fog"], "answer": "Snow"},
    {"question": "What color is the sky when it's clear?", "choices": ["Blue", "Green", "Red", "Yellow"], "answer": "Blue"},
    {"question": "What do we call water falling from the sky?", "choices": ["Rain", "Snow", "Wind", "Fog"], "answer": "Rain"},
    {"question": "What do you wear when it's raining?", "choices": ["Raincoat", "Sweater", "T-shirt", "Sunglasses"], "answer": "Raincoat"},
    {"question": "What is a rainbow?", "choices": ["A colorful arc in the sky", "A cloud", "A type of rain", "A storm"], "answer": "A colorful arc in the sky"},
    {"question": "What season comes after winter?", "choices": ["Spring", "Fall", "Summer", "Winter"], "answer": "Spring"},
    {"question": "What do you wear when it's snowing?", "choices": ["Coat", "Shorts", "T-shirt", "Sandals"], "answer": "Coat"},
    {"question": "What is a thunderstorm?", "choices": ["A storm with thunder and lightning", "A sunny day", "A snowstorm", "A calm breeze"], "answer": "A storm with thunder and lightning"},
    {"question": "What do you see in the sky when it rains?", "choices": ["Clouds", "Sun", "Stars", "Fog"], "answer": "Clouds"},
    {"question": "Is snow cold or warm?", "choices": ["Cold", "Warm", "Hot", "Mild"], "answer": "Cold"},
    {"question": "Can you see the sun on a cloudy day?", "choices": ["No", "Yes", "Sometimes", "Always"], "answer": "Sometimes"},
    {"question": "What is the coldest season of the year?", "choices": ["Winter", "Spring", "Summer", "Fall"], "answer": "Winter"},
    {"question": "What do we use to stay dry when it rains?", "choices": ["Umbrella", "Sunglasses", "Hat", "Scarf"], "answer": "Umbrella"},
    {"question": "What season comes after summer?", "choices": ["Fall", "Spring", "Winter", "Summer"], "answer": "Fall"},
    {"question": "What do you wear when it's hot outside?", "choices": ["T-shirt", "Coat", "Gloves", "Sweater"], "answer": "T-shirt"},
    {"question": "How does the sun feel on your skin?", "choices": ["Warm", "Cold", "Wet", "Windy"], "answer": "Warm"},
    {"question": "What do we call a strong wind?", "choices": ["Gale", "Breeze", "Fog", "Rain"], "answer": "Gale"},
    {"question": "Is rain wet or dry?", "choices": ["Wet", "Dry", "Cold", "Hot"], "answer": "Wet"},
    {"question": "What do you wear when it's windy outside?", "choices": ["Jacket", "Shorts", "Sandals", "Swimsuit"], "answer": "Jacket"},
    {"question": "What season is the warmest?", "choices": ["Summer", "Winter", "Fall", "Spring"], "answer": "Summer"},
    {"question": "What do you build out of snow?", "choices": ["Snowman", "Sandcastle", "House", "Boat"], "answer": "Snowman"},
    {"question": "What happens to ice when it gets warm?", "choices": ["It melts", "It grows", "It freezes", "It evaporates"], "answer": "It melts"},
    {"question": "Can you see your breath in cold weather?", "choices": ["Yes", "No", "Only in summer", "Only in spring"], "answer": "Yes"},
    {"question": "What do leaves do in the fall?", "choices": ["They change color", "They grow", "They disappear", "They turn blue"], "answer": "They change color"},
    {"question": "What kind of weather happens in a desert?", "choices": ["Hot and dry", "Cold and snowy", "Wet and rainy", "Windy and cold"], "answer": "Hot and dry"},
    {"question": "What do clouds look like?", "choices": ["Fluffy and white", "Green and square", "Blue and round", "Clear and flat"], "answer": "Fluffy and white"},
    {"question": "What makes thunder?", "choices": ["Lightning", "Wind", "Snow", "Sunshine"], "answer": "Lightning"},
    {"question": "What causes lightning?", "choices": ["Electricity in the clouds", "Rain", "Snow", "Fog"], "answer": "Electricity in the clouds"},
    {"question": "What do we call frozen rain?", "choices": ["Hail", "Snow", "Raindrops", "Wind"], "answer": "Hail"},
    {"question": "What do you call a strong storm with wind and rain?", "choices": ["Hurricane", "Snowstorm", "Breeze", "Rainbow"], "answer": "Hurricane"},
    {"question": "How can you tell if it's going to rain?", "choices": ["Dark clouds", "Clear skies", "Sunshine", "Snow"], "answer": "Dark clouds"},
    {"question": "What do you wear on your head when it's cold?", "choices": ["Hat", "T-shirt", "Sandals", "Sunglasses"], "answer": "Hat"},
    {"question": "What season is known for flowers blooming?", "choices": ["Spring", "Summer", "Winter", "Fall"], "answer": "Spring"},
    {"question": "What happens when the sun sets?", "choices": ["It gets dark", "It gets warmer", "It starts raining", "It snows"], "answer": "It gets dark"},
    {"question": "What do you call the ice that forms on the grass in the morning?", "choices": ["Frost", "Snow", "Rain", "Clouds"], "answer": "Frost"},
    {"question": "Can you play outside when it's raining?", "choices": ["Yes, with rain gear", "No, never", "Only in summer", "Only with an umbrella"], "answer": "Yes, with rain gear"},
    {"question": "What season do we wear shorts in?", "choices": ["Summer", "Winter", "Spring", "Fall"], "answer": "Summer"},
    {"question": "What do you call a big storm with snow?", "choices": ["Blizzard", "Hurricane", "Thunderstorm", "Tornado"], "answer": "Blizzard"},
    {"question": "What helps plants grow?", "choices": ["Sun and rain", "Wind and snow", "Clouds and thunder", "Fog and hail"], "answer": "Sun and rain"},
    {"question": "What does hail look like?", "choices": ["Small ice balls", "Large raindrops", "Snowflakes", "Clouds"], "answer": "Small ice balls"},
    {"question": "Is fog thick or thin?", "choices": ["Thick", "Thin", "Clear", "Wet"], "answer": "Thick"},
    {"question": "What happens to the sun during the night?", "choices": ["It sets", "It rises", "It disappears", "It gets brighter"], "answer": "It sets"},
    {"question": "Do we see stars during the day?", "choices": ["No", "Yes", "Only sometimes", "Always"], "answer": "No"},
    {"question": "What is a breeze?", "choices": ["A light wind", "A strong wind", "A rainstorm", "A type of cloud"], "answer": "A light wind"}
]

MED_QUESTIONS = [
    {"question": "What type of cloud is associated with thunderstorms?", "choices": ["Cumulonimbus", "Cirrus", "Stratus", "Cumulus"], "answer": "Cumulonimbus"},
    {"question": "What is the boundary between two different air masses called?", "choices": ["Front", "Wind shear", "Jet stream", "Cyclone"], "answer": "Front"},
    {"question": "What is the main gas found in Earth's atmosphere?", "choices": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Hydrogen"], "answer": "Nitrogen"},
    {"question": "Which instrument is used to measure atmospheric pressure?", "choices": ["Barometer", "Anemometer", "Hygrometer", "Thermometer"], "answer": "Barometer"},
    {"question": "Which layer of the atmosphere contains the ozone layer?", "choices": ["Stratosphere", "Troposphere", "Mesosphere", "Thermosphere"], "answer": "Stratosphere"},
    {"question": "What is the process by which water vapor turns into liquid called?", "choices": ["Condensation", "Evaporation", "Sublimation", "Precipitation"], "answer": "Condensation"},
    {"question": "What is a tornado over water called?", "choices": ["Waterspout", "Cyclone", "Hurricane", "Tropical storm"], "answer": "Waterspout"},
    {"question": "What is the scale used to measure the strength of hurricanes?", "choices": ["Saffir-Simpson scale", "Fujita scale", "Richter scale", "Beaufort scale"], "answer": "Saffir-Simpson scale"},
    {"question": "Which wind belt is located near the equator?", "choices": ["Trade winds", "Westerlies", "Polar easterlies", "Jet stream"], "answer": "Trade winds"},
    {"question": "What is the greenhouse effect?", "choices": ["The warming of Earth's surface due to trapped heat", "Cooling of Earth's surface", "The creation of clouds", "The process of ozone depletion"], "answer": "The warming of Earth's surface due to trapped heat"},
    {"question": "Which type of cloud often indicates fair weather?", "choices": ["Cumulus", "Nimbus", "Cirrostratus", "Nimbostratus"], "answer": "Cumulus"},
    {"question": "What phenomenon causes the sky to appear blue?", "choices": ["Scattering of sunlight", "Reflection from water", "Absorption by ozone", "Refraction in the atmosphere"], "answer": "Scattering of sunlight"},
    {"question": "Which of the following is NOT a form of precipitation?", "choices": ["Dew", "Rain", "Snow", "Hail"], "answer": "Dew"},
    {"question": "What is a sudden downburst of wind during a storm called?", "choices": ["Microburst", "Tornado", "Gale", "Typhoon"], "answer": "Microburst"},
    {"question": "Which weather instrument measures wind speed?", "choices": ["Anemometer", "Barometer", "Hygrometer", "Rain gauge"], "answer": "Anemometer"},
    {"question": "What does a hygrometer measure?", "choices": ["Humidity", "Air pressure", "Temperature", "Wind speed"], "answer": "Humidity"},
    {"question": "What type of precipitation forms when raindrops freeze before hitting the ground?", "choices": ["Sleet", "Hail", "Snow", "Freezing rain"], "answer": "Sleet"},
    {"question": "What is the name for the line that separates areas of high and low pressure?", "choices": ["Isobar", "Isohyet", "Contour", "Isotherm"], "answer": "Isobar"},
    {"question": "What is the name of a narrow, high-speed wind current in the atmosphere?", "choices": ["Jet stream", "Trade winds", "Gulf Stream", "Westerlies"], "answer": "Jet stream"},
    {"question": "Which of the following clouds is the highest in the sky?", "choices": ["Cirrus", "Cumulus", "Stratus", "Nimbus"], "answer": "Cirrus"},
    {"question": "What type of weather phenomenon is El Niño associated with?", "choices": ["Warming of ocean waters in the Pacific", "Cooling of ocean waters", "Formation of hurricanes", "Global cooling"], "answer": "Warming of ocean waters in the Pacific"},
    {"question": "Which instrument is used to measure rainfall?", "choices": ["Rain gauge", "Barometer", "Anemometer", "Thermometer"], "answer": "Rain gauge"},
    {"question": "What term describes the amount of moisture in the air?", "choices": ["Humidity", "Precipitation", "Condensation", "Dew point"], "answer": "Humidity"},
    {"question": "What kind of front occurs when a cold air mass overtakes a warm air mass?", "choices": ["Cold front", "Warm front", "Stationary front", "Occluded front"], "answer": "Cold front"},
    {"question": "What is the main source of energy for weather patterns on Earth?", "choices": ["The Sun", "The Moon", "The Earth's core", "The atmosphere"], "answer": "The Sun"},
    {"question": "Which cloud type brings steady rain over a long period?", "choices": ["Nimbostratus", "Cumulonimbus", "Cirrus", "Altostratus"], "answer": "Nimbostratus"},
    {"question": "What is the Beaufort scale used to measure?", "choices": ["Wind speed", "Temperature", "Pressure", "Rainfall"], "answer": "Wind speed"},
    {"question": "What causes wind?", "choices": ["Differences in air pressure", "The rotation of the Earth", "Cloud formation", "Sunlight heating the air"], "answer": "Differences in air pressure"},
    {"question": "What is the term for the lowest layer of Earth's atmosphere?", "choices": ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"], "answer": "Troposphere"},
    {"question": "Which term refers to the process of water turning into vapor?", "choices": ["Evaporation", "Condensation", "Precipitation", "Transpiration"], "answer": "Evaporation"},
    {"question": "What is the wind speed required for a storm to be classified as a hurricane?", "choices": ["74 mph or higher", "100 mph or higher", "50 mph or higher", "150 mph or higher"], "answer": "74 mph or higher"},
    {"question": "What weather condition is measured by the heat index?", "choices": ["How hot it feels when humidity is factored in", "The actual air temperature", "Wind chill", "Dew point"], "answer": "How hot it feels when humidity is factored in"},
    {"question": "What does the Coriolis effect influence?", "choices": ["Wind direction", "Air pressure", "Humidity", "Cloud formation"], "answer": "Wind direction"},
    {"question": "What is the process by which plants release water into the atmosphere called?", "choices": ["Transpiration", "Condensation", "Evaporation", "Sublimation"], "answer": "Transpiration"},
    {"question": "What is a cyclone in the Southern Hemisphere called?", "choices": ["Cyclone", "Typhoon", "Hurricane", "Tornado"], "answer": "Cyclone"},
    {"question": "Which of the following is used to measure humidity?", "choices": ["Hygrometer", "Barometer", "Anemometer", "Thermometer"], "answer": "Hygrometer"},
    {"question": "What is a cold, fast-moving air current that moves down a mountain slope called?", "choices": ["Katabatic wind", "Jet stream", "Gale", "Chinook wind"], "answer": "Katabatic wind"},
    {"question": "Which weather event is measured using the Fujita scale?", "choices": ["Tornadoes", "Hurricanes", "Tsunamis", "Floods"], "answer": "Tornadoes"},
    {"question": "What kind of storm is a typhoon?", "choices": ["A tropical cyclone in the western Pacific Ocean", "A tornado", "A cold front storm", "A snowstorm"], "answer": "A tropical cyclone in the western Pacific Ocean"},
    {"question": "What is the point at which air becomes saturated with moisture called?", "choices": ["Dew point", "Condensation level", "Freezing point", "Cloud base"], "answer": "Dew point"},
    {"question": "What is the process of ice changing directly into water vapor called?", "choices": ["Sublimation", "Evaporation", "Condensation", "Precipitation"], "answer": "Sublimation"},
    {"question": "What is the name for a high-pressure system in the atmosphere?", "choices": ["Anticyclone", "Cyclone", "Typhoon", "Storm front"], "answer": "Anticyclone"},
    {"question": "What type of fog forms when cool air moves over warm water?", "choices": ["Steam fog", "Radiation fog", "Advection fog", "Valley fog"], "answer": "Steam fog"},
    {"question": "Which of these is not a type of cloud?", "choices": ["Cyclonus", "Nimbus", "Cumulonimbus", "Altocumulus"], "answer": "Cyclonus"},
    {"question": "What is the process of warm air rising and cool air sinking called?", "choices": ["Convection", "Radiation", "Advection", "Conduction"], "answer": "Convection"},
    {"question": "What is the name of the climate zone found near the poles?", "choices": ["Polar", "Tropical", "Temperate", "Subtropical"], "answer": "Polar"},
    {"question": "What happens during a temperature inversion?", "choices": ["Warm air is trapped above cool air", "Cold air sinks to the surface", "Clouds form in the upper atmosphere", "Winds blow from the poles"], "answer": "Warm air is trapped above cool air"},
    {"question": "What type of front is formed when two air masses meet but neither is strong enough to move the other?", "choices": ["Stationary front", "Cold front", "Warm front", "Occluded front"], "answer": "Stationary front"},
    {"question": "What is the term for a period of abnormally dry weather that causes significant water shortages?", "choices": ["Drought", "Monsoon", "Flood", "Heatwave"], "answer": "Drought"},
    {"question": "Which type of precipitation occurs when rain passes through a layer of freezing air near the ground?", "choices": ["Freezing rain", "Sleet", "Hail", "Snow"], "answer": "Freezing rain"},
    {"question": "What do we call the white, fluffy things in the sky?", "choices": ["Clouds", "Stars", "Birds", "Planes"], "answer": "Clouds"},
    {"question": "What happens when the temperature drops below freezing?", "choices": ["It snows", "It rains", "It gets foggy", "It gets sunny"], "answer": "It snows"},
    {"question": "What do we use to measure temperature?", "choices": ["Thermometer", "Barometer", "Compass", "Rain gauge"], "answer": "Thermometer"},
    {"question": "Which season is usually the warmest?", "choices": ["Summer", "Winter", "Spring", "Fall"], "answer": "Summer"},
    {"question": "What do you wear to protect your head when it's sunny?", "choices": ["Hat", "Scarf", "Gloves", "Boots"], "answer": "Hat"}
]

HARD_QUESTIONS = [
    {"question": "What phenomenon causes winds to deflect to the right in the Northern Hemisphere?", "choices": ["Coriolis effect", "Jet stream", "Turbulence", "Ekman spiral"], "answer": "Coriolis effect"},
    {"question": "What term describes a large-scale system of winds rotating around a low-pressure center?", "choices": ["Cyclone", "Anticyclone", "Doldrums", "Monsoon"], "answer": "Cyclone"},
    {"question": "Which type of cloud is found in the middle of the troposphere and often signals changing weather?", "choices": ["Altostratus", "Cumulonimbus", "Cirrostratus", "Stratus"], "answer": "Altostratus"},
    {"question": "What is the primary driver of ocean currents that affect global weather patterns?", "choices": ["Wind", "Moon's gravity", "Earth's rotation", "Ocean temperature"], "answer": "Wind"},
    {"question": "Which process is responsible for the transfer of heat through fluid movement in the atmosphere?", "choices": ["Convection", "Conduction", "Radiation", "Sublimation"], "answer": "Convection"},
    {"question": "Which of the following describes the temperature at which water vapor condenses into liquid?", "choices": ["Dew point", "Humidity", "Saturation point", "Freezing point"], "answer": "Dew point"},
    {"question": "What type of fog forms when warm, moist air moves over a cooler surface?", "choices": ["Advection fog", "Radiation fog", "Steam fog", "Valley fog"], "answer": "Advection fog"},
    {"question": "What is the process by which clouds form due to rising warm air that cools and condenses?", "choices": ["Convection", "Orographic lifting", "Convergence", "Radiation"], "answer": "Convection"},
    {"question": "What is the name of the effect that causes coastal areas to have milder climates than inland areas?", "choices": ["Maritime effect", "Continental effect", "Oceanic buffer", "Sea breeze effect"], "answer": "Maritime effect"},
    {"question": "What term describes the sudden, sharp rise in water level caused by a storm, often associated with hurricanes?", "choices": ["Storm surge", "Tsunami", "Flash flood", "Rip current"], "answer": "Storm surge"},
    {"question": "What is the name of the boundary where two different air masses meet?", "choices": ["Front", "Jet stream", "Pressure ridge", "Trough"], "answer": "Front"},
    {"question": "Which type of cloud is responsible for producing heavy precipitation and thunderstorms?", "choices": ["Cumulonimbus", "Stratus", "Altocumulus", "Nimbostratus"], "answer": "Cumulonimbus"},
    {"question": "Which weather phenomenon is caused by the rapid upward movement of warm, moist air?", "choices": ["Thunderstorm", "Cold front", "Tornado", "Hailstorm"], "answer": "Thunderstorm"},
    {"question": "What is the term for a powerful downdraft of air that can cause significant damage, often associated with thunderstorms?", "choices": ["Microburst", "Tornado", "Cyclone", "Derecho"], "answer": "Microburst"},
    {"question": "Which global wind pattern affects the weather in the mid-latitudes and drives the movement of weather systems?", "choices": ["Westerlies", "Trade winds", "Polar easterlies", "Jet stream"], "answer": "Westerlies"},
    {"question": "What type of front forms when a cold air mass overtakes a warm air mass, lifting the warm air aloft?", "choices": ["Occluded front", "Warm front", "Cold front", "Stationary front"], "answer": "Occluded front"},
    {"question": "What is the term for the horizontal movement of air in the atmosphere?", "choices": ["Advection", "Convection", "Diffusion", "Conduction"], "answer": "Advection"},
    {"question": "What causes a rain shadow effect on the leeward side of mountains?", "choices": ["Orographic lifting", "Convection currents", "Adiabatic cooling", "Subduction"], "answer": "Orographic lifting"},
    {"question": "Which weather event occurs when cold air rapidly displaces warm air, often causing severe storms?", "choices": ["Cold front", "Occluded front", "Warm front", "Tropical depression"], "answer": "Cold front"},
    {"question": "What term refers to the temperature change that occurs when air is compressed or expands without exchanging heat?", "choices": ["Adiabatic process", "Convection", "Radiative cooling", "Latent heat"], "answer": "Adiabatic process"},
    {"question": "Which weather phenomenon occurs when a high-pressure system causes warm, dry air to descend from a mountain?", "choices": ["Chinook wind", "Foehn wind", "Sirocco", "Monsoon"], "answer": "Chinook wind"},
    {"question": "What is the term for the scale that measures the intensity of tornadoes?", "choices": ["Enhanced Fujita scale", "Saffir-Simpson scale", "Richter scale", "Beaufort scale"], "answer": "Enhanced Fujita scale"},
    {"question": "Which type of precipitation forms when snow partially melts and then refreezes before hitting the ground?", "choices": ["Sleet", "Freezing rain", "Graupel", "Hail"], "answer": "Sleet"},
    {"question": "What is the term for the steady flow of ocean water caused by the wind, Earth's rotation, and temperature differences?", "choices": ["Ocean current", "Rip current", "Upwelling", "Thermocline"], "answer": "Ocean current"},
    {"question": "Which phenomenon is characterized by the periodic warming of ocean surface waters in the central and eastern Pacific Ocean?", "choices": ["El Niño", "La Niña", "Southern Oscillation", "Upwelling"], "answer": "El Niño"},
    {"question": "Which weather phenomenon occurs when strong, sustained winds push water against the coast, often causing flooding?", "choices": ["Storm surge", "Tsunami", "Upwelling", "Rip current"], "answer": "Storm surge"},
    {"question": "What is the process by which cold, nutrient-rich water from deep in the ocean rises to the surface?", "choices": ["Upwelling", "Downwelling", "El Niño", "Thermocline"], "answer": "Upwelling"},
    {"question": "What is the term for the shift in wind patterns and weather systems caused by El Niño and La Niña?", "choices": ["Southern Oscillation", "Monsoon effect", "Jet stream", "Polar vortex"], "answer": "Southern Oscillation"},
    {"question": "Which type of cloud forms at high altitudes and appears thin, wispy, and made of ice crystals?", "choices": ["Cirrus", "Stratus", "Cumulus", "Altostratus"], "answer": "Cirrus"},
    {"question": "What is the name of the line on a weather map that connects points of equal atmospheric pressure?", "choices": ["Isobar", "Isotherm", "Contour line", "Isohyet"], "answer": "Isobar"},
    {"question": "What is the term for the temperature difference between the actual air temperature and the temperature it feels like due to wind?", "choices": ["Wind chill", "Heat index", "Dew point", "Thermal gradient"], "answer": "Wind chill"},
    {"question": "Which layer of the Earth's atmosphere is where most weather occurs?", "choices": ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"], "answer": "Troposphere"},
    {"question": "Which global wind pattern flows from the west to the east and is strongest in the upper atmosphere?", "choices": ["Jet stream", "Trade winds", "Westerlies", "Polar easterlies"], "answer": "Jet stream"},
    {"question": "Which atmospheric layer contains the ozone layer that protects the Earth from harmful ultraviolet radiation?", "choices": ["Stratosphere", "Troposphere", "Mesosphere", "Thermosphere"], "answer": "Stratosphere"}
]

# --- Application Setup ---
class WeatherQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Trivia Quiz")
        self.root.geometry("600x500")
        self.root.minsize(500, 400)

        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.questions = []
        self.current_q_index = 0
        self.score = 0

        self.setup_start_screen()

    def setup_start_screen(self):
        """Builds the main menu frame."""
        self.clear_window()

        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill="both")

        title_label = ttk.Label(frame, text="Weather Trivia Quiz", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=20)

        subtitle_label = ttk.Label(frame, text="Select Difficulty Level:", font=("Helvetica", 12))
        subtitle_label.pack(pady=10)

        self.diff_var = tk.StringVar(value="Easy")
        diff_options = [("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard"), ("All Mixed", "All")]

        for text, value in diff_options:
            rb = ttk.Radiobutton(frame, text=text, value=value, variable=self.diff_var)
            rb.pack(anchor="center", pady=5)

        start_btn = ttk.Button(frame, text="Start Quiz", command=self.start_quiz)
        start_btn.pack(pady=25)

    def start_quiz(self):
        """Initializes the quiz parameters based on user selection."""
        difficulty = self.diff_var.get()
        
        if difficulty == "Easy":
            self.questions = EASY_QUESTIONS.copy()
        elif difficulty == "Medium":
            self.questions = MED_QUESTIONS.copy()
        elif difficulty == "Hard":
            self.questions = HARD_QUESTIONS.copy()
        else:
            self.questions = EASY_QUESTIONS + MED_QUESTIONS + HARD_QUESTIONS

        random.shuffle(self.questions)
        self.current_q_index = 0
        self.score = 0
        
        self.setup_quiz_screen()
        self.show_question()

    def setup_quiz_screen(self):
        """Builds the interactive quiz UI."""
        self.clear_window()

        self.quiz_frame = ttk.Frame(self.root, padding="20")
        self.quiz_frame.pack(expand=True, fill="both")

        # Top Bar: Progress and Score
        top_frame = ttk.Frame(self.quiz_frame)
        top_frame.pack(fill="x", pady=5)

        self.progress_label = ttk.Label(top_frame, text="", font=("Helvetica", 10, "italic"))
        self.progress_label.pack(side="left")

        self.score_label = ttk.Label(top_frame, text="Score: 0", font=("Helvetica", 10, "bold"))
        self.score_label.pack(side="right")

        # Question Text
        self.q_label = ttk.Label(self.quiz_frame, text="", font=("Helvetica", 13, "bold"), wraplength=520, justify="center")
        self.q_label.pack(pady=25)

        # Answer Options Buttons
        self.opt_buttons = []
        for i in range(4):
            btn = ttk.Button(self.quiz_frame, text="", command=lambda idx=i: self.check_answer(idx))
            btn.pack(fill="x", pady=5, ipady=5)
            self.opt_buttons.append(btn)

        # Feedback Message Label
        self.feedback_label = ttk.Label(self.quiz_frame, text="", font=("Helvetica", 11, "bold"))
        self.feedback_label.pack(pady=15)

    def show_question(self):
        """Populates the UI controls with current question data."""
        q_data = self.questions[self.current_q_index]

        self.progress_label.config(text=f"Question {self.current_q_index + 1} of {len(self.questions)}")
        self.score_label.config(text=f"Score: {self.score}")
        self.q_label.config(text=q_data["question"])
        self.feedback_label.config(text="")

        choices = q_data["choices"].copy()
        # Ensure choices are shuffled so correct answer position isn't static
        random.shuffle(choices)
        self.current_choices = choices

        for i in range(4):
            self.opt_buttons[i].config(text=choices[i], state="normal")

    def check_answer(self, choice_idx):
        """Evaluates chosen answer and moves to the next turn."""
        selected_text = self.current_choices[choice_idx]
        correct_text = self.questions[self.current_q_index]["answer"]

        # Disable all option buttons during evaluation
        for btn in self.opt_buttons:
            btn.config(state="disabled")

        if selected_text == correct_text:
            self.score += 1
            self.feedback_label.config(text="Correct!", foreground="green")
        else:
            self.feedback_label.config(text=f"Incorrect! Answer: {correct_text}", foreground="red")

        # Wait 1.25 seconds before moving to next question
        self.root.after(1250, self.next_question)

    def next_question(self):
        """Advances question index or completes quiz."""
        self.current_q_index += 1
        if self.current_q_index < len(self.questions):
            self.show_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        """Displays completion results and option to restart."""
        total = len(self.questions)
        pct = (self.score / total) * 100
        
        messagebox.showinfo(
            "Quiz Complete!", 
            f"Final Score: {self.score} / {total}\nPercentage: {pct:.1f}%"
        )
        self.setup_start_screen()

    def clear_window(self):
        """Removes existing widgets from root window."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherQuizApp(root)
    root.mainloop()
