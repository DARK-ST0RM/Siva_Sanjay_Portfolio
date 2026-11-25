
"""All portfolio content lives in this file. Edit it; app.py needs no changes.
Empty lists/strings hide their section or field, so nothing placeholder ever shows."""

NAME = "Siva Sanjay P"
INITIALS = "SS"

TITLE = "Python · SQL · ML · Data Science"
OPEN_TO = "Open to data science and ML roles"

INTRO = (
    "Bioinformatics graduate who builds in Python and SQL, from data preprocessing "
    "and feature engineering to validated predictive models and working apps."
)

TAGLINE = "Turning scientific and clinical data into validated models and working apps."

EMAIL = "sivasanjay1920@gmail.com"
PHONE = "+91 73394 83665"

GITHUB = "https://github.com/DARK-ST0RM"
LINKEDIN = "https://www.linkedin.com/in/siva-sanjay"

RESUME_FILE = "assets/resume.pdf"
RESUME_PREVIEW = "assets/resume_preview.jpg"
RESUME_UPDATED = "November 2026"

PROFILE_IMAGE = "assets/profile.jpg"


ABOUT = {
    "paragraphs": [
        (
            "I’m a 2026 B.Tech Bioinformatics graduate from SASTRA University "
            "with an interest in data science, machine learning and Python development. "
            "I enjoy working with datasets, building predictive models and developing practical applications."
        ),
        (
            "My academic projects include a machine learning framework for predicting "
            "Deep Eutectic Solvent density using quantum-chemical descriptors, and a healthcare "
            "application that extracts laboratory parameters using OCR and generates "
            "rule-based dietary recommendations."
        ),
    ],

    "strengths": [
        "Data preprocessing and feature engineering",
        "Machine learning and predictive modeling",
        "Model evaluation and performance analysis",
        "Developing applications using Python and Streamlit",
    ],

    "interests": [
        "Applied Machine Learning and AI",
        "Data Science and Predictive Analytics",
        "Computational Biology and Bioinformatics",
        "Healthcare and Clinical Data Applications",
    ],

    "objective": (
        "To join a data science or machine learning team where I can apply "
        "predictive modeling to real problems and keep growing."
    ),

    "approach": (
        "I approach problems by understanding the requirements, "
        "breaking complex tasks into manageable steps, and analyzing the available data." 
        " then I select suitable tools and techniques to develop practical solutions, "
        "evaluate the results, and refine them for better performance."
   
    ),

    "learning": [],
}


SKILLS = {
    "Programming": [
        "Python",
        "SQL",
        "R",
    ],

    "Machine learning": [
        "Scikit-learn",
        "Predictive modeling",
        "Model evaluation",
        "Feature engineering",
    ],

    "Data and libraries": [
        "Pandas",
        "NumPy",
        "OCR",
    ],

    "Scientific computing": [
        "GFN2-xTB",
        "RDKit",
        "Open Babel",
    ],

    "Backend and web": [
        "Flask",
        "REST APIs",
        "Streamlit",
        "HTML",
    ],

    "Tools": [
        "Linux",
        "VS Code",
        "Git",
        "GitHub",
    ],

    "Professional": [
        "Team collaboration",
        "Time management",
        "Adaptability",
        "Problem solving",
    ],
}


EDUCATION = [
    {
        "degree": "B.Tech Bioinformatics",
        "institution": "SASTRA Deemed to be University",
        "location": "Thanjavur, Tamil Nadu",
        "start": "2022",
        "end": "2026",
        "status": "Graduated",
        "details": ["CGPA 7.09"],
    },

    {
        "degree": "HSC",
        "institution": "Maxwell Matriculation Higher Secondary School",
        "location": "",
        "start": "2020",
        "end": "2022",
        "status": "Completed",
        "details": ["72%"],
    },

    {
        "degree": "SSLC",
        "institution": "Best Matriculation Higher Secondary School",
        "location": "",
        "start": "2019",
        "end": "2020",
        "status": "Completed",
        "details": ["70%"],
    },
]


# Add only real items.
# Each: {"name","issuer","date","credential_id","url","image"}

CERTIFICATIONS = []


# Categories: Hackathons, Competitions, Awards, Research,
# Technical events, Open source.
# Each achievement: {"title","detail","url"}

ACHIEVEMENTS = {}


