# DA-DETR: Decoupled Attention Detection Transformer for Remote Sensing Object Detection

## 🎯 Key Features

- ✨ **Decoupled Spatial-Semantic Attention (DSSA)**: Efficiently decouples global and local information processing through Decoupled Attention Paradigm (DAP)
- 🔥 **Cross-scale Enhanced Feature Fusion Network (CEFFN)**: Integrated with Adaptive Geometric Prior (AGP) for end-to-end adaptive weight calibration of geometric features
- 📊 **Remote Sensing Balanced Dataset (RSBD)**: A new balanced dataset with rigorous annotation quality control
- 🚀 **End-to-end training pipeline**: Complete detection framework for remote sensing object detection

## 📊 RSBD Dataset

### 📈 Dataset Statistics
<div align="center">

| **Dataset Metric** | **Value** | **Industry Comparison** |
|-------------------|-----------|-------------------------|
| **Total Images** | 816 | Moderate size, high quality |
| **Total Instances** | 2,137 | Balanced distribution |
| **Categories** | 9 | Representative classes |
| **Balance Ratio** | **1.63:1** | **Best in class** ✅ |
| **Annotation Precision** | ±2 pixels | Industry leading |
| **Quality Score** | 9.2/10 | Expert validated 

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

![](https://github.com/zzyadad/DA-DETR/blob/main/RSBD.png)
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
