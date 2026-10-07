import streamlit as st

# ============================================================
# SMART DIE CASTING ENGINEERING APP
# HPDC + HOT CHAMBER | LEARNING | QUIZ | EXERCISES | CALCULATORS
# ============================================================

st.set_page_config(
    page_title="Smart Die Casting Engineering App",
    page_icon="⚙️",
    layout="wide"
)

# ----------------------------- DATA -----------------------------

PARTS = {
    "Honda 70 / Small Motorcycle": [
        "Engine covers", "Side covers", "Brackets", "Small housings",
        "Levers and small aluminium components"
    ],
    "Chingchi / Three-Wheeler": [
        "Engine covers", "Aluminium housings", "Brackets",
        "Transmission-related housings", "Small mechanical parts"
    ],
    "Millat Tractor": [
        "Aluminium covers", "Housings", "Brackets",
        "Pump-related components", "Transmission-related components"
    ],
    "Other Motorcycles / Bikes": [
        "Clutch covers", "Engine covers", "Brake-related housings",
        "Brackets", "Small aluminium housings"
    ],
    "Automotive / Industrial": [
        "Gearbox housings", "Motor housings", "Covers",
        "Brackets", "Pulleys and other non-ferrous components"
    ]
}

DEFECTS = {
    "Porosity": {
        "causes": ["Gas entrapment", "Poor venting", "Turbulent filling",
                   "Excess lubricant", "Shrinkage"],
        "solutions": ["Improve venting", "Optimize injection velocity",
                      "Check vacuum/air evacuation", "Control lubricant",
                      "Optimize pressure and cooling"]
    },
    "Misrun": {
        "causes": ["Low metal temperature", "Low die temperature",
                   "Slow filling", "Thin section", "Poor gating"],
        "solutions": ["Optimize metal temperature", "Control die temperature",
                      "Optimize injection speed", "Review gating and thin sections"]
    },
    "Cold Shut": {
        "causes": ["Two metal fronts meet without fusion",
                   "Low metal temperature", "Slow filling", "Poor gate location"],
        "solutions": ["Optimize metal/die temperature", "Optimize filling speed",
                      "Improve gate location", "Improve flow pattern"]
    },
    "Flash": {
        "causes": ["High pressure", "Low clamping force",
                   "Die misalignment", "Damaged parting surface", "Die wear"],
        "solutions": ["Check pressure", "Check clamping force",
                      "Align die", "Repair parting surface", "Inspect die wear"]
    },
    "Shrinkage": {
        "causes": ["Solidification shrinkage", "Hot spots",
                   "Improper pressure", "Uneven cooling"],
        "solutions": ["Optimize pressure", "Improve cooling",
                      "Reduce hot spots", "Review die design"]
    },
    "Blisters": {
        "causes": ["Trapped gas", "Poor venting", "Excess lubricant",
                   "Gas expansion during heating"],
        "solutions": ["Improve venting", "Control lubricant",
                      "Optimize filling", "Check vacuum system"]
    },
    "Die Soldering": {
        "causes": ["High die temperature", "Aluminium sticking",
                   "Poor lubrication", "High metal velocity"],
        "solutions": ["Control die temperature", "Use suitable lubricant",
                      "Optimize velocity", "Clean and inspect die surface"]
    },
    "Cracks": {
        "causes": ["Thermal stress", "Residual stress",
                   "Uneven cooling", "Poor design", "Premature ejection"],
        "solutions": ["Balance cooling", "Reduce thermal stress",
                      "Improve design", "Check ejection timing"]
    },
    "Cold Flow": {
        "causes": ["Poor metal flow", "Low metal temperature",
                   "Low die temperature", "Poor gate location"],
        "solutions": ["Optimize temperatures", "Improve gate location",
                      "Optimize injection speed"]
    },
    "Erosion": {
        "causes": ["High metal velocity", "High temperature",
                   "Poor gate design", "Thermal cycling"],
        "solutions": ["Optimize velocity", "Control temperature",
                      "Improve gate design", "Inspect die material/surface"]
    }
}

