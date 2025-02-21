# Predicting Trump's Future Actions Using LLM

## Project Overview

The return of Donald Trump to the presidency introduces a high degree of uncertainty to global affairs. Understanding his potential actions and policies in advance could help individuals, businesses, and governments prepare for the potential consequences. This project aims to build a **fine-tuned Large Language Model (LLM)** that can predict Trump's future actions based on his past speeches, social media posts, debates, and official statements.

## Data Collection

To fine-tune the model effectively, we will collect and preprocess multiple sources of information:

- **Trump's Public Speeches**: Official speeches from campaign events, rallies, and press conferences.
- **Social Media Posts**:
  - Twitter posts from his official account before it was banned.
  - Posts from Truth Social, his self-created platform.
- **Presidential Debates**:
  - Debates between Trump and Biden.
  - Debates involving Kamala Harris to understand the Democratic stance.
- **Official White House News**:
  - News releases from the Trump administration to capture policy-related statements.

## Methodology

1. **Data Scraping & Preprocessing**:
   - Extract and clean text data from various sources.
   - Handle encoding issues (e.g., GBK vs. UTF-8) to ensure proper text representation.
2. **Fine-Tuning the LLM**:
   - Utilize pre-trained transformer models (e.g., LLaMA, GPT-4, or Mistral) and fine-tune them using Trump-related data.
   - Apply techniques like reinforcement learning from human feedback (RLHF) to improve model accuracy.
3. **Model Evaluation**:
   - Ask the model predictive questions based on Trump’s historical behavior.
   - Analyze the model’s responses regarding **Project 2025**, a set of policy proposals that may shape his second term.

## Goals & Impact

- **Understanding Trump's Future Policies**: Predict potential executive orders, diplomatic moves, and economic policies.
- **Enhancing Political Forecasting**: Provide insights into how Trump's administration may shape domestic and international affairs.
- **Testing LLM Predictive Capabilities**: Evaluate how well a fine-tuned model can predict political behavior based on historical data.

## Future Work

- Expand the dataset with real-time updates from Trump’s speeches and posts.
- Improve model fine-tuning with reinforcement learning techniques.
- Compare predictions with real-world events to measure accuracy.

## Disclaimer

This project is for research purposes only. The predictions made by the model are not definitive and should not be considered as factual statements about future events.

---

### **Contact & Contributions**

If you're interested in contributing or have suggestions, feel free to reach out!



