# import pymc as pm
import numpy as np
import pandas as pd
import arviz as az
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# 🔹 NumPy のランダムシードを設定（PyMC のランダム性にも影響）
np.random.seed(42)

# 各認知機能スコアでベイズ線形回帰分析
for col in df.columns[6:]:
    print('')
    print(f'============================================{col}============================================')

    # nanを除去（df を更新）
    df_removed = df[~df[col].isna()].copy()
    
    # 説明変数
    X = df_removed[['検査時の年齢', '性別', '教育歴', 'group']].copy()
    
    # カテゴリ変数のエンコーディング（group: DPA = 0, naPPA = 1）
    X['group'] = (df_removed['group'] == 'nappa').astype(int)  # naPPA = 1, DPA = 0
    X = pd.get_dummies(X, columns=['性別'], drop_first=True, dtype=int).copy()
    
    # 目的変数（認知機能スコア）
    y = df_removed[col].values  # 連続変数として扱う

    # 標準化（連続変数のみ）
    scaler = StandardScaler()
    num_cols = ['検査時の年齢', '教育歴']
    X[num_cols] = scaler.fit_transform(X[num_cols])

    # PyMCによるベイズ線形回帰
    with pm.Model() as model:
        beta_age = pm.Normal("beta_age", mu=0, sigma=5)
        beta_edu = pm.Normal("beta_edu", mu=0, sigma=5)
        beta_gender = pm.Normal("beta_gender", mu=0, sigma=5)
        beta_group = pm.Normal("beta_group", mu=0, sigma=5)  # DPA vs naPPA の影響
        intercept = pm.Normal("intercept", mu=0, sigma=10)

        # 線形結合
        mu = (
            intercept
            + beta_age * X["検査時の年齢"].values
            + beta_edu * X["教育歴"].values
            + beta_gender * X["性別_男"].values
            + beta_group * X["group"].values  # DPA vs naPPA の影響
        )

        sigma = pm.HalfNormal("sigma", sigma=5)  # ノイズの標準偏差

        # 線形回帰の尤度（観測値 y は正規分布に従う）
        y_obs = pm.Normal("y_obs", mu=mu, sigma=sigma, observed=y)

        # ✅ MCMCサンプリング
        trace = pm.sample(2000, tune=1000, return_inferencedata=True, idata_kwargs={"log_likelihood": True})

    # ✅ 事後分布の可視化
    az.plot_trace(trace, figsize=(20, 12))
    plt.tight_layout()
    az.plot_posterior(trace, hdi_prob=0.95)
    plt.show()

    # 事後分布の要約
    summary = az.summary(trace, stat_funcs={"median": np.median}, hdi_prob=0.95)
    print(summary)

    print('')

    # 事後確率を計算
    def compute_posterior_probabilities(trace, param):
        """事後確率を求める"""
        samples = trace.posterior[param].values.flatten()
        prob_positive = (samples > 0).mean()
        prob_negative = (samples < 0).mean()
        return prob_positive, prob_negative

    print("\n事後確率:")
    for param in ["beta_age", "beta_edu", "beta_gender", "beta_group"]:
        p_pos, p_neg = compute_posterior_probabilities(trace, param)
        print(f"{param}: P(β > 0) = {p_pos:.3f}, P(β < 0) = {p_neg:.3f}")
