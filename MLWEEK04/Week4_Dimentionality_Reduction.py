import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif, RFE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import sklearn.datasets as DS
#=======
def RF_Classs(X,Y,XS,YS):
    RF = RandomForestClassifier()
    RF.fit(X,Y)
    PR = RF.predict(XS)
    print(accuracy_score(PR,YS))

#==Compare tye resu;ts of RF for PCA

Data =DS.load_breast_cancer()
X = Data['data']
Y = Data['target']
P1 = PCA(n_components=0.95)
X_train,X_test,y_train,y_test = train_test_split(X,Y,train_size=0.3)
print('Result of raw data')
RF_Classs(X_train,y_train,X_test,y_test)
#=====Scaler
Sc = StandardScaler()
X_train_S = Sc.fit_transform(X_train)
X_Test_S = Sc.transform(X_test)
print('Result of scaled data')
RF_Classs(X_train_S,y_train,X_Test_S,y_test)

#=======
XPCA1 = P1.fit_transform(X_train_S)
XPCAS = P1.transform(X_Test_S)

# Record the number of components retained by PCA
n_components_retained = P1.n_components_
print(f'Number of components retained by PCA (95% variance): {n_components_retained}')
print(f'Original number of features: {X_train_S.shape[1]}')
print(f'Variance explained by each component: {P1.explained_variance_ratio_}')
print(f'Cumulative variance explained: {np.cumsum(P1.explained_variance_ratio_)[-1]:.4f}')
print('Result of PCA data')
RF_Classs(XPCA1,y_train,XPCAS,y_test)
