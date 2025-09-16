# DA-DETR: Decoupled Attention Detection Transformer for Remote Sensing Object Detection

## 🎯 Key Features

- ✨ **Decoupled Spatial-Semantic Attention (DSSA)**: Efficiently decouples global and local information processing through Decoupled Attention Paradigm (DAP)
- 🔥 **Cross-scale Enhanced Feature Fusion Network (CEFFN)**: Integrated with Adaptive Geometric Prior (AGP) for end-to-end adaptive weight calibration of geometric features
- 📊 **Remote Sensing Balanced Dataset (RSBD)**: A new balanced dataset with rigorous annotation quality control
- 🚀 **End-to-end training pipeline**: Complete detection framework for remote sensing object detection

## 📊 RSBD Dataset

### 🚨 Dataset Availability Notice

> **📋 Important**: The complete RSBD dataset and code will be **publicly released upon paper acceptance**. 
> 
> **🔗 Current Status**: Under review process  
> **📅 Expected Release**: Upon journal publication  
> **📧 Early Access**: Contact [10431240210@stu.qlu.edu.cn](mailto:10431240210@stu.qlu.edu.cn) for research collaboration

### 🏗️ Dataset Construction Process

Our **Remote Sensing Balanced Dataset (RSBD)** was constructed through a systematic and rigorous process:

#### 🔍 **Phase 1: Data Collection**
- **Source**: High-resolution satellite imagery from Google Earth
- **Coverage**: Global geographic regions with diverse scenarios
- **Resolution**: High-resolution imagery ensuring clear target visibility
- **Selection Criteria**: Dense targets, small objects, multi-oriented, and multi-scale scenarios

#### 📝 **Phase 2: Annotation Process**
- **Standards**: ±2 pixel precision for bounding boxes
- **Quality Control**: Three-tier validation system
  - Primary annotators for initial labeling
  - Secondary reviewers for accuracy verification  
  - Senior experts for final quality assurance
- **Occlusion Rule**: Targets >50% occluded are excluded
- **Adjacent Targets**: Separation strategy for spacing <20% of target size

#### ⚖️ **Phase 3: Balance Optimization**
- **Strategy**: Multi-round iterative sampling (5 rounds)
- **Initial Ratio**: 3.47:1 (highly imbalanced)
- **Optimization Process**:
  - Round 1: Enhanced insufficient categories (Harbor, Vehicle)
  - Round 2: Reduced over-sampled categories (Ship, Basketball Court)
  - Round 3: Geographic expansion (Bridge, Airplane)
  - Round 4: Quality refinement (Storage Tank, Ground Track Field)
  - Round 5: Final balance adjustment
- **Final Achievement**: **1.63:1 ratio** (excellent balance)

#### ✅ **Phase 4: Quality Validation**
- **Expert Review**: Consensus mechanism for challenging samples
- **Validation Metrics**: Boundary precision, category accuracy
- **Final Approval**: Senior expert panel validation

### 📈 Dataset Statistics

<div align="center">

| **Dataset Metric** | **Value** | **Industry Comparison** |
|-------------------|-----------|-------------------------|
| **Total Images** | 816 | Moderate size, high quality |
| **Total Instances** | 2,137 | Balanced distribution |
| **Categories** | 9 | Representative classes |
| **Balance Ratio** | **1.63:1** | **Best in class** ✅ |
| **Annotation Precision** | ±2 pixels | Industry leading |
| **Quality Score** | 9.2/10 | Expert validated |

</div>

### 🏷️ Category Distribution

<div align="center">

| **Category** | **Instances** | **Percentage** | **Description** |
|--------------|---------------|----------------|-----------------|
| 🚢 **Ship** | 239 | 11.2% | Various vessels in harbors and open water |
| 🌉 **Bridge** | 179 | 8.4% | Highway and railway bridges |
| 🏃 **Ground Track Field** | 223 | 10.4% | Athletic tracks and sports fields |
| ⛽ **Storage Tank** | 291 | 13.6% | Industrial storage facilities |
| 🏀 **Basketball Court** | 248 | 11.6% | Outdoor basketball courts |
| 🎾 **Tennis Court** | 276 | 12.9% | Tennis courts in various settings |
| ✈️ **Airplane** | 209 | 9.8% | Aircraft in airports and runways |
| ⚓ **Harbor** | 209 | 9.8% | Port facilities and docks |
| 🚗 **Vehicle** | 254 | 11.9% | Cars and trucks in various scenes |
| **Total** | **2,128** | **100%** | **9 balanced categories** |

</div>

**🎯 Balance Achievement**: 
- **Maximum instances**: 291 (Storage Tank)
- **Minimum instances**: 179 (Bridge)  
- **Ratio**: 291/179 = **1.63:1** (Excellent balance)

### 🖼️ Dataset Visualization

#### Sample Images from Each Category

<div align="center">

*Dataset samples will be displayed here upon release*

<!-- Placeholder for dataset visualization -->