LEARNING = {
    "1. What is Die Casting?": (
        "Die casting is a manufacturing process in which molten non-ferrous "
        "metal is forced into a reusable metal die. The die gives the casting "
        "its required shape and dimensions.",
        ["High production rate", "Good dimensional accuracy",
         "Good surface finish", "Complex shapes are possible",
         "Common alloys include aluminium, zinc and magnesium"]
    ),
    "2. HPDC": (
        "High Pressure Die Casting (HPDC) uses high-speed, high-pressure "
        "injection to fill a reusable die. It is widely used for high-volume "
        "production of aluminium components.",
        ["Fast filling", "High production", "Thin sections possible",
         "Good repeatability", "Venting and gas evacuation are important",
         "Injection pressure and velocity must be controlled"]
    ),
    "3. Hot Chamber Die Casting": (
        "In hot chamber die casting, the injection mechanism is immersed in "
        "or directly connected to the molten metal supply. This can provide "
        "rapid cycles, but alloy compatibility with the machine is important.",
        ["Fast cycle", "Injection system remains with molten metal",
         "Commonly used with suitable lower-melting-point alloys",
         "Good for high-volume small/medium parts",
         "Machine and alloy compatibility must be checked"]
    ),
    "4. HPDC vs Hot Chamber": (
        "HPDC describes the high-pressure filling process, while hot chamber "
        "describes the arrangement of the injection system. A hot-chamber "
        "machine is a type of high-pressure die-casting setup when it uses "
        "high-pressure injection.",
        ["HPDC = process/filling method",
         "Hot chamber = injection-system arrangement",
         "Cold chamber uses a separate shot of molten metal",
         "Alloy selection depends on machine and process"]
    ),
    "5. Die Components": (
        "A die contains the cavity and supporting systems that control filling, "
        "cooling and ejection.",
        ["Fixed die", "Moving die", "Cavity", "Core", "Runner", "Gate",
         "Vent", "Overflow", "Cooling channels", "Ejector pins"]
    ),
    "6. Injection System": (
        "The injection system transfers molten metal into the die. Filling "
        "velocity, pressure and timing strongly affect casting quality.",
        ["Plunger", "Shot sleeve for cold chamber machines",
         "Injection velocity", "Injection pressure",
         "Intensification/holding pressure"]
    ),
    "7. Die Cooling": (
        "Cooling channels remove heat from the die and help maintain a suitable "
        "thermal condition for stable production.",
        ["Controls die temperature", "Controls solidification",
         "Influences cycle time", "Helps dimensional stability",
         "Uneven cooling can create thermal stress"]
    ),
    "8. Die Venting": (
        "Venting provides a path for air and gases to leave the cavity during "
        "filling. Poor venting can contribute to gas-related defects.",
        ["Reduces trapped gas", "Improves filling",
         "Helps reduce gas porosity", "Vacuum can improve gas evacuation"]
    ),
    "9. Die Lubrication": (
        "Die lubricant helps release the casting and reduce sticking. The "
        "amount and application must be controlled.",
        ["Reduces sticking", "Assists ejection",
         "Can affect die temperature", "Excess lubricant can create gas"]
    ),
    "10. Common Defects": (
        "Casting defects may result from incorrect temperature, pressure, "
        "velocity, venting, cooling, lubrication or die condition.",
        list(DEFECTS.keys())
    ),
    "11. Important Process Parameters": (
        "Process parameters are variables that control filling, solidification "
        "and production stability.",
        ["Metal temperature", "Die temperature", "Injection velocity",
         "Injection pressure", "Filling time", "Cooling time",
         "Lubricant quantity", "Venting", "Clamping force", "Cycle time"]
    ),
    "12. Applications and Parts": (
        "Die casting is widely used for motorcycle, three-wheeler, tractor, "
        "automotive and industrial non-ferrous components.",
        ["Honda 70-type small motorcycle parts", "Chingchi parts",
         "Millat tractor aluminium parts", "Other bike parts",
         "Automotive housings", "Industrial brackets and covers"]
    )
}

