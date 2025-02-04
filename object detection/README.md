# Parasitic Detection using YOLOv11

## 🦠 Project Overview
This project implements an object detection system for identifying different types of parasites in microscopic images. The system is capable of detecting 8 different types of parasites:

- Ancylostoma Spp
- Ascaris Lumbricoides
- Enterobius Vermicularis
- Fasciola Hepatica
- Hymenolepis
- Schistosoma
- Taenia Sp
- Trichuris Trichiura

## 📊 Dataset
The dataset used in this project is sourced from Roboflow Universe, containing 2,110 annotated microscopic images. The dataset is part of the [RF100](https://rf100.org) initiative, sponsored by Intel.

### Dataset Structure   

parastic dataset/
├── train/
│ ├── images/
│ └── labels/
├── valid/
│ ├── images/
│ └── labels/
└── test/
├── images/
└── labels/
```

## 🛠️ Setup and Installation

1. Clone the repository
```bash
git clone [your-repo-url]
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Training

The model is trained using YOLOv11 architecture. Training configuration can be found in `parastic dataset/data.yaml`.

## 📝 License
- Dataset License: CC BY 4.0
- Original dataset created by [Joao Paulo Martins](https://universe.roboflow.com/graduao/)

## 🙏 Acknowledgments
- [Roboflow](https://roboflow.com/) for dataset hosting and management
- [RF100](https://rf100.org) initiative
- Intel for sponsoring the RF100 benchmark

## 📊 Model Performance
[Add your model's performance metrics here]

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📫 Contact
[Add your contact information here]

## 📜 Citation
```bibtex
@dataset{parasites_dataset,
    author = {Joao Paulo Martins},
    title = {Parasites Detection Dataset},
    year = {2024},
    publisher = {Roboflow Universe},
    url = {https://universe.roboflow.com/roboflow-100/parasites-1s07h}
}
```

This README includes:
1. Clear project overview
2. Dataset information
3. Setup instructions
4. Training information
5. License details
6. Acknowledgments
7. Placeholder sections for model performance and contact information
8. Citation information

You can customize this README by:
1. Adding your specific model performance metrics
2. Including your contact information
3. Adding any specific usage instructions
4. Including screenshots or example detections
5. Adding your repository URL in the clone command

Would you like me to modify any section or add additional information?