PROJECTS = [

    # -------------------------------------------------
    # PROJECT 1: DEEP EUTECTIC SOLVENT DENSITY PREDICTION
    # -------------------------------------------------

    {
        "id": "des",

        "category": "Machine Learning Project",

        "title": "AI-Augmented Computational Design of Deep Eutectic Solvent",

        "short": "Machine Learning-Based Density Prediction of Deep Eutectic Solvents",

        "dates": "Jan 2026 – Apr 2026",

        "summary": (
            "A QSPR pipeline that predicts deep eutectic solvent density from "
            "composition and quantum-chemical descriptors."
        ),

        "stack": [
            "Python",
            "Scikit-learn",
            "GFN2-xTB",
            "RDKit",
            "Feature engineering",
        ],

        "image": "assets/des_results.jpg",

        "caption": (
            "From the thesis: predicted vs. actual density, residuals and model "
            "comparison on the 26 held-out solvent systems."
        ),

        "overview": (
            "Final-year thesis project at SASTRA University that combines "
            "semi-empirical quantum chemistry (GFN2-xTB) with machine learning "
            "to predict the density of deep eutectic solvents (DES)."
        ),

        "problem": (
            "Measuring density in the lab for every possible hydrogen-bond "
            "acceptor and donor combination is slow and resource-intensive."
        ),

        "objective": (
            "Build an automated, reproducible and interpretable QSPR framework "
            "that predicts DES density, with rigorous system-wise validation."
        ),

        "solution": (
            "A four-phase pipeline from raw solvent data to model predictions, "
            "followed by a comparison of ten algorithms."
        ),

        "role": (
            "Team project of two. I executed preprocessing and molecular "
            "optimization workflows, contributed to descriptor extraction, "
            "feature engineering and dataset preparation, and took part in "
            "model training, workflow analysis and interpreting results."
        ),

        "features": [
            "Automated, reproducible workflow from SMILES strings to predictions",
            "13 engineered system-level features: composition, weighted averages and inter-component differences",
            "System-wise train/test split so no solvent appears in both sets",
            "Ten algorithms compared, with feature-importance analysis",
        ],

        "process": [
    (
        "Dataset Preparation",
        "Collected DES composition and experimental density data. Validated SMILES, "
        "handled incomplete records and prepared the dataset for computational analysis."
    ),
    (
        "Molecular Structure Optimization",
        "Generated molecular structures and performed geometry optimization using "
        "Open Babel and GFN2-xTB to obtain stable molecular configurations."
    ),
    (
        "Quantum Descriptor Calculation",
        "Extracted electronic and molecular properties, including HOMO, LUMO, "
        "dipole moment and solvation energy, to represent solvent characteristics."
    ),
    (
        "Feature Engineering",
        "Combined HBA and HBD descriptors using weighted averages and difference-based "
        "calculations to construct 13 system-level features."
    ),
    (
        "Model Development",
        "Trained and compared multiple machine learning algorithms, including "
        "Random Forest and Gradient Boosting, to identify the best-performing model."
    ),
    (
        "Model Validation",
        "Applied system-wise train-test splitting and grouped cross-validation "
        "to evaluate predictive performance and reduce data leakage."
    ),
    ],

        "challenges": [
            (
                "12 of 140 formulations could not be used: 6 failed geometry "
                "optimization and 6 lacked temperature data.",
                "Kept the 128 systems with complete descriptors for modelling."
            ),

            (
                "A random split would leak the same solvent into training and test data.",
                "Used a system-wise split: 102 systems for training and 26 for testing."
            ),

            (
                "Uneven representation of solvent families across validation folds.",
                None
            ),
        ],

        "metrics": [
            ("0.788", "Test R², Gradient Boosting"),
            ("0.060", "Test RMSE (g/cm³)"),
            ("3.77%", "Test MAPE"),
            ("0.738 ± 0.056", "Grouped 5-fold CV R²"),
        ],

        "results": [
            "Gradient Boosting scored best, ahead of Random Forest (R² 0.762); linear models reached only 0.27 to 0.41.",

            "Weighted electronic features carried 81.1% of feature importance, led by weighted LUMO energy at 41.9%.",
        ],

        "limitations": [
            "Covers binary solvent systems only.",
            "Metal-based solvents are not included.",
        ],

        "github": "https://github.com/DARK-ST0RM/QSPR_DES_Density_Prediction",

        "demo": "",
    },


    # -------------------------------------------------
    # PROJECT 2: LAB REPORT ANALYZER
    # -------------------------------------------------

    {
        "id": "lab",

        "category": "OCR Project",

        "title": "Lab Report Analyzer and Personalized Health Recommendation System",

        "short": "Lab Report Analyzer",

        "dates": "Sep 2025 – Nov 2025",

        "summary": (
            "A Python app that reads clinical parameters from laboratory reports "
            "with OCR and suggests personalized diets."
        ),

        "stack": [
            "Python",
            "OCR",
            "Pandas",
            "NumPy",
            "SQL",
            "Streamlit",
        ],

        "image": "",

        "caption": "",

        "overview": (
            "A healthcare application that extracts clinical values from "
            "laboratory reports and turns them into personalized dietary recommendations."
        ),

        "problem": (
            "Diet plans rarely take a person’s actual lab results into account, "
            "and there is little automation for reading nutritional information "
            "from medical reports."
        ),

        "objective": (
            "Give people personalized food recommendations based on the values "
            "in their own clinical reports."
        ),

        "solution": (
            "OCR extracts the clinical parameters, Pandas and NumPy process them, "
            "SQL manages the data, and a Streamlit interface presents the "
            "information and recommendations."
        ),

        "role": "Team project of three.",

        "features": [
            "Extracts clinical parameters from laboratory reports with OCR",
            "Processes and analyzes the extracted values with Pandas and NumPy",
            "SQL-based data management",
            "Streamlit interface showing clinical information and dietary recommendations",
        ],

        "process": [
    (
        "Report Upload and Input Collection",
        "Accepted laboratory reports in PDF and image formats, along with "
        "user details such as age, gender, BMI and dietary preferences."
    ),
    (
        "OCR-Based Data Extraction",
        "Applied OCR to extract text and relevant clinical parameters from "
        "uploaded laboratory reports."
    ),
    (
        "Clinical Data Processing",
        "Used Python, Pandas and NumPy to organize extracted values and "
        "compare clinical parameters against predefined reference ranges."
    ),
    (
        "Personalized Recommendation",
        "Implemented rule-based logic to identify out-of-range parameters "
        "and generate dietary suggestions based on user inputs."
    ),
    (
        "Web Development",
        "Integrated the processing workflow into a Streamlit interface "
        "to display extracted results and personalized recommendations."
    ),
    ],

        "challenges": [
            (
                "Report formats vary and handwritten entries are hard to read.",
                None
            ),

            (
                "Clinical test reports can be inconsistent.",
                None
            ),
        ],

        "metrics": [],

        "results": [],

        "limitations": [],

        "github": "",

        "demo": "",
    },
]
