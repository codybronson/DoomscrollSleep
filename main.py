import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':

    #reading csv
    df = pd.read_csv('Social_media_impact_on_life.csv')

    #cleaning and testing data---
    #checking first few rows
    # print(df.head())

    #see row/col counts
    # print(df.shape)

    #see datatypes and non-null counts
    # df.info()

    #charting missing values
    # df.isna().sum().plot(kind='bar')
    # plt.show()

    #dropping null rows
    clean_df = df.dropna(subset=['Perceived_Stress_Score', 'Academic_Performance_GPA'])

    #checking after drop
    # clean_df.info()
    # clean_df.isna().sum().plot(kind='bar')
    # plt.show()


    #exploratory analysis---
    #bar graph comparing Late_Night_Usage and Sleep_Quality_Score
    ct = pd.crosstab(clean_df['Late_Night_Usage'], clean_df['Sleep_Quality_Score'], normalize='index') * 100

    ax = ct.plot(kind='bar', stacked=True, colormap='RdYlGn', figsize=(8, 5))
    ax.set_ylabel('Percentage of Students (%)')
    ax.set_title('Sleep Quality Distribution by Late-Night Screen Usage')
    plt.xticks(rotation=0)
    plt.legend(title='Sleep Quality (1-5)', bbox_to_anchor=(1.05, 1))
    plt.tight_layout()
    plt.show()

    #strip plot with jitter
    fig, ax = plt.subplots(figsize=(7, 5))

    # Convert boolean to 0 and 1, then add random noise
    x_jitter = clean_df['Late_Night_Usage'].astype(int) + np.random.uniform(-0.15, 0.15, size=len(clean_df))
    y_jitter = clean_df['Sleep_Quality_Score'] + np.random.uniform(-0.15, 0.15, size=len(clean_df))

    ax.scatter(x_jitter, y_jitter, alpha=0.15, s=15, color='#2b5c8f')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['No Late-Night Usage', 'Late-Night Usage'])
    ax.set_ylabel('Sleep Quality Score (1–5)')
    ax.set_title('Jittered Distribution of Sleep Quality Scores')
    plt.show()

    #box plot
    fig1, ax = plt.subplots(figsize=(7, 5))

    no_late = clean_df[clean_df['Late_Night_Usage'] == False]['Sleep_Quality_Score']
    yes_late = clean_df[clean_df['Late_Night_Usage'] == True]['Sleep_Quality_Score']

    ax.boxplot([no_late, yes_late], label=['No Late-Night Usage', 'Late-Night Usage'], patch_artist=True)
    ax.set_ylabel('Sleep Quality Score (1–5)')
    ax.set_title('Impact of Late-Night Usage on Sleep Quality')
    plt.show()

    #Interaction between Late-night usage & academic level on sleep quality
    fig2, ax = plt.subplots(figsize=(8, 5))

    sns.pointplot(
        data=clean_df,
        x='Late_Night_Usage',
        y='Sleep_Quality_Score',
        hue='Academic_Level',
        palette='Set2',
        markers=['o', 's', '^'],
        linestyles=['-', '--', '-.'],
        capsize=0.1,
        ax=ax
    )

    ax.set_xticklabels(['No Late-Night Usage', 'Late-Night Usage'])
    ax.set_ylabel('Mean Sleep Quality Score (1–5)')
    ax.set_xlabel('')
    ax.set_title('Interaction Effect: Late-Night Usage & Academic Level on Sleep Quality')
    ax.legend(title='Academic Level', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()