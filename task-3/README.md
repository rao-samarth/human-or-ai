# Task-3 - Why is our tier-c model classifying with low confidence when it is?

We used SHAP to find the specific reasons for which our the confidence score of our tier-c model was low, in the previous section (ie task-2).

The code for this can be found in [task-3.ipynb](task-3.ipynb) and the results can be found in [low_confidence_analysis/](low_confidence_analysis/).  
We have 3 specific categories:

## Output Structure

The analysis generated 3 samples per class (9 total) with the **lowest confidence scores**. For each sample, we have 3 types of visualizations:

### 1. Text Files (`.txt`)
- `low-confidence-class-1-human.txt` - Contains the 3 human-written paragraphs with lowest confidence
- `low-confidence-class-2-generic.txt` - Contains the 3 generic AI paragraphs with lowest confidence  
- `low-confidence-class-3-mimic.txt` - Contains the 3 mimicry AI paragraphs with lowest confidence

Each entry shows the confidence score, source file, and the full text.

### 2. Waterfall Plots (`.png`)
Files like `Class_1_Human_Sample_1_waterfall.png` show:
- How individual words/tokens push the prediction score up or down
- Top ~12 most influential features
- Red bars = pushed score toward the predicted class
- Blue bars = pushed score away from the predicted class

### 3. Bar Charts (`.png`)
Files like `Class_1_Human_Sample_1_bar.png` show:
- **The Summary**: Global importance ranking of features
- Which tokens had the strongest absolute impact on the classification
- Sorted by magnitude of SHAP values

### 4. Interactive Heatmaps (`.html`)
Files like `Class_1_Human_Sample_1_heatmap.html` show:
- **The Context**: The full text with color-coded highlights
- Red highlighting = words that increased confidence in the predicted class
- Blue highlighting = words that decreased confidence
- Intensity of color = strength of the effect
- Open these files in a web browser for interactive exploration

## Sample Naming Convention

Format: `Class_{label}_{class_name}_Sample_{number}_{visualization_type}`

- **Class 1** = Human-written text
- **Class 2** = Generic AI (no style mimicry)
- **Class 3** = Mimic AI (attempting to copy author style)

Examples:
- `Class_1_Human_Sample_1_waterfall.png` - Waterfall plot for the lowest-confidence human sample
- `Class_3_Mimic_AI_Sample_3_heatmap.html` - Interactive heatmap for 3rd lowest-confidence mimicry sample