MCQS = [
    ("What is the main purpose of a die?",
     ["Give the casting its shape", "Melt the metal", "Remove all defects", "Increase voltage"], 0),
    ("Which defect is commonly associated with trapped gas?",
     ["Porosity", "Flash", "Erosion", "Misalignment"], 0),
    ("What is the main purpose of venting?",
     ["Allow air/gas to escape", "Increase casting weight", "Melt the die", "Increase lubricant"], 0),
    ("Metal freezes before filling the cavity completely. Which defect can result?",
     ["Misrun", "Flash", "Blister", "Erosion"], 0),
    ("Which parameter directly affects filling speed?",
     ["Injection velocity", "Paint colour", "Room lighting", "Machine label"], 0),
    ("Excessive pressure may contribute to which defect?",
     ["Flash", "Perfect venting", "Zero defects", "No die wear"], 0),
    ("What do cooling channels do?",
     ["Control die temperature", "Melt the die", "Heat the room", "Remove ejectors"], 0),
    ("Which component helps push the casting out?",
     ["Ejector pin", "Runner", "Vent", "Gate"], 0),
    ("Casting yield is generally useful casting mass divided by:",
     ["Total shot mass", "Die mass", "Lubricant mass", "Machine mass"], 0),
    ("Aluminium sticking to a die surface is called:",
     ["Die soldering", "Misrun", "Cold shut", "Shrinkage"], 0),
    ("Which parameter affects solidification?",
     ["Die temperature", "Screen brightness", "Machine colour", "Operator handwriting"], 0),
    ("Poor venting can increase the risk of:",
     ["Gas porosity", "Perfect filling", "Lower gas", "No defects"], 0),
    ("A runner primarily:",
     ["Carries molten metal toward the cavity", "Pushes the casting out",
      "Cools the machine", "Measures hardness"], 0),
    ("A gate primarily controls:",
     ["Entry of metal into the cavity", "Room temperature",
      "Die hardness", "Machine voltage"], 0),
    ("A hot chamber system has its injection system:",
     ["Directly associated with the molten metal supply",
      "Always outside the factory", "Inside the cooling water tank", "In the ejector pin"], 0)
]

TRUE_FALSE = [
    ("Poor die venting can contribute to gas porosity.", True),
    ("Misrun means excessive flash at the parting line.", False),
    ("Injection velocity affects metal filling behaviour.", True),
    ("Cooling has no effect on die temperature.", False),
    ("Ejector pins help remove the casting.", True),
    ("Flash can be related to low clamping force.", True),
    ("Hot chamber means the injection system is directly associated with molten metal.", True),
    ("A runner and a gate perform exactly the same function.", False)
]

# ----------------------------- HELPERS -----------------------------

def show_header(title, subtitle=""):
    st.header(title)
    if subtitle:
        st.write(subtitle)

# ----------------------------- SIDEBAR -----------------------------

st.sidebar.title("⚙️ Smart Die Casting App")
menu = st.sidebar.radio(
    "Select Section",
    [
        "🏠 Home",
        "🔍 Problems & Solutions",
        "🧮 Calculators",
        "📖 Learning Center",
        "📝 Quiz",
        "🎯 Exercises",
        "🔩 Parts & Applications"
    ]
)

# ----------------------------- HOME -----------------------------

if menu == "🏠 Home":
    show_header(
        "Smart Die Casting Engineering App",
        "A student-friendly tool for HPDC and Hot Chamber Die Casting."
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Processes", "2")
    c2.metric("Defects", len(DEFECTS))
    c3.metric("Learning Topics", len(LEARNING))
    c4.metric("MCQs", len(MCQS))

    st.divider()
    st.subheader("What can you study here?")
    for x in [
        "HPDC fundamentals and process parameters",
        "Hot Chamber Die Casting",
        "Motorcycle, Chingchi and tractor applications",
        "Casting defects and troubleshooting",
        "Engineering calculators",
        "Learning Center",
        "MCQs and True/False quiz",
        "Beginner to advanced exercises"
    ]:
        st.write("• " + x)

# ----------------------------- PROBLEMS -----------------------------

elif menu == "🔍 Problems & Solutions":
    show_header("🔍 Problems & Solutions",
                "Select a process, application and defect to get possible causes and corrective actions.")

    process = st.selectbox("Process", ["HPDC", "Hot Chamber Die Casting"])
    application = st.selectbox("Application", list(PARTS.keys()))
    problem = st.selectbox("Casting Problem", list(DEFECTS.keys()))

    st.info(f"Process: {process} | Application: {application} | Problem: {problem}")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("⚠️ Possible Causes")
        for x in DEFECTS[problem]["causes"]:
            st.write("• " + x)

    with col2:
        st.subheader("🛠️ Possible Solutions")
        for x in DEFECTS[problem]["solutions"]:
            st.write("• " + x)

    st.warning(
        "These are educational troubleshooting guidelines. Actual production "
        "parameters should be confirmed with the machine, alloy, die and process data."
    )

# ----------------------------- CALCULATORS -----------------------------

elif menu == "🧮 Calculators":
    show_header("🧮 HPDC & Hot Chamber Calculators")

    calc = st.selectbox(
        "Choose Calculator",
        [
            "Clamping Force",
            "Injection Force",
            "Metal Volume",
            "Shot Weight",
            "Casting Yield",
            "Cycle Time",
            "Production Rate",
            "Parts per Day",
            "Material Mass",
            "Runner Ratio",
            "Metal Fill Rate",
            "Filling Time from Volume and Flow Rate"
        ]
    )

    if calc == "Clamping Force":
        st.subheader("Clamping Force")
        area = st.number_input("Projected Area (cm²)", min_value=0.0, value=250.0)
        pressure = st.number_input("Effective Pressure (MPa)", min_value=0.0, value=70.0)
        safety = st.number_input("Safety Factor", min_value=1.0, value=1.10)
        if st.button("Calculate"):
            force_kn = area * 100 * pressure / 1000
            force_ton = force_kn / 9.80665
            required = force_ton * safety
            st.success(f"Base force = {force_kn:.2f} kN = {force_ton:.2f} ton-force")
            st.success(f"With safety factor = {required:.2f} ton-force")

    elif calc == "Injection Force":
        area = st.number_input("Plunger/Effective Area (cm²)", min_value=0.0, value=50.0)
        pressure = st.number_input("Injection Pressure (MPa)", min_value=0.0, value=70.0)
        if st.button("Calculate"):
            force_kn = area * 100 * pressure / 1000
            st.success(f"Injection force = {force_kn:.2f} kN")

    elif calc == "Metal Volume":
        mass = st.number_input("Metal Mass (g)", min_value=0.0, value=540.0)
        density = st.number_input("Density (g/cm³)", min_value=0.01, value=2.70)
        if st.button("Calculate"):
            st.success(f"Volume = {mass / density:.2f} cm³")

    elif calc == "Shot Weight":
        casting = st.number_input("Casting Mass (kg)", min_value=0.0, value=7.5)
        runner = st.number_input("Runner + Biscuit Mass (kg)", min_value=0.0, value=1.5)
        overflow = st.number_input("Overflow Mass (kg)", min_value=0.0, value=0.5)
        if st.button("Calculate"):
            st.success(f"Shot weight = {casting + runner + overflow:.2f} kg")

    elif calc == "Casting Yield":
        good = st.number_input("Good Casting Mass (kg)", min_value=0.0, value=8.0)
        shot = st.number_input("Total Shot Mass (kg)", min_value=0.001, value=10.0)
        if st.button("Calculate"):
            st.success(f"Casting yield = {(good / shot) * 100:.2f}%")

    elif calc == "Cycle Time":
        filling = st.number_input("Filling Time (s)", min_value=0.0, value=0.10)
        solidification = st.number_input("Solidification/Cooling Time (s)", min_value=0.0, value=8.0)
        ejection = st.number_input("Ejection Time (s)", min_value=0.0, value=2.0)
        other = st.number_input("Other Time (s)", min_value=0.0, value=3.0)
        if st.button("Calculate"):
            total = filling + solidification + ejection + other
            st.success(f"Total cycle time = {total:.2f} s")

    elif calc == "Production Rate":
        cycle = st.number_input("Cycle Time (s)", min_value=0.01, value=30.0)
        cavities = st.number_input("Number of Cavities", min_value=1, value=1, step=1)
        if st.button("Calculate"):
            st.success(f"Theoretical production = {(3600 / cycle) * cavities:.2f} parts/hour")

    elif calc == "Parts per Day":
        hourly = st.number_input("Theoretical Parts/Hour", min_value=0.0, value=120.0)
        hours = st.number_input("Operating Hours/Day", min_value=0.0, value=8.0)
        efficiency = st.number_input("Efficiency (%)", min_value=0.0, max_value=100.0, value=85.0)
        if st.button("Calculate"):
            st.success(f"Estimated parts/day = {hourly * hours * efficiency / 100:.0f}")

    elif calc == "Material Mass":
        volume = st.number_input("Volume (cm³)", min_value=0.0, value=100.0)
        density = st.number_input("Density (g/cm³)", min_value=0.01, value=2.70)
        if st.button("Calculate"):
            st.success(f"Mass = {volume * density:.2f} g")

    elif calc == "Runner Ratio":
        casting = st.number_input("Casting Mass (g)", min_value=0.01, value=500.0)
        runner = st.number_input("Runner + Biscuit Mass (g)", min_value=0.0, value=100.0)
        if st.button("Calculate"):
            ratio = runner / casting
            st.success(f"Runner-to-casting ratio = {ratio:.3f}:1")

    elif calc == "Metal Fill Rate":
        volume = st.number_input("Cavity Volume (cm³)", min_value=0.01, value=100.0)
        time = st.number_input("Filling Time (s)", min_value=0.001, value=0.10)
        if st.button("Calculate"):
            st.success(f"Average fill rate = {volume / time:.2f} cm³/s")

    elif calc == "Filling Time from Volume and Flow Rate":
        volume = st.number_input("Cavity Volume (cm³)", min_value=0.01, value=100.0)
        flow = st.number_input("Average Flow Rate (cm³/s)", min_value=0.01, value=1000.0)
        if st.button("Calculate"):
            st.success(f"Estimated filling time = {volume / flow:.4f} s")

    st.caption(
        "Calculator results are simplified educational calculations; real die-casting "
        "design uses machine, die, alloy, flow and safety data."
    )

# ----------------------------- LEARNING CENTER -----------------------------

elif menu == "📖 Learning Center":
    show_header(
        "📖 Learning Center",
        "Read the topic, revise the important points, then test yourself in the Quiz."
    )

    topic = st.selectbox("Choose Topic", list(LEARNING.keys()))
    explanation, points = LEARNING[topic]

    st.subheader("📌 Simple Explanation")
    st.write(explanation)

    st.subheader("📚 Important Points")
    for p in points:
        st.write("• " + p)

    with st.expander("🎓 Quick Viva Questions"):
        if "HPDC" in topic:
            st.write("Q: What does HPDC mean?")
            st.write("A: High Pressure Die Casting.")
            st.write("Q: Why is high injection velocity important?")
            st.write("A: It helps fill the die rapidly before premature solidification.")
        elif "Hot Chamber" in topic:
            st.write("Q: What is special about a hot chamber machine?")
            st.write("A: Its injection system is directly associated with the molten metal supply.")
        elif "Defect" in topic or "Common" in topic:
            st.write("Q: Name common die-casting defects.")
            st.write("A: Porosity, misrun, cold shut, flash, shrinkage, blisters and soldering.")
        else:
            st.write("Q: Why is this topic important?")
            st.write("A: It helps understand process control, quality and troubleshooting.")

# ----------------------------- QUIZ -----------------------------

elif menu == "📝 Quiz":
    show_header("📝 Die Casting Quiz", "Practice MCQs, True/False and a mixed quiz.")

    quiz_type = st.radio("Quiz Type", ["MCQs", "True / False", "Mixed Quiz"], horizontal=True)

    if quiz_type == "MCQs":
        answers = []
        for i, (q, options, correct) in enumerate(MCQS):
            ans = st.radio(f"{i+1}. {q}", options, key=f"mcq_{i}")
            answers.append(options.index(ans))

        if st.button("✅ Check MCQ Result"):
            score = sum(a == MCQS[i][2] for i, a in enumerate(answers))
            pct = score / len(MCQS) * 100
            st.success(f"Score: {score}/{len(MCQS)}  |  {pct:.1f}%")
            if pct >= 80:
                st.balloons()
                st.success("Excellent performance!")
            elif pct >= 60:
                st.info("Good work. Revise weak topics and try again.")
            else:
                st.warning("Review the Learning Center and practice again.")

    elif quiz_type == "True / False":
        answers = []
        for i, (q, correct) in enumerate(TRUE_FALSE):
            ans = st.radio(f"{i+1}. {q}", ["True", "False"], key=f"tf_{i}")
            answers.append(ans == "True")

        if st.button("✅ Check True/False Result"):
            score = sum(a == TRUE_FALSE[i][1] for i, a in enumerate(answers))
            pct = score / len(TRUE_FALSE) * 100
            st.success(f"Score: {score}/{len(TRUE_FALSE)}  |  {pct:.1f}%")

    else:
        st.write("### Part A — MCQs")
        mixed_mcq = MCQS[:6]
        mcq_answers = []
        for i, (q, options, correct) in enumerate(mixed_mcq):
            ans = st.radio(f"{i+1}. {q}", options, key=f"mixm_{i}")
            mcq_answers.append(options.index(ans))

        st.write("### Part B — True / False")
        mixed_tf = TRUE_FALSE[:4]
        tf_answers = []
        for i, (q, correct) in enumerate(mixed_tf):
            ans = st.radio(f"{i+7}. {q}", ["True", "False"], key=f"mixt_{i}")
            tf_answers.append(ans == "True")

        if st.button("✅ Check Mixed Quiz"):
            score = sum(a == mixed_mcq[i][2] for i, a in enumerate(mcq_answers))
            score += sum(a == mixed_tf[i][1] for i, a in enumerate(tf_answers))
            total = len(mixed_mcq) + len(mixed_tf)
            pct = score / total * 100
            st.success(f"Score: {score}/{total}  |  {pct:.1f}%")

# ----------------------------- EXERCISES -----------------------------

elif menu == "🎯 Exercises":
    show_header(
        "🎯 Engineering Exercises",
        "Move from simple concepts to calculations and troubleshooting."
    )

    level = st.selectbox(
        "Difficulty",
        ["Level 1 — Beginner", "Level 2 — Basic",
         "Level 3 — Intermediate", "Level 4 — Advanced"]
    )

    if level == "Level 1 — Beginner":
        st.subheader("🟢 Beginner")
        questions = [
            "Define die casting in your own words.",
            "What is HPDC?",
            "What is hot chamber die casting?",
            "Name five die components.",
            "What is porosity?",
            "Why is venting important?",
            "What is the function of an ejector pin?"
        ]
        answers = [
            "Die casting forces molten non-ferrous metal into a reusable die.",
            "HPDC means High Pressure Die Casting.",
            "It is a high-pressure process with the injection system directly associated with molten metal.",
            "Cavity, core, runner, gate, vent, cooling channels and ejector pins are examples.",
            "Porosity is unwanted void space caused by gas or shrinkage.",
            "Venting allows air and gases to escape.",
            "Ejector pins help remove the solidified casting."
        ]
        for i, q in enumerate(questions):
            st.write(f"**{i+1}. {q}**")
        with st.expander("💡 Show Answers"):
            for a in answers:
                st.write("• " + a)

    elif level == "Level 2 — Basic":
        st.subheader("🟡 Basic Engineering")
        st.write("**1.** A casting mass is 540 g and density is 2.70 g/cm³. Calculate volume.")
        if st.button("Answer 1"):
            st.success("Volume = Mass/Density = 540/2.70 = 200 cm³")

        st.write("**2.** Good casting mass = 8 kg and total shot = 10 kg. Calculate yield.")
        if st.button("Answer 2"):
            st.success("Yield = 8/10 × 100 = 80%")

        st.write("**3.** Cycle time is 30 s and there is one cavity. Calculate parts/hour.")
        if st.button("Answer 3"):
            st.success("Production = 3600/30 = 120 parts/hour")

        st.write("**4.** Give three possible causes of misrun.")
        with st.expander("Answer 4"):
            st.write("Low metal temperature, low die temperature, slow filling, thin section or poor gating.")

    elif level == "Level 3 — Intermediate":
        st.subheader("🟠 Intermediate")
        st.write("**1. Clamping Force:** Projected area = 250 cm², pressure = 70 MPa. Calculate approximate force.")
        if st.button("Answer 1 — Intermediate"):
            kn = 250 * 100 * 70 / 1000
            ton = kn / 9.80665
            st.success(f"Force = {kn:.2f} kN ≈ {ton:.2f} ton-force")

        st.write("**2. Production:** Cycle = 25 s, cavities = 2.")
        if st.button("Answer 2 — Intermediate"):
            st.success("Production = (3600/25) × 2 = 288 parts/hour")

        st.write("**3.** A casting has flash and porosity together. What should you inspect?")
        with st.expander("Suggested Investigation"):
            for x in [
                "Clamping force and die locking",
                "Injection pressure and velocity",
                "Die parting surface and alignment",
                "Venting/vacuum",
                "Turbulence and filling pattern",
                "Lubricant quantity",
                "Cooling and die temperature"
            ]:
                st.write("• " + x)

    else:
        st.subheader("🔴 Advanced")
        st.write("**1.** Projected area = 400 cm², pressure = 80 MPa, safety factor = 1.15.")
        if st.button("Answer 1 — Advanced"):
            base_kn = 400 * 100 * 80 / 1000
            base_ton = base_kn / 9.80665
            required = base_ton * 1.15
            st.success(f"Base = {base_ton:.2f} ton-force; Required ≈ {required:.2f} ton-force")

        st.write("**2.** Develop a systematic investigation for porosity.")
        with st.expander("Suggested Solution"):
            steps = [
                "Identify porosity location and type.",
                "Check die vents and vacuum/air evacuation.",
                "Check injection velocity and filling pattern.",
                "Check turbulence and gate/runner design.",
                "Check lubricant quantity.",
                "Check metal and die temperatures.",
                "Check pressure and solidification conditions.",
                "Make one controlled change at a time and inspect trial castings."
            ]
            for i, x in enumerate(steps, 1):
                st.write(f"{i}. {x}")

        st.write("**3.** Compare HPDC and Hot Chamber Die Casting.")
        with st.expander("Suggested Answer"):
            st.write(
                "HPDC refers to high-pressure filling. Hot chamber refers to the "
                "injection system being directly associated with the molten metal. "
                "Hot chamber is suitable only when the alloy and machine are compatible."
            )

# ----------------------------- PARTS -----------------------------

else:
    show_header("🔩 Parts & Applications",
                "Examples of components that may be produced by die casting. Actual process depends on alloy, geometry and machine.")

    selected = st.selectbox("Select Application", list(PARTS.keys()))

    st.subheader(selected)
    for part in PARTS[selected]:
        st.write("• " + part)

    st.divider()
    st.subheader("Process Selection Guide")

    st.write("### HPDC")
    st.write(
        "Commonly selected for high-volume production of aluminium and other "
        "suitable non-ferrous components requiring good repeatability and complex geometry."
    )

    st.write("### Hot Chamber")
    st.write(
        "Suitable when the alloy is compatible with the hot-chamber injection "
        "system and the required component/production conditions fit the process."
    )

    st.info(
        "Honda 70, Chingchi, Millat tractor and other bike/automotive names in "
        "this app are application categories/examples, not a claim that every "
        "listed component is manufactured by one specific casting process."
    )

# ----------------------------- FOOTER -----------------------------

st.divider()
st.caption(
    "Smart Die Casting Engineering App | Metallurgy & Materials Engineering Project | Educational Use"
)